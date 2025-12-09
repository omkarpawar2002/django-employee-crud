from django.urls import path
from .views import ( Add_Employee,Show_Employee,Update_Employee,Delete_Employee )

urlpatterns = [
    path('add_emp/',Add_Employee,name='Add_Employee'),
    path('show_emp/',Show_Employee,name='Show_Employee'),
    path('update_emp/<int:pk>/',Update_Employee,name='Update_Employee'),
    path('delete_emp/<int:pk>/',Delete_Employee,name='Delete_Employee')
]