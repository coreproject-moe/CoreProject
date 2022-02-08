from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


# class UserDatabase(models.Model):
#     previous_song_index = models.PositiveIntegerField(
#         default=1,
#         validators=[
#             # MaxValueValidator(UploadModel.objects.all().count()), # <- Causes Bug
#             MinValueValidator(0),
#         ],
#     )
#     volume = models.FloatField(
#         default=20,
#         validators=[MaxValueValidator(1), MinValueValidator(0)],
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"User: {self.user} | Volume: {self.volume} | Previous Song Index : {self.previous_song_index}"
