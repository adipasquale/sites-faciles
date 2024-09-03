# Generated by Django 5.0.8 on 2024-08-23 13:26

import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content_manager", "0039_rename_notice_cmsdsfrconfig_notice_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="cmsdsfrconfig",
            name="notice_description",
            field=wagtail.fields.RichTextField(
                blank=True, default="", help_text="Can include HTML", verbose_name="Notice description"
            ),
        ),
        migrations.AddField(
            model_name="cmsdsfrconfig",
            name="notice_icon_class",
            field=models.CharField(
                blank=True,
                default="",
                help_text="For weather alerts only",
                max_length=200,
                verbose_name="Notice icon class",
            ),
        ),
        migrations.AddField(
            model_name="cmsdsfrconfig",
            name="notice_is_collapsible",
            field=models.BooleanField(default=False, verbose_name="Collapsible?"),
        ),
        migrations.AddField(
            model_name="cmsdsfrconfig",
            name="notice_link",
            field=models.URLField(
                blank=True,
                default="",
                help_text="Standardized consultation link at the end of the notice.",
                verbose_name="Notice link",
            ),
        ),
        migrations.AddField(
            model_name="cmsdsfrconfig",
            name="notice_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Generic notices", [("info", "Information"), ("warning", "Warning"), ("alert", "Alert")]),
                    (
                        "Weather alert notices",
                        [
                            ("weather-orange", "Orange weather alert"),
                            ("weather-red", "Red weather alert"),
                            ("weather-purple", "Purple weather alert"),
                        ],
                    ),
                    (
                        "Alert notices",
                        [
                            ("attack", "Attack alert"),
                            ("witness", "Call for witnesses"),
                            ("cyberattack", "Cyberattack"),
                        ],
                    ),
                ],
                default="info",
                help_text='Use is strictly regulated, see             <a href="https://www.systeme-de-design.gouv.fr/composants-et-modeles/composants/bandeau-d-information-importante/">documentation</a>.',
                max_length=20,
                verbose_name="Notice type",
            ),
        ),
        migrations.AlterField(
            model_name="cmsdsfrconfig",
            name="notice_title",
            field=wagtail.fields.RichTextField(
                blank=True, default="", help_text="Can include HTML", verbose_name="Notice title"
            ),
        ),
    ]