from django.contrib import admin
from .models import About, Skill, Project, FilesWord

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo_about','texto_about','titulo_about_dos','texto_about_dos')
    search_fields = ('titulo_about','titulo_about_dos')

admin.site.register(About, AboutAdmin)

class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tipo_skill','nombre_skill','imagen_skill','porcentaje_skill')
    search_fields = ('nombre_skill','tipo_skill')

admin.site.register(Skill, SkillAdmin)

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name_project','tipo_project','desc_project','imagen_project','link_project','desc_project_one','desc_project_one_imagen','desc_project_two','desc_project_two_imagen','desc_project_three','desc_project_three_imagen','desc_project_four','desc_project_four_imagen')
    search_fields = ('tipo_project','name_project')

admin.site.register(Project, ProjectAdmin)

class FilesWordAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(FilesWord, FilesWordAdmin)