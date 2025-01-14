# Generated by Django 5.1.2 on 2024-10-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='Xarajat qilgan odamni ismi')),
                ('title', models.CharField(max_length=150, verbose_name='Xarajat nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Xarajat izohi')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Xarajat narxi')),
                ('date', models.DateTimeField(verbose_name='Xarajat sanasi')),
            ],
        ),
    ]
