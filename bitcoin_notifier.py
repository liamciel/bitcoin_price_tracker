import requests
import time
from datetime import datetime

IFTTT_WEBSHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/bGpcGg2hDbkrhPVl4XGXDW'
BITCOIN_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json' # The api updates the bitcoin price every minute
BITCOIN_THRESHOLD = 30000 # Threshold for bitcoin

def main():
    bitcoin_history = []
    while True: # Create an infinite loop
        price = get_latest_bitcoin_price()
        date = datetime.now()
        date = str(date)
        price = str(price)
        bitcoin_history.append({'value1': date, 'value2': price}) # Set the keys to be 'value1' and 'value2' as set up in IFTTT event configuration

        #send the emergency notification
        # if price > BITCOIN_THRESHOLD:
        #     post_ifttt_webhook("bitcoin_price_emergency", bitcoin_history[-1])
        
        # Send the price updates notifications
        post_ifttt_webhook('bitcoin_update', bitcoin_history[-1])
            
            # # Reset the bitcoin_history list
            # bitcoin_history = [] 
        # sleep for 5 minutes
        time.sleep(1)

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    bitcoin_value = response_json['bpi']['USD']['rate_float']
    return bitcoin_value

def post_ifttt_webhook(event, data):
    # The payload of the that will be sent to IFTTT service
    # insert our desired event
    print
    ifttt_webhooks_url = IFTTT_WEBSHOOKS_URL.format(event)
    requests.post(ifttt_webhooks_url, json = data)

if __name__ == "__main__":
    main()
    
