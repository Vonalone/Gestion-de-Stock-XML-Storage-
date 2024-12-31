class Fournisseur:
    def __init__(self, idF, nom, contact, adresse):
        self.idF = idF
        self.nom = nom
        self.contact = contact
        self.adresse = adresse

    @property
    def idF(self):
        return self._idF

    @idF.setter
    def idF(self, idF):
            self._idF = idF

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
            self._nom = nom

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact):
            self._contact = contact


    @property
    def adresse(self):
        return self._adresse

    @adresse.setter
    def adresse(self, adresse):
            self._adresse = adresse


    @property
    def produits_fournis(self):
        return self._produits_fournis




    def __str__(self):
        return f"{self.idF}, {self.nom}, {self.contact}, {self.adresse}"





