from django.db import models

# Create your models here.

#about
class About(models.Model):
    titulo_about = models.CharField('titulo',max_length=200, null=False, blank=False)
    texto_about = models.TextField('texto',max_length=2000, null=False, blank=False)
    titulo_about_dos = models.CharField('titulo dos',max_length=200, null=True, blank=True)
    texto_about_dos = models.TextField('texto dos',max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"
        # ordering =["-created"] asi se crea para poner el ultimo creado de primero
        ordering = ["titulo_about"]

    def __str__(self):
        return self.titulo_about
    

class Skill(models.Model):
    tipo_skill = models.CharField('tipo',max_length=200, null=False, blank=False)
    nombre_skill = models.TextField('nombre',max_length=2000, null=False, blank=False)
    imagen_skill = models.ImageField(upload_to="imagen_skill", null=True, blank=True)
    porcentaje_skill = models.IntegerField('%', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"
        # ordering =["-created"] asi se crea para poner el ultimo creado de primero
        ordering = ["nombre_skill"]

    def __str__(self):
        return self.nombre_skill
    
class Project(models.Model):
    name_project = models.CharField('nombre',max_length=200, null=False, blank=False)
    tipo_project = models.CharField('tipo',max_length=200, null=False, blank=False)
    desc_project = models.TextField('descripcion',max_length=2000, null=False, blank=False)
    imagen_project = models.ImageField(upload_to="imagen_skill", null=True, blank=True)
    link_project = models.CharField('link',max_length=200, null=True, blank=False)
    desc_project_one = models.CharField('descripcion 1',max_length=500, null=True, blank=True)
    desc_project_one_imagen = models.ImageField(upload_to="imagen_project", null=True, blank=True)
    desc_project_two = models.CharField('descripcion 2',max_length=500, null=True, blank=True)
    desc_project_two_imagen = models.ImageField(upload_to="imagen_project", null=True, blank=True)
    desc_project_three = models.CharField('descripcion 3',max_length=500, null=True, blank=True)
    desc_project_three_imagen = models.ImageField(upload_to="imagen_project", null=True, blank=True)
    desc_project_four = models.CharField('descripcion 4',max_length=500, null=True, blank=True)
    desc_project_four_imagen = models.ImageField(upload_to="imagen_project", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        # ordering =["-created"] asi se crea para poner el ultimo creado de primero
        ordering = ["name_project"]

    def __str__(self):
        return self.name_project


class FilesWord(models.Model):
    adminupload = models.FileField('word',upload_to='media')
    title = models.CharField('nombre',max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "word"
        verbose_name_plural = "words"
        # ordering =["-created"] asi se crea para poner el ultimo creado de primero
        ordering = ["title"]

    def __str__(self):
        return self.title