
import time, uuid, hashlib, hmac, requests, json, os
BINANCE_API_URL = 'https://bpay.binanceapi.com/binancepay/openapi'
def _signature(payload, nonce, timestamp, cert_sn, api_secret):
    data = f"{timestamp}\n{nonce}\n{payload}\n"
    return hmac.new(api_secret.encode(), data.encode(), hashlib.sha512).hexdigest()
def create_binance_order(amount, api_key, api_secret, cert_sn):
    endpoint = '/v2/order'
    url = BINANCE_API_URL + endpoint
    nonce = uuid.uuid4().hex
    timestamp = str(int(time.time() * 1000))
    payload = {
        "merchantTradeNo": uuid.uuid4().hex,
        "orderAmount": str(amount),
        "currency": "USDT",
        "goods": {
            "goodsType": "01",
            "goodsCategory": "D000",
            "referenceGoodsId": "AXIS_DEPOSIT",
            "goodsName": "AxisCapital Deposit",
            "goodsDetail": "Deposit to trading wallet"
        }
    }
    payload_json = json.dumps(payload, separators=(',', ':'))
    sign = _signature(payload_json, nonce, timestamp, cert_sn, api_secret)
    headers = {
        "content-type": "application/json",
        "BinancePay-Timestamp": timestamp,
        "BinancePay-Nonce": nonce,
        "BinancePay-Certificate-SN": cert_sn,
        "BinancePay-Signature": sign,
    }
    response = requests.post(url, headers=headers, data=payload_json)
    response.raise_for_status()
    return response.json()
