from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=256, default='')
    current_frame = models.IntegerField(default=1)
    first_roll = models.IntegerField(null=True)
    second_roll = models.IntegerField(null=True)
    strike_frame = models.IntegerField(null=True)
    strike_reserve = models.IntegerField(default=0)
    spare_frame = models.IntegerField(null=True)
    spare_reserve = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    all_time_score = models.IntegerField(default=0)
    games_bowled = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        models.Model.save(self, *args, **kwargs)
