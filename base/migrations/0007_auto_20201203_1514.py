# Generated by Django 3.1.4 on 2020-12-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20201203_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='confirm_on_pep_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_person_on_pep_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='confirm_on_sanction_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='is_person_on_sanction_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('INIT', 'Initialized'), ('SC', 'Sanction Check'), ('SCC', 'Sanction Check Completed'), ('PC', 'PEP Check'), ('PCC', 'PEP Check Completed'), ('AS', 'Assessment'), ('ACCEPTED', 'Accepted'), ('DENIED', 'Denied')], default='SC', max_length=20),
        ),
    ]