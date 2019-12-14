"""Cat Store URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('cats/', include(('cats.urls', 'cats'), namespace='cats')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
