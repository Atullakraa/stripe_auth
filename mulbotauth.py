import requests
import telebot
import time
import os
import threading
from queue import Queue
from telebot import types
from auth2 import Tele

token = '8091522425:AAGejhiwqgdDhVLLkyGfQWK-GOuaagPZTOc'
bot = telebot.TeleBot(token, parse_mode="HTML")

# Shared variables for threading
processing_lock = threading.Lock()
card_queue = Queue()
stop_flag = False

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.id not in [5980629524, 1762371536]:
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @fouroneul")
        return
    bot.reply_to(message, "Send the file now")

def process_card(message, cc, ko, approved, declined, total):
    global stop_flag
    
    if stop_flag:
        return
    
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith(".stop"):
            with processing_lock:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, 
                                     text='STOP ✅\nBOT BY ➜ @fouroneul')
                os.remove('stop.stop')
                stop_flag = True
            return
    
    try: 
        data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
    except: 
        data = {}
    
    brand = data.get('brand', 'Unknown')
    card_type = data.get('type', 'Unknown')
    country = data.get('country_name', 'Unknown')
    country_flag = data.get('country_flag', 'Unknown')
    bank = data.get('bank', 'Unknown')
    
    start_time = time.time()
    try:
        last = str(Tele(cc))
    except Exception as e:
        print(e)
        last = 'missing payment form'
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    with processing_lock:
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        status = types.InlineKeyboardButton(f"• STATUS ➜ {last} •", callback_data='u8')
        cm3 = types.InlineKeyboardButton(f"• APPROVED ➜ [ {approved[0]} ] •", callback_data='x')
        cm4 = types.InlineKeyboardButton(f"• DECLINED ➜ [ {declined[0]} ] •", callback_data='x')
        cm8 = types.InlineKeyboardButton(f"• TOTAL ➜ [ {total} ] •", callback_data='x')
        stop = types.InlineKeyboardButton(f"[ STOP ]", callback_data='stop')
        mes.add(cm1, status, cm3, cm4, cm8, stop)
        
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, 
                            text='''Wait For Processing\nby ➜ @fouroneul''', 
                            reply_markup=mes)
        
        if 'requires_action' in last or 'succeeded' in last or 'next_action' in last or 'return_url' in last or 'payment_type' in last or 'client_secret' in last or 'true' in last:
            approved[0] += 1
            msg = f'''
𝐂𝐀𝐑𝐃: <code>{cc}</code>
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>APPROVED CARD ✅</code>
𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
𝐁𝐚𝐧𝐤: <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} second</code> 
𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: @fouroneul'''
            bot.reply_to(message, msg)
            with open("hits.txt", "a") as hits_file:
                hits_file.write(f"{cc}\n")
        else:
            declined[0] += 1

@bot.message_handler(content_types=["document"])
def main(message):
    global stop_flag
    
    if message.chat.id not in [5980629524, 1762371536]:
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @fouroneul")
        return
    
    stop_flag = False
    approved = [0]
    declined = [0]
    ko = (bot.reply_to(message, "CHECKING....⌛").message_id)
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    
    with open("combo.txt", "wb") as w:
        w.write(ee)
    
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            
            # Create threads (3 threads for concurrent processing)
            threads = []
            for cc in lino:
                if stop_flag:
                    break
                
                cc = cc.strip()
                if not cc:
                    continue
                
                t = threading.Thread(target=process_card, args=(message, cc, ko, approved, declined, total))
                threads.append(t)
                t.start()
                
                # Limit to 3 concurrent threads
                while len(threads) >= 30:
                    for t in threads:
                        if not t.is_alive():
                            threads.remove(t)
                    time.sleep(0.1)
            
            # Wait for remaining threads to finish
            for t in threads:
                t.join()
            
            if not stop_flag:
                with processing_lock:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, 
                                         text='CHECKED ✅\nBOT BY ➜ @fouroneul')
    
    except Exception as e:
        print(e)
        with processing_lock:
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, 
                                 text=f'ERROR: {str(e)}\nBOT BY ➜ @fouroneul')

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    global stop_flag
    stop_flag = True
    with open("stop.stop", "w") as file:
        pass
    bot.answer_callback_query(call.id, "Processing stopped!")

bot.polling()