from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from stdimage.models import StdImageField

# Create your models here.


class Base(models.Model):
    created_at = models.DateField('Created At', auto_now_add=True)
    updated_at = models.DateField('Updated At', auto_now=True)
    status = models.BooleanField('Status', default=True)

    class Meta:
        abstract = True


class Product(Base):
    name = models.CharField('Nome', max_length=120)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Estoque')
    image = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=120, blank=True, editable=False)

    def __str__(self):
        return self.name


def product_pre_save(signal, instance, sender, **kwars):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
