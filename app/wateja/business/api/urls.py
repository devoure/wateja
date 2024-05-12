from django.urls import path
from . import views

urlpatterns = [
    # Overview endpoint
    path("", views.index, name="index"),
    # Business endpoints
    path("business-list/", views.get_businesses, name="get-businesses"),
    path("business-detail/<str:uuid>/", views.get_business_detail,
         name="get-business-detail"),
    path("business-create/", views.add_business, name="add-business"),
    path("business-update/<str:uuid>", views.update_business,
         name="update-business"),
    path("business-delete/<str:uuid>", views.delete_business,
         name="delete-business"),
    # Categories endpoints
    path("business-cat-list/", views.get_business_categories,
         name="get-business-categories"),
    path("business-cat-detail/<str:uuid>/",
         views.get_business_category_detail,
         name="get-business-category-detail"),
    path("business-cat-create/", views.add_business_category,
         name="add-business-category"),
    path("business-cat-update/<str:uuid>",
         views.update_business_category,
         name="update-business-category"),
    path("business-cat-delete/<str:uuid>", views.delete_business_category,
         name="delete-business-category")
]
