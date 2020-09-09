from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children');
    title = models.CharField(max_length=120, verbose_name='kategori')
    slug = models.SlugField(unique=True, editable=False)

    # content = models.TextField(verbose_name = 'metin')
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    # ----------------------------parent-----------------------------
    def __str__(self):
        full_path = [ self.title ]

        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[ ::1 ])

    def get_cat_list(self):
        k = self.category
        breadcrumb = [ "dummy" ]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[ i ] = '/'.join(breadcrumb[ -1:i - 1:-1 ])
        return breadcrumb[ -1:0:-1 ]

    # ----------------------------slug-----------------------------
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Category, self).save(*args, **kwargs)


class Blog(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='yazar', on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=120, verbose_name='başlık')
    # content = models.TextField(verbose_name = 'metin')
    content = RichTextField(verbose_name='metin')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    image = models.ImageField(null=True, blank=True, verbose_name='foto')
    publishing_date = models.DateTimeField(verbose_name='tarih')
    onem = models.BooleanField(default='True')
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Blog, self).save(*args, **kwargs)
