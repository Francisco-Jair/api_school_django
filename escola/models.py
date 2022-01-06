from django.db import models
from django.db.models.base import Model

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9) 
    cpf = models.CharField(max_length=11) 
    data_nascimento = models.DateField()

    def __str__(self) -> str:
        """O que vai aparecer no Admin e para informar o objeto"""
        return self.nome 


class Curso(models.Model):
    NIVEL = (
        ('B', "Básico"),
        ('I', "Intermediario"),
        ('A', "Avançado")
    )

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self) -> str:
        return self.descricao