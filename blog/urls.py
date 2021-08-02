from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include
from blog.views import *


# 여긴 사용 안합니다~~
# 혹시 몰라서 삭제는 안함

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r"^detail/(?P<pk>\w+)/$", QuestionDetail.as_view()),
    path('', home, name='home'),


    path('home/<int:pk>', posting, name="posting"),


]
