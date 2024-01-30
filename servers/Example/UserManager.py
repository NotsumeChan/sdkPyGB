import json

def LoadBans() -> dict:
    """
    carga los bans desde bans.json\n
    se espera cambiar a una base de datos
    """
    with open("bans.json", "r") as f:
        return json.load(f)

def SaveBans(bans : dict):
    """
    guarda los bans en bans.json\n
    se espera cambiar a una base de datos
    """
    with open("bans.json", "w") as f:
        json.dump(bans, f)

def Ban(user : str, bans : dict):
    """
    Agrega un usuario a la lista dinamica de bans\n
    se espera cambiar a una consulta de la base de datos
    """
    bans["users"].append(user)
    return bans

def BanIp(ip : str, bans : dict):
    """
    Agrega una ip a la lista dinamica de bans\n
    se espera cambiar a una consulta de la base de datos
    """
    bans["ips"].append(ip)
    return bans

def UnBan(user : str, bans : dict):
    """
    Elimina un usuario de la lista dinamica de bans\n
    se espera cambiar a una consulta de la base de datos
    """
    bans["users"].remove(user)
    return bans

def UnBanIp(ip : str, bans : dict):
    """
    Elimina una ip de la lista dinamica de bans\n
    se espera cambiar a una consulta de la base de datos
    """
    bans["ips"].remove(ip)
    return bans
