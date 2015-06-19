from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^signin/$','jobsite.views.signin'),
    url(r'^auth/$','jobsite.views.auth_view'),
    url(r'^signout/$','jobsite.views.signout'),
    url(r'^dashboard/$','jobsite.views.dashboard'),
    url(r'^invalid/$','jobsite.views.invalid'),
    url(r'^signup/$','jobsite.views.signup'),
    url(r'^registered/$', 'jobsite.views.register_success'),
    url(r'^home/(?P<job_id>\d+)/$', 'jobsite.views.home', name='home'),
    url(r'^home/$', 'jobsite.views.jobs', name='jobs'),
    url(r'^apply/$', 'jobsite.views.employer', name='employer'),
    url(r'^post/$', 'jobsite.views.post_job', name='post_job'),

   
)