from django.db import models


# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area = models.CharField(max_length=15)

    def __str__(self):
        return "{} {}.{}~{}.{}".format(self.area,
                                       self.start_date.month,
                                       self.start_date.day,
                                       self.end_date.month,
                                       self.end_date.day,
                                       )


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} {} :: {}".format(self.poll,
                                 self.candidate,
                                 self.votes)
