from django.db import models

# Create your models here.

class Home(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=600, null=True, blank=True)
    button = models.URLField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Home"
class SocialLinks(models.Model):
    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()
    instagram = models.URLField()