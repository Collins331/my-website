from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('stk_push', views.stk_push, name='stk_push'),
    path('thank_you', views.thank_you, name='thank_you')
]
