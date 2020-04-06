def access(dictionnary, keys, default = None):
    if len(keys) == 0:
        return dictionnary
    key = keys[0]
    rem_keys = keys[1:]
    if key in dictionnary.keys():
        return access(dictionnary[key], rem_keys, default)
    return default
