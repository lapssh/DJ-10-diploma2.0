from django.db import models


class Section(models.Model):
    """
    Модель позволяет менять панель навигации, добавляя/удаляя секции разделов
    Имеет имея и слаг, для урлов.
    """
    name = models.CharField(max_length=50, verbose_name='Наименование раздела')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Модель позволяет в разделах создавать подразделы - категории.
    Обьлегчает навигацию, позволяет впихнуть невпихуемое.
    """
    name = models.CharField(max_length=50, verbose_name='Наименование категории')
    section = models.ForeignKey(
        Section, related_name='categories', on_delete=models.PROTECT, verbose_name='Раздел'
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name









