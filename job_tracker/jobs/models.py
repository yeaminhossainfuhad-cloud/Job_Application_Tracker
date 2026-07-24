from django.db import models
from django.utils import timezone

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    job_location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    application_date = models.DateField(default=timezone.now)
    deadline = models.DateField()
    notes = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"