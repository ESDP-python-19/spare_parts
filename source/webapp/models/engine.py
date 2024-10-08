from django.db import models

type_choices = [
    ('gasoline', 'Бензиновый'),
    ('diesel', 'Дизельный'),
    ('electric', 'Электрический'),
    ('hybrid', 'Гибридный'),
]


# Модель для двигателей
class Engine(models.Model):
    engine_type = models.CharField(max_length=50, choices=type_choices)  # тип двигателя
    displacement = models.DecimalField(max_digits=5, decimal_places=2)  # объём двигателя (литр)
    horsepower = models.PositiveIntegerField()  # мощность (лошадиные силы)
    torque = models.PositiveIntegerField()  # крутящий момент (Нм)

    def __str__(self):
        return f"{self.get_engine_type_display()} {self.displacement}L, {self.horsepower} HP"

    class Meta:
        verbose_name_plural = "Двигатели"
        verbose_name = 'Двигатель'
        db_table = 'engine'
