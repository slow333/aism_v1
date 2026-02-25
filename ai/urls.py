from django.urls import path
from django.views.generic import TemplateView

app_name = "ai"

urlpatterns = [
    path("index/", TemplateView.as_view(template_name="ai/index.html"), name="index"),
    path(
        "numpy/",
        TemplateView.as_view(template_name="ai/numpy.html"),
        name="numpy",
    ),
    path(
        "scikit-learn/",
        TemplateView.as_view(template_name="ai/scikit-learn.html"),
        name="scikit-learn",
    ),
    path(
        "linear-regression/",
        TemplateView.as_view(template_name="ai/linear-regression.html"),
        name="linear-regression",
    ),
]
