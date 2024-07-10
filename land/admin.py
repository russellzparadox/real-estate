from django.contrib import admin
from .models import Land, TypeOfPropertyUse, Status

# Register your models here.
admin.site.register(Land)
admin.site.register(TypeOfPropertyUse)
admin.site.register(Status)
