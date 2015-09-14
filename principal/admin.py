from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from principal.models import User, UserProfile, Picture, Post, Dog, Comment
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Post, LeafletGeoAdmin)
admin.site.register(Dog)
admin.site.register(Comment)