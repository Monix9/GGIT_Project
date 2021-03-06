# Generated by Django 4.0.4 on 2022-06-03 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='nazwisko')),
                ('about', models.TextField(blank=True, verbose_name='o reżyserze')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'reżyser',
                'verbose_name_plural': 'reżyserzy',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title'], 'verbose_name': 'film', 'verbose_name_plural': 'filmy'},
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.director', verbose_name='reżyser'),
        ),
    ]
