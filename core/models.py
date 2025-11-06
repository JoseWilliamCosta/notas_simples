from django.db import models

# Create your models here.

class Nota(models.Model):
    # Aqui temos que pensar como vai ficar essa ligação com Usuario e os outros relacionamentos.
    #usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notas') 
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.ImageField(upload_to='imagens_notas/', blank=True, null=True)
    arquivo = models.FileField(upload_to='arquivos_notas/', blank=True, null=True)

    # 🔗  relacionamentos
    #curso = models.ForeignKey('Curso', on_delete=models.SET_NULL, null=True, blank=True, related_name='notas')
    #campus = models.ForeignKey('Campus', on_delete=models.SET_NULL, null=True, blank=True, related_name='notas')

    def __str__(self):
        return self.titulo
