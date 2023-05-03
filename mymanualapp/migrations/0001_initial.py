# Generated by Django 4.2 on 2023-05-03 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='gusto_disgusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto_favorito', models.CharField(max_length=30)),
                ('deseos_intimos', models.CharField(max_length=30)),
                ('donde_tocas', models.CharField(max_length=10)),
                ('comida_favorita', models.CharField(max_length=30)),
                ('me_gusta_de_otros', models.CharField(max_length=30)),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymanualapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='decifrarme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuando_borracho', models.CharField(max_length=200)),
                ('cuando_triste', models.CharField(max_length=200)),
                ('cuando_no_respondo', models.CharField(max_length=200)),
                ('cuando_peleamos', models.CharField(max_length=200)),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymanualapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='confianza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField()),
                ('confia_en', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='confia_en', to='mymanualapp.persona')),
                ('quien_confia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quien_confia', to='mymanualapp.persona')),
            ],
        ),
        migrations.CreateModel(
            name='actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=20)),
                ('musica', models.CharField(max_length=20)),
                ('hobbie', models.CharField(max_length=20)),
                ('idpersona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymanualapp.persona')),
            ],
        ),
    ]