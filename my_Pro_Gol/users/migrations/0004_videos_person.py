# Generated by Django 4.2.7 on 2023-11-26 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.person'),
        ),
    ]
