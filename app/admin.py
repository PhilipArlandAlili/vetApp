from django.contrib import admin
from .models import Veterinarian, Pet, Owner, MedicalRecord, Appointment

admin.site.register(Veterinarian)
admin.site.register(MedicalRecord)
admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Appointment)

# @admin.register(Veterinarian)
# class VeterinarianAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'licenseNumber')
#     search_fields = ('first_name', 'last_name', 'licenseNumber')

# @admin.register(AnimalPatient)
# class AnimalPatientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'species', 'age')
#     search_fields = ('name', 'species')

# @admin.register(Petowner)
# class PetownerAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'birth_date', 'petname')
#     search_fields = ('first_name', 'last_name', 'birth_date', 'petname')

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     PAYMENT_METHOD_CHOICES = [
#         ('cash', 'Cash'),
#         ('credit_card', 'Credit Card'),
#     ]

# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('veterinarian', 'animal_patient', 'appointment_date')
#     list_display = ('veterinarian', 'animal_patient', 'appointment_date')

