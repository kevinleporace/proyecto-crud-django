from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='inicio'),
    path('productos/',views.consultar,name='consultar'),
    path('productos/guardar',views.guardar,name='guardar'),
]
