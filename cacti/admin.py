from django.contrib import admin

# Register your models here.
from cacti.models import User
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')
admin.site.register(User,UserAdmin)