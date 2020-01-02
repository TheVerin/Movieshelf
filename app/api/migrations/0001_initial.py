# Generated by Django 3.0.1 on 2020-01-02 08:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('rated', models.CharField(blank=True, max_length=255, null=True)),
                ('released', models.DateField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('genre', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
                ('director', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
                ('writer', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
                ('actors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None)),
                ('plot', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('awards', models.CharField(blank=True, max_length=255, null=True)),
                ('poster', models.CharField(blank=True, max_length=255, null=True)),
                ('ratings', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), size=None), size=None)),
                ('metascore', models.IntegerField(blank=True, null=True)),
                ('imdb_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imdb_votes', models.IntegerField(blank=True, null=True)),
                ('imdb_id', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('dvd', models.DateField(blank=True, null=True)),
                ('box_office', models.IntegerField(blank=True, null=True)),
                ('production', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('response', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
