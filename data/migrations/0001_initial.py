# Generated by Django 2.2 on 2020-05-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('usertype', models.IntegerField(choices=[(1, '管理员'), (2, '超级管理员')], verbose_name='用户类型')),
            ],
        ),
    ]
