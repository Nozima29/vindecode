from django.urls import path
from .views import *

urlpatterns = [
    path('<str:vin>/', CreateVin.as_view()),

]
