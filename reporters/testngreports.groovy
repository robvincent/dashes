#!/usr/bin/env groovy

import org.json.simple.JSONObject
import org.json.simple.JSONArray

def dash = new JSONObject()
dash.put("title", "TextNG Errors")
dash.put("updated", new Date().getDateTimeString())

def headers = new JSONArray()
headers.add("Class")
headers.add("Method")
dash.put("headers", headers)

def data = new JSONArray()

def url = new URL(args[0])
def input = new InputStreamReader(url.openStream())

def suites = new XmlParser().parse(input)
for (record in suites.test.classes.class) {
  def className = record.'@name'
  for (test in record.methods.include) {
	/* always lists these two methods, even with no errors */
    if (!"setUp".equals(test.'@name') && !"tearDown".equals(test.'@name')) {
		def point = new JSONArray()
		point.add(className)
		point.add(test.'@name')
		data.add(point)
    }
  }
}

dash.put("data", data)

print dash.toString()
