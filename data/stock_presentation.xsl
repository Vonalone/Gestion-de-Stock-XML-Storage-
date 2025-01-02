<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html>
            <head>
                <title>Gestion du Stock</title>
                <link rel="stylesheet" type="text/css" href="style.css"/>
            </head>
            <body>
                <h1>Clients</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Nom</th>
                        <th>Adresse</th>
                        <th>Email</th>
                        <th>Téléphone</th>
                    </tr>
                    <xsl:for-each select="stock/clients/client">
                        <tr>
                            <td><xsl:value-of select="idCl"/></td>
                            <td><xsl:value-of select="nom"/></td>
                            <td><xsl:value-of select="adresse"/></td>
                            <td><xsl:value-of select="email"/></td>
                            <td><xsl:value-of select="telephone"/></td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h1>Produits</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Nom</th>
                        <th>Quantité</th>
                        <th>Prix</th>
                        <th>Catégorie</th>
                        <th>Description</th>
                    </tr>
                    <xsl:for-each select="stock/produits/produit">
                        <tr>
                            <td><xsl:value-of select="idP"/></td>
                            <td><xsl:value-of select="nom"/></td>
                            <td><xsl:value-of select="quantite"/></td>
                            <td><xsl:value-of select="prix"/></td>
                            <td><xsl:value-of select="categorie"/></td>
                            <td><xsl:value-of select="description"/></td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h1>Commandes</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Client ID</th>
                        <th>Produit ID</th>
                        <th>Quantité</th>
                        <th>Statut</th>
                        <th>Prix Total</th>
                        <th>Date Commande</th>
                        <th>Date Livraison</th>
                    </tr>
                    <xsl:for-each select="stock/commandes/commande">
                        <tr>
                            <td><xsl:value-of select="idCmd"/></td>
                            <td><xsl:value-of select="idCl"/></td>
                            <td><xsl:value-of select="idP"/></td>
                            <td><xsl:value-of select="quantite"/></td>
                            <td><xsl:value-of select="statut"/></td>
                            <td><xsl:value-of select="prix_total"/></td>
                            <td><xsl:value-of select="order_date"/></td>
                            <td><xsl:value-of select="arrival_date"/></td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h1>Fournisseurs</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Nom</th>
                        <th>Contact</th>
                        <th>Adresse</th>
                    </tr>
                    <xsl:for-each select="stock/fournisseurs/fournisseur">
                        <tr>
                            <td><xsl:value-of select="idF"/></td>
                            <td><xsl:value-of select="nom"/></td>
                            <td><xsl:value-of select="contact"/></td>
                            <td><xsl:value-of select="adresse"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
