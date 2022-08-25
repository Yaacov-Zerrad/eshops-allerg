from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', views.LasterProductList.as_view()),
]
