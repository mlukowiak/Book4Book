from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    series = models.CharField(max_length=256)
    publishingHouse = models.CharField(max_length=256)
    publishYear = models.IntegerField()

    def __str__(self):
        return self.title

    def copies_number(self):
        copies = Copy.objects.filter(book=self)
        return len(copies)

class Copy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    photo = models.ImageField(upload_to='copies', blank=True)
    date = models.DateTimeField(default=timezone.now)