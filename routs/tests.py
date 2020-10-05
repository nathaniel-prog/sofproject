from django.test import TestCase

# Create your tests here.


class Animal:
    def __init__(self,name,age):
         self.name= name
         self.age= age
         print(self.name , self.age)


    def aboyer(self):
        return print(f" i am{self.name}grrrrrrr")

   


class Mamifer(Animal):
    def __init__(self):
        self.name= 'coucoucou'
        Animal.__init__(self)
        return print("have 9 month pregency")





class Dogs(Animal):
    def __init__(self, name,age):
        self.name= name
        self.age= age
        #print("i am a dog ")
        super().aboyer()
        Animal.__init__(self,'chahon',43)



dog1 = Dogs('rocki ', 23)
dog1.aboyer()
dog1.name



class Diamand(Dogs,Mamifer):
    pass

d= Diamand()




