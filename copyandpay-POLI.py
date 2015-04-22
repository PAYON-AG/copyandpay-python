#!/usr/bin/python

import urllib, urllib2, json

def prepareCheckout():
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		"authentication.userId": "8a8294174b7ecb28014b9699220015cc",
		"authentication.password": "sy6KJsT8",
		"authentication.entityId": "8a8294174b7ecb28014b9699a3cf15d1",
		"paymentType": "DB",
		"amount": "50.99",
		"currency": "AUD",
		"bankAccount.country": "AU",
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data))
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

checkoutId = prepareCheckout()["id"];
print checkoutId;