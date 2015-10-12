from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^bob/$', 'blog.apps.bob.views.index', name='bob'),
    url(r'^login/$', 'blog.apps.login_reg.views.login', name='login_reg'),
    url(r'^doLogin/$','blog.apps.login_reg.views.doLogin',name='doLogin'),
    url(r'^reg/','blog.apps.login_reg.views.reg',name='reg'),
    url(r'^doReg/','blog.apps.login_reg.views.doReg',name='doReg'),
    url(r'^admin/', include(admin.site.urls)),
)
