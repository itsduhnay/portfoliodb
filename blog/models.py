from django.db import models
from django.utils.text import Truncator

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    summary = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
       
    @property
    def preview(self):
        return Truncator(self.summary).words(20)

    def __str__(self):
        return self.title
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')