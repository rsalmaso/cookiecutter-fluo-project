from django.contrib.postgres.operations import CITextExtension
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    operations = [
        CITextExtension(),
    ]
