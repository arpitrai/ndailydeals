from django.db import models

class DailyDeals(models.Model):
    source_website_url = models.CharField(max_length=100)
    source_website_logo = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    url = models.URLField(verify_exists=False)
    city = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    created_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return 'Deal from: %s on date: %s' %(self.source_website_url, str(self.created_date))
