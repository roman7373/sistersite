from django.db import models
from django.urls import reverse

class UploadedFile(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    slug = models.SlugField(max_length=250, unique_for_date = 'publish')
    fullname = models.TextField()
    author = models.TextField()
    abstract = models.TextField()
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=False)
    journal = models.CharField(max_length=250)
    issn = models.CharField(max_length=9)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Published')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.fullname[:25]

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year,
                        self.publish.month, self.publish.day])
