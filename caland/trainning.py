import datetime
import pytz

dt_mtn=datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
print(dt_mtn.strftime('%B %d,%Y'))
dt_str= 'September 11,2020'
dt=datetime.datetime.strptime(dt_str,'%B %d,%Y')
print(dt)

t = datetime.date(2020,10,5)
print(t)


def my_ftion( *args):# le faire egalement sans le *
    for arg in args:
        print(arg)


colors=("blueu", "red")
person=["nathaniel", "manue"]

#my_ftion("jeanpiere ", "florence","flo",,person)

my_ftion(*person,*colors)
#print(colors[1])
my_ftion(person,colors)
