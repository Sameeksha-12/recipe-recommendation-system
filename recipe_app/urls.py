from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL for the dashboard
    path('recommendations/', views.recommendations, name='recommendations'),  # URL for recommendations
    path('recipe/<int:ID>/', views.recipe_details, name='recipe_details')
]
