from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add-category', views.CategoryCreateView.as_view(), name="add-category"),
    # path('add-product', views.new_product, name="add-product"),
    # path('product/<int:pk>/renew', views.renew_product_librarian, name='renew-product-librarian'), #??
]

