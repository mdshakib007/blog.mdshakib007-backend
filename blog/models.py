from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.URLField(null=True, blank=True)
    body = models.TextField()

    tags = models.ManyToManyField(Tag, related_name='blogs', blank=True)
    clap_count = models.PositiveIntegerField(default=0)
    reads = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=20)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} on {self.blog.title}"
