from django.conf.urls import url
from django.conf.urls.static import static
import app.settings as settings

from . import views

urlpatterns = [
    url('^',views.home,name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
