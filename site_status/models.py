from django.db import models


class Status(models.Model):
    POSITIVE = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    LEVELS = (
        (POSITIVE, "Positive"),
        (INFO, "Info"),
        (WARNING, "Warning"),
        (ERROR, "Error"),
        (CRITICAL, "Critical")
    )

    level = models.PositiveSmallIntegerField(choices=LEVELS)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    body = models.TextField()

