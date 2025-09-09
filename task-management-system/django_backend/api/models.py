from django.db import models
from django.contrib.auth.models import User
"""
https://docs.djangoproject.com/en/5.2/topics/auth/default/#:~:text=user_gains_perms%28request%2C%20user_id%29%3A
The primary attributes of the default user are:

username

password

email

first_name

last_name
"""


from django.contrib.postgres.fields import JSONField




"""
Enum Constants representing the status or priority of a task.
"""
STATUS_CHOICES = [
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
]

PRIORITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

"""
Class model representing a tag on postgreSQL database.
@ManyToMany relationship between Task and Tag.
"""
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

"""
Class model representing a task on postgreSQL database.
@ManyToMany relationship between Task and User.
@ForeignKey relationship with User (author).
"""
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES)
    priority = models.CharField(choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    estimated_hours = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    actual_hours = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    # Relationships
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assigned_ToUsers = models.ManyToManyField(User, related_name='assigned_to_users')
    tags = models.ManyToManyField(Tag, related_name='tags')
    parent_task = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING)
    # Metadata
    metadata = models.JSONField(default=dict)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)

