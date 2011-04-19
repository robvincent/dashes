Dashes - the very simplest dashboard system possible.

by Rob Vincent (rob.vincent@rocketmail.com)
April 2011

Reads report files, called dashes, and displays each in a div-tag on a single web page.  Dashes are written
in JSON format with only a few standard fields: title, updated, headers, note, and data (which is an
array of arrays).

Sample scripts for generating dashes are in the /reporters directory.

Besides displaying the dashes, the application also returns a list of the dash files (/list) and can either
display (/view/<dashname.dash>) or retrieve specific dashes (/get/<dashname.dash>). This is for collecting
dashes from other dashboard servers.


CONFIGURATION
=============

- set application/page title and number of columns in lib/app_globals.py
- email to receive alerts in /production.ini
- number of columns in /

IDEAS FOR IMPROVEMENTS
======================

- add a level of security by assigning keys to each dashboard server
- add scripting (such as ERB) to make dashes more dynamic or allow mashing separate or distributed dashes
- graphs
- display changes in dash values
- sort by time or priority
- coding for links and alerts for dash values
