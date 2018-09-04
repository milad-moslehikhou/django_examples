from django.db import models


class Alert(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=20)

    def __str__(self):
        return '{}-{}'.format(self.id, self.text)
