from .models import MaterialMaterial
from .exportaUtils import (
    creaCarpeta,
    extreuImatges,
    desa_imatges,
    desa_md)
from .exportaMdUtils import fixaSintaxiGitHub


def run():
    for m in MaterialMaterial.objects.all():
        creaCarpeta(m)

        cooked_md = m.contingut

        # cooked_md, imatges = extreuImatges(cooked_md)
        # desa_imatges(m, imatges)
        # cooked_md = substitueixPathsAntics(cooked_md)
        cooked_md = fixaSintaxiGitHub(cooked_md)

        desa_md(m, cooked_md)
