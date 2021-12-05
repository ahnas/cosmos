from django.db import models

# Create your models here.


class CycleService(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    nearestBranch = models.TextField()
    details = models.TextField()
	
    class Meta:
        verbose_name = ('CycleService')
        verbose_name_plural = ('CycleServices')

    def __str__(self):
        return str(self.name)

class ShuttleService(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    nearestBranch = models.TextField()
    details = models.TextField()
	
    class Meta:
        verbose_name = ('ShuttleService')
        verbose_name_plural = ('ShuttleServices')

    def __str__(self):
        return str(self.name)

class FitnessServiceBranch(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    nearestBranch = models.TextField()
    details = models.TextField()
	
    class Meta:
        verbose_name = ('FitnessServiceBranch')
        verbose_name_plural = ('FitnessServiceBranch')

    def __str__(self):
        return str(self.name)

class FitnessServiceOnsite(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    nearestBranch = models.TextField()
    details = models.TextField()
	
    class Meta:
        verbose_name = ('FitnessServiceOnsite')
        verbose_name_plural = ('FitnessServiceOnsite')

    def __str__(self):
        return str(self.name)