from django.urls import path
from AppMateo.views import *


urlpatterns = [
    path("familia/", familiares, name="familiares"),



]