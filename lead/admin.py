from django.contrib import admin
from lead.models import lead

class leadAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'phone', 'date'
   

admin.site.register(lead, leadAdmin)



