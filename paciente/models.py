from django.db import models

# Create your models here.


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Tipo usuario: {self.nombre} id: {self.id}'


class TipoSangre(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Tipo sangre: {self.nombre}'


class TipoSexo(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Tipo Sexo: {self.nombre}'


class Paciente(models.Model):
    tipo_usuario = models.ForeignKey(
        TipoUsuario, verbose_name='Tipo de usuario', on_delete=models.PROTECT)
    tipo_sangre = models.ForeignKey(
        TipoSangre, verbose_name='Tipo de sangre', on_delete=models.PROTECT)
    tipo_sexo = models.ForeignKey(
        TipoSexo, verbose_name='Tipo de sexo', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    foto = models.ImageField(
        upload_to='fotopaciente/%Y/%m/%d', null=True, blank=True)
    email = models.EmailField(
        verbose_name='correo electronico', blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'id: {self.id} Usuario: {self.nombre} tipo usuario: {self.tipo_usuario}'


class DatosGeneral(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    domicilio = models.CharField(max_length=150, blank=True, null=True)
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    cp = models.PositiveIntegerField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=150, blank=True, null=True)
    ocupacion = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    clave_app = models.CharField(max_length=10, blank=True, null=True)
    datofiscal = models.FileField(
        upload_to='datofiscal/%Y/%m/%d', null=True, blank=True, verbose_name='Curriculum vitae')

    def __str__(self):
        return f'Id: {self.id} {self.propietario}'


class Preferencia(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    nombre_pareja = models.CharField(max_length=25, blank=True, null=True)
    fecha_aniversario = models.DateField(blank=True, null=True)
    nombre_hijos = models.CharField(max_length=25, blank=True, null=True)
    fecha_hijo = models.DateField(blank=True, null=True)
    nombre_empresa = models.CharField(max_length=50, blank=True, null=True)
    puesti = models.CharField(max_length=50, blank=True, null=True)
    fecha_empresa = models.DateField(blank=True, null=True)
    deportes = models.CharField(max_length=150, blank=True, null=True)
    pelicula_serie = models.CharField(max_length=150, blank=True, null=True)
    musica = models.CharField(max_length=150, blank=True, null=True)
    vehiculo = models.CharField(max_length=150, blank=True, null=True)
    comida = models.CharField(max_length=150, blank=True, null=True)


class NotaPaciente(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    alergias = models.CharField(max_length=250, blank=True, null=True)
    expectativas = models.CharField(max_length=250, blank=True, null=True)
    pade_actual = models.CharField(max_length=250, blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'


class AntecedentePersonal(models.Model):
    propietario = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    casa = models.CharField(max_length=25, blank=True, null=True)
    lav_dientes = models.CharField(max_length=25, blank=True, null=True)
    tipo_pasta = models.CharField(max_length=25, blank=True, null=True)
    amalgama_puente = models.CharField(max_length=25, blank=True, null=True)
    brakets = models.CharField(max_length=25, blank=True, null=True)
    actividad_fisica = models.CharField(max_length=25, blank=True, null=True)
    ultima_desparacita = models.DateField(blank=True, null=True)
    inmunizaciones = models.CharField(max_length=25, blank=True, null=True)
    check_up = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'


class AntecedenteFamiliar(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    hermanos = models.PositiveIntegerField(default=0)
    diabetes = models.CharField(max_length=25, blank=True, null=True)
    hip_arterial = models.CharField(max_length=25, blank=True, null=True)
    cardiopatias = models.CharField(max_length=25, blank=True, null=True)
    hepatopatias = models.CharField(max_length=25, blank=True, null=True)
    urologicos = models.CharField(max_length=25, blank=True, null=True)
    neurologicos = models.CharField(max_length=25, blank=True, null=True)
    respiratorios = models.CharField(max_length=25, blank=True, null=True)
    cancer = models.CharField(max_length=25, blank=True, null=True)
    alergias = models.CharField(max_length=25, blank=True, null=True)
    metabolicas = models.CharField(max_length=25, blank=True, null=True)
    sanguineas = models.CharField(max_length=25, blank=True, null=True)
    articulares = models.CharField(max_length=25, blank=True, null=True)
    inmunologicas = models.CharField(max_length=25, blank=True, null=True)
    malformaciones = models.CharField(max_length=25, blank=True, null=True)
    dermatologicas = models.CharField(max_length=25, blank=True, null=True)
    otros = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'


class AntecedentePatologico(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    enf_infancia = models.CharField(max_length=25, blank=True, null=True)
    diabetes = models.CharField(max_length=25, blank=True, null=True)
    hip_arterial = models.CharField(max_length=25, blank=True, null=True)
    respiratorias = models.CharField(max_length=25, blank=True, null=True)
    oftalmico = models.CharField(max_length=25, blank=True, null=True)
    cardeovasculares = models.CharField(max_length=25, blank=True, null=True)
    neurologicos = models.CharField(max_length=25, blank=True, null=True)
    gastro_intestinal = models.CharField(max_length=25, blank=True, null=True)
    hepaticas = models.CharField(max_length=25, blank=True, null=True)
    metabolicas = models.CharField(max_length=25, blank=True, null=True)
    urologicos = models.CharField(max_length=25, blank=True, null=True)
    circulatorio = models.CharField(max_length=25, blank=True, null=True)
    traumaticas = models.CharField(max_length=25, blank=True, null=True)
    articulares = models.CharField(max_length=25, blank=True, null=True)
    dermatologicas = models.CharField(max_length=25, blank=True, null=True)
    quirurgicas = models.CharField(max_length=25, blank=True, null=True)
    transfusionales = models.CharField(max_length=25, blank=True, null=True)
    alergias = models.CharField(max_length=25, blank=True, null=True)
    vectores = models.CharField(max_length=25, blank=True, null=True)
    autoimunes = models.CharField(max_length=25, blank=True, null=True)
    emocionales = models.CharField(max_length=25, blank=True, null=True)
    adicciones = models.CharField(max_length=25, blank=True, null=True)
    hosp_previas = models.CharField(max_length=25, blank=True, null=True)
    pesticidas = models.CharField(max_length=25, blank=True, null=True)
    dx_ca = models.CharField(max_length=25, blank=True, null=True)
    otros = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'


class AntecedenteAlimenticio(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    comidas = models.CharField(max_length=50, blank=True, null=True)
    tortillas = models.CharField(max_length=25, blank=True, null=True)
    pan = models.CharField(max_length=25, blank=True, null=True)
    cereales = models.CharField(max_length=25, blank=True, null=True)
    refrescos = models.CharField(max_length=25, blank=True, null=True)
    jugos = models.CharField(max_length=25, blank=True, null=True)
    aguas_frescas = models.CharField(max_length=25, blank=True, null=True)
    frutas = models.CharField(max_length=25, blank=True, null=True)
    frutos_secos = models.CharField(max_length=25, blank=True, null=True)
    verduras = models.CharField(max_length=25, blank=True, null=True)
    agua_natural = models.CharField(max_length=25, blank=True, null=True)
    golosinas = models.CharField(max_length=25, blank=True, null=True)
    carnes_rojas = models.CharField(max_length=25, blank=True, null=True)
    pollo = models.CharField(max_length=25, blank=True, null=True)
    pescado = models.CharField(max_length=25, blank=True, null=True)
    mariscos = models.CharField(max_length=25, blank=True, null=True)
    leche = models.CharField(max_length=25, blank=True, null=True)
    derivados = models.CharField(max_length=25, blank=True, null=True)
    huevos = models.CharField(max_length=25, blank=True, null=True)
    arroz = models.CharField(max_length=25, blank=True, null=True)
    legumbres = models.CharField(max_length=25, blank=True, null=True)
    miel = models.CharField(max_length=25, blank=True, null=True)
    aceite = models.CharField(max_length=25, blank=True, null=True)
    sal = models.CharField(max_length=25, blank=True, null=True)
    azucar = models.CharField(max_length=25, blank=True, null=True)
    cafe = models.CharField(max_length=25, blank=True, null=True)
    te = models.CharField(max_length=25, blank=True, null=True)
    sazonadores = models.CharField(max_length=25, blank=True, null=True)
    embutidos = models.CharField(max_length=25, blank=True, null=True)
    enlatados = models.CharField(max_length=25, blank=True, null=True)
    pastas = models.CharField(max_length=25, blank=True, null=True)
    sumplementos_energe = models.CharField(
        max_length=25, blank=True, null=True)
    otros = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'


class Exploracion(models.Model):
    propietario = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    cerebro = models.CharField(max_length=150, blank=True, null=True)
    nervioso = models.CharField(max_length=150, blank=True, null=True)
    ocular = models.CharField(max_length=150, blank=True, null=True)
    endocrino = models.CharField(max_length=150, blank=True, null=True)
    corazon = models.CharField(max_length=150, blank=True, null=True)
    circulatorio = models.CharField(max_length=150, blank=True, null=True)
    respiratorio = models.CharField(max_length=150, blank=True, null=True)
    hepatico = models.CharField(max_length=150, blank=True, null=True)
    pancreas = models.CharField(max_length=150, blank=True, null=True)
    renal = models.CharField(max_length=150, blank=True, null=True)
    gastro = models.CharField(max_length=150, blank=True, null=True)
    oseoarticular = models.CharField(max_length=150, blank=True, null=True)
    tendo = models.CharField(max_length=150, blank=True, null=True)
    reproductivo = models.CharField(max_length=150, blank=True, null=True)
    inmunologico = models.CharField(max_length=150, blank=True, null=True)
    extremidades = models.CharField(max_length=150, blank=True, null=True)
    piel_tejido = models.CharField(max_length=150, blank=True, null=True)
    otros = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f'{self.propietario}'
