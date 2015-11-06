from django.contrib import admin
from principal.models import User, UserProfile, Picture, Post, Dog, Comment, Feedback
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Post)
admin.site.register(Dog)
admin.site.register(Comment)
admin.site.register(Feedback)