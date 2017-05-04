from django.shortcuts import render#, get_object_or_404
from .models import Ilac, EtkenMadde, Mustahzar
from .forms import IletisimForm
from django.conf import settings
from django.core.mail import send_mail

def ilactemel(request):
	ilaclar = Ilac.objects.all()
	query = request.GET.get("q")
	if query:
	    ilaclar = ilaclar.filter(ilac_adi__icontains=query)
	template = "ilactemel.html"
	context = {
	    'ilaclar': ilaclar,
	}
	return render(request, template, context)

def ilaccesit(request, id, **kwargs):
	ilaclar = Ilac.objects.all()
	ilaccesitleri = Mustahzar.objects.filter(ilac=id)

	template = "ilaccesit.html"
	context = {
	    'ilaclar': ilaclar,
	    'ilaccesitleri': ilaccesitleri,
	}
	return render(request, template, context)

def ilacdetay(request, id, pk, **kwargs):
	ilaclar = Ilac.objects.all()
	ilaccesitleri = Mustahzar.objects.filter(ilac=id)
	ilacdetaylari = Mustahzar.objects.filter(id=pk)
	template = "ilacdetay.html"
	context = {
	    'ilaclar': ilaclar,
	    'ilaccesitleri': ilaccesitleri,
	    #'ilacdozbirim1' : ilacdozbirim1,
	    'ilacdetaylari': ilacdetaylari,
	}
	return render(request, template, context)

# def emtemel(request):
#     etkenmaddeler = EtkenMadde.objects.all()
#     query = request.GET.get("q")
#     if query:
#         etkenmaddeler = etkenmaddeler.filter(isim__icontains=query)
#     template = "emtemel.html"
#     context = {
#         'etkenmaddeler': etkenmaddeler,
#     }
#     return render(request, template, context)

# def emcesit(request, idsi):
#     etkenmaddeler = EtkenMadde.objects.all()
#     emcesitleri = Bilgi.objects.filter(etkenmadde=idsi)
#     template = "emcesit.html"
#     context = {
#         'etkenmaddeler': etkenmaddeler,
#         'emcesitleri': emcesitleri,
#     }
#     return render(request, template, context)

def iletisim(request):
    form = IletisimForm(request.POST or None)
    if form.is_valid():
        form_ad_soyad = form.cleaned_data.get("ad_soyad")
        form_konu = form.cleaned_data.get("konu")
        form_eposta = form.cleaned_data.get("eposta")
        form_mesaj = form.cleaned_data.get("mesaj")
        # print(ad_soyad, konu, eposta, mesaj)

        konu = 'RxMuadil İletişim Formu'
        epostam = settings.EMAIL_HOST_USER
        kime_eposta = [epostam, ]
        iletisim_mesaji = """
            Adı Soyadı : %s
            Konu : %s
            Mesaj : %s
            Eposta : %s
        """ %(
                form_ad_soyad,
                form_konu,
                form_mesaj,
                form_eposta
            )

        send_mail(
            konu,
            iletisim_mesaji,
            epostam,
            kime_eposta,
            fail_silently=False
                )

    context = {
        "form": form,
    }
    return render(request, "iletisim.html", context)

def kimimben(request):
    return render(request, "kimimben.html", {})
