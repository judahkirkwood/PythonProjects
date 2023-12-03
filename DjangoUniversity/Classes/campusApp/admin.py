from django.contrib import admin
from .models import UniversityCampus
# Register your models here.
class UniversityCampusAdmin(admin.ModelAdmin):
    # Customize the way UniversityCampus is displayed in the admin site if needed
    list_display = ('campus_name', 'state', 'campus_id')

admin.site.register(UniversityCampus, UniversityCampusAdmin)
