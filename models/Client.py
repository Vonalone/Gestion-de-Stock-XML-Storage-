class Client:
    def __init__(self, idCl, nom, adresse, email, telephone):
        self.idCl = idCl
        self.nom = nom
        self.adresse = adresse
        self.email = email
        self.telephone = telephone


        @property
        def idCl(self):
            return self._idCl

        @idCl.setter
        def idCl(self, idCl):
                self._idCl = idCl


        @property
        def nom(self):
            return self._nom

        @nom.setter
        def nom(self, nom):
                self._nom = nom


        @property
        def adresse(self):
            return self._adresse

        @adresse.setter
        def adresse(self, adresse):
                self._adresse = adresse

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, email):
            if "@" in email.value and "." in email:
                self._email = email
            else:
                raise ValueError("Email invalide.")

        @property
        def telephone(self):
            return self._telephone

        @telephone.setter
        def telephone(self, telephone):
                self._telephone = telephone

    def __str__(self):
        return f"{self.idCl}, {self.nom}, {self.email}, {self.telephone}"
