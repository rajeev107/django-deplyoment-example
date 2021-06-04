from django.conf.urls import url
from basic_template_app import views

# Template Tagg
# This name 'basic_template_app' is used inside html
app_name = 'basic_template_app'

urlpatterns = [

    url(r'^relative/$',views.relative, name = 'relative'),
    url(r'^other/$',views.other, name = 'other'),
]
