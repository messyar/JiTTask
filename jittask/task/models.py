from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    """
    Model representing units for tasks
    """
    name = models.CharField(max_length=100, help_text='Введите наименование еденицы измерения')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Profile(models.Model):
    """
    Extends Profile of user
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    default_task_name = models.CharField(
        max_length=200,
        blank=True,
    )
    cost = models.PositiveSmallIntegerField(
        blank=True,
        help_text='Введите стомость работы по умолчанию за еденицу',
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True,
        help_text='Выберите еденицу измерения работ',
    )
    

class Client(models.Model):
    """
    Model representing clients
    """
    name = models.CharField(
        max_length=100,
        help_text='Введите наименование клиента',
    )
    inn = models.CharField(
        max_length=12,
        blank=True,
        help_text='Введите ИНН клиента(не обязательно)',
        unique=True,
    )
    tel = models.CharField(
        max_length=16,
        blank=True,
        help_text='Введите телефон клиента(не обязательно)',
    )
    email = models.EmailField(
        blank=True,
        help_text='Введит email (не обязательно)',
    )
    cost = models.PositiveSmallIntegerField(
        blank=True,
        help_text='Введите стомость работы по умолчанию за еденицу',
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Task(models.Model):
    """
    Model representing tasks
    """
    name = models.CharField(
        max_length=150,
        help_text='Введите наименование задачи',
    )
    describe = models.TextField(
        max_length=400,
        blank=True,
        help_text='Введите описание задачи (не обязательно)',
    )
    count = models.PositiveSmallIntegerField(
        blank=True,
        help_text='Введите количество затраченного времени'
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True,
    )
    sum = models.PositiveSmallIntegerField(
        help_text='Введите сумму',
    )
    date_of_task = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    paid = models.BooleanField(
        default=False,
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
