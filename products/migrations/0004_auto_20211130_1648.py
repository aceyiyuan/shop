# Generated by Django 3.2 on 2021-11-30 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211128_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portion',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.size', verbose_name='Size'),
        ),
    ]