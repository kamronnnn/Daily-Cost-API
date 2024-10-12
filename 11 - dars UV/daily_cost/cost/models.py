from django.db import models

# Create your models here.


class DailyCost(models.Model):
    user = models.CharField(max_length=50, verbose_name='Xarajat qilgan odamni ismi')
    title = models.CharField(max_length=150, verbose_name='Xarajat nomi')
    description = models.TextField(null=True, blank=True, verbose_name='Xarajat izohi')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Xarajat narxi')
    date = models.DateTimeField(verbose_name='Xarajat sanasi')


    def __str__(self):
        return self.user
