from django.urls import path
from .views import ( Sign_Up,Sign_In,Sign_Out )

urlpatterns = [
    path('sign_up/',Sign_Up,name='Sign_Up'),
    path('sign_in/',Sign_In,name='Sign_In'),
    path('sign_out/',Sign_Out,name='Sign_Out')
]