from django.db import models


class Player(models.Model):
    name = CharField()
    overall_score = IntegerField()
    frames_bowled = IntegerField()


class Frame(models.Model):
    number = CharField(max_length=2)
    first_bowl = IntegerField()
    second_bowl = IntegerField()
    final_score = IntegerField()
