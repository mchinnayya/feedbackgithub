from django.urls import path
from dynamicform.backgroundimage import views
from feedback import settings
from django.conf.urls.static import static
from django.conf import settings

app_name = 'backgroundimage'
urlpatterns = [

    path('list/<int:formmasterid>', views.BackgroundImageList.as_view(), name='backgroundimage_list'),
    path('create/<int:formmasterid>', views.BackgroundImageCreate.as_view(), name='backgroundimage_create'),
    path('delete/', views.backgroundimage_delete, name='backgroundimage_delete'),


]