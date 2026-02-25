from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from django.contrib import messages
from django.core.paginator import Paginator
from .models_resource import CPUUsage, MemoryUsage, NetworkUsage, DiskUsage
from .views_common import (
    common_chart,
    common_export,
    common_list,
    filter_by_q_and_hostlist,
)


# =============== Disk usage 관련 Celery ===============
@login_required
def disk_usage_list(request):
    queryset, query, host_list = filter_by_q_and_hostlist(request, DiskUsage)

    usage_threshold = request.GET.get("usage_threshold")
    if usage_threshold:
        try:
            threshold = int(usage_threshold)
            queryset = queryset.filter(use_p__gte=threshold)
        except ValueError:
            pass

    paginator = Paginator(queryset, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    context = {
        "page_obj": page_obj,
        "query": query,
        "host_list": host_list,
        "usage_threshold": usage_threshold,
    }
    return render(request, "asct/disk_usage/list.html", context)


@login_required
def disk_usage_export(request):
    headers = [
        "Hostname",
        "IP",
        "Device",
        "Mounted",
        "Size(GB)",
        "Usage(%)",
        "Checked At",
        "Confirmed",
        "Comment",
    ]

    def mapper(obj, dt_val):
        return [
            obj.hostname,
            obj.ip,
            obj.device,
            obj.mounted,
            obj.size,
            obj.use_p,
            dt_val,
            "Yes" if obj.is_confirmed else "No",
            obj.comment,
        ]

    return common_export(
        "disk_usage_list.xlsx", "Disk Usage", headers, DiskUsage, mapper
    )


@login_required
def disk_usage_chart(request):
    def extractor(entry):
        return [(f"{entry.hostname}:{entry.mounted}({entry.size}G) ", entry.use_p)]

    return common_chart(
        request,
        DiskUsage,
        "Disk Usage",
        "Usage (%)",
        extractor,
        "asct/disk_usage/chart.html",
    )


# =============== Traffic usage 관련 CRUD ===============
@login_required
def traffic_usage_list(request):
    return common_list(request, NetworkUsage, "asct/traffic_usage/list.html")


@login_required
def traffic_usage_export(request):
    headers = [
        "Hostname",
        "IP",
        "Date Time",
        "Interface",
        "Speed",
        "RX(kB/s)",
        "TX(kB/s)",
        "Confirmed",
        "Comment",
    ]

    def mapper(obj, dt_val):
        return [
            obj.hostname,
            obj.ip,
            dt_val,
            obj.if_name,
            obj.speed,
            obj.rxkB_s,
            obj.txkB_s,
            "Yes" if obj.is_confirmed else "No",
            obj.comment,
        ]

    return common_export(
        "traffic_usage_list.xlsx", "Traffic Usage", headers, NetworkUsage, mapper
    )


@login_required
def traffic_usage_chart(request):
    def extractor(entry):
        return [
            (f"{entry.hostname} - {entry.if_name} (RX)", entry.rxkB_s),
            (f"{entry.hostname} - {entry.if_name} (TX)", entry.txkB_s),
        ]

    return common_chart(
        request,
        NetworkUsage,
        "Traffic Usage",
        "Speed (kB/s)",
        extractor,
        "asct/traffic_usage/chart.html",
    )


# =============== Memory usage 관련 CRUD ===============
@login_required
def memory_usage_list(request):
    return common_list(request, MemoryUsage, "asct/memory_usage/list.html")


@login_required
def memory_usage_chart(request):
    def extractor(entry):
        return [(entry.hostname, entry.usage_p)]

    return common_chart(
        request,
        MemoryUsage,
        "Memory Usage",
        "Usage (%)",
        extractor,
        "asct/memory_usage/chart.html",
    )


@login_required
def memory_usage_export(request):
    headers = [
        "Hostname",
        "IP",
        "Date Time",
        "Total Memory(MB)",
        "Usage(%)",
        "Confirmed",
        "Comment",
    ]

    def mapper(obj, dt_val):
        return [
            obj.hostname,
            obj.ip,
            dt_val,
            obj.total_memory,
            obj.usage_p,
            "Yes" if obj.is_confirmed else "No",
            obj.comment,
        ]

    return common_export(
        "memory_usage_list.xlsx", "Memory Usage", headers, MemoryUsage, mapper
    )


# =============== CPU usage 관련 CRUD ===============
@login_required
def cpu_usage_list(request):
    return common_list(request, CPUUsage, "asct/cpu_usage/list.html")


@login_required
def cpu_usage_chart(request):
    def extractor(entry):
        return [(entry.hostname, entry.usage_p)]

    return common_chart(
        request,
        CPUUsage,
        "CPU Usage",
        "Usage (%)",
        extractor,
        "asct/cpu_usage/chart.html",
    )


@login_required
def cpu_usage_export(request):
    headers = [
        "Hostname",
        "IP",
        "Date Time",
        "CPU Cores",
        "Usage(%)",
        "Confirmed",
        "Comment",
    ]

    def mapper(obj, dt_val):
        return [
            obj.hostname,
            obj.ip,
            dt_val,
            obj.cpu_cores,
            obj.usage_p,
            "Yes" if obj.is_confirmed else "No",
            obj.comment,
        ]

    return common_export("cpu_usage_list.xlsx", "CPU Usage", headers, CPUUsage, mapper)
