from django.contrib import admin
from .models import Ilac, EtkenMadde, Mustahzar, EDB

class IlacAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	
	class Meta:
		model = Ilac

class EtkenMaddeAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'id')
	class Meta:
		model = EtkenMadde

class EDBInline(admin.TabularInline):
	#list_display = ('__str__', 'id')
	model = EDB
	extra = 1

class MustahzarAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'barkod', 'firma', 'aktif', 'id') #,'doz', 'birim')
	list_per_page = 20
	list_filter = ('firma', 'aktif')
	search_fields = ('ilac', 'barkod')
	ordering = ('ilac' , 'ekisim',)

	inlines = [EDBInline]

	# def uzun_isim(self, obj):
	#     return "%s %s %s %s %s" %(str(obj.ilac), obj.doz, obj.birim, obj.adet, obj.form)

	fieldsets = (
		(None, {
			'fields': (('ilac', 'ekisim', 'adet', 'form'), ('barkod', 'renk', 'firma', 'resim'), ('muadil', 'yakin_muadil'), )
		}),
		('Diğer Bilgiler', {
			'classes': ('collapse',),
			'fields': ('pera_fiyat', 'kamu_fiyat', 'kamu_odenen', 'depo_fiyat', 'imal_fiyat', 'aktif', ('sut', 'prospektus', 'kub', 'kt'), ),
		}),
	)

	class Meta:
		model = Mustahzar

admin.site.register(Ilac, IlacAdmin)
admin.site.register(EtkenMadde, EtkenMaddeAdmin)
admin.site.register(Mustahzar, MustahzarAdmin)
