from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from datetime import datetime

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['home', 'policy','ceo','meeting','carrer','iot','sales','about','contact']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        return datetime.now()
