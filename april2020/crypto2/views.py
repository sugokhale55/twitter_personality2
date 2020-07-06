from django.shortcuts import render
def home(request):
	import requests
	import json
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	api_request2 = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP&tsyms=USD")
	api2 = json.loads(api_request2.content)
	api_tx = requests.get("https://api.smartbit.com.au/v1/blockchain/transactions?limit=1&sort=size")
	apitx1 = json.loads(api_tx.content)
	apitxtop5 = requests.get("https://api.smartbit.com.au/v1/blockchain/transactions/confirmed?limit=10&sort=input_amount")
	apitx44 = json.loads(apitxtop5.content)

	return render(request, 'home.html',{'api':api,'api2':api2,'apitx1':apitx1,'apitx44':apitx44})
# Create your views here.
