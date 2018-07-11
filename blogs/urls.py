from django.urls import path
from . import views
     
urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('index/', views.index, name='index'),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
]