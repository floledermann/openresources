from django.contrib import admin

from openresources.models import *

try:
    from transmeta import get_fallback_fieldname
except ImportError:
    get_fallback_fieldname = lambda name: name


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1
    fk_name = 'resource'
    readonly_fields = ['value_date','value_relation']
    
    # this is dangerous - TextInputWidget destroys nelines in tag values!
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        # replace 'value' field for tags with single-line input
#        field = super(TagInline, self).formfield_for_dbfield(db_field, **kwargs)
#               
#        if db_field.name == 'value':
#            field.widget = admin.widgets.AdminTextInputWidget()

#        return field


class ResourceAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    prepopulated_fields = {'shortname': ('name',)} 
    save_on_top = True
    list_filter = ['creation_date', 'creator',]

    fieldsets = (
        (None, {'fields': ('name', )}),
        ('Navigation options', {'fields': ('shortname', 'start_date', 'end_date'),}),
        ('Editing', {'fields': ('creator', ),
                     'classes': ('collapse', )}),
    )

class TagTemplateInline(admin.TabularInline):
    model = TagTemplate
    extra = 1

    # replace textarea with input in admin (FIXME: this destroys newlines, so should be done via styled textarea)
    def formfield_for_dbfield(self, db_field, **kwargs):
        
        field = super(TagTemplateInline, self).formfield_for_dbfield(db_field, **kwargs)
               
        if db_field.name == 'value':
            field.widget = admin.widgets.AdminTextInputWidget()

        return field


class TagTemplateGroupInline(admin.TabularInline):
    model = TagTemplateGroup
    extra = 1


class ResourceTemplateAdmin(admin.ModelAdmin):
    inlines = [TagTemplateGroupInline, TagTemplateInline]
    prepopulated_fields = {'shortname': (get_fallback_fieldname('name'),)} 
    save_on_top = True


class TagQueryInline(admin.TabularInline):  
    model = TagQuery
    extra = 1


class ViewAdmin(admin.ModelAdmin):
    inlines = [TagQueryInline]
    prepopulated_fields = {'shortname': (get_fallback_fieldname('name'),)} 
    save_on_top = True


admin.site.register(Resource, ResourceAdmin)
admin.site.register(View, ViewAdmin)
admin.site.register(ResourceTemplate, ResourceTemplateAdmin)

admin.site.register(Icon)
admin.site.register(Area)
admin.site.register(UserProfile)


