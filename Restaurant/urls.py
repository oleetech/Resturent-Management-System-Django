from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company_create',views.company_create,name='company_create'),       
    
    path('setting_page',views.setting_page,name='setting_page'), 
    path('resturent_create',views.resturent_create,name='resturent_create'),       
    path('resturent_detail<int:pk>/',views.resturent_detail,name='resturent_detail'),
    
    path('category_create',views.category_create,name='category_create'),
    path('category_detail<int:pk>/',views.category_detail,name='category_detail'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    path('menuitem_create',views.menuitem_create,name='menuitem_create'),

    path('menuitem_detail/<int:pk>/',views.menuitem_detail,name='menuitem_detail'),
    path('menuitem/<int:pk>/update/', views.menuitem_update, name='menuitem_update'),
    
    path('order_create',views.order_create,name='order_create'),
    path('add_to_temp_order',views.add_to_temp_order,name='add_to_temp_order'),    
    path('add_to_order',views.add_to_order,name='add_to_order'),     
    path('need_cook',views.need_cook,name='need_cook'),     
    path('orderitem/<int:doc_no>/', views.order_item, name='orderitem'),
    path('cookfinish/<int:doc_no>/', views.cookfinish, name='cookfinish'),
    path('needbill',views.needbill,name='needbill'),     
    path('billfinish/<int:doc_no>/', views.billfinish, name='billfinish'),
    path('table_list',views.table_list,name='table_list'),     
    path('get_brtables/',views.get_brtables,name='get_brtables'),     
 
]