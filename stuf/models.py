# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class MaterialColleccio(models.Model):
    titol = models.CharField(unique=True, max_length=100)
    uf = models.ForeignKey('UfsUf', models.DO_NOTHING)
    es_publica = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'material_colleccio'


class MaterialComentarimaterial(models.Model):
    material = models.ForeignKey('MaterialMaterial', models.DO_NOTHING)
    perfil = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True)
    comentari = models.TextField()
    data = models.DateTimeField()
    comentari_html = models.TextField()

    class Meta:
        managed = False
        db_table = 'material_comentarimaterial'


class MaterialImatgematerial(models.Model):
    material = models.ForeignKey(
        'MaterialMaterial', models.DO_NOTHING, blank=True, null=True)
    imatge_url = models.CharField(max_length=200)
    perfil = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True)
    data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'material_imatgematerial'


class MaterialMaterial(models.Model):
    colleccio = models.ForeignKey(
        MaterialColleccio, models.DO_NOTHING, blank=True, null=True)
    titol = models.CharField(unique=True, max_length=200)
    slug = models.CharField(max_length=200)
    tipus = models.CharField(max_length=2)
    uf = models.ForeignKey('UfsUf', models.DO_NOTHING)
    contingut = models.TextField()
    esborrat = models.BooleanField()
    autor = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True, related_name="autor_de")
    autor_txt = models.CharField(max_length=40)
    editat_per = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True, related_name="editor_de")
    data_creacio = models.DateTimeField()
    data_edicio = models.DateTimeField()
    total_util_per_c = models.IntegerField()
    total_favorit_per_c = models.IntegerField()
    data_tancat = models.DateTimeField(blank=True, null=True)
    data_esborrat = models.DateTimeField(blank=True, null=True)
    resultats_aprenentatge_txt = models.CharField(max_length=100)
    continguts_txt = models.CharField(max_length=100)
    contingut_html = models.TextField()
    total_social_per_c = models.IntegerField()
    pinned = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'material_material'


