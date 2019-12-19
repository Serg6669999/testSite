from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='page'),
    path('data', views.page, name='data'),
    path('slack', views.slack, name='slack'),
    path('email', views.send_data_users, name='email'),
]
