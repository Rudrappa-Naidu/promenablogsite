from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin

from .models import *

# Register your models here.


admin.site.register(BlogPost)
admin.site.register(CommentModel)
admin.site.register(ReplyModel)


