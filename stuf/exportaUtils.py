from django.conf import settings
import os
from .models import UfsUfEquivalents


def creaCarpeta(m):

    # carpeta arrel ---
    tot_el_cami = settings.EXPORT_DIR
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)

    # resta de carpetes ---
    creaCarpetaCicle(m.uf.mp.cicle)
    creaCarpetaMP(m.uf.mp)
    creaCarpetaUF(m.uf)
    creaCarpetaMaterial(m)


def extreuImatges(cooked_md):
    # return cooked_md, imatges
    pass


def desa_imatges(m, imatges):
    pass


def desa_md(m, cooked_md):
    cami = CarpetaReadmeMaterial(m)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    with open(tot_el_cami, "w") as text_file:
        print(cooked_md, file=text_file)


# Cicle ----------------------------------


def carpetaCicle(cicle):
    return [cicle.codi]


def creaCarpetaCicle(cicle):
    cami = carpetaCicle(cicle)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)
        creaReadMeDeCicle(tot_el_cami, cicle)


def creaReadMeDeCicle(tot_el_cami, cicle):
    pass


# MP ---------------------------

def carpetaMP(mp):
    return carpetaCicle(mp.cicle) + [mp.codi]


def creaCarpetaMP(mp):
    cami = carpetaMP(mp)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)
        creaReadMeDeMP(tot_el_cami, mp)


def creaReadMeDeMP(tot_el_cami, mp):
    pass

# UF ---------------------------


def carpetaUF(uf):
    return carpetaMP(uf.mp) + [uf.codi]


def creaCarpetaUF(uf):
    cami = carpetaUF(uf)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)
        creaReadMeDeUF(tot_el_cami, uf)


def creaReadMeDeUF(tot_el_cami, uf):
    pass

# Material ---------------------------


def carpetaMaterial(material):
    return carpetaUF(material.uf) + [material.slug]


def CarpetaReadmeMaterial(material):
    return carpetaMaterial(material) + ["readme.md"]


def creaCarpetaMaterial(material):
    cami = carpetaMaterial(material)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)
        creaReadMeDeMaterial(tot_el_cami, material)


def creaReadMeDeMaterial(tot_el_cami, material):
    pass

# Credits ------


def calculaCredits(material):
    md_splited = ["", "---", ""]

    # Autor
    perfil = material.autor.nom_usuari  # display_centre_to()
    moment = material.data_creacio.strftime("%Y.%m.%d %H:%M:%S")
    md_splited.append(f"#### Autor: {perfil} {moment}")

    # Darrera edicio
    if bool(material.editat_per):
        perfil = material.editat_per.nom_usuari  # display_centre_to()
        moment = material.data_edicio.strftime("%Y.%m.%d %H:%M:%S")
        md_splited.append(f"#### Editat per: {perfil} {moment}")

    # Llicència
    md_splited.append(
        "###### [CC BY](https://creativecommons.org/licenses/by/4.0/) ![CC BY](https://licensebuttons.net/l/by/3.0/80x15.png)")

    return "\r\n".join(md_splited)

# Titol -----


def calculaTitol(material):
    md_splited = []
    titol = f"# {material.titol}"
    md_splited.append(titol)
    md_splited.append("")

    return "\r\n".join(md_splited)

# Etiquetes -----


def get_etiquetes(uf):
    equivalents = list(
        [x.to_uf for x in UfsUfEquivalents.objects.filter(from_uf=uf)]) + [uf]
    ufs = " ".join(set([x.etiqueta for x in equivalents]))
    mps = " ".join(set([x.mp.etiqueta for x in equivalents]))
    cicles = " ".join(set([x.mp.cicle.etiqueta for x in equivalents]))
    families = " ".join(
        set([x.mp.cicle.familia.etiqueta for x in equivalents]))
    return "{} {} {} {}".format(families, cicles, mps, ufs)


def calculaEtiquetes(material):
    etiquetes = get_etiquetes(material.uf)
    md_splited = []
    md_splited.append("")
    md_splited.append("---")
    md_splited.append("")
    md_splited.append(etiquetes)
    md_splited.append("")

    return "\r\n".join(md_splited)
