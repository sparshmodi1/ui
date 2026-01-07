from django.db import models

class vidNote(models.Model):
    video_url = models.URLField()
    video_title = models.CharField(max_length=200)
    transcript = models.TextField()
    gen_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.video_title
    
    
    
