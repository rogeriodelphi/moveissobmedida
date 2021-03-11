from django.db import models


class Movel(models.Model):
    situacao_CHOICES = (
        ("NO", "Novo"),
        ("US", "Usado"),
        ("CD", "Com Defeito")
    )
    categoria_CHOICES = (
        ("RE", "Residencial"),
        ("EC", "Escritório"),
        ("HO", "Home-office"),
        ("ES", "Estudante"),
    )

    nome = models.CharField('Nome', max_length=60)
    descricao = models.TextField('Descrição', blank=True, null=True)
    cor = models.CharField('Cor', max_length=40)
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor R$")
    situacao = models.CharField('Situação', max_length=2, choices=situacao_CHOICES)
    categoria = models.CharField('Situação', max_length=2, choices=categoria_CHOICES)

    class Meta:
        managed = True
        db_table = 'Movel'
        ordering = ['nome']
        verbose_name = 'Móvel'
        verbose_name_plural = 'Móveis'

    def __str__(self):
        return self.nome
