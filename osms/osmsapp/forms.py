from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CreateHospitalDetailForm(ModelForm):
    class Meta:
        model = HospitalDetail
        fields = ['name','total_doctors','total_nurses', 'location', 'contact_details', 'mail_id']
# class CreateHospitalOxygenCylinderStockForm(ModelForm):
#     class Meta:
#         model = HospitalOxygenCylinderStock
#         fields = ['incoming_oxygen_cylinders_stock','oxygen_cylinders_taken_for_use']
# class CreateHospitalOxygenSupportedBedStockForm(ModelForm):
#     class Meta:
#         model = HospitalOxygenSupportedBedStock
#         # exclude = ['oxygen_supported_beds_remaining','id']
#         fields = ['oxygen_supported_beds_incoming','oxygen_supported_beds_in_use']
# class CreateSupplierDetailForm(ModelForm):
#     class Meta:
#         model = SupplierDetail
#         fields = ['name','location_of_supply_center','contact_details', 'mail_id']
#         # exclude = ['user','unique_supplier_id']
