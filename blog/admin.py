from django.contrib import admin

from blog.models import Study, Reference, Memo


# Register your models here.
@admin.register(Study)
class MyStudyAdmin(admin.ModelAdmin):
    pass


@admin.register(Reference)
class MyReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Memo)
class MyMemoAdmin(admin.ModelAdmin):
    pass
