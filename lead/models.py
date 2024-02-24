from django.db import models


class lead(models.Model):
    name = models.CharField(max_length=300)
    phone = models.IntegerField()
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
