<%def name="printHeaders(headers)">
    <tr>
    % for h in headers:
      <th>${h}</th>
    % endfor
    </tr>
</%def>

<div class="dash">
  <span class="title">${c.title}</span>
  <table>
    ${printHeaders(c.headers)}
	% if not c.data:
	<tr><td colspan="${len(c.headers)}" align="center">No data available</td></tr>
	% else:
	<% i=1 %>
    % for row in c.data:
    <tr class="${['odd','even'][i%2]}">
      % for value in row:
      <td>${value}</td>
      % endfor
    </tr>
    <% i = i+1 %>
    % endfor
	% endif
  </table>
  <span class="updated">UPDATED: ${c.updated}</span><br/>
  <span class="note">${c.note}</span>
</div>
