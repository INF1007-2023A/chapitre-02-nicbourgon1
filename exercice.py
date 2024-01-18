def majuscule(mot):
    nouveau_mot = ''
    for x in mot:
        if 97 <= ord(x) <= 122:
            nouveau_mot += chr(ord(x) - 32)
        elif 65 <= ord(x) <= 90:
            nouveau_mot += chr(ord(x) + 32)
        else:
            nouveau_mot += x
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
