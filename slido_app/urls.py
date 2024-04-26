from slido_app.views import home
from django.urls import path

urlpatterns = [
    path('', view=home, name='home'),
]