import logging, glob, time, os.path
#import yaml
import simplejson as json
from pylons import request, response, session, config, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from webhelpers.html import literal

from main.lib.base import BaseController, render

log = logging.getLogger(__name__)

class DashController(BaseController):
	
	NUM_COLUMNS=2
	
	def read_dash(self, fname):
		try:
			dash = json.load(file(fname))
			c.title = dash.get('title', os.path.basename(fname))
			c.updated = dash.get('updated', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.path.getmtime(fname))))
			c.headers = dash.get('headers', [])
			c.note = dash.get('note', '')
			c.data = dash.get('data', [])
			return render('/dash.mako')
		except:
			return "ERROR - %s" % fname
		
	def scan_dashes(self):
		body = ""
		files = glob.glob('%s/dashes/*.dash' % config['global_conf']['here'])
		files.sort()
		col = 0
		for f in files:
			body += self.read_dash(f)
			col += 1
   			if (col >= self.NUM_COLUMNS):
				col = 0
				body += literal(u'<br clear="both">')
                
		return body
		
	def list(self):
		files = [os.path.basename(f) for f in glob.glob('%s/dashes/*.dash' % config['global_conf']['here'])]
		return json.dumps(files)
		
	def view(self, id):
		f = open('%s/dashes/%s' % (config['global_conf']['here'], id))
		return f.read()
		
	def get(self, id):
		response.headers['Content-type'] = 'text/json'
		return self.view(id)
		
	def index(self):
		c.body = self.scan_dashes()
		return render('/index.mako')
