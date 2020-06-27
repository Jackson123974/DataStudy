from django.shortcuts import HttpResponse,render,redirect
from data import models
from data.forms.user import UserModelForm
from data.forms.new import NewModelForm
from data.forms.match import MatchModelForm
from data.forms.res import ResModelForm
from data.forms.tie import TieModelForm
from functools import wraps

def check_login(func):
    @wraps(func)  #装饰器修复技术
    def inner(request,*args,**kwargs):
        #已经登录过的继续执行
        ret = request.get_signed_cookie("is_login", default="0", salt="dsb")
        if ret == "1":
            return func(request,*args,**kwargs)
        #没有登录过的跳转登录界面
        else:
            #获取当前访问的URl
            next_url = request.path_info
            print(next_url)
            return redirect("/data/login/?next={}".format(next_url))
    return inner

@check_login
def index(request):
    return render(request,'index.html')

@check_login
def stuindex(request):
    return render(request,'stuindex.html')

def login(request):
    errmsg = ""
    if request.method == "POST":
        usertype = request.POST['seltype']
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.GET.get("next")
        if usertype == "普通用户":
            stu_obj = models.UserManager.objects.filter(username=username,password=password,usertype=1)
            if stu_obj:
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect('/data/stuindex/')
                rep.set_signed_cookie("is_login", "1", salt="dsb", max_age=60 * 60 * 24 * 7)
                return rep
            else:
                return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
        else:
            object = models.UserManager.objects.filter(username=username, password=password,usertype=2)
            if object:
                if next_url:
                    rep = redirect(next_url)
                else:
                    rep = redirect('/data/index/')
                rep.set_signed_cookie("is_login", "1", salt="dsb", max_age=60 * 60 * 24 * 7)
                return rep
            else:
                return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
    return render(request, 'login.html')

def logout(request):
    rep = redirect("/data/login/")
    rep.delete_cookie("is_login")
    return rep

@check_login
def userlist(request):
    teach_queryset = models.UserManager.objects.all()
    return render(request, 'userlist.html', {"teach_queryset": teach_queryset})

@check_login
def adduser(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_form.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/userlist/')
    return render(request, 'user_form.html', {"form": form})

@check_login
def edituser(request, nid):
    obj = models.UserManager.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=obj)
        return render(request, 'user_form.html', {"form": form})
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/userlist/')
    return render(request, 'user_form.html', {"form": form})

@check_login
def deluser(request, nid):
    models.UserManager.objects.filter(id=nid).delete()
    return redirect('/data/userlist/')

@check_login
def stunewlist(request):
    teach_queryset = models.News.objects.all()
    return render(request, 'stunewlist.html', {"teach_queryset": teach_queryset})

@check_login
def newlist(request):
    teach_queryset = models.News.objects.all()
    return render(request, 'newlist.html', {"teach_queryset": teach_queryset})

@check_login
def addnew(request):
    if request.method == "GET":
        form = NewModelForm()
        return render(request, 'user_form.html', {"form": form})
    form = NewModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/newlist/')
    return render(request, 'user_form.html', {"form": form})


@check_login
def editnew(request, nid):
    obj = models.News.objects.filter(id=nid).first()
    if request.method == "GET":
        form = NewModelForm(instance=obj)
        return render(request, 'user_form.html', {"form": form})
    form = NewModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/newlist/')
    return render(request, 'user_form.html', {"form": form})

@check_login
def delnew(request, nid):
    models.News.objects.filter(id=nid).delete()
    return redirect('/data/newlist/')

@check_login
def stumatchlist(request):
    teach_queryset = models.Match.objects.all()
    return render(request, 'stumatchlist.html', {"teach_queryset": teach_queryset})

@check_login
def matchlist(request):
    teach_queryset = models.Match.objects.all()
    return render(request, 'matchlist.html', {"teach_queryset": teach_queryset})

@check_login
def addmatch(request):
    if request.method == "GET":
        form = MatchModelForm()
        return render(request, 'user_form.html', {"form": form})
    form = MatchModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/matchlist/')
    return render(request, 'user_form.html', {"form": form})


@check_login
def editmatch(request, nid):
    obj = models.Match.objects.filter(id=nid).first()
    if request.method == "GET":
        form = MatchModelForm(instance=obj)
        return render(request, 'user_form.html', {"form": form})
    form = MatchModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/matchlist/')
    return render(request, 'user_form.html', {"form": form})


@check_login
def delmatch(request, nid):
    models.Match.objects.filter(id=nid).delete()
    return redirect('/data/matchlist/')


@check_login
def reslist(request):
    teach_queryset = models.Result.objects.all()
    return render(request, 'reslist.html', {"teach_queryset": teach_queryset})

@check_login
def addres(request):
    if request.method == "GET":
        form = ResModelForm()
        return render(request, 'user_form.html', {"form": form})
    form = ResModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/reslist/')
    return render(request, 'user_form.html', {"form": form})

@check_login
def editres(request, nid):
    obj = models.Result.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ResModelForm(instance=obj)
        return render(request, 'user_form.html', {"form": form})
    form = ResModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/reslist/')
    return render(request, 'user_form.html', {"form": form})

@check_login
def delres(request, nid):
    models.Result.objects.filter(id=nid).delete()
    return redirect('/data/newlist/')



@check_login
def stutielist(request):
    teach_queryset = models.Tieba.objects.all()
    return render(request, 'stutielist.html', {"teach_queryset": teach_queryset})

@check_login
def addstutie(request):
    if request.method == "GET":
        form = TieModelForm()
        return render(request, 'stu_form.html', {"form": form})
    form = TieModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/stutielist/')
    return render(request, 'stu_form.html', {"form": form})

@check_login
def tielist(request):
    teach_queryset = models.Tieba.objects.all()
    return render(request, 'tielist.html', {"teach_queryset": teach_queryset})

@check_login
def deltie(request, nid):
    models.Tieba.objects.filter(id=nid).delete()
    return redirect('/data/tielist/')

@check_login
def echarts(request):
    import json
    if request.method == "GET":
        date=[]
        lesss = []
        info_queryset = models.Result.objects.order_by('-score').all()[:5]
        for  row in info_queryset:
            date.append(row.person)
            lesss.append(row.score)
        print("===========================")
        print(date)
        print(lesss)
        msg = {"diwen":
            [
            {"AREA":date[0],"LANDNUM":lesss[0]},
            {"AREA":date[1],"LANDNUM":lesss[1]},
            {"AREA":date[2],"LANDNUM":lesss[2]},
            {"AREA":date[3],"LANDNUM":lesss[3]},
            {"AREA":date[4],"LANDNUM":lesss[4]}
            ]}
        return HttpResponse(json.dumps(msg))
@check_login
def keshihua(request):
    query = models.Match.objects.all()
    number = models.Result.objects.all().count()
    return render(request,'keshihua.html',{"queryset":query,"number":number})
