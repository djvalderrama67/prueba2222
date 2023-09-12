from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Vehiculo (models.Model):
    idVehiculo = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Nombre del vehiculo')
    capacidad = models.IntegerField(verbose_name='Capacidad del vehiculo')
    volumen_carga = models.FloatField(verbose_name='Volumen de carga (m³)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

class Bodega (models.Model):
    idBodega = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50, verbose_name='Nombre de la bodega')
    capacidad = models.IntegerField(verbose_name='Capacidad de la bodega')
    area = models.FloatField(verbose_name='Area (m²)')
    volumen = models.FloatField(verbose_name='Volumen (m³)')
    altura = models.FloatField(verbose_name='Altura (m)')
    largo = models.FloatField(verbose_name='Largo (m)')
    ancho = models.FloatField(verbose_name='Ancho (m)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'

class Objeto (models.Model):
    idObjeto = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50, verbose_name='Nombre del objeto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    largo = models.FloatField(verbose_name='Largo (m)')
    ancho = models.FloatField(verbose_name='Ancho (m)')
    alto = models.FloatField(verbose_name='Alto (m)')
    volumen = models.FloatField(verbose_name='Volumen (m³)', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.volumen = self.largo * self.ancho * self.alto
        super(Objeto, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'

class Calculo (models.Model):
    idCalculo = models.AutoField(primary_key=True, verbose_name='ID')
    objetos = models.ManyToManyField(Objeto)
    volumen_Total = models.FloatField(verbose_name='Volumen Total (m³)')
    idVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    idBodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.volumen_Total = sum(objeto.volumen for objeto in self.objetos.all())
        super(Calculo, self).save(*args, **kwargs)

    def __str__(self):
        return self.idCalculo

    class Meta:
        verbose_name = 'Calculo'
        verbose_name_plural = 'Calculos'