import json 
import requests
import random 
from costack_sdk.costack_lambda import costack_http
# add some thing 
"""
to see the format of the event input, refer to `sample_api_request.json`
"""

# there are only three tickers available
# all tickers are duck related because duck is our mascot, the perfect companion to programers
TICKERS = ["DUCK1", "DUCK2", "DUCK3", "DUCK4"]

@costack_http(methods=["GET"])
def ping(event, context):
    # simple test
    return {"message": "welcome to duck exchange! Start trading duck coins with api."}

# accept post method
@costack_http(methods=["POST"])
def get_ticker_price(request, context):
    body = json.loads(request.body)
    ticker = body['ticker']
    if ticker not in TICKERS:
        return {f"error": "unknown ticker {ticker}"}
    return {"ticker_name": ticker, "price": random.uniform(1.5, 1.9)*100}

@costack_http(methods=["GET"])
def list_tickers(request, context):
    if request.http_method!="GET":
        return {"error":"wrong http method"}
    return {"tickers": TICKERS}

@costack_http(methods=["POST"])
def place_trade(request, context):
    body = request.bdoy
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