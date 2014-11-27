#coding=utf8
from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.forms import ModelForm
from quan.models import Group, Person
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget
from import_export.admin import ImportExportModelAdmin
# Register your models here.

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

class PersonAdmin(ImportExportModelAdmin):
    form = PersonForm
    list_display = ( 'full_name', 'phone','image_thumb' ,)
    list_display_links = ( 'full_name',)
    list_filter = (GroupFilter, 'importance', )
    # fields = ('lastname', 'firstname', 'phone','image_thumb',)
    search_fields = ('firstname', )
    readonly_fields = ('image_thumb',) # 必须将image_thumb置为readonlyfield，或者会报错
admin.site.register(Group)
admin.site.register(Person, PersonAdmin)