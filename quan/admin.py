#coding=utf8
from django.db import models
from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.forms import ModelForm
from quan.models import Group, Person, PersonalStatus
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget
from import_export.admin import ImportExportModelAdmin
from datetimewidget.widgets import DateTimeWidget
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget, AutosizedTextarea
from django.contrib.admin import TabularInline
# Register your models here.

class PersonalStatusAdmin(ModelAdmin):
    list_display = ('get_person', 'update_time', 'status_desc')

    def get_person(self, obj):
        return obj.person.lastname  + obj.person.firstname
    get_person.short_description = "姓名"

class GroupFilter(SimpleListFilter):
    """
    For Foreignkey related select filter
  List filter example that shows only referenced(used) values
  """
    title = '关系'
    parameter_name = 'group'

    def lookups(self, request, model_admin):
        # You can use also "Group" instead of "model_admin.model"
        # if this is not direct relation
        groups = set([g for g in Group.objects.all()])
        return [(g.id, g.name) for g in groups]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(group__id__exact=self.value())
        else:
            return queryset
class GroupChoices(AutoModelSelect2Field):
    pass
    # queryset = Group.objects
    # search_fields = ['name__icontains',]

class PersonForm(ModelForm):
    # formfield_overrides = {
    #     models.DateTimeField: {'widget': DateTimeWidget(attrs={}, usel10n=True, bootstrap_version=3) }
    # }
    # group_verbose_name = Group._meta.verbose_name
    # group = GroupChoices(
    #     label=group_verbose_name.capitalize(),
    #     widget=AutoHeavySelect2Widget(
    #         select2_options={
    #             'width': '220px',
    #             'placeholder': 'Lookup %s ...' % group_verbose_name
    #         }
    #     )
    # )

    
    class Meta:
        model = Person
        widgets = {
            # 'hobby': AutosizedTextarea,
            'hobby': AutosizedTextarea(attrs={'row':3 , 'class':'input-xlarge'}),
            'skill': AutosizedTextarea(attrs={'row':3 , 'class':'input-xlarge'}),

       }

class PersonalStatusInline(TabularInline):
    """docstring for PersonalStatusInline"""
    model = PersonalStatus
    suit_classes = 'suit-tab suit-tab-pstatus'
    # sortable = 'update_time'
        

class PersonAdmin(ImportExportModelAdmin):
    inlines = (PersonalStatusInline,)
    form = PersonForm
    list_display = ( 'full_name', 'phone', 'last_connection_time', 'image_thumb' ,)
    list_display_links = ( 'full_name',)
    list_filter = (GroupFilter, 'importance', 'gender', 'location','hometown')
    # fields = ('lastname', 'firstname', 'phone','image_thumb',)
    search_fields = ('firstname', )
    readonly_fields = ('image_thumb',) # '必须将image_thumb置为readonlyfield，或者会报错'
    fieldsets = [
    ('基本资料',{
        'classes':('suit-tab', 'suit-tab-general',),
        'fields':['lastname', 'firstname', 'gender', 'birth', 'location', 'hometown','group' ]
        }),
    ('职业资料',{
        'classes':('suit-tab', 'suit-tab-general',),
        'fields':['company', 'job_position']
        }),
    ('兴趣爱好',{
        'classes':('suit-tab', 'suit-tab-general',),
        'fields':['hobby', 'skill']
        }),
    ('联系状况',{
        'classes':('suit-tab', 'suit-tab-connection',),
        'fields':['acquaint_time', 'last_connection_time', 'importance']
        }),
    ('联系方式',{
        'classes':('suit-tab', 'suit-tab-connection',),
        'fields':['email', 'phone', 'qq', 'wechat',]
        }),
    ('照片管理',{
        'classes':('suit-tab', 'suit-tab-photoes',),
        'fields':['image_thumb', 'photo',]
        }),

    ]

    suit_form_tabs = (('general', 'General'), ('connection', 'Connection'), ('pstatus', 'Status'),('photoes', 'Photo'),('info','Info')

        )

    suit_form_includes = (        
        ('admin/person/tab_info.html', '', 'info'),
    )

    # suit_form_includes = (
    #     ('admin/examples/country/custom_include.html', 'middle', 'cities'),
    #     ('admin/examples/country/tab_info.html', '', 'info'),
    # )

admin.site.register(Group)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonalStatus, PersonalStatusAdmin)
