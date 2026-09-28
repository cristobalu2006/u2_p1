from django.db import models

class categoria(models.Model):
    #DJANGO crea automáticamente el ID de la serial. NO es necesario un atributo de ID adicional.
    nombre = models.CharField(max_length=80, unique=True)

    class Meta: #Esta función permite agregar metadatos de la clase, como su nombre en plural, el orden de los datos, etc.
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        return self.nombre


class producto(models.Model):
    nombre = models.CharField(max_length=120, null=False)
    descripcion = models.TextField(null=False)

    precio = models.PositiveBigIntegerField(null=False, default=0)

    stock = models.PositiveBigIntegerField(null=False, default=0)
    activo = models.BooleanField(default=False, null=True)
    creado = models.DateTimeField(null=False, auto_now_add=True)
    codigo = models.CharField(max_length=20,null=False)

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        return f"{self.nombre} ${self.precio}"





class cliente(models.Model):
    nombre = models.CharField(max_length=120, null=False)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Email: {self.email}"



#____________________________________________________________

