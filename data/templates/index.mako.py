# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1303347770.8929169
_template_filename='/Users/rvincent/Workspace/pylons/dashes/main/templates/index.mako'
_template_uri='/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        app_globals = context.get('app_globals', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n  <head>\n    <title>')
        # SOURCE LINE 5
        __M_writer(escape(app_globals.TITLE))
        __M_writer(u'</title>\n\t<link rel="stylesheet" href="/styles.css" type="text/css" />\n  </head>\n  <body>\n\t<div id="header">\n  \t\t<h1>')
        # SOURCE LINE 10
        __M_writer(escape(app_globals.TITLE))
        __M_writer(u'</h1>\n    </div>\n\t<div id="body">\n\t\t')
        # SOURCE LINE 13
        __M_writer(escape(c.body))
        __M_writer(u'\n\t</div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


