from django.contrib import admin
from app.models import RobotCategory, Manufacturer, Robot

# Register your models here.
admin.site.register(RobotCategory)
admin.site.register(Manufacturer)
admin.site.register(Robot)
