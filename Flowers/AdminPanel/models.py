from django.db import models


class Categories(models.Model):
    name = models.CharField(verbose_name="Раздел бота", max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел бота"
        verbose_name_plural = "Разделы бота"


class System(models.Model):
    variable = models.CharField(verbose_name="Переменная", max_length=255, help_text="Это поле не редактируется")
    text = models.CharField(verbose_name="Значение")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Раздел")
    screen = models.IntegerField(verbose_name="Экран")

    def __str__(self):
        return self.variable

    class Meta:
        verbose_name = "Системная переменная"
        verbose_name_plural = "Системные переменные"


class Buttons(models.Model):
    variable = models.CharField(verbose_name="Переменная", max_length=255, help_text="Это поле не редактируется")
    text = models.CharField(verbose_name="Значение", max_length=20, help_text="Максимальное количество символов: 20")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Раздел")
    screen = models.IntegerField(verbose_name="Экран")

    def __str__(self):
        return self.variable

    class Meta:
        verbose_name = "Кнопка бота"
        verbose_name_plural = "Кнопки бота"


class Messages(models.Model):
    variable = models.CharField(verbose_name="Переменная", max_length=255, help_text="Это поле не редактируется")
    text = models.TextField(verbose_name="Значение", max_length=1024, help_text="Максимальное количество символов: 1024")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Раздел")
    screen = models.IntegerField(verbose_name="Экран")

    def __str__(self):
        return self.variable

    class Meta:
        verbose_name = "Сообщение бота"
        verbose_name_plural = "Сообщения бота"


class Lists(models.Model):
    variable = models.CharField(verbose_name="Переменная", max_length=255, help_text="Это поле не редактируется")
    text = models.CharField(verbose_name="Значение", max_length=20, help_text="Максимальное количество символов: 20")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Раздел")
    screen = models.IntegerField(verbose_name="Экран")

    def __str__(self):
        return self.variable

    class Meta:
        verbose_name = "Список бота"
        verbose_name_plural = "Списки бота"


class ListTitles(models.Model):
    variable = models.CharField(verbose_name="Переменная", max_length=255, help_text="Это поле не редактируется")
    text = models.CharField(verbose_name="Значение", max_length=20, help_text="Максимальное количество символов: 20")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name="Раздел")
    screen = models.IntegerField(verbose_name="Экран")

    def __str__(self):
        return self.variable

    class Meta:
        verbose_name = "Заголовок списка"
        verbose_name_plural = "Заголовки списков"


class BouquetType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип букета"
        verbose_name_plural = "Типы букетов"


class FlowerType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20)
    bouquet_type = models.ForeignKey(BouquetType, on_delete=models.CASCADE, related_name='flower_types', verbose_name="Тип букета")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип цветка"
        verbose_name_plural = "Типы цветков"


class FlowerSubtype(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20)
    flower_type = models.ForeignKey(FlowerType, on_delete=models.CASCADE, related_name='sub_types', verbose_name="Тип цветка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подвид цветка"
        verbose_name_plural = "Подвиды цветков"


class FlowerColor(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20)
    flower_subtype = models.ForeignKey(FlowerSubtype, on_delete=models.CASCADE, related_name='colors', verbose_name="Подтип цветка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет цветка"
        verbose_name_plural = "Цвета цветков"
