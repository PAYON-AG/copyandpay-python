#!/usr/bin/python

import urllib
import urllib2
import json

def prepareCheckout(): 
	url = "https://test.oppwa.com/v1/checkouts"
	data = {
		"authentication.userId": "8a8294184b4f2868014b4f86f767015d",
		"authentication.password": "F8T7N4PD",
		"authentication.entityId": "8a8294184b4f2868014b4f87bf160173",
		"paymentType": "DB",
		"amount": "50.99",
		"currency": "EUR"
	}
	try:
		response = urllib2.urlopen(url, urllib.urlencode(data) )
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

checkoutId = prepareCheckout()["id"];
print checkoutId