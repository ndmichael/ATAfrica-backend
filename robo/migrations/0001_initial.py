# Generated by Django 4.2 on 2024-01-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_score', models.IntegerField()),
                ('nigeria_stocks', models.CharField(max_length=50)),
                ('foreign_stocks', models.CharField(max_length=50)),
                ('emerging_stocks', models.CharField(max_length=50)),
                ('nigeria_bonds', models.CharField(max_length=50)),
                ('foreign_bonds', models.CharField(max_length=50)),
                ('commodities', models.CharField(max_length=50)),
                ('real_estate', models.CharField(max_length=50)),
                ('t_bills', models.CharField(max_length=50)),
                ('alternative', models.CharField(max_length=50)),
            ],
        ),
    ]
