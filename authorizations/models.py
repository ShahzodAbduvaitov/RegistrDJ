from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи для авторизации'
        verbose_name_plural = 'Пользователи для авторизации'