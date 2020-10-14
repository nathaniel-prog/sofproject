from .models import Town , Hotels ,Appartement , User



def counttown():
    list=[1,2,4]
    for int in list:
        town=Town.objects.get(id=int)
        print(town)

counttown()

