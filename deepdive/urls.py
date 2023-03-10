from django.urls import path 
from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("user", views.user, name="user"),
    path('post/<slug:slug>',views.post_details,name='post_details'),
    path('add_item',views.add_item,name='add_item'),
    path('create_post',views.create_post,name='create_post'),
    path('completed',views.completed,name='completed'),
    path('analyzingPeople',views.analyzingPeople,name='analyzingPeople'),
    path('add_analysis',views.add_analysis,name='add_analysis'),
    path('journal',views.journal,name='journal'),
    path('add_journal',views.add_journal,name='add_journal'),
    path('mindfulness',views.mindfulness,name='mindfulness'),
    path('create_image',views.create_image,name='create_image'),
]