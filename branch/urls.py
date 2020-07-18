from django.urls import path
from branch import views
app_name = "branch"
urlpatterns = [

    path('list/', views.BranchList.as_view(), name='branch_list'),
    path('view/<int:pk>', views.BranchDetails.as_view(), name='branch_view'),
    path('create/', views.BranchCreate.as_view(), name='branch_create'),
    path('update/<int:pk>', views.BranchUpdate, name='branch_edit'),
    path('delete/', views.BranchDelete, name='branch_delete'),
    path('search/',views.branch_search, name='search'),
]