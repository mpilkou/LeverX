from django.urls import path
from . import views

# login
urlpatterns = [
    path('login', views.api_login),
    path('signup', views.api_signup),
    path('logout', views.api_logout),

    # course
    path('course', views.course),

    path('test', views.test),

    
]
