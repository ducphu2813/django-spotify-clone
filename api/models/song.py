from django.db import models

# song model
class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    #khóa ngoại đến bảng artist
    artist = models.ForeignKey(
        'Artist'
        , on_delete=models.CASCADE
    )
    # Media
    image_url = models.URLField(blank=True, null=True, help_text="Ảnh thumbnail")  # link ảnh từ AWS S3
    audio_url = models.URLField(blank=True, null=True, help_text="File âm thanh - lưu URL S3")  # link âm thanh từ AWS S3
    video_url = models.URLField(blank=True, null=True, help_text="Video đi kèm nếu có")  # link video từ AWS S3

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name