# Generated by Django 2.0.9 on 2018-10-22 16:59

from django.utils.timezone import datetime
from django.db import migrations, models
from pytz import UTC
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('ideax', '0022_auto_20180816_1625'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AlterModelTable('UserProfile', 'users_userprofile'),
                migrations.AlterField(
                    model_name='use_term',
                    name='final_date',
                    field=models.DateTimeField(default=datetime(2018, 12, 31, tzinfo=UTC)),
                    preserve_default=False,
                ),
            ],
            state_operations=[
                migrations.RemoveField(
                    model_name='userprofile',
                    name='user',
                ),
                migrations.AlterField(
                    model_name='challenge',
                    name='author',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='comment',
                    name='author',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='evaluation',
                    name='valuator',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='idea',
                    name='author',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_author', to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='idea',
                    name='authors',
                    field=models.ManyToManyField(related_name='authors', to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='phase_history',
                    name='author',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='popular_vote',
                    name='voter',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='use_term',
                    name='creator',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile'),
                ),
                migrations.AlterField(
                    model_name='vote',
                    name='voter',
                    field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.UserProfile'),
                ),
                migrations.DeleteModel(
                    name='UserProfile',
                ),
            ],
        ),
    ]
