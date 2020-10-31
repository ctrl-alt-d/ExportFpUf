from .models import UfsUfEquivalents


def ufsEquivalentsA(uf):
    return (
        [x.to_uf for x in UfsUfEquivalents.objects.filter(from_uf=uf)]
        + [uf])
