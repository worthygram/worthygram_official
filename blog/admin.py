from django.contrib import admin
from .models import Post, Comment,PostReport,Quotes,Certify,Do,Story_Urls,Story,Exercise,Do_Exercise
from parler.admin import TranslatableAdmin



admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostReport)
admin.site.register(Quotes,TranslatableAdmin)
admin.site.register(Do_Exercise,TranslatableAdmin)
admin.site.register(Do,TranslatableAdmin)
admin.site.register(Exercise,TranslatableAdmin)
admin.site.register(Story_Urls,TranslatableAdmin)
admin.site.register(Story,TranslatableAdmin)
admin.site.register(Certify)

