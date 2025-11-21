from django.db import models
from django.utils.text import slugify
from django.conf import settings
from account.models import User



class Category(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    cover = models.ImageField(upload_to='posts/covers/', blank=True, null=True)
    banner = models.ImageField(upload_to='posts/banners/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    running_time = models.IntegerField(blank=True, null=True, help_text="Duration in minutes")
    country = models.CharField(max_length=20, blank=True, null=True)
    actors = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True, default=0.0,
        help_text="Rating between 0 and 10"
    )

    AGE_CHOICES = [
        ("+7", "+7"),
        ("+12", "+12"),
        ("+15", "+15"),
        ("+16", "+16"),
        ("+18", "+18"),
    ]
    age_rating = models.CharField(max_length=5, choices=AGE_CHOICES, blank=True, null=True, default="+16")

    QUALITY_CHOICES = [
        ("SD", "SD"),
        ("HD", "HD"),
        ("FHD", "Full HD"),
        ("4K", "4K"),
    ]
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES, blank=True, null=True, default="HD")

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Photo(models.Model):
    my_model = models.ForeignKey(Post, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/photos/')


class Comment(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies',
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

    @property
    def is_parent(self):
        return self.parent is None
