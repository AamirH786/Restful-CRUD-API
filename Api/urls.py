from django.urls import path
from . import views

# Create Your Urls Here

urlpatterns = [
    path('', views.GetEmployeeDetails, name='GetDetails'),
    path('<int:id>/', views.GetEditDel, name='UpdateRemove'),
]


