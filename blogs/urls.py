from django.urls import path
from . import views
from django.conf import settings
     
urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('index/', views.index, name='index'),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
    path('archivepost/<int:post_id>/', views.archivepost, name='archivepost'),
    path('archivelist/', views.archivelist, name='archivelist'),
    path('unarchivepost/<int:post_id>/', views.unarchivepost, name='unarchivepost'),
]
