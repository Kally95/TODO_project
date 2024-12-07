from django.db import models
from django.utils.translation import gettext_lazy as _

class Todo(models.Model):
    
    class StatusType(models.TextChoices):
        PENDING = "1", _("PENDING")
        COMPLETED = "2", _("COMPLETED")
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    status_type = models.CharField(
        max_length=2,
        choices=StatusType.choices,
        default=1,
    )
    
    def __str__(self):
        return self.title
