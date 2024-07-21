from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home-page'),
    path('register/',views.register, name='register'),
    path('login/',views.loginpage,name='login'),
     path('logout/',views.user_logout,name='logout'),
     path('delete-task/<uuid:id>',views.DeleteTask,name='delete'),
      path('update/<uuid:id>',views.Update,name='update')
]