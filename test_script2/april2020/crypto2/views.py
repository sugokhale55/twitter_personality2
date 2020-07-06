from django.shortcuts import render
def home(request):
	import requests
	import json
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	api_request2 = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP&tsyms=USD")
	api2 = json.loads(api_request2.content)
	return render(request, 'home.html',{'api':api,'api2':api2})
# Create your views here.
