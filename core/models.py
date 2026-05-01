from django.db import models


class Action(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class Agenda(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='agendas')
    name = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    date = models.DateField()

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.name} ({self.action.name})'
