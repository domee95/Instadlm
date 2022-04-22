from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Relationship(models.Model):

    unique_together = ("origin", "target") #funcionaria con postgresql o mysql

    origin = models.ForeignKey(User, related_name='relationship_origin', on_delete=models.CASCADE,)
    target = models.ForeignKey(User, related_name='relationship_target', on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)

