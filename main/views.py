from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timezone, datetime
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . forms import *
from . models import *


# Create your views here.
def index(response):
    return render(response, 'index.html')

def input(response):
    if response.method == 'POST':
        
        profilform = ProfilInput(response.POST)

        if profilform.is_valid():
            nik = profilform.cleaned_data['nik']
            nama = profilform.cleaned_data['nama']
            nikibu = profilform.cleaned_data['nikibu']
            tgl = profilform.cleaned_data['tgl']
            kelamin = profilform.cleaned_data['kelamin']
            namaibu = profilform.cleaned_data['namaibu']
            dusun = profilform.cleaned_data['dusun']

        p = Profil(nik=nik, nama=nama, tgl=tgl, nikibu=nikibu, dusun=dusun, kelamin=kelamin, namaibu=namaibu)
        p.save()

        profilform = ProfilInput()
        notif = "Sukses memasukan data"

        context = {
            'profilform'    : profilform,
            'notif'         : notif
        }

        return render(response, 'input.html', context)
    else:
        profilform = ProfilInput()
    
    return render(response, 'input.html', {'profilform' : profilform})

def action(response):
    profils = Profil.objects.all()
    umur = 0
    
    for profil in profils:
        date = profil.tgl
        umur = (datetime.now().date() - date).days // 7
        profil.umur = umur

    return render(response, 'action.html', {'profils' : profils, 'umur' : umur})


def posyandu(request, nik):
    x = Profil.objects.get(nik=nik)
    if request.method == 'POST':
        forms = PosyanduForm(request.POST, instance=x)
        if forms.is_valid():
            bulan = forms.cleaned_data['bulan']
            dusun = forms.cleaned_data['dusun']
            nik = forms.cleaned_data['nik']
            bb = forms.cleaned_data['bb']
            tb = forms.cleaned_data['tb']
            ll = forms.cleaned_data['ll']
            lk = forms.cleaned_data['lk']
            ket = forms.cleaned_data['ket']
            
            p = Profil.objects.get(nik=nik)
            p.posyandu_set.create(bulan=bulan, bb=bb, tb=tb, ll=ll, lk=lk, ket=ket, dusun=dusun)
            p.save()
            return redirect('main:action')  # Replace 'profil_list' with the actual URL name for your Profil list view
    else:
        forms = PosyanduForm()
    return render(request, 'posyandu.html', {'forms': forms, 'x' : x})

def inputposyandu(response, nik):
    data = Profil.objects.get(nik=nik)
    if response.method == 'POST':
        forms = PosyanduForm(response.POST)
        if forms.is_valid():
            bulan = forms.cleaned_data['bulan']
            bb = forms.cleaned_data['bb']
            tb = forms.cleaned_data['tb']
            ll = forms.cleaned_data['ll']
            lk = forms.cleaned_data['lk']
            ket = forms.cleaned_data['ket']
            
            p = Profil.objects.get(nik=nik)
            p.posyandu_set.create(bulan=bulan, bb=bb, tb=tb, ll=ll, lk=lk, ket=ket)
            p.save()
            return redirect('main:action')
    else:
        forms = PosyanduForm()
    
    return render(response, 'posyandu.html', {'forms' : forms, 'data' : data})

            
def riwayat(response):

    # profils = Profil.objects.all()
    # posyandus = Posyandu.objects.all()

    # context = {
    #     'pf' : profils,
    #     'ps' : posyandus,
    # }
    # return render(response, 'all.html', context)

    profils = Profil.objects.prefetch_related('posyandu_set')
    
    return render(response, 'all.html', {'profils': profils})

def riwayatfilter(request):
    bulan = request.GET.get('bulan')
    posyandu_list = Profil.objects.prefetch_related('posyandu_set')
    if bulan:
        pl = posyandu_list.filter(bulan=bulan)
        
        context = {
            'pl' : pl,
            'posyandu_list' : posyandu_list,
        }
        return render(request, 'riwayatfilter.html', context)