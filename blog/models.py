from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название статьи", help_text="Например: Новости")
    slug = models.CharField(max_length=200, verbose_name="URL-адрес", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Название статьи", help_text="Например: сегодня 2025 года будет праздник!")
    slug = models.CharField(max_length=200, verbose_name="URL-адрес", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    content = models.TextField(verbose_name="Контент", blank=False)
    image = models.ImageField(upload_to="blog/", verbose_name="Изображение поста", blank=False, null=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title