"""
Sitemap for the medical clinic website.
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Page


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages."""
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return [
            'medical:home',
            'medical:about', 
            'medical:services',
            'medical:contact',
            'medical:appointments',
        ]

    def location(self, item):
        return reverse(item)