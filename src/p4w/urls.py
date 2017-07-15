from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dashboard/', include('dashboard.urls', namespace="dashboard")),
    url(r'^admin/', include(admin.site.urls)),
]
