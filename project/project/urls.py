from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'), 
    path('login/', Login, name='login'),
    path('category/', category, name='category'),
    path('product/', product, name='product'),
    path('comment/', comment, name='comment'),
    path('savat/', savat, name='savat'),
    path('logout', Logout, name='logout'),
    path('detail/<int:id>/', detail, name='detail'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete_product, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
