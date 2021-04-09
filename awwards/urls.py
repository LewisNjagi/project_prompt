from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
#     path('profile/<str:username>',views.profile,name = 'profile'),
#     path('review/<post>', views.review, name='review'),
#     path('api/profile/', views.ProfileList.as_view()),
#     path('api/users/', views.UserList.as_view()),
#     path('api/posts/', views.PostList.as_view()),
]