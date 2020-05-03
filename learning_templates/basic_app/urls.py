from django.conf.urls import url
from basic_app import views

#Template Tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$',views.relative_url_templates,name='relative'),
    url(r'^other/$',views.other,name='other')
]
