from django.conf.urls import url,include
from django.contrib import admin
from  data.views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', home.index),
    url(r'^stuindex/', home.stuindex),
    url(r'^login/', home.login),


    url(r'^userlist/', home.userlist),
    url(r'^adduser/', home.adduser),
    url(r'^edituser/(\d+)/', home.edituser),
    url(r'^deluser/(\d+)/', home.deluser),

    url(r'^stunewlist/', home.stunewlist),

    url(r'^newlist/', home.newlist),
    url(r'^addnew/', home.addnew),
    url(r'^editnew/(\d+)/', home.editnew),
    url(r'^delnew/(\d+)/', home.delnew),

    url(r'^stumatchlist/', home.stumatchlist),

    url(r'^matchlist/', home.matchlist),
    url(r'^addmatch/', home.addmatch),
    url(r'^editmatch/(\d+)/', home.editmatch),
    url(r'^delmatch/(\d+)/', home.delmatch),

    url(r'^reslist/', home.reslist),
    url(r'^addres/', home.addres),
    url(r'^editres/(\d+)/', home.editres),
    url(r'^delres/(\d+)/', home.delres),


    url(r'^stutielist/', home.stutielist),
    url(r'^tielist/', home.tielist),
    url(r'^addstutie/', home.addstutie),
    url(r'^deltie/(\d+)/', home.deltie),

    url(r'^keshihua/', home.keshihua),
    url(r'^echarts/', home.echarts),

]