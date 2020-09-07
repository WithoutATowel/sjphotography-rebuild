from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    cover_photo = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length=1000)
    image = models.FileField()
    collection = models.ForeignKey(Collection, related_name='collection', on_delete=models.CASCADE)
    uploaded_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.image.url