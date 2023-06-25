from django.db import models

# Create your models here.
class Profil(models.Model):
    nik     = models.IntegerField()
    nama    = models.CharField(max_length=40)
    tgl     = models.DateField()
    kelamin = models.CharField(max_length=10)
    namaibu = models.CharField(max_length=40)
    nikibu  = models.IntegerField()
    dusun  = models.CharField(max_length=30, default='Sumberejo')

    def __str__(self):
        return f"{self.nik}, {self.nama}, {self.namaibu}"
    
class Posyandu(models.Model):
    bulan  = models.CharField(max_length=20, default='Januari')
    nik = models.ForeignKey(Profil, on_delete=models.CASCADE)
    tb  = models.IntegerField()
    bb  = models.IntegerField()
    ll  = models.IntegerField()
    lk  = models.IntegerField()
    ket = models.CharField(max_length=20,)

    def __str__(self):
        return f"{self.nik.nama}, {self.bulan}, {self.tb}, {self.bb}"