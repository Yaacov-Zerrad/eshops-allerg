from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('checkout/paypal', views.checkout_paypal),
    path('orders/', views.OrderList.as_view()),
]
