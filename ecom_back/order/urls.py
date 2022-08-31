from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('checkout/paypal', views.checkout_paypal),
    path('checkout/valid-paypal/<int:pk>/', views.ValidePaypalClass.as_view()),
    # path('checkout/valide-paypal', views.valide_paypal),
    path('orders/', views.OrdersList.as_view()),
]
