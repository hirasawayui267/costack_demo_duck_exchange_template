import json 
import requests
import random 


"""
to see the format of the event input, refer to `sample_api_request.json`
"""

# there are only three tickers available
TICKERS = ["DUCK1", "DUCK2", "DUCK3"]

def hello_world(event, context):
    # simple test
    return {"message": "welcome to duck exchange! Start trading duck coins with api."}

def parse_lambda_input_request(event):
    http_method = event['requestContext']['http']['method']
    headers = event['headers']
    # GET Method does not have a body
    body = json.loads(event['body']) if "body" in event else None
    return http_method, headers, body

# accept post method
def get_ticker_price(event, context):
    http_method, headers, body = parse_lambda_input_request(event)
    if http_method!="POST":
        return {"error":"wrong http method"}
    # parse the event 
    body = json.loads(event['body'])
    if "ticker" not in body:
        return {f"error": "no ticker found in request body"}
    ticker = body['ticker']
    if ticker not in TICKERS:
        return {f"error": "unknown ticker {ticker}"}
    return {"ticker_name": ticker, "price": random.uniform(1.5, 1.9)*100}

def list_tickers(event, context):
    http_method, headers, body = parse_lambda_input_request(event)
    if http_method!="GET":
        return {"error":"wrong http method"}
    return {"tickers": TICKERS}

def place_trade(event, context):
    http_method, headers, body = parse_lambda_input_request(event)
    if http_method!="POST":
        return {"error":"wrong http method"}
    ticker = body['ticker']
    if "ticker" not in body:
        return {f"error": "no ticker found in request body"}
    side = body['side']
    quantity = body['quantity']
    order_type = body['order_type']
    if order_type not in ['market', 'limit']:
        return {f"error": "invalid order type, choose market or limit"}
    # no price needed for market order 
    price = body.get('price',None)
    order_summary= {"ticker":ticker, "side": side, "quantity": quantity, "order_type": order_type, "price": price}
    return {"response": "processing order", "order_summary": order_summary}

def try_duck_lottery(event, context):
    http_method, headers, body = parse_lambda_input_request(event)
    if http_method!="POST":
        return {"error":"wrong http method"}
    # magic is a number from 1-100 
    magic = body['magic']
    duck_number = random.randint(0,100)
    if magic>duck_number:
        return {"response": "congrats! you got duck lottery"}
    else:
        return {"response": "sorry, you did not win duck lottery this time"}
