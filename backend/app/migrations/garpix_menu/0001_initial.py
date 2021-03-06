# Generated by Django 3.1 on 2021-07-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_for_admin', models.CharField(blank=True, default='', max_length=100, verbose_name='Название для админа')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('menu_type', models.CharField(choices=[('header_menu', 'Header menu'), ('footer_menu', 'Footer menu')], default='', max_length=100, verbose_name='Тип меню')),
                ('url', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Внешний URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Включено')),
                ('target_blank', models.BooleanField(default=False, verbose_name='Открывать в новом окне')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('sort', models.IntegerField(default=100, help_text='Чем меньше число, тем выше будет элемент в списке.', verbose_name='Сортировка')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ('sort',),
            },
        ),
    ]
