from django.contrib import admin
from .models import *
admin.site.register(HospitalDetail)
admin.site.register(HospitalOxygenCylinderStock)
admin.site.register(HospitalOxygenSupportedBedStock)
admin.site.register(SupplierDetail)