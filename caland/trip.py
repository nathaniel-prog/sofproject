import datetime

import pytz

dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
#print(dt_mtn.strftime('%B %d,%Y'))

"""
import pytz

dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
#print(dt_mtn.strftime('%B %d,%Y'))


Put this in your template (in my case agenda/month_cal.html):

<table class="cal_month_calendar">
<tr>
{% for day in headers %}
<th>{{ day|date:"D"|slice:":2" }}</hd>
{% endfor %}
</tr>
{% for week in calendar %}
<tr>
{% for day in week %}
<td{% if not day.in_month %} class="cal_not_in_month"{% endif %}>{% if day.event %}<a href="/calendar/{{ day.day|date:"Y/m" }}/">{{ day.day|date:"j" }}</a>{% else %}{{ day.day|date:"j" }}{% endif %}</td>
{% endfor %}
</tr>
{% endfor %}
</table>

"""
dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
#print(dt_mtn)
#print(dt_mtn.strftime('%B %d,%Y'))
dt_str= 'September 11,2020'
dt=datetime.datetime.strptime(dt_str,'%B %d,%Y')
#print(dt)


dtday= datetime.date.today()
a_date= datetime.date(2020,9,11)
#print(a_date)
tdelta= datetime.timedelta(weeks=7)
f_date= dtday + tdelta
#print(f_date)



#print(dt)
# strftime= convert a datetime to str
# strptime= convert a str to a datztimd

def book_date(dtday,days):
    t_delta=datetime.timedelta(days=days)
    end_day= dtday + t_delta
    print(end_day)
    return end_day

book_date(dtday,23)





