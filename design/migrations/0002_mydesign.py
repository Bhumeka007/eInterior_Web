# Generated by Django 4.0.5 on 2022-10-02 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDesign',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('tag_des', models.CharField(default='Added', max_length=10)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_dessing', to='design.design')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_design', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
