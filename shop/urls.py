
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views# reset password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('',include('cart.urls')),
    path('',include('authentication.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



