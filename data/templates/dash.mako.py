# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1302757192.2236741
_template_filename='/Users/rvincent/Workspace/pylons/dashboard/main/templates/dash.mako'
_template_uri='/dash.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['printHeaders']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def printHeaders(headers):
            return render_printHeaders(context.locals_(__M_locals),headers)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n\n<div class="dash">\n  <span class="title">')
        # SOURCE LINE 10
        __M_writer(escape(c.title))
        __M_writer(u'</span>\n  <table>\n    ')
        # SOURCE LINE 12
        __M_writer(escape(printHeaders(c.headers)))
        __M_writer(u'\n')
        # SOURCE LINE 13
        if not c.data:
            # SOURCE LINE 14
            __M_writer(u'\t<tr><td colspan="')
            __M_writer(escape(len(c.headers)))
            __M_writer(u'" align="center">No data available</td></tr>\n')
            # SOURCE LINE 15
        else:
            # SOURCE LINE 16
            __M_writer(u'\t')
            i=1 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            # SOURCE LINE 17
            for row in c.data:
                # SOURCE LINE 18
                __M_writer(u'    <tr class="')
                __M_writer(escape(['odd','even'][i%2]))
                __M_writer(u'">\n')
                # SOURCE LINE 19
                for value in row:
                    # SOURCE LINE 20
                    __M_writer(u'      <td>')
                    __M_writer(escape(value))
                    __M_writer(u'</td>\n')
                    pass
                # SOURCE LINE 22
                __M_writer(u'    </tr>\n    ')
                # SOURCE LINE 23
                i = i+1 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                pass
            pass
        # SOURCE LINE 26
        __M_writer(u'  </table>\n  <span class="updated">UPDATED: ')
        # SOURCE LINE 27
        __M_writer(escape(c.updated))
        __M_writer(u'</span><br/>\n  <span class="note">')
        # SOURCE LINE 28
        __M_writer(escape(c.note))
        __M_writer(u'</span>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_printHeaders(context,headers):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <tr>\n')
        # SOURCE LINE 3
        for h in headers:
            # SOURCE LINE 4
            __M_writer(u'      <th>')
            __M_writer(escape(h))
            __M_writer(u'</th>\n')
            pass
        # SOURCE LINE 6
        __M_writer(u'    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


