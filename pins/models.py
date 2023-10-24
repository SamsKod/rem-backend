from django.db import models
from django.contrib.auth.models import User
from notes.models import Note


    """
    Pin model, related to 'owner'
    """

class Pin(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(
    	Note, 
    	on_delete=models.CASCADE, 
    	related_name='pins',
    	)
    created_at = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'note']

    def __str__(self):
        return f'{self.owner} {self.note}'