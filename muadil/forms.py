from django import forms

class IletisimForm(forms.Form):
	ad_soyad = forms.CharField(max_length=32)
	konu = forms.CharField(max_length=255)
	e_posta = forms.EmailField()
	mesaj = forms.CharField(widget=forms.Textarea)
