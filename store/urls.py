from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('subcategories/', views.get_subcategories, name='subcategories'),
    path('get_more_categories/', views.get_more_categories, name='get_more_categories'),
    path('more_categories/<str:subcategory_id>', views.more_categories, name='more_categories'),
    path('more_category/<str:more_category_id>', views.more_category, name='more_category'),
    path('brand/<str:brand_id>', views.brand, name='brand'),
    path('sort_by_price/<str:subcategory_id>/<str:price>', views.sort_by_price, name='sort_by_price'),
    path('sort_by_price_more_category/<str:more_category_id>/<str:price>', views.sort_by_price_more_category, name='sort_by_price_more_category'),
    path('sort_by_price_brand/<str:brand_id>/<str:price>', views.sort_by_price_brand, name='sort_by_price_brand'),
    path('product_details/<str:product_id>', views.product_details, name='product_details'),
    path('order_item/', views.order_item, name='order_item'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart_item/', views.delete_cart_item, name='delete_cart_item'),
    path('increment_quantity/', views.increment_quantity, name='increment_quantity'),
    path('decrement_quantity/', views.decrement_quantity, name='decrement_quantity'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist_item/', views.wishlist_item, name='wishlist_item'),
    path('delete_wishlist_item/', views.delete_wishlist_item, name='delete_wishlist_item'),
    path('checkout/', views.checkout, name='checkout'),
]
