from django.contrib import admin

from todoapp.models import Project, ToDo, WorkGroup


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner')


class WorkGroupAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'project', 'owner')


admin.site.register(Project, ProjectAdmin)
admin.site.register(WorkGroup, WorkGroupAdmin)
admin.site.register(ToDo, ToDoAdmin)
