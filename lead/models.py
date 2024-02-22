from django.db import models


class lead(models.Model):
    name = models.CharField(max_lenght=300)
    phone = models.IntegerField(11)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        name
