from django.urls import path
from role import views

app_name = "role"
urlpatterns = [

    path('list/', views.RoleList.as_view(), name='role_list'),
    path('view/<int:pk>', views.RoleDetails.as_view(), name='role_view'),
    path('create/', views.RoleCreate.as_view(), name='role_create'),
    path('update/<int:pk>', views.role_update, name='role_edit'),
    path('delete/', views.role_delete, name='role_delete'),


]
