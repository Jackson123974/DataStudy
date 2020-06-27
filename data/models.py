from django.db import models

# Create your models here.

# 账户表信息
class UserManager(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    user_choice = (
        (1, '普通用户'),
        (2, '管理员'),
    )
    usertype = models.IntegerField(verbose_name='用户类型', choices=user_choice)
    def __str__(self):
        return self.username

# 新闻列表信息
class News(models.Model):
    title = models.CharField(verbose_name="新闻标题",max_length=128)
    info = models.TextField(verbose_name="新闻内容")
    def __str__(self):
        return self.title
#比赛列表信息
class Match(models.Model):
    name = models.CharField(verbose_name="赛事名称",max_length=128)
    addr = models.CharField(verbose_name="比赛地点",max_length=128)
    date = models.CharField(verbose_name="比赛时间",max_length=128)
    def __str__(self):
        return self.name


# 帖子列表信息
class Tieba(models.Model):
    title = models.CharField(verbose_name="帖子标题",max_length=128)
    info = models.TextField(verbose_name="帖子内容")
    def __str__(self):
        return self.title

#比赛结果
class Result(models.Model):
    name = models.ForeignKey(verbose_name="关联赛事名称", to=Match,on_delete=models.CASCADE)
    person = models.CharField(verbose_name="比赛队伍", max_length=128)
    score = models.IntegerField(verbose_name="赛事得分", max_length=128)
    def __str__(self):
        return self.name


