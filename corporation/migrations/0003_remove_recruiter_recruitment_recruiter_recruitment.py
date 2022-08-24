# Generated by Django 4.1 on 2022-08-24 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "corporation",
            "0002_remove_corporation_country_remove_corporation_region_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="recruiter", name="recruitment",),
        migrations.AddField(
            model_name="recruiter",
            name="recruitment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="corporation.recruitment",
                verbose_name="채용공고",
            ),
        ),
    ]