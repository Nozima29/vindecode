from django.urls import path
from .views import *

urlpatterns = [
    path('', view_vins),
    path('<str:vin>/', get_vin),

]
