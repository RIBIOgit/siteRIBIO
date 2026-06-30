from django.urls import path
from .views import content_list, content_detail

urlpatterns = [
    path("", content_list, name="content_list"),
    path("<int:pk>/", content_detail, name="content_detail"),
]   