# Generated by Django 3.2 on 2021-04-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_api', '0002_cake'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCaketoCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cakeid', models.IntegerField(default='')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='', upload_to='pic/')),
                ('price', models.IntegerField(default='')),
                ('weight', models.FloatField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='cake',
            name='cakeid',
            field=models.AutoField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cake',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cake',
            name='flavour',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cake',
            name='image',
            field=models.ImageField(default='', upload_to='pic/'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='ingredients',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='cake',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
