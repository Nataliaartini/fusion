import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


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
    product_description = models.TextField('Descrição', blank=True)
    product_icon = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)

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
    member_photo = StdImageField('Foto', upload_to=get_file_path, variations={'thumbnail': (480, 480, True)})
    facebook = models.CharField('Facebook', blank=True, default='#', max_length=100)
    twitter = models.CharField('Twitter', blank=True, default='#', max_length=100)
    linkedin = models.CharField('Linkedin', blank=True, default='#', max_length=100)
    github = models.CharField('Github', blank=True, default='#', max_length=100)
    instagram = models.CharField('Instagram', blank=True, default='#', max_length=100)

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def __str__(self):
        return self.member_name


class Feature(BaseModel):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Crescimento'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    feature_name = models.CharField('Recurso', max_length=100)
    feature_description = models.TextField('Descrição', blank=True)
    feature_icon = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)
