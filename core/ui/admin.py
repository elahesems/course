from django.contrib import admin
from ui import models
# Register your models here.
from ui.models import Home, SocialLinks

admin.site.register(Home)
admin.site.register(SocialLinks)
