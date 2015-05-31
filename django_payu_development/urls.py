from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'django_payu_development.example_views.index', name="index"),
    url(r'^get_status/(?P<payment_id>\w+)/$', 'django_payu_development.example_views.get_status', name='get_status'),
    url(r'^payment_completed$', 'django_payu_development.example_views.payment_completed', name='django_pay_complete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django_payu/', include('django_payu.urls')),
]
