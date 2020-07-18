from django.urls import path
from dynamicform.formfield import views

app_name = "formfield"
urlpatterns = [

    path('list/', views.FormFieldList.as_view(), name='formfield_list'),
    path('view/<int:pk>', views.FormFieldDetails.as_view(), name='formfield_view'),
    path('create/<int:formmasterid>', views.FormFieldCreate.as_view(), name='formfield_create'),
    path('update/<int:pk>', views.formfield_update, name='formfield_edit'),
    path('delete/', views.formfield_delete, name='formfield_delete'),


]