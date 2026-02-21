from django.contrib import admin
from .models_resource import CPUUsage

@admin.register(CPUUsage)
class CPUUsageAdmin(admin.ModelAdmin):
    list_display = ('ssh_info', 'hostname','ip','cpu_cores','usage_p', 'data_time','comment','is_confirmed')
    search_fields = ('hostname',)
    ordering = ('hostname','-data_time',)
    list_filter = ('is_confirmed','ssh_info__name')
