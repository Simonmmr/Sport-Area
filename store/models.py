from django.db import models
from django.utils.timezone import now
import re
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    


class Product(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100 ,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')
    description = models.CharField(max_length=4000, default='', blank=True, null=True)
    image_one =models.ImageField(upload_to='uploads/products/one_file', blank=True, null=True)
    description_one = models.CharField(max_length=4000, default='', blank=True, null=True)
    image_two =models.ImageField(upload_to='uploads/products/two_file', blank=True, null=True)
    description_two = models.CharField(max_length=4000, default='', blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    video_description =  models.CharField(max_length=4000, default='', blank=True, null=True)
    created_at = models.DateTimeField(default=now, editable=False)


    @property
    def video_id(self):
        """Extracts the YouTube video ID from the video URL."""
        if self.video_url:
            regex = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^&\n]{11})'
            match = re.search(regex, self.video_url)
            return match.group(1) if match else None


    def __str__(self):
        return self.title
