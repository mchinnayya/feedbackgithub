from django.urls import path
from organization import views
app_name = "organization"
urlpatterns = [

    path('list/', views.OrganizationList.as_view(), name='organization_list'),
    path('view/<int:pk>', views.OrganizationDetails.as_view(), name='organization_view'),
    path('create/', views.OrganizationCreate.as_view(), name='organization_create'),
    path('update/<int:pk>', views.OrganizationUpdate, name='organization_edit'),
    path('delete/', views.OrganizationDelete, name='organization_delete'),
    path('search/',views.organization_search, name='search'),

]