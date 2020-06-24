from django.contrib import admin

from .models import Division, Farm
# Register your models here.


class DivisionAdmin(admin.ModelAdmin):
    list_display = (
        "division_name",
        "division_code",
    )


admin.site.register(Division, DivisionAdmin)
admin.site.register(Farm)
