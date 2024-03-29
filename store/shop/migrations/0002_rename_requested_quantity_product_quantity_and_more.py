# Generated by Django 4.2 on 2023-04-07 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="requested_quantity", new_name="quantity",
        ),
        migrations.RemoveField(model_name="order", name="transaction",),
        migrations.RemoveField(model_name="transaction", name="available_quantity",),
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="shop.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transaction",
            name="order",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="shop.order",
            ),
            preserve_default=False,
        ),
    ]
