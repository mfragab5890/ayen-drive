from django.urls import path
from .views import ayen_file_upload, ayen_file_search

urlpatterns = [
    path('file/upload/', ayen_file_upload),
    path('file/search/', ayen_file_search),

]
