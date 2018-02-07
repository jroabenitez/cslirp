# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Cedulas(models.Model):
	cedula = models.CharField(primary_key=True, max_length=25)
	nombre = models.CharField(max_length=250, blank=True, null=True)
	apellido = models.CharField(max_length=250, blank=True, null=True)
	fechanac = models.DateField(blank=True, null=True)
	lugnac = models.CharField(max_length=50, blank=True, null=True)
	nacio = models.CharField(max_length=25, blank=True, null=True)
	sexo = models.CharField(max_length=10, blank=True, null=True)
	profesion = models.CharField(max_length=25, blank=True, null=True)
	estado_civil = models.CharField(max_length=10, blank=True, null=True)
	domicilio = models.CharField(max_length=120, blank=True, null=True)
	barrio_ciudad = models.CharField(max_length=120, blank=True, null=True)
	telefono = models.CharField(max_length=50, blank=True, null=True)
	celular = models.CharField(max_length=50, blank=True, null=True)
	padre_cedul = models.CharField(max_length=25, blank=True, null=True)
	padre_nombre = models.CharField(max_length=50, blank=True, null=True)
	padre_apelli = models.CharField(max_length=50, blank=True, null=True)
	madre_cedul = models.CharField(max_length=25, blank=True, null=True)
	madre_nombre = models.CharField(max_length=50, blank=True, null=True)
	madre_apelli = models.CharField(max_length=50, blank=True, null=True)
	conyu_cedul = models.CharField(max_length=25, blank=True, null=True)
	conyu_nombre = models.CharField(max_length=50, blank=True, null=True)
	conyu_apelli = models.CharField(max_length=50, blank=True, null=True)
	nuevo = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
	actualizado = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'cedulas'


class DjangoMigrations(models.Model):
	app = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	applied = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_migrations'


class Mabatch(models.Model):
	maba_user = models.CharField(max_length=30, blank=True, null=True)
	maba_dmaio = models.DateField(blank=True, null=True)
	maba_horio = models.CharField(max_length=8, blank=True, null=True)
	maba_prog = models.CharField(max_length=45, blank=True, null=True)
	maba_des = models.CharField(max_length=120, blank=True, null=True)
	maba_estad = models.CharField(max_length=3, blank=True, null=True)
	maba_param = models.TextField(blank=True, null=True)
	maba_dmace = models.DateField(blank=True, null=True)
	maba_horce = models.CharField(max_length=8, blank=True, null=True)
	maba_obs = models.TextField(blank=True, null=True)
	maba_resul = models.CharField(max_length=250, blank=True, null=True)
	maba_prior = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'mabatch'


