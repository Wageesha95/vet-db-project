from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('farms', views.farms, name='farms'),
    path('farm/<int:farm_id>', views.farm, name="farm"),
    path('divisions', views.divisions, name="divisions"),
    path('division/<int:division_id>', views.division, name="division")
]