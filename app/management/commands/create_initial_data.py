import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from app.models import Owner, Pet, Appointment, Veterinarian, MedicalRecord

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Populating the database..."))

        # Create Owners
        owners = []
        for _ in range(10):
            owner = Owner.objects.create(
                name=f"Owner-{random.randint(1, 100)}",
                email=f"owner_{random.randint(1, 100)}@example.com",
                phone_number=f"+1234567890"
            )
            owners.append(owner)

        # Create Pets for each Owner
        pets = []
        for owner in owners:
            for _ in range(10):
                pet = Pet.objects.create(
                    name=f"Pet-{random.randint(1, 100)}",
                    species=f"Species-{random.randint(1, 10)}",
                    birth_date=datetime.now() - timedelta(days=random.randint(365, 3650)),
                    owner=owner
                )
                pets.append(pet)

        # Create Appointments for each Pet
        appointments = []
        for pet in pets:
            for _ in range(10):
                appointment = Appointment.objects.create(
                    date=datetime.now() + timedelta(days=random.randint(1, 30)),
                    reason=f"Reason-{random.randint(1, 100)}",
                    pet=pet
                )
                appointments.append(appointment)

        # Create Veterinarians
        veterinarians = []
        for _ in range(5):
            veterinarian = Veterinarian.objects.create(
                name=f"Vet-{random.randint(1, 100)}",
                email=f"vet_{random.randint(1, 100)}@example.com",
                specialty=f"Specialty-{random.randint(1, 5)}"
            )
            veterinarians.append(veterinarian)

        # Assign Veterinarians to Appointments
        for appointment in appointments:
            appointment.veterinarians.set(random.sample(veterinarians, random.randint(1, 3)))

        # Create Medical Records for each Appointment
        for appointment in appointments:
            medical_record = MedicalRecord.objects.create(
                diagnosis=f"Diagnosis-{random.randint(1, 100)}",
                treatment=f"Treatment-{random.randint(1, 100)}",
                cost=random.uniform(50.0, 500.0),
                appointment=appointment
            )

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
