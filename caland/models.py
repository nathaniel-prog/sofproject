from django.db import models

import datetime
import pytz

dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
#print(dt_mtn.strftime('%B %d,%Y'))
dt_str= 'September 11,2020'
dt=datetime.datetime.strptime(dt_str,'%B %d,%Y')
#print(dt)
# strftime= convert a datetime to str
# strptime= convert a str to a datztimd


#t_d= datetime.datetime.today()
#t_x=datetime.datetime.now()
#t_w=datetime.datetime.utcnow()


class Trip(models.Model):
    start_date= models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f"you book from {self.start_date} until {self.end_date} "





