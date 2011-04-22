#!/usr/bin/env python
#
# dashes reporter for icecast status
#
# by Rob Vincent - April 2011
#
from icecaststats import IcecastStats

stats = IcecastStats()
stats.getStatistics('icecast.example.com','Icecast Realm','http://icecast.example.com/admin/','admin','admin-password')
		
	
