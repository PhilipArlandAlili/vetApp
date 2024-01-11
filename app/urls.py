from .views import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .views import PetListView, PetDetailView, PetCreateView, PetUpdateView, PetDeleteView
from .views import AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView
from .views import VeterinarianListView, VeterinarianDetailView, VeterinarianCreateView, VeterinarianUpdateView, VeterinarianDeleteView, VeterinarianAppointmentListView
from .views import MedicalRecordListView, MedicalRecordDetailView, MedicalRecordCreateView, MedicalRecordUpdateView, MedicalRecordDeleteView
from django.urls import path

urlpatterns = [
    path('', OwnerListView.as_view(), name='owner-list'),
    path('owners/', OwnerListView.as_view(), name='owner-list'),
    path('owners/<int:pk>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('owners/create/', OwnerCreateView.as_view(), name='owner-create'),
    path('owners/<int:pk>/update/', OwnerUpdateView.as_view(), name='owner-update'),
    path('owners/<int:pk>/delete/', OwnerDeleteView.as_view(), name='owner-delete'),

    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
    path('pets/create/', PetCreateView.as_view(), name='pet-create'),
    path('pets/<int:pk>/edit/', PetUpdateView.as_view(), name='pet-edit'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),

    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment-edit'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),

    path('veterinarians/', VeterinarianListView.as_view(), name='veterinarian-list'),
    path('veterinarians/<int:pk>/', VeterinarianDetailView.as_view(), name='veterinarian-detail'),
    path('veterinarians/create/', VeterinarianCreateView.as_view(), name='veterinarian-create'),
    path('veterinarians/<int:pk>/edit/', VeterinarianUpdateView.as_view(), name='veterinarian-edit'),
    path('veterinarians/<int:pk>/delete/', VeterinarianDeleteView.as_view(), name='veterinarian-delete'),
    path('veterinarians/<int:pk>/appointments/', VeterinarianAppointmentListView.as_view(), name='veterinarian-appointment-list'),

    path('medical-records/', MedicalRecordListView.as_view(), name='medical-record-list'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('medical-records/create/', MedicalRecordCreateView.as_view(), name='medical-record-create'),
    path('medical-records/<int:pk>/edit/', MedicalRecordUpdateView.as_view(), name='medical-record-edit'),
    path('medical-records/<int:pk>/delete/', MedicalRecordDeleteView.as_view(), name='medical-record-delete'),
]