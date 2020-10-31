from .models import MaterialMaterial
from .exportaUtils import creaCarpeta, extreuImatges, desa_imatges, desa_md


def run():
    for m in MaterialMaterial.objects.all():
        creaCarpeta(m)
        # nou_md, imatges = extreuImatges(m)
        # desa_imatges(m, imatges)
        # desa_md(m, nou_md)
