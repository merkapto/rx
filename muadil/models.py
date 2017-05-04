from django.db import models
from django import forms
#from ckeditor.fields import RichTextField

class Ilac(models.Model):
	ilac_adi = models.CharField(max_length=32, blank=True, null=True)
	def __str__(self):
		return self.ilac_adi
	class Meta:
		ordering = ['ilac_adi']
		verbose_name = "İlaç"
		verbose_name_plural = "İlaçlar"

class EtkenMadde(models.Model):
	etkenmadde_adi = models.CharField(max_length=32, blank=True, null=True)
	def __str__(self):
		return self.etkenmadde_adi
	class Meta:
		ordering = ['etkenmadde_adi']
		verbose_name = "Etken Madde"
		verbose_name_plural = "Etken Maddeler"

def ilac_resim_yeri(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.ilac, instance, extension)
	#return "%s/%s" %(instance.id, instance)

class Mustahzar(models.Model):
	form_secenek = (
		('tabletler', (
			('ağızda çözünür tablet', 'ağızda çözünür tablet'),
			('çiğneme tableti', 'çiğneme tableti'),
			('efervesan tablet', 'efervesan tablet'),
			('enterik tablet', 'enterik tablet'),
			('film tablet', 'film tablet'),
			('kontrollü salım tablet', 'kontrollü salım tablet'),
			('sublingual tablet', 'sublingual tablet'),
			('suda çözünür tablet', 'suda çözünür tablet'),
			('tablet', 'tablet'),
			('topikal harici çözünür tablet', 'topikal harici çözünür tablet'),
			('transmukozal terapötik sistem', 'transmukozal terapötik sistem'),
			('vajinal tablet', 'vajinal tablet'),
					)
		),
		('kapsüller', (
			('enterik kapsül', 'enterik kapsül'),
			('enterik mikropellet kapsül', 'enterik mikropellet kapsül'),
			('kapsül', 'kapsül'),
			('retard/SR kapsül', 'retard/SR kapsül'),
			('retard/SR mikropellet kapsül', 'retard/SR mikropellet kapsül'),
			('yumuşak jelatin kapsül', 'yumuşak jelatin kapsül'),
			('vajinal kapsül', 'vajinal kapsül'),
					)
		),
		('drajeler', (
			('çiğneme drajesi', 'çiğneme drajesi'),
			('draje', 'draje'),
			('enterik draje', 'enterik draje'),
			('retard draje', 'retard draje'),
					)
		),
		('diğerleri',(
			('ampul', 'ampul'),
			('flakon', 'flakon'),
			('poşet', 'poşet'),
					)
		),
	)

	renk_secenek = (
		('beyaz', 'beyaz'),
		('kırmızı', 'kırmızı'),
		('yeşil', 'yeşil'),
		('mor', 'mor'),
		('turuncu', 'turuncu'),
		('mavi', 'mavi'),
	)
	ilac = models.ForeignKey(Ilac, on_delete=models.CASCADE)
	ekisim = models.CharField(max_length=32, blank=True, null=True)
	resim = models.FileField(upload_to=ilac_resim_yeri, blank=True, null=True)
	adet = models.PositiveSmallIntegerField(blank=True, null=True)
	form = models.CharField('Form', max_length=64, choices=form_secenek, default='tablet', blank=True, null=True)
	firma = models.CharField('Firma', max_length=32, blank=True, null=True)
	barkod = models.CharField('Barkod', max_length=13, blank=True, null=True)
	muadil = models.ManyToManyField("self", blank=True)
	yakin_muadil = models.ManyToManyField("self", blank=True)
	aktif = models.BooleanField(default=True)
	renk = models.CharField('Renk', max_length=32, choices=renk_secenek, default='beyaz', blank=True, null=True)
#	sut = RichTextField(blank=True, null=True)
#	prospektus = RichTextField(blank=True, null=True)
#	kub = RichTextField(blank=True, null=True)
#	kt = RichTextField(blank=True, null=True)
	pera_fiyat = models.DecimalField('Fiyat', max_digits=6, decimal_places=2, blank=True, null=True)
	kamu_fiyat = models.DecimalField('Kamu Fiyatı', max_digits=6, decimal_places=2, blank=True, null=True)
	kamu_odenen = models.DecimalField('Kamu Ödenen', max_digits=6, decimal_places=2, blank=True, null=True)
	depo_fiyat = models.DecimalField('Depocu Fiyatı', max_digits=6, decimal_places=2, blank=True, null=True)
	imal_fiyat = models.DecimalField('İmalatçı Fiyatı', max_digits=6, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return "%s %s %s" %(str(self.ilac), self.ekisim, self.form)

	class Meta:
		verbose_name = "MustahzarBilgisi"
		verbose_name_plural = "Mustahzar Bilgileri"
		ordering = ['ilac', 'ekisim', 'adet', 'form']

class EDB(models.Model):
	birim_secenek = (
		('mg', 'miligram'),
		('gr', 'gram'),
		('ml', 'mililitre'),
		('ünite', 'ünite')
	)

	#id = models.AutoField(primary_key=True)
	mustahzar = models.ForeignKey(Mustahzar, on_delete=models.CASCADE)
	etkenmadde = models.ForeignKey(EtkenMadde, on_delete=models.CASCADE)
	#ilac = models.ForeignKey(Ilac, on_delete=models.CASCADE)
	doz = models.CommaSeparatedIntegerField(max_length=1000, blank=True, null=True)
	birim = models.CharField('Birim', max_length=2, choices=birim_secenek, default='mg', blank=True, null=True)

	def __str__(self):
		return "%s %s %s" %(str(self.etkenmadde), self.doz, self.birim)
