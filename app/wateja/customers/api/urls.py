from django.urls import path
from . import views

urlpatterns = [
    # Overview endpoint
    path("", views.index, name="index"),
    # Business endpoints
    path("customers-list/", views.get_customers, name="get-customers"),
    path("customer-detail/<str:uuid>/", views.get_customer_detail,
         name="get-customer-detail"),
    path("customer-create/", views.add_customer, name="add-customer"),
    path("customer-update/<str:uuid>", views.update_customer,
         name="update-customer"),
    path("customer-delete/<str:uuid>", views.delete_customer,
         name="delete-customer"),
]
