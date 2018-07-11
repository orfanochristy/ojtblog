from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.Register,name='Register'),
    path('signin/', views.Signin,name='Signin'),    
    path('dashboard/<int:user_id>/', views.Dashboard,name='Dashboard'),    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
