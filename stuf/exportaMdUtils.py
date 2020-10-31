def fixaSintaxiGitHub(md):
    """
    Converteix la sintaxi md actual a la de github
    """
    md = fixaBlocs(md)
    md = fixaLiniesComencenPerCometes(md)
    return md


def fixaBlocs(md):
    """
    Converteix els blocs que comencen per ::: amb blocs que comencen per ```
    """
    new_md = []
    md = md.replace("\r\n", "\n")
    md_splitted = md.split("\n")
    target_pattern = "    :::"
    keep_block_pattern = "    "
    in_block = False
    for line in md_splitted:
        previous_in_block = in_block
        in_block = in_block or line.startswith(target_pattern)
        in_block = in_block and line.startswith(keep_block_pattern)

        #
        starting_block = in_block and not previous_in_block
        if starting_block:
            cooked_line = line[len(target_pattern):]
            new_md.append(f"```{cooked_line}")

        #
        keeping_in_block = in_block and previous_in_block
        if keeping_in_block:
            cooked_line = line[len(keep_block_pattern):]
            new_md.append(cooked_line)

        #
        exiting_block = previous_in_block and not in_block
        if exiting_block:
            new_md.append("```")

        #
        if not in_block:
            new_md.append(line)
    
    if in_block:
        new_md.append("```")

    return "\r\n".join(new_md) + "\r\n"


def fixaLiniesComencenPerCometes(md):
    """
    Si una línia comença per ` i no té un cr davant, li posa una línia nova a davant.
    Ull! Només afecta un cas.
    """
    new_md = []
    md = md.replace("\r\n", "\n")
    md_splitted = md.split("\n")

    is_apos = False
    is_cr = True
    for line in md_splitted:
        previous_is_apos = is_apos
        previous_is_cr = is_cr
        is_apos = line.startswith("`") and not line[1:].startswith("`")
        is_cr = line.replace(" ", "") == ""

        #
        if is_apos and not previous_is_cr:
            new_md.append("\n")

        #
        new_md.append(line)

        #
        if previous_is_apos and not is_cr:
            new_md.append("\n")

    return "\r\n".join(new_md)
