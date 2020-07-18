from django.urls import path,include
from dynamicform import views

app_name = 'dynamicform'
urlpatterns = [

    path('', views.DynamicFormList.as_view(), name='dynamicform_list'),
    path('view/<int:pk>', views.DynamicFormDetails.as_view(), name='dynamicform_view'),
    path('create/', views.DynamicFormCreate.as_view(), name='dynamicform_create'),
    path('update/<int:pk>', views.dynamicform_update, name='dynamicform_edit'),
    path('delete/', views.dynamicform_delete, name='dynamicform_delete'),
    path('search/',views.dynamicform_search, name='search'),
    path('userassign/', views.user_assign, name='user_assign'),
    path('formfield/', include('dynamicform.formfield.urls')),
    path('backgroundimage/', include('dynamicform.backgroundimage.urls')),
    path('layout/', include('dynamicform.layout.urls')),
    path('feedback/<int:pk>', views.feedbackDetails.as_view(), name='feedback'),
    # path('urlpage/<int:formmasterid>', views.urlpage_view, name='urlpage'),
    # path('formlist/', views.feedbackform_list_view, name='feedbackformlist'),
    path('report/<int:formmasterid>', views.Report.as_view(), name='report'),
    path('demo/<int:formmasterid>', views.demo, name='demo'),
    path('test/',views.test)

]