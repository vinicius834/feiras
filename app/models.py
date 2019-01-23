from django.db import models

class Feira(models.Model):
    id = models.AutoField(primary_key=True)
    long = models.CharField(max_length=255, null=False, default="")
    lat = models.CharField(max_length=255, null=False, default="")
    set_cens = models.CharField(max_length=255, null=False, default="")
    areap = models.CharField(max_length=255, null=False, default="")
    cod_dist = models.CharField(max_length=255, null=False, default="")
    distrito = models.CharField(max_length=255, null=False, default="")
    cod_sub_pref = models.CharField(max_length=255, null=False, default="")
    sub_prefe = models.CharField(max_length=255, null=False, default="")
    regiao5 = models.CharField(max_length=255, null=False, default="")
    regiao8 = models.CharField(max_length=255, null=False, default="")
    nome_feira = models.CharField(max_length=255, null=False, default="")
    registro = models.CharField(max_length=255, null=False, default="")
    logradouro = models.CharField(max_length=255, null=False, default="")
    numero = models.CharField(max_length=255, null=False, default="")
    bairro = models.CharField(max_length=255, null=False, default="")
    referecia = models.CharField(max_length=255, null=False, default="")


    def __str__(self):
        return """{0},
                  {1},
                  {2},
                  {3},
                  {4},
                  {5},
                  {6},
                  {7},
                  {8},
                  {9},
                  {10},
                  {11},
                  {12},
                  {13},
                  {14},
                  {15},
                  {16}""".format(self.id, self.long, self.lat, self.set_cens, self.areap, self.cod_dist,
                               self.distrito, self.cod_sub_pref, self.sub_prefe, self.regiao5, self.regiao8,
                               self.nome_feira, self.registro, self.logradouro, self.numero, self.bairro, self.referecia)
