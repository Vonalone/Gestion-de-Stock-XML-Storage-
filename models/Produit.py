class Produit:
    def __init__(self, idP, nom, quantite, prix, categorie, description, idF):
        self.idP = idP
        self.nom = nom
        self.quantite = quantite
        self.prix = prix
        self.categorie = categorie
        self.description = description
        self.idF =idF

    @property
    def idP(self):
        return self._idP

    @idP.setter
    def idP(self, idP):
        self._idP = idP

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom


    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, qte):
            self._quantite = qte


    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, prix):
            self._prix = prix



    @property
    def categorie(self):
        return self._categorie

    @categorie.setter
    def categorie(self, categori):
        self._categorie = categori

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def idF(self):
        return self._idF

    @idF.setter
    def idF(self, idF):
        self._idF = idF


    def __str__(self):
        return f"{self.idP}, {self.nom}, {self.quantite}, {self.prix}, {self.categorie}, {self.description}, {self.idF}"
