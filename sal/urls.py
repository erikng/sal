from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import django.contrib.auth.views as auth_views
from django.contrib.staticfiles import views

urlpatterns = [
    # Examples:
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout_then_login'),
    url(r'^changepassword/$', auth_views.password_change, name='password_change'),
    url(r'^changepassword/done/$', auth_views.password_change_done, name='password_change_done'),
   	url(r'^', include('server.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^licenses/', include('licenses.urls')),
    url(r'^catalog/', include('catalog.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
