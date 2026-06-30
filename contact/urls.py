from django.urls import path
from .views import contact_list, contact_detail

urlpatterns = [
    path("", contact_list, name="contact_list"),
    path("<int:pk>/", contact_detail, name="contact_detail"),
]