from django.contrib import admin

from core.models import Doctor

# Register admin
admin.site.admin_view(Doctor)    
