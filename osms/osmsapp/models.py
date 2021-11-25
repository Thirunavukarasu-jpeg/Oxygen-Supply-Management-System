from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from osms.settings import EMAIL_HOST_USER

class HospitalDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    unique_hospital_id = models.CharField(max_length=1000,null=False,blank=False, unique=True)
    name = models.CharField(max_length=1000,null=False,blank=False)
    location = models.CharField(max_length=1000,null=False,blank=False)
    total_doctors = models.IntegerField(blank=True,default=0)
    total_nurses = models.IntegerField(blank=True,default=0)
    contact_details = models.CharField(max_length=1000,null=False,blank=False)
    mail_id = models.EmailField(max_length=254)


    def __str__(self):
        return self.unique_hospital_id


    
class HospitalOxygenCylinderStock(models.Model):
    id = models.AutoField(primary_key=True)
    unique_hospital_id = models.CharField(max_length=1000,null=False,blank=False, unique=True)
    name = models.CharField(max_length=1000,null=False,blank=False)
    total_oxygen_cylinders_stock = models.IntegerField(blank=True,default=0)
    incoming_oxygen_cylinders_stock = models.IntegerField(blank=True,default=0)
    oxygen_cylinders_in_use = models.IntegerField(blank=True,default=0)
    oxygen_cylinders_taken_for_use = models.IntegerField(blank=True,default=0)
    oxygen_cylinders_remaining = models.IntegerField(blank=True,default=0)
    

    def calculate(self):
        print(self.incoming_oxygen_cylinders_stock)
        self.total_oxygen_cylinders_stock += self.incoming_oxygen_cylinders_stock
        self.oxygen_cylinders_in_use += self.oxygen_cylinders_taken_for_use
        oxygen_cylinders_remaining = (self.total_oxygen_cylinders_stock) - (self.oxygen_cylinders_in_use)
        self.oxygen_cylinders_taken_for_use = 0
        self.incoming_oxygen_cylinders_stock = 0
        if oxygen_cylinders_remaining < 20:
            send_mail('jhiii', 'dciadbci', EMAIL_HOST_USER, ['mailme.thiru.sum@gmail.com'])
        return oxygen_cylinders_remaining

    def save(self, *args, **kwargs):
        self.oxygen_cylinders_remaining = self.calculate()
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.unique_hospital_id)


    

class HospitalOxygenSupportedBedStock(models.Model):
    id = models.AutoField(primary_key=True)
    unique_hospital_id = models.CharField(max_length=1000,null=False,blank=False, unique=True)
    name = models.CharField(max_length=1000,null=False,blank=False)
    total_oxygen_supported_beds = models.IntegerField(blank=True,default=0)
    oxygen_supported_beds_incoming = models.IntegerField(blank=True,default=0)
    oxygen_supported_beds_in_use = models.IntegerField(blank=True,default=0)
    oxygen_supported_beds_taken_for_use = models.IntegerField(blank=True,default=0)
    oxygen_supported_beds_free_for_use = models.IntegerField(blank=True,default=0)
    oxygen_supported_beds_remaining = models.IntegerField(blank=True,default=0)
    
    def calculate(self):
        oxygen_supported_beds_remaining = (self.total_oxygen_supported_beds+self.oxygen_supported_beds_incoming+self.oxygen_supported_beds_free_for_use) - (self.oxygen_supported_beds_in_use+self.oxygen_supported_beds_taken_for_use)
        self.oxygen_supported_beds_in_use += self.oxygen_supported_beds_taken_for_use - self.oxygen_supported_beds_free_for_use
        self.total_oxygen_supported_beds += self.oxygen_supported_beds_incoming
        self.oxygen_supported_beds_free_for_use = 0
        self.oxygen_supported_beds_incoming = 0
        self.oxygen_supported_beds_taken_for_use = 0
        return oxygen_supported_beds_remaining

    def save(self, *args, **kwargs):
        self.oxygen_supported_beds_remaining = self.calculate()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.unique_hospital_id)

    

class SupplierDetail(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000,null=False,blank=False)
    location_of_supply_center = models.CharField(max_length=1000,null=False,blank=False)
    contact_details = models.CharField(max_length=1000,null=False,blank=False)
    mail_id = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


   
