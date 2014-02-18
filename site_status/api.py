from datetime import datetime

from site_status import models


def get_statuses():
    current_datetime = datetime.now()

    statuses = models.Status.objects.all()\
        .filter(start_time__lt=current_datetime)\
        .filter(end_time__gt=current_datetime)

    return statuses


def add_status(level, body, end_time, start_time=None):
    if start_time is None:
        start_time = datetime.now()

    status = models.Status(level=level,
                           body=body,
                           start_time=start_time,
                           end_time=end_time)
    status.save()
    return status