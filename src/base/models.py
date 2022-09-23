from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = None
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
    body = RichTextField(null=True, blank=True)
    created = models.TimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(null=True, blank=True)
    git = models.URLField(verbose_name=None, name=None, null=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug is None:
            slug = slugify(self.headline)
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
