from django.conf import settings
import os
from .exportaMdUtils import fixaSintaxiGitHub
from .exportaMaterialUtils import (
    calculaCredits, calculaEtiquetes, calculaTitol)
from .exportaHelpers import desa_md, ufsEquivalentsA


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
    creaReadMeDeCicle(cicle)


def creaReadMeDeCicle(cicle):
    md_splited = []
    md_splited.append(f"# {cicle.codi}")
    md_splited.append(f"## {cicle.nom}")
    md_splited.append(f"### {cicle.familia.nom}")
    md_splited.append("")
    md_splited.append("Exercicis i material de cicles formatius"
                      f" {cicle.familia.nom}")
    md_splited.append("")
    md_splited.append(f"###### {cicle.familia.etiqueta} {cicle.etiqueta}")

    md = "\r\n".join(md_splited)
    cami = carpetaReadmeCicle(cicle)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    desa_md(md, tot_el_cami)


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
    creaReadMeDeMP(mp)


def creaReadMeDeMP(mp):
    md_splited = []
    md_splited.append(f"# {mp.cicle.codi} - {mp.nom}")
    md_splited.append(f"## {mp.cicle.nom}")
    md_splited.append(f"### {mp.cicle.familia.nom}")
    md_splited.append("")
    md_splited.append("Exercicis i material de cicles formatius"
                      f" {mp.cicle.familia.nom}")
    md_splited.append("")
    md_splited.append(f"Exercicis de {mp.nom}")
    md_splited.append("")
    md_splited.append(f"###### {mp.cicle.familia.etiqueta}"
                      f" {mp.cicle.etiqueta}"
                      f" {mp.etiqueta}")

    md = "\r\n".join(md_splited)
    cami = CarpetaReadmeMP(mp)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    desa_md(md, tot_el_cami)

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
    creaReadMeDeUF(uf)


def creaReadMeDeUF(uf):
    etiquetes = [
        uf_equivalent.etiqueta
        for uf_equivalent
        in ufsEquivalentsA(uf)]
    etiquetes_txt = " ".join(etiquetes)

    md_splited = []
    md_splited.append(f"# {uf.mp.cicle.codi} - {uf.mp.nom}")
    md_splited.append(f"# {uf.nom}")
    md_splited.append(f"## {uf.mp.cicle.nom}")
    md_splited.append(f"### {uf.mp.cicle.familia.nom}")
    md_splited.append("")
    md_splited.append("Exercicis i material de cicles formatius"
                      f" {uf.mp.cicle.familia.nom}")
    md_splited.append("")
    md_splited.append(f"Exercicis de {uf.nom}")
    md_splited.append("")
    md_splited.append(f"###### {uf.mp.cicle.familia.etiqueta}"
                      f" {uf.mp.cicle.etiqueta} {etiquetes_txt}")

    pinned = list(uf.materialmaterial_set.filter(pinned=True))
    if (pinned):
        md_splited.append("")
        md_splited.append("Material indexat")
        for m in pinned:
            carpeta = CarpetaReadmeMaterial(m)
            cami = "/".join(carpeta)
            md_splited.append(f"* [{m.titol}](/{cami})")

    md = "\r\n".join(md_splited)
    cami = carpetaReadmeUF(uf)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    desa_md(md, tot_el_cami)


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
