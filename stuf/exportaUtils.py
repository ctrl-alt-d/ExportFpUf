from django.conf import settings
import os
from .exportaMdUtils import fixaSintaxiGitHub
from .exportaMaterialUtils import (
    calculaCredits, calculaEtiquetes, calculaTitol)


def creaCarpeta(uf):

    creaCarpetaArrel()
    creaCarpetaCicle(uf.mp.cicle)
    creaCarpetaMP(uf.mp)
    creaCarpetaUF(uf)


def creaCarpetaArrel():
    tot_el_cami = settings.EXPORT_DIR
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)


def extreuImatges(cooked_md):
    # return cooked_md, imatges
    pass


def desa_imatges(m, imatges):
    pass


def desa_md(md, tot_el_cami):
    with open(tot_el_cami, "w") as text_file:
        print(md, file=text_file)


# Cicle ----------------------------------


def carpetaCicle(cicle):
    return [cicle.codi]


def carpetaReadmeCicle(cicle):
    return carpetaCicle(cicle) + ["readme.md"]


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


def CarpetaReadmeMP(mp):
    return carpetaMP(mp) + ["readme.md"]


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


def carpetaReadmeUF(uf):
    return carpetaUF(uf) + ["readme.md"]


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
    exportaMaterial(material)


def creaReadMeDeMaterial(tot_el_cami, material):
    pass


def exportaMaterial(m):
    cooked_md = m.contingut

    # cooked_md, imatges = extreuImatges(cooked_md)
    # desa_imatges(m, imatges)
    # cooked_md = substitueixPathsAntics(cooked_md)
    cooked_md = fixaSintaxiGitHub(cooked_md)

    titol_md = calculaTitol(m)
    credits_md = calculaCredits(m)
    etiquestes_md = calculaEtiquetes(m)

    md = titol_md + cooked_md + credits_md + etiquestes_md

    cami = CarpetaReadmeMaterial(m)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)

    desa_md(md, tot_el_cami)
