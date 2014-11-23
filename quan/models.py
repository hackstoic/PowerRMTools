#coding=utf8
from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField("组名称", max_length=20)

    def __unicode__(self):
        return "%s" % self.name

class Person(models.Model):
    GENDER = (
        ('male', "男"),
        ("female", "女"),
    )
    IMPORTANCE  = (
        ("vip", "非常重要"),
        ("important", "一般重要"),
        ("normal", "普通"),
    )
    firstname = models.CharField("名字", max_length=10)
    lastname = models.CharField("姓氏", max_length=10)
    gender = models.CharField("性别", max_length=10, choices=GENDER )
    birth = models.DateField("生日")
    location = models.CharField("所在地", max_length=50)
    hometown = models.CharField("家乡", max_length=50)
    company = models.CharField("公司", max_length=50)
    job_position = models.CharField("所任职位", max_length=20)
    hobby = models.TextField("爱好")
    skill = models.TextField("技能")
    relationship = models.ForeignKey(Group)
    acquaint_time = models.DateField("认识时间")
    importance = models.CharField("重要程度", max_length=10, choices=IMPORTANCE)
    photo = models.ImageField("照片")

    def __unicode__(self):
        return "%s" % (self.lastname + self.firstname)
    