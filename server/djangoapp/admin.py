from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here


from .models import *
# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)
