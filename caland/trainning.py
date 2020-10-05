



def my_ftion( *args):# le faire egalement sans le *
    for arg in args:
        print(arg)


colors=("blueu", "red")
person=["nathaniel", "manue"]

#my_ftion("jeanpiere ", "florence","flo",,person)

my_ftion(*person,*colors)
#print(colors[1])
my_ftion(person,colors)
