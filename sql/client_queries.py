GET_ALL_CLIENTS = """
SELECT
    ClientId,
    NomSociete,
    ContactNom,
    ContactTitre,
    Adresse,
    Ville,
    Region,
    CodePostal,
    Pays,
    Telephone,
    Fax
FROM client
ORDER BY ClientId
"""
GET_CLIENT_BY_ID = """
SELECT
    ClientId,
    NomSociete,
    ContactNom,
    ContactTitre,
    Adresse,
    Ville,
    Region,
    CodePostal,
    Pays,
    Telephone,
    Fax
from client
where ClientId = ?
"""

ADD_CLIENT = """
insert into client (
    ClientId,
    NomSociete,
    ContactNom,
    ContactTitre,
    Adresse,
    Ville,
    Region,
    CodePostal,
    Pays,
    Telephone,
    Fax
)
values(?,?,?,?,?,?,?,?,?,?,?)
"""

UPDATE_CLIENT = """
update client 
set
    NomSociete=?,
    ContactNom=?,
    ContactTitre=?,
    Adresse=?,
    Ville=?,
    Region=?,
    CodePostal=?,
    Pays=?,
    Telephone=?,
    Fax=?
where ClientId= ?
"""

DELETE_CLIENT = """
delete from client
where ClientId=?
"""
