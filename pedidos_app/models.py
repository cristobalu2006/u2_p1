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



class pedido(models.Model):
    fecha = models.DateTimeField(null=False)
    pagado = models.BooleanField(null=False)


    #1-N: un cliente realiza muchos pedidos
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE) #FK con cliente

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ["fecha"]
    
    def __str__(self) -> str:
        return f"Id de Cliente: {self.cliente} Fecha: {self.fecha} Pagado: {self.pagado}"




class item(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.PROTECT)

    cantidad = models.PositiveIntegerField(null=False)
    precio_unitario = models.PositiveIntegerField(null=False)
    
    class Meta:
        verbose_name_plural = "Items"
        #ordering = ["precio"]
    
    def __str__(self) -> str:
        return f"cantidad: {self.cantidad} precio: {self.precio_unitario}"


class producto_categorias(models.Model):
    productos = models.ForeignKey(producto, on_delete=models.CASCADE)
    categorias = models.ForeignKey(categoria, on_delete=models.CASCADE)

    class meta:
        verbose_name_plural = "productos"
        #ordering = ["precio"]
    
    def __str__(self) -> str:
        return f""