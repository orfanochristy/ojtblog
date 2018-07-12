from django.urls import path
from . import views
from django.conf import settings
     
urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('index/', views.index, name='index'),
    path('post_details/<int:post_id>/', views.post_details, name='post_details'),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
    path('archivepost/<int:post_id>/', views.archivepost, name='archivepost'),
    path('archivelist/', views.archivelist, name='archivelist'),
    path('unarchivepost/<int:post_id>/', views.unarchivepost, name='unarchivepost'),
    path('search_form/', views.search_form, name='post_list'),
	path('search/', views.search, name="search"),
	path('search_result/<int:post_id>/', views.search_result, name='search_result'),
]

