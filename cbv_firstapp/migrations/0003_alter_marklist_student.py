# Generated by Django 3.2.3 on 2021-06-07 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbv_firstapp', '0002_rename_student_no_studentlist_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marklist',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='cbv_firstapp.studentlist'),
        ),
    ]