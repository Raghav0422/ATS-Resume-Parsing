from django.urls import path
from . import views

urlpatterns = [
    # ... your upload path ...
    path('home/', views.dashboard_view, name='dashboard'),
]