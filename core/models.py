from django.db import models
from stdimage.models import StdImageField


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Crescimento'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    product_name = models.CharField('Produto', max_length=100)
    description = models.TextField('Descrição', blank=True)
    icon = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.product_name


class Role(BaseModel):
    role_name = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.role_name


class Team(BaseModel):
    member_name = models.CharField('Nome', max_length=50)
    member_role = models.ForeignKey('core.Role', verbose_name='Cargo', on_delete=models.CASCADE)
    member_bio = models.TextField('Biografia', blank=True, max_length=200)
    member_photo = StdImageField('Foto', upload_to='team', variations={'thumbnail': (480, 480, True)})