class Macedula(models.Model):
	mace_cialf = models.CharField(db_column='MACE_CIALF', primary_key=True, max_length=20)  # Field name made lowercase.
	mace_cinum = models.DecimalField(db_column='MACE_CINUM', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
	mace_papel = models.CharField(db_column='MACE_PAPEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
	mace_sapel = models.CharField(db_column='MACE_SAPEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
	mace_pnomb = models.CharField(db_column='MACE_PNOMB', max_length=80, blank=True, null=True)  # Field name made lowercase.
	mace_snomb = models.CharField(db_column='MACE_SNOMB', max_length=80, blank=True, null=True)  # Field name made lowercase.
	mace_nombr = models.CharField(db_column='MACE_NOMBR', max_length=120)  # Field name made lowercase.
	mace_apell = models.CharField(db_column='MACE_APELL', max_length=120)  # Field name made lowercase.
	mace_sexo = models.CharField(db_column='MACE_SEXO', max_length=1, blank=True, null=True)  # Field name made lowercase.
	mace_nacio = models.CharField(db_column='MACE_NACIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
	mace_direc = models.CharField(db_column='MACE_DIREC', max_length=254, blank=True, null=True)  # Field name made lowercase.
	mace_dmana = models.DateField(db_column='MACE_DMANA', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'macedula'


class Maclisuc(models.Model):
	macs_id = models.AutoField(primary_key=True)
	macs_maclid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	macs_razon = models.CharField(max_length=120, blank=True, null=True)
	macs_direccion = models.CharField(max_length=250, blank=True, null=True)
	macs_telefonos = models.CharField(max_length=50, blank=True, null=True)
	macs_email = models.CharField(max_length=50, blank=True, null=True)
	macs_ciudad = models.CharField(max_length=50, blank=True, null=True)
	macs_contacto = models.CharField(max_length=120, blank=True, null=True)
	macs_estado = models.CharField(max_length=3, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maclisuc'


class Maempres(models.Model):
	maem_nomem = models.CharField(max_length=80)
	maem_direm = models.CharField(max_length=80)
	maem_codem = models.CharField(primary_key=True, max_length=2)
	maem_telef = models.CharField(max_length=20)

	class Meta:
		managed = False
		db_table = 'maempres'


class Maesttac(models.Model):
	matc_secta = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matc_codsi = models.ForeignKey('Masistem', db_column='matc_codsi')
	matc_tabla = models.CharField(max_length=40, blank=True, null=True)
	matc_tabno = models.CharField(max_length=255, blank=True, null=True)
	matc_log = models.CharField(max_length=1, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maesttac'


class Maesttad(models.Model):
	matd_codta = models.ForeignKey(Maesttac, db_column='matd_codta')
	matd_campo = models.CharField(max_length=40, blank=True, null=True)
	matd_tipo = models.CharField(max_length=5, blank=True, null=True)
	matd_long = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matd_decim = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matd_camno = models.CharField(max_length=255, blank=True, null=True)
	matd_camge = models.CharField(max_length=40, blank=True, null=True)
	matd_camta = models.CharField(max_length=40, blank=True, null=True)
	matd_sec = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matd_oblig = models.CharField(max_length=5, blank=True, null=True)
	matd_const = models.CharField(max_length=5, blank=True, null=True)
	matd_tabre = models.CharField(max_length=40, blank=True, null=True)
	matd_camre = models.CharField(max_length=40, blank=True, null=True)
	matd_selec = models.CharField(max_length=255, blank=True, null=True)
	matd_liord = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matd_url = models.CharField(max_length=80, blank=True, null=True)
	matd_untog = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	matd_vadef = models.CharField(max_length=40, blank=True, null=True)
	matd_flin = models.CharField(max_length=1, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maesttad'


class Magrupos(models.Model):
	magr_nombr = models.CharField(max_length=80, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'magrupos'


class Maparam(models.Model):
	mapc_idpar = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
	mapc_valor = models.CharField(max_length=120, blank=True, null=True)
	mapc_nombr = models.CharField(max_length=250, blank=True, null=True)
	mapc_tipo = models.CharField(max_length=3, blank=True, null=True)
	mapc_idpad = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	mapc_mant = models.CharField(max_length=3, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maparam'


class Maprogra(models.Model):
	mapr_codem = models.ForeignKey(Maempres, db_column='mapr_codem')
	mapr_codsi = models.ForeignKey('Masistem', db_column='mapr_codsi')
	mapr_tippr = models.ForeignKey('Matiprog', db_column='mapr_tippr')
	mapr_numpr = models.DecimalField(max_digits=2, decimal_places=0)
	mapr_nompr = models.CharField(max_length=80)
	mapr_banha = models.CharField(max_length=1)
	mapr_pagin = models.CharField(max_length=80, blank=True, null=True)
	mapr_padre = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
	mapr_copro = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maprogra'


class Maprogru(models.Model):
	mapg_codgr = models.ForeignKey(Magrupos, db_column='mapg_codgr')
	mapg_copro = models.ForeignKey(Maprogra, db_column='mapg_copro')

	class Meta:
		managed = False
		db_table = 'maprogru'


class Maprousu(models.Model):
	mapu_copro = models.ForeignKey(Maprogra, db_column='mapu_copro')
	mapu_codus = models.IntegerField()
	mapu_codgr = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	mapu_codsi = models.CharField(max_length=2, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maprousu'


class Maruc(models.Model):
	maru_ruc = models.CharField(max_length=30, blank=True, null=True)
	maru_razon = models.TextField(blank=True, null=True)
	maru_digve = models.CharField(max_length=1, blank=True, null=True)
	maru_rucvie = models.CharField(max_length=30, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'maruc'


class Masistem(models.Model):
	masi_codem = models.ForeignKey(Maempres, db_column='masi_codem')
	masi_nomsi = models.CharField(max_length=80)
	masi_habsi = models.CharField(max_length=1)
	masi_codsi = models.CharField(primary_key=True, max_length=2)
	masi_dirpr = models.CharField(max_length=80, blank=True, null=True)
	masi_peram = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
	masi_dirar = models.CharField(max_length=80, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'masistem'


class Matiprog(models.Model):
	matp_nomtp = models.CharField(max_length=80)
	matp_tippr = models.CharField(primary_key=True, max_length=3)

	class Meta:
		managed = False
		db_table = 'matiprog'


class Pralmacen(models.Model):
	pral_id = models.AutoField(primary_key=True)
	pral_descripcion = models.CharField(max_length=120, blank=True, null=True)
	pral_tipo = models.CharField(max_length=3, blank=True, null=True)
	pral_sucid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'pralmacen'


class Prcategoria(models.Model):
	prca_id = models.AutoField(primary_key=True)
	prca_nombre = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prcategoria'


class Prenviosc(models.Model):
	prec_id = models.AutoField(primary_key=True)
	prec_dmaenv = models.DateField(blank=True, null=True)
	prec_maclid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prec_estado = models.CharField(max_length=3, blank=True, null=True)
	prec_obs = models.TextField(blank=True, null=True)
	prec_now = models.TimeField(blank=True, null=True)
	prec_user = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prenviosc'


class Prenviosd(models.Model):
	pred_id = models.AutoField(primary_key=True)
	pred_precid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pred_pridid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pred_estado = models.CharField(max_length=3, blank=True, null=True)
	pred_dmadev = models.DateField(blank=True, null=True)
	pred_user = models.CharField(max_length=50, blank=True, null=True)
	pred_now = models.TimeField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prenviosd'


class Prinventarioc(models.Model):
	pric_id = models.AutoField(primary_key=True)
	pric_numini = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pric_numfin = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pric_cantidad = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pric_estado = models.CharField(max_length=3, blank=True, null=True)
	pric_tipo = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	pric_dmaing = models.DateField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prinventarioc'


class Prinventariod(models.Model):
	prid_id = models.AutoField(primary_key=True)
	prid_pricid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prid_codigo = models.CharField(max_length=50, blank=True, null=True)
	prid_dmaing = models.DateField(blank=True, null=True)
	prid_dmaegr = models.DateField(blank=True, null=True)
	prid_estado = models.CharField(max_length=3, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prinventariod'


class Prmovc(models.Model):
	prmc_id = models.AutoField(primary_key=True)
	prmc_dmamov = models.DateField(blank=True, null=True)
	prmc_tipmov = models.CharField(max_length=3, blank=True, null=True)
	prmc_alori = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_aldes = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_macsid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_dmarec = models.DateField(blank=True, null=True)
	prmc_responsable = models.CharField(max_length=120, blank=True, null=True)
	prmc_user = models.CharField(max_length=50, blank=True, null=True)
	prmc_now = models.TimeField(blank=True, null=True)
	prmc_estado = models.CharField(max_length=3, blank=True, null=True)
	prmc_maclid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_numrec = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_receptor = models.CharField(max_length=120, blank=True, null=True)
	prmc_macsfin = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmc_macsfino = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prmovc'


class Prmovd(models.Model):
	prmd_id = models.AutoField(primary_key=True)
	prmd_prmcid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmd_prprid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prmd_serie = models.CharField(max_length=50, blank=True, null=True)
	prmd_estado = models.CharField(max_length=3, blank=True, null=True)
	prmd_cantidad = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prmovd'


class Prproducto(models.Model):
	prod_id = models.AutoField(primary_key=True)
	prod_nombre = models.CharField(max_length=250, blank=True, null=True)
	prod_categoria = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prod_codigo = models.CharField(max_length=50, blank=True, null=True)
	prod_estado = models.CharField(max_length=3, blank=True, null=True)
	prod_obs = models.TextField(blank=True, null=True)
	prod_canpres = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	prod_recibo = models.CharField(max_length=1, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'prproducto'


class Rh003(models.Model):
	rh03_periodo = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	rh03_ccosto = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	rh03_funcionario = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	rh03_id = models.AutoField(primary_key=True)
	rh03_razon = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'rh003'


class Roles(models.Model):
	rol_id = models.AutoField(primary_key=True)
	rol_nombre = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'roles'


class Rolpro(models.Model):
	ropr_id = models.AutoField(primary_key=True)
	ropr_proid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	ropr_rolid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'rolpro'


class Rolusu(models.Model):
	rous_id = models.AutoField(primary_key=True)
	rous_rolid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	rous_usuid = models.CharField(max_length=50, blank=True, null=True)
	rous_dmaasi = models.DateField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'rolusu'
		unique_together = (('rous_rolid', 'rous_usuid'),)


class Stdepartamentos(models.Model):
	stdp_id = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
	stdp_nombre = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'stdepartamentos'
		verbose_name='Departamentos'
	def __unicode__(self):
		return '%s / %s ' % (self.stdp_id, self.stdp_nombre )

class Stdistritos(models.Model):
	stdi_stdpid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	stdi_nombre = models.CharField(max_length=120, blank=True, null=True)
	stdi_stcod = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	stdi_id = models.AutoField(primary_key=True)

	class Meta:
		managed = False
		db_table = 'stdistritos'
		verbose_name='Distritos'
	def __unicode__(self):
		return '%s / %s ' % (self.stdi_id, self.stdi_nombre )

class Stlocalidades(models.Model):
	stlo_id = models.AutoField(primary_key=True)
	stlo_stdiid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	stlo_nombre = models.CharField(max_length=250, blank=True, null=True)
	stlo_stcod = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'stlocalidades'
		verbose_name='Localidades'
	def __unicode__(self):
		return '%s / %s ' % (self.stlo_id, self.stlo_nombre )


class Strrhh(models.Model):
	strh_id = models.AutoField(primary_key=True)
	strh_documento = models.CharField(max_length=20, blank=True, null=True)
	strh_dv = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_papell = models.CharField(max_length=50, blank=True, null=True)
	strh_sapell = models.CharField(max_length=50, blank=True, null=True)
	strh_pnombre = models.CharField(max_length=50, blank=True, null=True)
	strh_snombre = models.CharField(max_length=50, blank=True, null=True)
	strh_sttpid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_monbru = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_desjub = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_dessegsoc = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_desotr = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_monagui = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_email = models.CharField(max_length=100, blank=True, null=True)
	strh_stdpid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_stdiid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_stlocid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_direccion = models.CharField(max_length=100, blank=True, null=True)
	strh_plb = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_nlb = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_pcel = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_cel = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_stteid = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_estado = models.CharField(max_length=3, blank=True, null=True)
	strh_escon = models.CharField(max_length=3, blank=True, null=True)
	strh_prep = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_sprep = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
	strh_dmarep = models.DateField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'strrhh'
		verbose_name='Recursos Humanos'
	def __unicode__(self):
		return '%s / %s / %s' % (self.strh_documento, self.strh_papell,self.strh_pnombre)

class Sttipoempleado(models.Model):
	stte_id = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
	stte_nombre = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'sttipoempleado'
		verbose_name='Tipo de Empleado'
	def __unicode__(self):
		return '%s / %s ' % (self.stte_id, self.stte_nombre )


class Sttipopago(models.Model):
	sttp_id = models.DecimalField(primary_key=True, max_digits=15, decimal_places=0)
	sttp_nombre = models.CharField(max_length=120, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'sttipopago'
		verbose_name='Tipo de Pago'
	def __unicode__(self):
		return '%s / %s ' % (self.sttp_id, self.sttp_nombre )


class Usuarios(models.Model):
	usu_id = models.CharField(primary_key=True, max_length=50)
	usu_tipo = models.CharField(max_length=1, blank=True, null=True)
	usu_nombres = models.CharField(max_length=50, blank=True, null=True)
	usu_apellidos = models.CharField(max_length=50, blank=True, null=True)
	usu_estado = models.CharField(max_length=3, blank=True, null=True)
	usu_dmauin = models.CharField(max_length=50, blank=True, null=True)
	usu_pass = models.CharField(max_length=120, blank=True, null=True)
	pori = models.CharField(max_length=20, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'usuarios'
