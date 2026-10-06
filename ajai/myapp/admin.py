from django.contrib import admin
from .models import VehicleService_DB


class VehicleService_DBAdmin(admin.ModelAdmin):
    list_display = [
        "Service_ID",
        "Customer_Name",
        "Vehicle_No",
        "Service_Date",
        "Status"
    ]


admin.site.register(VehicleService_DB, VehicleService_DBAdmin)