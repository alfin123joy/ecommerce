from django.urls import path
from.import views
from ecomm_app.views import login


urlpatterns = [
    path('register', views.register,name="register"),
    path('', views.login,name="login"),
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('single/<int:pk>/',views.single,name="single"),
    path('cart/<int:pk>/', views.cart,name='cart'),
    path('view_cart', views.view_cart,name='view_cart'),
    path('blog', views.blog,name="blog"),
    path('checkout', views.checkout,name="checkout"),
    path('services', views.services,name="services"),
    path('thankyou', views.thankyou,name="thankyou"),
    path('shop', views.shop,name="shop"),
    path('contact', views.contact,name="contact"),
   

  
]
