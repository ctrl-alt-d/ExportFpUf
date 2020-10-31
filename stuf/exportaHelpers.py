from .models import UfsUfEquivalents


def ufsEquivalentsA(uf):
    return (
        [x.to_uf for x in UfsUfEquivalents.objects.filter(from_uf=uf)]
        + [uf])


def desa_md(md, tot_el_cami):
    with open(tot_el_cami, "w") as text_file:
        print(md, file=text_file)