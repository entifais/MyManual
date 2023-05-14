from django.db import models

class persona(models.Model):
	nombre=models.CharField(max_length=30)
	email=models.EmailField()
	genero=models.CharField(max_length=10)
	def __str__(self):
		return self.nombre
class gusto_disgusto(models.Model):
	idpersona=models.ForeignKey(persona,on_delete=models.CASCADE)
	objeto_favorito=models.CharField(max_length=30)
	deseos_intimos=models.CharField(max_length=30)
	donde_tocas=models.CharField(max_length=10)
	comida_favorita=models.CharField(max_length=30)
	me_gusta_de_otros=models.CharField(max_length=30)
	def __str__(self):
		return "gustos "+str(self.idpersona)
class confianza(models.Model):
	confia_en=models.ForeignKey(persona,on_delete=models.CASCADE,related_name='confia_en')
	quien_confia=models.ForeignKey(persona,on_delete=models.CASCADE,related_name='quien_confia')
	nivel=models.IntegerField()
	def __str__(self):
		return "confianza de "+str(self.confia_en)+" a "+str(self.quien_confia)
class decifrarme(models.Model):
	idpersona=models.ForeignKey(persona,on_delete=models.CASCADE)
	cuando_borracho=models.CharField(max_length=200)
	cuando_triste=models.CharField(max_length=200)
	cuando_no_respondo=models.CharField(max_length=200)
	cuando_peleamos=models.CharField(max_length=200)
	def __str__(self):
		return "desifrarme de "+str(self.idpersona)

class actividades(models.Model):
	idpersona=models.ForeignKey(persona,on_delete=models.CASCADE)
	deporte=models.CharField(max_length=20)
	serie=models.CharField(max_length=20)
	musica=models.CharField(max_length=20)
	hobbie=models.CharField(max_length=20)
	def __str__(self):
		return "actividades de "+str(self.idpersona)

#finish actividades
#categorias=models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)