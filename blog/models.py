from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    #Field for post title
    title = models.CharField(max_length=250)
    #Used for creating unique urls
    slug=models.SlugField(max_length=250,
                          unique_for_date='publish')
    #Uses foreign key so users can have multiple posts
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body=models.TextField()
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering=('-publish',)

        def __str__(self):
            return self.title