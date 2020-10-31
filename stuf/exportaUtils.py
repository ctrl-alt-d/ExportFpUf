from django.conf import settings
import os


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


def extreuImatges(m):
    # return nou_md, imatges
    pass


def desa_imatges(m, imatges):
    pass


def desa_md(m, nou_md):
    pass

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


def creaCarpetaMaterial(material):
    cami = carpetaMaterial(material)
    tot_el_cami = os.path.join(settings.EXPORT_DIR, *cami)
    if not os.path.exists(tot_el_cami):
        print(f"creant {tot_el_cami}")
        os.mkdir(tot_el_cami)
        creaReadMeDeMaterial(tot_el_cami, material)


def creaReadMeDeMaterial(tot_el_cami, material):
    pass
