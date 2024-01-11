from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Owner(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pet(BaseModel):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name

class Appointment(BaseModel):
    date = models.DateTimeField()
    reason = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f"{self.pet.name}'s appointment on {self.date}"

class Veterinarian(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    specialty = models.CharField(max_length=100)
    appointments = models.ManyToManyField(Appointment, related_name='veterinarians')

    def __str__(self):
        return self.name

class MedicalRecord(BaseModel):
    diagnosis = models.TextField()
    treatment = models.TextField()
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='medical_record')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Medical record for {self.appointment.pet.name} on {self.appointment.date}"
