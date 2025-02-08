from django.db import models

class Task(models.Model):
    PENDING = 'pending'
    COMPLETE = 'complete'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    #status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return self.title
