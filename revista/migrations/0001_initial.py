# Generated by Django 2.1.4 on 2019-01-08 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_da_mae', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('grupo_amigo', models.CharField(choices=[('1', 'Predio'), ('2', 'Escola')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('etiqueta', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='coleçao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField()),
                ('data_devoluçao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ediçao', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.caixa')),
                ('coleçao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.coleçao')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.emprestimo')),
            ],
        ),
        migrations.AddField(
            model_name='amigo',
            name='emprestimo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.emprestimo'),
        ),
    ]
