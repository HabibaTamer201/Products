from django.db import models

class Product(models.Model):
    
    name = models.CharField(max_length=100, verbose_name="Product Name")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    
    category = models.CharField(
        max_length=50,
        choices=[('ELEC', 'Electronics'), ('CLOT', 'Clothing')],
        help_text="Select product category"
    )

    
    release_date = models.DateField(blank=True, null=True)
    available_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    
    def __str__(self):
        return f"{self.name} - {self.price}"


    class Meta:
        ordering = ['-name']   