from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import ContactUsView
app_name = 'polls'

urlpatterns = [
    path('', include([
    path('', views.index ),
    path('', ContactUsView.as_view(), {}, 'polls'),
    path('success/', TemplateView.as_view(
        template_name='polls/contact_success.html'),
        {}, 'polls-success'),
    ]))
]
