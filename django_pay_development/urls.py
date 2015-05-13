from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'django_pay_development.example_views.index'),
    url(r'^payment_completed$', 'django_pay_development.example_views.payment_completed', name='django_pay_complete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djangopay/', include('djangopay.urls')),
]
