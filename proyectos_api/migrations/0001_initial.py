# Generated by Django 4.2 on 2023-04-17 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=125, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'estado',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=125)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fk_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos_api.estado')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estados', to='usuarios_api.usuario')),
            ],
            options={
                'db_table': 'proyecto',
                'unique_together': {('nombre', 'fk_usuario')},
            },
        ),
        migrations.CreateModel(
            name='AsignarProyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fk_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos_api.proyecto')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios_api.usuario')),
            ],
            options={
                'db_table': 'asignar_proyecto',
                'unique_together': {('fk_proyecto', 'fk_usuario')},
            },
        ),
    ]
