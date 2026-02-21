from django.urls import path
from . import views_basic as v_basic, views_resource as v_resource, views_dashboard
app_name = 'asct'

urlpatterns = [
    path('', views_dashboard.dashboard, name='index'),
    path('celery/status/', views_dashboard.check_celery_status, name='celery_status'),
    
    path('command/list/', v_basic.cmd_list, name='cmd_list'),
    path('command/add/', v_basic.cmd_add, name='cmd_add'),
    path('command/detail/<int:pk>/', v_basic.cmd_detail, name='cmd_detail'),
    path('command/update/<int:pk>/', v_basic.cmd_update, name='cmd_update'),
    path('command/delete/<int:pk>/', v_basic.cmd_delete, name='cmd_delete'),
    
    path('command/select/', v_basic.cmd_select, name='cmd_select'),
    path('command/history/', v_basic.cmd_history_list, name='cmd_history_list'),
    path('command/history/delete/<int:pk>', v_basic.cmd_history_delete, name='cmd_history_delete'),
    path('command/run/<int:ssh_id>/<int:cmd_id>/', v_basic.cmd_run, name='cmd_run'),
    
    path('sshinfo/list/', v_basic.sshinfo_list, name='sshinfo_list'),
    path('sshinfo/add/', v_basic.sshinfo_add, name='sshinfo_add'),
    path('sshinfo/detail/<int:pk>/', v_basic.sshinfo_detail, name='sshinfo_detail'),
    path('sshinfo/update/<int:pk>/', v_basic.sshinfo_update, name='sshinfo_update'),
    path('sshinfo/delete/<int:pk>/', v_basic.sshinfo_delete, name='sshinfo_delete'),
    
    path('svinfo/list/', v_basic.serverinfo_list, name='serverinfo_list'),
    path('svinfo/export/', v_basic.serverinfo_export, name='serverinfo_export'),
    
    path('cpu_usage/list/', v_resource.cpu_usage_list, name='cpu_usage_list'),
    path('cpu_usage/export/', v_resource.cpu_usage_export, name='cpu_usage_export'),
    path('cpu_usage/chart/', v_resource.cpu_usage_chart, name='cpu_usage_chart'),
    
    path('memory_usage/list/', v_resource.memory_usage_list, name='memory_usage_list'),
    path('memory_usage/export/', v_resource.memory_usage_export, name='memory_usage_export'),
    path('memory_usage/chart/', v_resource.memory_usage_chart, name='memory_usage_chart'),
    
    path('traffic_usage/list/', v_resource.traffic_usage_list, name='traffic_usage_list'),
    path('traffic_usage/export/', v_resource.traffic_usage_export, name='traffic_usage_export'),
    path('traffic_usage/chart/', v_resource.traffic_usage_chart, name='traffic_usage_chart'),
    
    path('disk_usage/list/', v_resource.disk_usage_list, name='disk_usage_list'),
    path('disk_usage/export/', v_resource.disk_usage_export, name='disk_usage_export'),
    path('disk_usage/chart/', v_resource.disk_usage_chart, name='disk_usage_chart'),

]