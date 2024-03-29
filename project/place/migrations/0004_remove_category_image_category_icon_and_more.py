# Generated by Django 5.0.1 on 2024-01-06 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_category'),
        ('state', '0002_delete_municipal'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(null=True, upload_to='category/'),
        ),
        migrations.AddField(
            model_name='place',
            name='id_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.category'),
        ),
        migrations.AddField(
            model_name='place',
            name='id_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='id_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='id_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='state.state'),
        ),
    ]
