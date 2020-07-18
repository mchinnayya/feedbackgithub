from django.urls import path
from account import views
app_name = "account"
urlpatterns = [

    path('list/', views.AccountUserList.as_view(), name='accountuser_list'),
    path('view/<int:pk>', views.AccountUserDetails.as_view(), name='accountuser_view'),
    path('create/', views.AccountCreate.as_view(), name='accountuser_create'),
    path('update/<int:pk>', views.account_user_update, name='accountuser_edit'),
    path('delete', views.delete_user_details, name='accountuser_delete'),
    path('search/',views.account_search, name='search'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    # path('user/assign/', views.role_assign, name='role_assign'),

]