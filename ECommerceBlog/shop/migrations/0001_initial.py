# Generated by Django 3.0.7 on 2020-08-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=80)),
                ('sub_category', models.CharField(default='', max_length=80)),
                ('description', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(default='', upload_to='shop/images')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
