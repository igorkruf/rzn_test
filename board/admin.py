from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Cat, Genre


# Register your models here.



admin.site.register(Cat, DraggableMPTTAdmin )
admin.site.register(Genre, DraggableMPTTAdmin )

