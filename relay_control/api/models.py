from django.db import models

class Relay(models.Model):
    relay_id = models.IntegerField(unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Relay {self.relay_id}: {'ON' if self.status else 'OFF'}"
