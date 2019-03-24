# Generated by Django 2.0.1 on 2019-03-24 10:14

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(help_text='This will be displayed on the product page', upload_to=main.models.get_image_filename, verbose_name='Picture')),
                ('low_res_picture', models.ImageField(blank=True, help_text='Please provide an low res version of the picture', null=True, upload_to=main.models.get_low_res_image_filename, verbose_name='Low Res Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, help_text='This will be the thumbnail for the project', null=True, upload_to='main/images/thumbnails/')),
                ('banner', models.ImageField(blank=True, help_text='This will be the banner for the project', null=True, upload_to='main/images/banners/')),
                ('video', models.FileField(blank=True, help_text='This is the main video for the project', null=True, upload_to='main/videos/')),
                ('project_type', models.CharField(choices=[('General', 'General'), ('Sketchbook', 'Sketchbook'), ('Exhibition', 'Exhibition'), ('Teaching', 'Teaching')], default='General', max_length=13)),
                ('date_field', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Project'),
        ),
    ]
