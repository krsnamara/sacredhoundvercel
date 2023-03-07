from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# app_name = 'sacred_hound_store'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.carts_detail, name='cart'),
    path('carts/<int:pk>/update/', views.CartUpdate.as_view(), name='carts_update'),
    path('carts/<int:pk>/delete/', views.CartDelete.as_view(), name='carts_delete'),
    path('shop/<int:item_id>/', views.item_detail, name='detail'),
    path('shop/create/', views.ItemCreate.as_view(), name='item_create'),
    path('shop/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('shop/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
    # path('cart/assoc_item/<int:item_id>/', views.assoc_item, name='add_to_cart')
    ]   