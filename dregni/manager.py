import datetime
from django.db import models
from django.contrib.sites.models import Site


class EventManager(models.Manager):
    def for_current_site(self):
        return self.filter(site=Site.objects.get_current())

    def after_date(self, reference_day, num_days):
        queryset = self.filter(start_date__gt=reference_day)
        if num_days:
            day_limit = reference_day + datetime.timedelta(days=num_days)
            queryset = queryset.filter(start_date__lt=day_limit)
        return queryset
