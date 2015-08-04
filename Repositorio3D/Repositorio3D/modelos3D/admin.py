from django.contrib import admin
from Repositorio3D.modelos3D.models import Model3D, TagsModelos, ImagenesModelos


class Modelos3DAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'valoracion', 'user')
admin.site.register(Model3D, Modelos3DAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('tag', 'modelo')
admin.site.register(TagsModelos, TagsAdmin)


class ImagenesAdmin(admin.ModelAdmin):
    list_display = ('imagen', 'modelo')
admin.site.register(ImagenesModelos, ImagenesAdmin)
