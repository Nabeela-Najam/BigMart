from django.urls import path
from webapp import views

urlpatterns=[

    path('', views.homepage, name="home"),

    path('about/', views.aboutpage, name="about"),

    path('contact/', views.contactpage, name="contact"),

    path('products/', views.ourproductspage, name="products"),

    path('save_contact/', views.save_contact, name="save_contact"),

    path('filtered_products/<cat_name>/', views.filtered_products, name="filtered_products"),

    path('single_product/<int:proid>/', views.single_product, name="single_product"),

    path('register/', views.register, name="register"),

    path('save_register/', views.save_register, name="save_register"),

    path('UserLogin/', views.UserLogin, name="UserLogin"),

    path('UserLogout/', views.UserLogout, name="UserLogout"),

    path('save_cart/', views.save_cart, name="save_cart"),

    path('cart/', views.cart, name="cart"),

    path('delete_item/<int:pid>/', views.delete_item, name="delete_item"),

    path('Userlogin/', views.Userlogin, name="Userlogin"),

]