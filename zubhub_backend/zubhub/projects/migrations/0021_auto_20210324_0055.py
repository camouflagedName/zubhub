# Generated by Django 2.2.7 on 2021-03-24 00:55

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_remove_comment_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='project',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='projects_pr_search__1d35f9_gin'),
        ),
    ]