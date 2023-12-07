from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('entry_list')

    def delete_entry_url(self):
        return reverse('delete_entry', args=[str(self.id)])

    def __str__(self):
        return f"{self.user.username} - {self.text}"
