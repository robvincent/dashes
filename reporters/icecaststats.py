#
# utilities for parsing XML status from icecast server
#
# by Rob Vincent - April 2011
#
import urllib2, xml.dom.minidom
import simplejson as json
from datetime import datetime

class IcecastStats:

	dash = {}
	dash['headers'] = ["Mount", "Name", "Listeners", "Peak"]
	dash['data'] = []

	def getText(self, nodelist):
	    rc = []
	    for node in nodelist.childNodes:
	        if node.nodeType == node.TEXT_NODE:
	            rc.append(node.data)
	    return ''.join(rc)

	def handleSources(self, sources):
		for source in sources:
			name = self.getText(source.getElementsByTagName("server_name")[0])
			mount = source.getAttribute('mount')
			listeners = self.getText(source.getElementsByTagName("listeners")[0])
			peak = self.getText(source.getElementsByTagName("listener_peak")[0])
			point = [mount, name, listeners, peak]
			self.dash['data'].append(point)
	
	def handleIceStats(self, icestats):
		self.handleSources(icestats.getElementsByTagName("source"))	

	
	def getStatistics(self, title, realm, uri, user, passwd):
		auth_handler = urllib2.HTTPBasicAuthHandler()
		auth_handler.add_password(realm=realm, uri=uri, user=user, passwd=passwd)
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
		xmlStats = urllib2.urlopen(uri).read()
		
		self.dash['title'] = title
		
		now = datetime.now()
		self.dash['updated'] = now.strftime('%Y-%m-%d %H:%M:%S')

		self.data= self.handleIceStats(xml.dom.minidom.parseString(xmlStats))

		print json.dumps(self.dash)
