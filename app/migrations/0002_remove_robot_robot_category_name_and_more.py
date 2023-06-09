# Generated by Django 4.2 on 2023-05-05 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='robot_category_name',
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='robot_category_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='made_in', to='app.robotcategory'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='robot', to='app.manufacturer'),
        ),
    ]
