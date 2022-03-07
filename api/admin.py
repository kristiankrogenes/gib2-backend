from django.contrib import admin
from .models import CurrentPosition, Developer, GasStation, Price

admin.site.register(Developer)
admin.site.register(CurrentPosition)
admin.site.register(GasStation)
admin.site.register(Price)