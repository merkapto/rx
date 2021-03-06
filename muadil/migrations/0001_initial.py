# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import muadil.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doz', models.CommaSeparatedIntegerField(blank=True, max_length=1000, null=True)),
                ('birim', models.CharField(blank=True, choices=[('mg', 'miligram'), ('gr', 'gram'), ('ml', 'mililitre'), ('ünite', 'ünite')], default='mg', max_length=2, null=True, verbose_name='Birim')),
            ],
        ),
        migrations.CreateModel(
            name='EtkenMadde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etkenmadde_adi', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'ordering': ['etkenmadde_adi'],
                'verbose_name_plural': 'Etken Maddeler',
                'verbose_name': 'Etken Madde',
            },
        ),
        migrations.CreateModel(
            name='Ilac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilac_adi', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'ordering': ['ilac_adi'],
                'verbose_name_plural': 'İlaçlar',
                'verbose_name': 'İlaç',
            },
        ),
        migrations.CreateModel(
            name='Mustahzar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ekisim', models.CharField(blank=True, max_length=32, null=True)),
                ('resim', models.FileField(blank=True, null=True, upload_to=muadil.models.ilac_resim_yeri)),
                ('adet', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('form', models.CharField(blank=True, choices=[('tabletler', (('ağızda çözünür tablet', 'ağızda çözünür tablet'), ('çiğneme tableti', 'çiğneme tableti'), ('efervesan tablet', 'efervesan tablet'), ('enterik tablet', 'enterik tablet'), ('film tablet', 'film tablet'), ('kontrollü salım tablet', 'kontrollü salım tablet'), ('sublingual tablet', 'sublingual tablet'), ('suda çözünür tablet', 'suda çözünür tablet'), ('tablet', 'tablet'), ('topikal harici çözünür tablet', 'topikal harici çözünür tablet'), ('transmukozal terapötik sistem', 'transmukozal terapötik sistem'), ('vajinal tablet', 'vajinal tablet'))), ('kapsüller', (('enterik kapsül', 'enterik kapsül'), ('enterik mikropellet kapsül', 'enterik mikropellet kapsül'), ('kapsül', 'kapsül'), ('retard/SR kapsül', 'retard/SR kapsül'), ('retard/SR mikropellet kapsül', 'retard/SR mikropellet kapsül'), ('yumuşak jelatin kapsül', 'yumuşak jelatin kapsül'), ('vajinal kapsül', 'vajinal kapsül'))), ('drajeler', (('çiğneme drajesi', 'çiğneme drajesi'), ('draje', 'draje'), ('enterik draje', 'enterik draje'), ('retard draje', 'retard draje'))), ('diğerleri', (('ampul', 'ampul'), ('flakon', 'flakon')))], default='tablet', max_length=64, null=True, verbose_name='Form')),
                ('firma', models.CharField(blank=True, max_length=32, null=True, verbose_name='Firma')),
                ('barkod', models.CharField(blank=True, max_length=13, null=True, verbose_name='Barkod')),
                ('aktif', models.BooleanField(default=True)),
                ('renk', models.CharField(blank=True, choices=[('beyaz', 'beyaz'), ('kırmızı', 'kırmızı'), ('yeşil', 'yeşil'), ('mor', 'mor'), ('turuncu', 'turuncu'), ('mavi', 'mavi')], default='beyaz', max_length=32, null=True, verbose_name='Renk')),
                ('sut', models.TextField(blank=True, null=True)),
                ('prospektus', models.TextField(blank=True, null=True)),
                ('kub', models.TextField(blank=True, null=True)),
                ('kt', models.TextField(blank=True, null=True)),
                ('pera_fiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Fiyat')),
                ('kamu_fiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Kamu Fiyatı')),
                ('kamu_odenen', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Kamu Ödenen')),
                ('depo_fiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Depocu Fiyatı')),
                ('imal_fiyat', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='İmalatçı Fiyatı')),
                ('ilac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muadil.Ilac')),
                ('muadil', models.ManyToManyField(blank=True, related_name='_mustahzar_muadil_+', to='muadil.Mustahzar')),
                ('yakin_muadil', models.ManyToManyField(blank=True, related_name='_mustahzar_yakin_muadil_+', to='muadil.Mustahzar')),
            ],
            options={
                'ordering': ['ilac', 'ekisim', 'adet', 'form'],
                'verbose_name_plural': 'Mustahzar Bilgileri',
                'verbose_name': 'MustahzarBilgisi',
            },
        ),
        migrations.AddField(
            model_name='edb',
            name='etkenmadde',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muadil.EtkenMadde'),
        ),
        migrations.AddField(
            model_name='edb',
            name='mustahzar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muadil.Mustahzar'),
        ),
    ]
