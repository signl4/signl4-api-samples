import sys
import json
import urllib2
import gzip
from collections import OrderedDict


# Triggers a new Signl with 3 dedicated parameters in category "Temperature"
def TriggerSignl():

	apiKey='Bearer XYZ' # TODO: Replace with your SIGNL4 API key
	requestURL = 'https://connect.signl4.com/api/alerts'

	parameters = [ OrderedDict(
			name='Temperature',
			value='28.1 °C',
			type=0
		),
		OrderedDict(
			name='Humidity',
			value='17.9%',
			type=0
		),
		OrderedDict(
			name='Container ID',
			value='09_LAP',
			type=0
		)
	]

	body = OrderedDict(
		title='Critical Temperature',
		text='Fluid temperature increased warning.',
		category='Temperature', #Replace with any of your team's categories
		parameters=parameters,
		severity=0,
		flags=0
	)	

	print >> sys.stderr, "INFO Sending POST request to url=%s with size=%d bytes payload" % (requestURL, len(body))
	print >> sys.stderr, "INFO Body: %s" % body

	try:
		req = urllib2.Request(requestURL, json.dumps(body), {"Content-Type": "application/json", "Authorization": apiKey})
		res = urllib2.urlopen(req)
		if 200 <= res.code < 300:
			print >> sys.stderr, "INFO SIGNL4 API responded with HTTP status=%d" % res.code
			return True
		else:
			print >> sys.stderr, "ERROR SIGNL4 API responded with HTTP status=%d" % res.code
			return False
	except urllib2.HTTPError, e:
		print >> sys.stderr, "ERROR Error sending SIGNL4 API request: %s" % e
	except urllib2.URLError, e:
		print >> sys.stderr, "ERROR Error sending SIGNL4 API request: %s" % e
	except ValueError, e:
		print >> sys.stderr, "ERROR Invalid URL: %s" % e
	return False


TriggerSignl()