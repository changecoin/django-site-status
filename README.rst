=====
Django Site Status
=====

.. image:: https://badge.fury.io/py/django-site-status.png
    :target: http://badge.fury.io/py/django-site-status

Django Site Status is a simple Django app to display time based statuses to your users.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "site_status" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'site_status',
    )

2. Add the status context processor to your template context processors like this::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'site_status.context_processors.inject_statuses'
    )

3. Run `python manage.py migrate` to create the status models.

4. Use statuses anywhere you like in your templates::

    {% for status in statuses %}
        ...
    {% endfor %}

