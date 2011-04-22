#!/usr/bin/env python
#
# dashes reporter that pulls dashes from remote servers using "dashboard protocol"
#
# by Rob Vincent - April 2011
#
import urllib, urllib2, sys
import simplejson as json

tag = sys.argv[1]
fromHost = sys.argv[2]
toDirectory = sys.argv[3]

#
# experimenting with a key to add some security
#
if len(sys.argv) > 4:
	key = sys.argv[4]
else:
	key = ''

dashes = json.load(urllib2.urlopen('%s/list/%s' % (fromHost, key)))
for dashName in dashes:
	if (key == ''):
		urllib.urlretrieve('%s/view/%s' % (fromHost, dashName), '%s/%s_%s' % (toDirectory, tag, dashName))
	else:
		urllib.urlretrieve('%s/view/%s/%s' % (fromHost, dashName, key), '%s/%s_%s' % (toDirectory, tag, dashName))
