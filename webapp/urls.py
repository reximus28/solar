from django.urls import path
from .views import home_view, about_page, order_view, create_customer, customer_list, update_customer, delete_customer

urlpatterns = [
    path('home/', home_view, name='home'),
    path('index/', about_page, name='about_page'),
    path('order/', order_view, name='place_order'),
    path('customer/create/', create_customer, name='create_customer'),
    path('customer/', customer_list, name='customer_list'),
    path('customer/update/', update_customer, name='update_customer'),
    path('customer/delete/', delete_customer, name='delete_customer'),
]