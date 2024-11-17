from lxml import etree
import os


def query_xml(xml_file):
    # Verificar se o arquivo XML existe
    if not os.path.exists(xml_file):
        print(f"Erro: Arquivo XML '{xml_file}' não encontrado.")
        return

    try:
        # Parsear o XML
        tree = etree.parse(xml_file)

        # 1. Itens com preço maior que 10
        expensive_items = tree.xpath("//Item[price > 10]")
        print("Itens com preço maior que 10:")
        for item in expensive_items:
            print(etree.tostring(item, pretty_print=True).decode("utf-8"))

        # 2. Itens de uma categoria específica
        category = "Category 1"  # Modifique conforme necessário
        category_items = tree.xpath(f"//Item[category='{category}']")
        print(f"\nItens da categoria '{category}':")
        for item in category_items:
            print(etree.tostring(item, pretty_print=True).decode("utf-8"))

        # 3. Contar o número de itens no XML
        total_items = tree.xpath("count(//Item)")
        print(f"\nNúmero total de itens no XML: {int(total_items)}")

    except Exception as e:
        print(f"Erro ao consultar XML: {e}")


# Definir o caminho do arquivo XML
base_dir = os.path.dirname(os.path.abspath(__file__))
xml_file = os.path.join(base_dir, "../xml_output/sub_xmls/Category_1_items.xml")

# Chamar a função
query_xml(xml_file)
