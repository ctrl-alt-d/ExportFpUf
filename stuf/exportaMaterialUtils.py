from .exportaHelpers import ufsEquivalentsA

# Credits ------


def calculaCredits(material):
    md_splited = ["", "---", ""]

    # Autor
    perfil = material.autor.nom_usuari  # display_centre_to()
    moment = material.data_creacio.strftime("%Y.%m.%d %H:%M:%S")
    md_splited.append(f"###### Autor: {perfil} {moment}")

    # Darrera edicio
    if bool(material.editat_per):
        perfil = material.editat_per.nom_usuari  # display_centre_to()
        moment = material.data_edicio.strftime("%Y.%m.%d %H:%M:%S")
        md_splited.append(f"###### Editat per: {perfil} {moment}")

    # Llicència
    md_splited.append(
        "###### [CC BY](https://creativecommons.org/licenses/by/4.0/)"
        " ![CC BY](https://licensebuttons.net/l/by/3.0/80x15.png)")

    return "\r\n".join(md_splited)

# Titol -----


def calculaTitol(material):
    md_splited = []
    titol = f"# {material.titol}"
    md_splited.append(titol)
    md_splited.append("")

    return "\r\n".join(md_splited)


def calculaTipus(material):
    md_splited = []
    if material.tipus == "EX":
        subtitol = f"## {material.uf.codi} - Exercici de {material.uf.nom}"
    else:
        subtitol = f"## {material.uf.codi} - Conceptes de {material.uf.nom}"
    md_splited.append(subtitol)
    md_splited.append("")

    return "\r\n".join(md_splited)

# Etiquetes -----


def get_etiquetes(uf):
    equivalents = ufsEquivalentsA(uf)
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

    if material.resultats_aprenentatge_txt:
        md_splited.append("* Resultats d'aprenentatge"
                          f" {material.resultats_aprenentatge_txt}")
    if material.continguts_txt:
        md_splited.append(f"* Continguts {material.continguts_txt}")

    return "\r\n".join(md_splited)
