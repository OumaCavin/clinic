"""
Main views for the clinic project.
Handles global error pages and core functionality.
"""

from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError


@requires_csrf_token
def handler404(request, exception):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)


@requires_csrf_token  
def handler500(request):
    """Custom 500 error handler."""
    return render(request, '500.html', status=500)


def not_found(request, exception=None):
    """Custom 404 not found handler."""
    return render(request, '404.html', status=404)