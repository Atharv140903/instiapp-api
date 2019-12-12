# Generated by Django 2.2.3 on 2019-07-19 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_event_promotion_boost'),
        ('achievements', '0002_auto_20190719_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='achievements', to='events.Event'),
        ),
    ]