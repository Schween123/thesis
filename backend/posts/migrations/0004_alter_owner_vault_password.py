# Generated by Django 5.0.7 on 2024-07-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_boardinghouse_faceimage_guardian_owner_room_tenant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='vault_password',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
