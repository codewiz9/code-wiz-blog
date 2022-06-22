from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Blog_Post(models.Model):
    slug = models.SlugField(max_length=1000, editable=False, null=True)
    post_title = models.CharField(max_length=100, editable=True, blank=False, null=True)
    blog_content = models.TextField(max_length=10000, blank=False, editable=True, null=True)
    date = models.DateTimeField(blank=False, null=True, auto_now=True, editable=False)
    likes = models.ManyToManyField(IpModel, related_name="post_likes", blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("mypage_detail", kwargs={"pk": self.pk})
