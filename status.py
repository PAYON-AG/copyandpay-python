#!/usr/bin/python

import urllib, urllib2, json

def getPaymentStatus(checkoutId): 
	url = "https://test.oppwa.com/v1/checkouts/" + checkoutId + "/payment";
	try:
		response = urllib2.urlopen(url)
		return json.loads(response.read());
	except urllib2.HTTPError, e:
		return e.code;

status = getPaymentStatus("06C7C8B8924DF5B77D8F9CCDC2869853.sbg-vm-tx02")
if (status["result"]["code"].startswith("000")):
	print "SUCCESS <br/><br/> Here is the result of your transaction: <br/><br/>"
	print status
else:
	print "ERROR <br/><br/> Here is the result of your transaction: <br/><br/>";
	print status