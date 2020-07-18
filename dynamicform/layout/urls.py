from django.urls import path
from dynamicform.layout import views

app_name = "layout"
urlpatterns = [
    path('create/<int:formmasterid>', views.LayoutCreate.as_view(), name='layout_create'),
    # path('update/<int:pk>', views.formfield_update, name='formfield_edit'),


]