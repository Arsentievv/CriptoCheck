from django.urls import path
from .views import (
    RegistrationView,
    Login,
    Logout,
)

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

]