class MaterialMaterialContinguts(models.Model):
    material = models.ForeignKey(MaterialMaterial, models.DO_NOTHING)
    contingut = models.ForeignKey('UfsContingut', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_material_continguts'
        unique_together = (('material', 'contingut'),)


class MaterialMaterialResultatsAprenentatge(models.Model):
    material = models.ForeignKey(MaterialMaterial, models.DO_NOTHING)
    resultataprenentatge = models.ForeignKey(
        'UfsResultataprenentatge', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_material_resultats_aprenentatge'
        unique_together = (('material', 'resultataprenentatge'),)


class MaterialMaterialversio(models.Model):
    original = models.ForeignKey(
        MaterialMaterial, models.DO_NOTHING, blank=True, null=True)
    titol = models.CharField(max_length=100)
    tipus = models.CharField(max_length=2)
    uf = models.ForeignKey('UfsUf', models.DO_NOTHING)
    contingut = models.TextField()
    contingut_diff = models.TextField()
    editat_per = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True)
    data_edicio = models.DateTimeField()
    resultats_aprenentatge_txt = models.CharField(max_length=100)
    continguts_txt = models.CharField(max_length=100)
    contingut_html = models.TextField()

    class Meta:
        managed = False
        db_table = 'material_materialversio'


class NotificacionsNotificacio(models.Model):
    perfil = models.ForeignKey('UsuarisPerfil', models.DO_NOTHING)
    assumpte = models.CharField(max_length=120)
    cos = models.TextField()
    enllac = models.CharField(max_length=200)
    tractament = models.SmallIntegerField()
    data = models.DateTimeField()
    data_lectura = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacions_notificacio'


class RegistrationRegistrationprofile(models.Model):
    activation_key = models.CharField(max_length=40)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthUsersocialauth(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class UfsCicle(models.Model):
    codi = models.CharField(unique=True, max_length=50)
    familia = models.ForeignKey('UfsFamilia', models.DO_NOTHING)
    nom = models.TextField()
    etiqueta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ufs_cicle'


class UfsContingut(models.Model):
    codi = models.CharField(max_length=50)
    uf = models.ForeignKey('UfsUf', models.DO_NOTHING)
    nom = models.TextField()

    class Meta:
        managed = False
        db_table = 'ufs_contingut'
        unique_together = (('uf', 'codi'),)


class UfsFamilia(models.Model):
    nom = models.CharField(unique=True, max_length=50)
    slug = models.CharField(unique=True, max_length=50)
    imatge = models.CharField(max_length=100, blank=True, null=True)
    etiqueta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ufs_familia'


class UfsMp(models.Model):
    numero = models.CharField(max_length=50)
    cicle = models.ForeignKey(UfsCicle, models.DO_NOTHING)
    codi = models.CharField(unique=True, max_length=50)
    nom = models.TextField()
    slug = models.CharField(unique=True, max_length=50)
    etiqueta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ufs_mp'


class UfsResultataprenentatge(models.Model):
    codi = models.CharField(max_length=50)
    uf = models.ForeignKey('UfsUf', models.DO_NOTHING)
    nom = models.TextField()

    class Meta:
        managed = False
        db_table = 'ufs_resultataprenentatge'
        unique_together = (('uf', 'codi'),)


class UfsUf(models.Model):
    numero = models.CharField(max_length=50)
    mp = models.ForeignKey(UfsMp, models.DO_NOTHING)
    codi = models.CharField(unique=True, max_length=50)
    nom = models.TextField()
    slug = models.CharField(unique=True, max_length=50)
    data_modificacio = models.DateTimeField()
    etiqueta = models.CharField(max_length=50)
    equivalents = models.ManyToManyField(
        'UfsUF', related_name="ufs_em_consideren_equivalent")

    class Meta:
        managed = False
        db_table = 'ufs_uf'


class UfsUfEquivalents(models.Model):
    from_uf = models.ForeignKey(
        UfsUf, models.DO_NOTHING, related_name="equivalent_from")
    to_uf = models.ForeignKey(UfsUf, models.DO_NOTHING,
                              related_name="equivalent_to")

    class Meta:
        managed = False
        db_table = 'ufs_uf_equivalents'
        unique_together = (('from_uf', 'to_uf'),)


class UfsUfequivalent(models.Model):
    una_uf = models.ForeignKey(
        UfsUf, models.DO_NOTHING, related_name='UFEquivalentOrigen')
    uf_equivalent = models.ForeignKey(
        UfsUf, models.DO_NOTHING, related_name='UFEquivalentDesti')

    class Meta:
        managed = False
        db_table = 'ufs_ufequivalent'


class UfsocialFavoritordre(models.Model):
    perfil = models.ForeignKey('UsuarisPerfil', models.DO_NOTHING)
    material = models.ForeignKey(MaterialMaterial, models.DO_NOTHING)
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ufsocial_favoritordre'
        unique_together = (('material', 'perfil'),)


class UfsocialMedalla(models.Model):
    data = models.DateTimeField()
    tipus = models.IntegerField()
    perfil = models.ForeignKey('UsuarisPerfil', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ufsocial_medalla'


class UfsocialMedallaeditor(models.Model):
    medalla_ptr = models.OneToOneField(
        UfsocialMedalla, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ufsocial_medallaeditor'


class UfsocialMedallafamiliamaster(models.Model):
    medalla_ptr = models.OneToOneField(
        UfsocialMedalla, models.DO_NOTHING, primary_key=True)
    familia = models.ForeignKey(UfsFamilia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ufsocial_medallafamiliamaster'


class UfsocialReputacio(models.Model):
    perfil_propietari = models.ForeignKey('UsuarisPerfil', models.DO_NOTHING)
    moment = models.DateTimeField()
    moment_lectura = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ufsocial_reputacio'


class UfsocialReputaciopertancar(models.Model):
    reputacio_ptr = models.OneToOneField(
        UfsocialReputacio, models.DO_NOTHING, primary_key=True)
    material_titol = models.CharField(max_length=200)
    punts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ufsocial_reputaciopertancar'


class UfsocialReputacioperutil(models.Model):
    reputacio_ptr = models.OneToOneField(
        UfsocialReputacio, models.DO_NOTHING, primary_key=True)
    perfil_otorga = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True)
    material = models.ForeignKey(
        MaterialMaterial, models.DO_NOTHING, blank=True, null=True)
    material_titol = models.CharField(max_length=200)
    punts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ufsocial_reputacioperutil'


class UfsocialReputacioperutilperduda(models.Model):
    reputacio_ptr = models.OneToOneField(
        UfsocialReputacio, models.DO_NOTHING, primary_key=True)
    perfil_otorga = models.ForeignKey(
        'UsuarisPerfil', models.DO_NOTHING, blank=True, null=True)
    material = models.ForeignKey(
        MaterialMaterial, models.DO_NOTHING, blank=True, null=True)
    material_titol = models.CharField(max_length=200)
    punts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ufsocial_reputacioperutilperduda'


class UfsocialReputaciosocial(models.Model):
    reputacio_ptr = models.OneToOneField(
        UfsocialReputacio, models.DO_NOTHING, primary_key=True)
    material = models.ForeignKey(
        MaterialMaterial, models.DO_NOTHING, blank=True, null=True)
    material_titol = models.CharField(max_length=200)
    likes_acumulats = models.IntegerField()
    diferencial_likes_c = models.IntegerField()
    punts = models.IntegerField()
    xarxa = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ufsocial_reputaciosocial'


class UfsocialVottancar(models.Model):
    perfil = models.ForeignKey('UsuarisPerfil', models.DO_NOTHING)
    material = models.ForeignKey(MaterialMaterial, models.DO_NOTHING)
    motiu = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ufsocial_vottancar'
        unique_together = (('material', 'perfil'),)


class UsuarisMotiubaixa(models.Model):
    usuari = models.OneToOneField(AuthUser, models.DO_NOTHING)
    motiu = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuaris_motiubaixa'


class UsuarisPerfil(models.Model):
    centre = models.CharField(max_length=120)
    localitat = models.CharField(max_length=120)
    mostrar_centre_i_localitat = models.CharField(max_length=1)
    telefon = models.CharField(max_length=120)
    soc_de_sucre = models.BooleanField()
    nom_usuari = models.CharField(max_length=40)
    usuari = models.OneToOneField(AuthUser, models.DO_NOTHING)
    mostrar_correu = models.CharField(max_length=1)
    darrera_uf_consultada = models.ForeignKey(
        UfsUf, models.DO_NOTHING, blank=True, null=True)
    rebre_butlleti = models.BooleanField()
    coneixe_m = models.TextField()
    reputacio_c = models.IntegerField()
    favorit_c = models.IntegerField()
    coneixe_m_html = models.TextField()

    class Meta:
        managed = False
        db_table = 'usuaris_perfil'

    @property
    def display_centre_to(self, usuari=None):
        if (self.mostrar_centre_i_localitat == self.TOTHOM or
            (bool(usuari) and self.mostrar_centre_i_localitat == self.USUARIS_REGISTRATS) or
                (bool(usuari) and usuari == self)
            ):
            localitat = u"( {localitat} )".format(
                localitat=self.localitat) if self.localitat else u""
            return u"{centre} {localitat}".format(centre=self.centre, localitat=localitat)
        else:
            return u""

    @property
    def display_correu_to(self, usuari=None):
        if (self.mostrar_correu == self.TOTHOM or
            (bool(usuari) and self.mostrar_correu == self.USUARIS_REGISTRATS) or
                (bool(usuari) and usuari == self)
            ):
            return u"{correu}".format(correu=self.usuari.email)
        else:
            return u""


class UsuarisPerfilLesMevesUfs(models.Model):
    perfil = models.ForeignKey(UsuarisPerfil, models.DO_NOTHING)
    uf = models.ForeignKey(UfsUf, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuaris_perfil_les_meves_ufs'
        unique_together = (('perfil', 'uf'),)
