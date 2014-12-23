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
    group = models.ForeignKey(Group)
    acquaint_time = models.DateField("认识时间")
    last_connection_time = models.DateField("最近联系时间")
    importance = models.CharField("重要程度", max_length=10, choices=IMPORTANCE)
    email = models.EmailField("电子邮箱")
    phone = models.CharField("手机号码", max_length=15)
    qq = models.CharField("QQ号", max_length=15, blank=True)
    wechat = models.CharField('微信号', max_length=25, blank=True)
    photo = models.ImageField("照片")

    def __unicode__(self):
        return "%s" % (self.lastname + self.firstname)
    def my_property(self):
        return self.lastname + self.firstname
    my_property.short_description = "姓名"
    full_name = property(my_property)

    def image_thumb(self):
        return '<img src="/media/%s" width="50" height="50" />' % (self.photo)
    image_thumb.short_description = "照片缩略图"
    image_thumb.allow_tags = True  #  这个设置为true可以显示图片，否则显示html 文本

class PersonalStatus(models.Model):
    """docstring for PersonalStatus"""
    person = models.ForeignKey(Person)
    update_time = models.DateField("更新时间", )
    status_desc = models.CharField("动态描述", max_length=1000)

    def __unicode__(self):
        return "%s ---->  %s" % (self.update_time, self.status_desc)
        
