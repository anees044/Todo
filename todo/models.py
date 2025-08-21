from django.db import models

class Tasks(models.Model):
    taskname=models.CharField(max_length=240)
    is_completed=models.BooleanField(default=False)
    createdat=models.DateTimeField(auto_now_add=True)
    modifiedat=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskname


