from .models import MaterialMaterial
from .exportaUtils import (
    creaCarpeta,
    calculaCredits,
    calculaTitol,
    calculaEtiquetes,
    desa_md)
from .exportaMdUtils import fixaSintaxiGitHub


def run():
    for m in MaterialMaterial.objects.filter(esborrat=False):
        creaCarpeta(m)

        cooked_md = m.contingut

        # cooked_md, imatges = extreuImatges(cooked_md)
        # desa_imatges(m, imatges)
        # cooked_md = substitueixPathsAntics(cooked_md)
        cooked_md = fixaSintaxiGitHub(cooked_md)

        titol_md = calculaTitol(m)
        credits_md = calculaCredits(m)
        etiquestes_md = calculaEtiquetes(m)

        desa_md(m, titol_md + cooked_md + credits_md + etiquestes_md)
