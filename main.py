from scripts import crud_operations
import xml.etree.ElementTree as ET
import os


database_file = "data/stock_data.xml"


def create_database():
    if not os.path.exists(database_file):
        root = ET.Element("stock")
        tree = ET.ElementTree(root)
        tree.write(database_file)

def load_database():
    tree = ET.parse(database_file)
    return tree, tree.getroot()

def save_database(tree):
   
    xml_data = ET.tostring(tree.getroot(), encoding="unicode")
    
    
    header = (
        '<?xml version="1.0"?>\n'
        '<!DOCTYPE stock SYSTEM "data/stock_structure.dtd">\n'
        '<?xml-stylesheet type="text/xsl" href="data/stock_presentation.xsl"?>\n'
    )
    xml_data = header + xml_data

    
    import xml.dom.minidom
    dom = xml.dom.minidom.parseString(xml_data)
    pretty_xml = dom.toprettyxml(indent="  ")

   
    with open(database_file, "w", encoding="utf-8") as file:
        file.write(pretty_xml)

def main():
    crud = crud_operations("data/stock_data.xml")
    
    print("Bienvenue dans le gestionnaire de stock!")
    print("1. Ajouter un client")
    print("2. Lire les clients")
    print("3. Mettre à jour un client")
    print("4. Supprimer un client")
    choice = input("Choisissez une option : ")
    
    if choice == "1":
        attributes = {
            "id": "2",
            "nom": "Marie Curie",
            "adresse": "456 Rue de Science",
            "email": "marie.curie@example.com",
            "telephone": "0987654321",
        }
        crud.create("client", attributes)
        print("Client ajouté!")
    elif choice == "2":
        clients = crud.read("client")
        for client in clients:
            print(client.attrib)
    elif choice == "3":
        crud.update("client", "1", {"nom": "Jean Dupont Updated"})
        print("Client mis à jour!")
    elif choice == "4":
        crud.delete("client", "1")
        print("Client supprimé!")

if __name__ == "__main__":
    main()
