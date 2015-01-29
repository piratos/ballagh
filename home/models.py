from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title
