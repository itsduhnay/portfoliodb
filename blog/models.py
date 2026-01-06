from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    summary = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    

    def __str__(self):
        return self.title