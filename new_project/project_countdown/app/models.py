from django.db import models

# Create your models here.
class team(models.Model):
    team_number = models.IntegerField(unique = True)
    score = models.IntegerField()

    def update_score(self, new_score):
        self.score = new_score
        self.save()
        
    def get_score(self):
        return self.score


    def __str__(self):
        return str(self.team_number)

class answer(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE,)
    answer = models.CharField(max_length = 264)


    def __str__(self):
        return self.answer

class score1(models.Model):
    team_num = models.ForeignKey(team, on_delete=models.CASCADE,)
    '''score = models.IntegerField()'''

    def __str__(self):
        return str('hello')
