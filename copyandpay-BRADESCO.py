#!/usr/bin/python

import urllib, urllib2, json

def prepareCheckout():
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		"paymentType": "PA",
		"amount": "10.00",
		"currency": "BRL",
		"customParameters[BRADESCO_cpfsacado]": "11111111111",
		"billing.country": "BR",
		"billing.postcode": "12345678",
		"billing.state": "SP",
		"billing.street1": "Amazonstda",
		"billing.city": "Brasilia",
		"customer.givenName": "Braziliano",
		"customer.surname": "Babtiste",
		"testMode": "EXTERNAL"
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

checkoutId = prepareCheckout()["id"];
print checkoutId;