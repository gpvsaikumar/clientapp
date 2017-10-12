from django.conf.urls import url
from clapp import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name='clapp'

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^read/$',views.read,name='read'),
	url(r'^create/$',views.create,name='create'),
	url(r'^test3/$',views.test3,name='test3')
]

urlpatterns = format_suffix_patterns(urlpatterns)


