class Commande:
    def __init__(self, idCmd, idCl, idP, quantite, statut, prix_total, order_date, arrival_date):
        self.idCmd = idCmd
        self.idCl = idCl
        self.idP = idP
        self.quantite = quantite
        self.statut = statut
        self.prix_total = prix_total
        self.order_date = order_date
        self.arrival_date = arrival_date

        @property
        def idCmd(self):
            return self._idCmd

        @idCmd.setter
        def idCmd(self, idCmd):
            self._idCmd = idCmd

        @property
        def idCl(self):
            return self._idCl

        @idCl.setter
        def idCl(self, idCl):
            self._idCl = idCl

        @property
        def idP(self):
            return self._idP

        @idP.setter
        def idP(self, idP):
            self._idP = idP

        @property
        def quantite(self):
            return self._quantite

        @quantite.setter
        def quantite(self, qte):
                self._quantite = qte

        @property
        def statut(self):
            return self._statut

        @statut.setter
        def statut(self, statut):
            self._statut =statut

        #Getter et setter pour prix_total
        @property
        def prix_total(self):
            return self._prix_total

        @prix_total.setter
        def prix_total(self, prix_total):
            self._prix_total = prix_total

        @property
        def order_date(self):
            return self._order_date

        @order_date.setter
        def order_date(self, order_date):
            self._order_date = order_date

        @property
        def arrival_date(self):
            return self._arrival_date

        @arrival_date.setter
        def arrival_date(self, arrival_date):
            self._arrival_date = arrival_date

    def __str__(self):
        return f"{self.idCmd}, {self.idCl}, {self.idP}, {self.quantite}, {self.statut}, {self.prix_total}, {self.order_date}, {self.arrival_date}"



