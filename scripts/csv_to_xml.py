import pandas as pd
import xml.etree.ElementTree as ET
import os


def csv_to_xml(csv_file, xml_file):
    # Verificar se o arquivo CSV existe
    if not os.path.exists(csv_file):
        print(f"Erro: Arquivo CSV '{csv_file}' não encontrado.")
        return

    # Ler o CSV usando pandas
    df = pd.read_csv(csv_file)

    # Criar o elemento raiz do XML
    root = ET.Element("Items")

    # Iterar pelas linhas do DataFrame e criar elementos XML
    for _, row in df.iterrows():
        item = ET.SubElement(root, "Item")
        for col_name, value in row.items():
            col_element = ET.SubElement(item, col_name)
            col_element.text = str(value)

    # Converter a árvore XML para string
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"XML gerado com sucesso em '{xml_file}'.")


# Obter caminhos absolutos
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(base_dir, "../dataset/input.csv")
xml_file = os.path.join(base_dir, "../xml_output/output.xml")

# Chamar a função
csv_to_xml(csv_file, xml_file)
