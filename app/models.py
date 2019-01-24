from django.db import models

class Feira(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    long = models.CharField(max_length=255, default="", blank=True)
    lat = models.CharField(max_length=255, default="", blank=True)
    set_cens = models.CharField(max_length=255, default="", blank=True)
    areap = models.CharField(max_length=255, default="", blank=True)
    cod_dist = models.CharField(max_length=255, default="", blank=True)
    distrito = models.CharField(max_length=255, default="", blank=True)
    cod_sub_pref = models.CharField(max_length=255, default="", blank=True)
    sub_prefe = models.CharField(max_length=255, default="", blank=True)
    regiao5 = models.CharField(max_length=255, default="", blank=True)
    regiao8 = models.CharField(max_length=255, default="", blank=True)
    nome_feira = models.CharField(max_length=255, default="")
    registro = models.CharField(max_length=255, default="", blank=True)
    logradouro = models.CharField(max_length=255, default="", blank=True)
    numero = models.CharField(max_length=255, default="", blank=True)
    bairro = models.CharField(max_length=255, default="", blank=True)
    referecia = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        db_table = "feira"
        ordering = ('id',)

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
