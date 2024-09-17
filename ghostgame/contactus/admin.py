from django.contrib import admin
from .models import ticket
class ticketAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","subject")
# Register your models here.
admin.site.register(ticket,ticketAdmin)