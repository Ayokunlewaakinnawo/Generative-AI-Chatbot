from django.urls import path
from .views import *

urlpatterns = [
    path('', chat, name='chat'),
    path('get-response/', get_response, name='get_response'),
]