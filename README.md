# costack_sample_api_backend


Route: `list_tickers` <br>
Method: `GET` <br>
Sample query: <br>
`curl -i -X GET https://92ae6ci4ad.execute-api.us-east-1.amazonaws.com/entropy-default/list_tickers` <br>

Route: place_trade <br>
Method: POST <br>
Sample query: <br>
`curl -X POST -H 'Content-Type: application/json' -d '{"ticker":"DUCK1", "side":"buy", "quantity": 100, "price": 100, "order_type":"market"}'  https://92ae6ci4ad.execute-api.us-east-1.amazonaws.com/entropy-default/place_trade` <br>

Route: try_duck_lottery <br>
Method: POST <br>
Sample query: <br>
`curl -X POST -H 'Content-Type: application/json' -d '{"magic": 100}'  https://92ae6ci4ad.execute-api.us-east-1.amazonaws.com/entropy-default/try_duck_lottery` <br>

Route: get_ticker_price <br>
Method: POST <br>
Sample query: <br>
`curl -X POST -H 'Content-Type: application/json' -d '{"ticker": "DUCK1"}'  https://92ae6ci4ad.execute-api.us-east-1.amazonaws.com/entropy-default/get_ticker_price` <br>
