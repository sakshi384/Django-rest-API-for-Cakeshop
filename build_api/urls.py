from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns=[
    path('register/',views.register_api.as_view(),name="register"),
    path('addcake/', views.Addcake.as_view(), name="addcake"),
    path('allcakes/', views.Allcake.as_view(), name="allcakes"),
    path('searchcake/', views.Searchcake.as_view(), name="searchcake"),
    path('descriptioncake/<int:pk>/', views.Descriptioncake.as_view(), name="descriptioncake"),
    path('addcaketocart/', views.Addcaketocart.as_view(), name="addcaketocart"),
    path('cart/', views.Cart.as_view(), name="cart"),
    path('removecakefromcart/',views.RemoveCakefromCart.as_view(),name="removecakefromcart"),
    path('checkout/', views.CheckOut.as_view(), name="checkout"),
    path('myorder/',views.MyOrder.as_view(),name="myorder"),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('change-password/',views.ChangePasswordView.as_view(), name='change-password'),


    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),

    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]