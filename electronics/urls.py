from django.urls import path
from . import views
from .views import details

urlpatterns = [
path('home', views.home, name='home'),
path('about', views.about, name='about'),
path('signup', views.signup, name='signup'),
path('details', details, name='details'),
# path('smartphones/', views.smartphones, name='smartphones'),


path('product/<str:id>/update/', views.update_product, name='update_product'),
path('product/<str:id>/delete/', views.delete_product, name='delete_product'),

path('product/create/', views.create_product, name='create_product'),

# path('product/<int:id>/', views.product_detail, name='product'),
]