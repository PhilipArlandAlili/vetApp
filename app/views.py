from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Owner, Pet, Appointment, Veterinarian, MedicalRecord

class OwnerListView(ListView):
    model = Owner
    template_name = 'owner_list.html'
    context_object_name = 'owners'

class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'owner_detail.html'
    context_object_name = 'owner'

class OwnerCreateView(CreateView):
    model = Owner
    template_name = 'owner_form.html'
    fields = ['name', 'email', 'phone_number']
    success_url = '/owners/'

class OwnerUpdateView(UpdateView):
    model = Owner
    template_name = 'owner_form.html'
    fields = ['name', 'email', 'phone_number']
    success_url = '/owners/'

class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'owner_confirm_delete.html'
    success_url = reverse_lazy('owner-list')



class PetListView(ListView):
    model = Pet
    template_name = 'pet_list.html'
    context_object_name = 'pets'

class PetDetailView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

class PetCreateView(CreateView):
    model = Pet
    template_name = 'pet_form.html'
    fields = ['name', 'species', 'birth_date', 'owner']
    success_url = '/pets/'

class PetUpdateView(UpdateView):
    model = Pet
    template_name = 'pet_form.html'
    fields = ['name', 'species', 'birth_date', 'owner']
    success_url = '/pets/'

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pet_confirm_delete.html'
    success_url = reverse_lazy('pet-list')  



class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment_list.html'
    context_object_name = 'appointments'

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'
    context_object_name = 'appointment'

class AppointmentCreateView(CreateView):
    model = Appointment
    template_name = 'appointment_form.html'
    fields = ['date', 'reason', 'pet']
    success_url = '/appointments/'

class AppointmentUpdateView(UpdateView):
    model = Appointment
    template_name = 'appointment_form.html'
    fields = ['date', 'reason', 'pet']
    success_url = '/appointments/'

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment-list')



class VeterinarianListView(ListView):
    model = Veterinarian
    template_name = 'veterinarian_list.html'
    context_object_name = 'veterinarians'

class VeterinarianDetailView(DetailView):
    model = Veterinarian
    template_name = 'veterinarian_detail.html'
    context_object_name = 'veterinarian'

class VeterinarianCreateView(CreateView):
    model = Veterinarian
    template_name = 'veterinarian_form.html'
    fields = ['name', 'email', 'specialty']
    success_url = '/veterinarians/'

class VeterinarianUpdateView(UpdateView):
    model = Veterinarian
    template_name = 'veterinarian_form.html'
    fields = ['name', 'email', 'specialty']

class VeterinarianDeleteView(DeleteView):
    model = Veterinarian
    template_name = 'veterinarian_confirm_delete.html'
    success_url = reverse_lazy('veterinarian-list')

class VeterinarianAppointmentListView(ListView):
    model = Veterinarian
    template_name = 'veterinarian_appointment_list.html'
    context_object_name = 'veterinarian'

    def get_queryset(self):
        veterinarian = Veterinarian.objects.get(pk=self.kwargs['pk'])
        return veterinarian.appointments.all()
    

class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'medical_record_list.html'
    context_object_name = 'medical_records'

class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'medical_record_detail.html'
    context_object_name = 'medical_record'

class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    template_name = 'medical_record_form.html'
    fields = ['diagnosis', 'treatment', 'appointment', 'cost']
    success_url = '/medical-records/'

class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    template_name = 'medical_record_form.html'
    fields = ['diagnosis', 'treatment', 'appointment', 'cost']

class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'medical_record_confirm_delete.html'
    success_url = reverse_lazy('medical-record-list')