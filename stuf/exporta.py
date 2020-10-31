from .models import MaterialMaterial
from .exportaUtils import creaCarpeta, creaCarpetaMaterial
from .exportaHelpers import ufsEquivalentsA


def run():

    #
    tot_el_material = list(MaterialMaterial.objects.filter(esborrat=False))
    totes_les_ufs = {e for m in tot_el_material for e in ufsEquivalentsA(m.uf)}

    #
    for uf in totes_les_ufs:
        creaCarpeta(uf)

    #
    for m in tot_el_material:
        creaCarpetaMaterial(m)
        
