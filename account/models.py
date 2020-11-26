from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    kota = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(Customer):
      return self.user.first_name + "(" + str(self.user.email) + ")"

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    KATEGORI = (
      ('Galeri Foto / Gambar','Galeri Foto / Gambar'),
      ('URL','URL'),
      ('Katalog File','Katalog File'),
      ('PodCast / Audio','PodCast / Audio'),
      ('WebToon','WebToon'),
      ('Fotografi', 'Fotografi'),
      ('Ilustrasi','Ilustrasi'),
      ('Software', 'Software'),
    )

    OPSI = (
      ('Wakaf Produktif','Wakaf Produktif'),
      ('Sedekah','Sedekah'),
    )

    STATUS = (
      ('proposal','proposal'),
      ('disetujui','disetujui'),
      ('ditolak','ditolak'),
      ('bermasalah','bermasalah'),
    )

    judul = models.CharField(max_length=200)
    gambar = models.ImageField(width_field=600, height_field=600, null=True, blank=True)
    description = models.TextField(null=True)
    opsi_wakaf = models.CharField(max_length=100, choices=OPSI)
    keterangan = models.TextField()
    kategori = models.CharField(max_length=100, choices=KATEGORI)
    konten_isi = models.BinaryField()
    tags = models.ManyToManyField(Tag)

    konten_bonus_tipe = models.CharField(max_length=100, choices=KATEGORI, null=True)
    konten_bonus_isi = models.BinaryField(null=True)

    featured = models.BooleanField(default=False)
    frontpage = models.BooleanField(default=False)
    review = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='proposal')
    
    def __str__(self):
      return str(self.judul) 


