import xml.etree.ElementTree as ET

class CRUDOperations:
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def create_client(self, idCl, nom, adresse, email, telephone):
        """
        Ajoute un nouveau client au fichier XML.
        """
        # Rechercher la section clients
        clients_section = self.root.find("clients")
        if clients_section is None:
            # Si la section clients n'existe pas, la créer
            clients_section = ET.SubElement(self.root, "clients")
        
        # Créer un nouvel élément client
        new_client = ET.SubElement(clients_section, "client")
        ET.SubElement(new_client, "idCl").text = str(idCl)
        ET.SubElement(new_client, "nom").text = nom
        ET.SubElement(new_client, "adresse").text = adresse
        ET.SubElement(new_client, "email").text = email
        ET.SubElement(new_client, "telephone").text = telephone

        # Sauvegarder dans le fichier XML
        self.tree.write(self.xml_file, encoding="utf-8", xml_declaration=True)

    def read(self, tag):
        """
        Retourne une liste des éléments correspondant au tag spécifié.
        """
        return self.root.findall(tag)

    def update_client(self, idCl, new_data):
        """
        Met à jour les informations d'un client existant.
        """
        for client in self.root.findall(".//client"):
            if client.find("idCl").text == str(idCl):
                for key, value in new_data.items():
                    elem = client.find(key)
                    if elem is not None:
                        elem.text = value
                self.tree.write(self.xml_file, encoding="utf-8", xml_declaration=True)
                return True
        return False

    def delete_client(self, idCl):
        """
        Supprime un client existant.
        """
        clients_section = self.root.find("clients")
        if clients_section is not None:
            for client in clients_section.findall("client"):
                if client.find("idCl").text == str(idCl):
                    clients_section.remove(client)
                    self.tree.write(self.xml_file, encoding="utf-8", xml_declaration=True)
                    return True
        return False
