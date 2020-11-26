# Generated by Django 3.1.2 on 2020-11-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201126_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=200)),
                ('gambar', models.ImageField(blank=True, height_field=600, null=True, upload_to='', width_field=600)),
                ('description', models.TextField(null=True)),
                ('opsi_wakaf', models.CharField(choices=[('Wakaf Produktif', 'Wakaf Produktif'), ('Sedekah', 'Sedekah')], max_length=100)),
                ('keterangan', models.TextField()),
                ('kategori', models.CharField(choices=[('Galeri Foto / Gambar', 'Galeri Foto / Gambar'), ('URL', 'URL'), ('Katalog File', 'Katalog File'), ('PodCast / Audio', 'PodCast / Audio'), ('WebToon', 'WebToon'), ('Fotografi', 'Fotografi'), ('Ilustrasi', 'Ilustrasi'), ('Software', 'Software')], max_length=100)),
                ('konten_isi', models.BinaryField()),
                ('konten_bonus_tipe', models.CharField(choices=[('Galeri Foto / Gambar', 'Galeri Foto / Gambar'), ('URL', 'URL'), ('Katalog File', 'Katalog File'), ('PodCast / Audio', 'PodCast / Audio'), ('WebToon', 'WebToon'), ('Fotografi', 'Fotografi'), ('Ilustrasi', 'Ilustrasi'), ('Software', 'Software')], max_length=100, null=True)),
                ('konten_bonus_isi', models.BinaryField(null=True)),
                ('featured', models.BooleanField(default=False)),
                ('frontpage', models.BooleanField(default=False)),
                ('review', models.TextField(null=True)),
                ('status', models.CharField(choices=[('proposal', 'proposal'), ('disetujui', 'disetujui'), ('ditolak', 'ditolak'), ('bermasalah', 'bermasalah')], default='proposal', max_length=20)),
                ('tags', models.ManyToManyField(to='account.Tag')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]