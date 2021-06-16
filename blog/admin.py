from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import (Author, Blog, Catagory, Comment, Contact, EmailSignUp,
                     Reply, Tag)


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Catagory,CatAdmin)

@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
	list_display = ['id', 'title','detail']
	summernote_fields = ('detail',)


admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(EmailSignUp)
admin.site.register(Contact)


# made by Nazrul Islam Yeasin 
# Facebook : facebook.com/yeariha.farsin
# Github : github.com/yeazin
# website : yeazin.github.io
