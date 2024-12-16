# Generated by Django 5.1.2 on 2024-11-10 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technicalIssues', '0006_issues_reporter_alter_issues_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='reporter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reported_issues', to=settings.AUTH_USER_MODEL),
        ),
    ]