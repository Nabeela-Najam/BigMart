from django.urls import path
from backend import views


urlpatterns=[

    path('index/', views.index, name="index"),

    path('category/', views.category, name="category"),

    path('save_category/', views.save_category, name="save_category"),

    path('display_category/', views.display_category, name="display_category"),

    path('edit_category/<int:catid>', views.edit_category, name="edit_category"),

    path('update_category/<int:catid>', views.update_category, name="update_category"),

    path('delete_category/<int:catid>', views.delete_category, name="delete_category"),

    path('admin_login/', views.admin_login, name="admin_login"),

    path('adminlogin/', views.adminlogin, name="adminlogin"),

    path('Adminlogout/', views.Adminlogout, name="Adminlogout"),

    path('product/', views.product, name="product"),

    path('save_product/', views.save_product, name="save_product"),

    path('display_product/', views.display_product, name="display_product"),

    path('edit_product/<int:pid>/', views.edit_product, name="edit_product"),

    path('delete_product/<int:pid>/', views.delete_product, name="delete_product"),

    path('display_contact/', views.display_contact, name="display_contact"),

    path('delete_contact/<int:conid>/', views.delete_contact, name="delete_contact"),

]