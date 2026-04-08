from django.urls import path
from django.views.generic import TemplateView

app_name = "ai"

urlpatterns = [
    path("index/", TemplateView.as_view(template_name="ai/index.html"), name="index"),
    path("tips/", TemplateView.as_view(template_name="ai/tips.html"), name="tips"),
    path("numpy_pandas/", TemplateView.as_view(template_name="ai/numpy_pandas.html"), name="numpy_pandas" ),
    path("matplotlib/", TemplateView.as_view(template_name="ai/matplotlib.html"), name="matplotlib"),
    path("keras/", TemplateView.as_view(template_name="ai/keras.html"), name="keras"),
    path("scikit-learn/", TemplateView.as_view(template_name="ai/scikit-learn.html"), name="scikit-learn"),
    path("linear-regression/", TemplateView.as_view(template_name="ai/linear-regression.html"), name="linear-regression"),
]
