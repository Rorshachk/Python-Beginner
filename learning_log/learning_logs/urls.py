"""定义learning_logs的URL模式"""

from django.conf.urls import url
# from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
]
app_name = "learning_logs"
