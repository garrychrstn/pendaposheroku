from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.input, name='input'),
    path('posyandu/<int:nik>', views.inputposyandu, name='posyandu'),
    path('action/', views.action, name='action'),
    # Riwayat Dusun
    path('riwayat', views.riwayat, name='riwayat'),
    path('riwayat/kadipeso', views.kadipeso, name='kadipeso'),
    path('riwayat/dumpul', views.dumpul, name=''),
    path('riwayat/derso', views.derso, name=''),
    path('riwayat/sumberejo', views.sumberejo, name=''),
    path('riwayat/plandakan', views.plandakan, name=''),
    path('riwayat/kerjo', views.kerjo, name=''),
    path('riwayatfilter', views.filtered, name='riwayatfilter'),
    path('login', views.login_request, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]