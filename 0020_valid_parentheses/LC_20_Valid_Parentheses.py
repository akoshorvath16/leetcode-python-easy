def is_valid(s):
    verem = []
    pars = {"]": "[", ")": "(", "}": "{"}

    for character in s:
        if character in pars:
            if verem == []:
                return False
            elif verem.pop() != pars[character]:
                return False
        else:
            verem.append(character)

    if verem == []:
        return True
    else:
        return False