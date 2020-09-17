from django.contrib import admin
from .models import Town ,Hotels , Appartement
from bemember.models import Post


admin.site.register(Town)
admin.site.register(Hotels)
admin.site.register(Post)
admin.site.register(Appartement)


# Register your models here.
