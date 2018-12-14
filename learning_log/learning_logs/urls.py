"""定义learning_logs的URL模式"""

from django.conf.urls import url
# from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
app_name = "learning_logs"
