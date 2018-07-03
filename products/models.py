from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=55)
    url = models.TextField()
    pub_date = models.DateTimeField()
    voted_total = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField(default=1)
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)
    class Meta:
        verbose_name_plural = 'Control Products'

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:57:]

    def pretty_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
