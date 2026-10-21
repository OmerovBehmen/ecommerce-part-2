from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class GeneralCategory(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories/images')
    general_category = models.ForeignKey(GeneralCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Campaign(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_slide = models.BooleanField(default=False)
    image = models.ImageField(upload_to="campaigns")
    discount_percent = models.FloatField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    old_price = models.FloatField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    price = models.FloatField()
    description = models.TextField()
    sizes = models.ManyToManyField(Size, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')
    categories = models.ManyToManyField(Category, related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title