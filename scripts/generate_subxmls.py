from lxml import etree
import os


def generate_subxmls(xml_file, output_dir):
    # Verificar se o arquivo XML existe
    if not os.path.exists(xml_file):
        print(f"Erro: Arquivo XML '{xml_file}' não encontrado.")
        return

    # Criar o diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Parsear o XML base
        tree = etree.parse(xml_file)
        root = tree.getroot()

        # Obter todas as categorias únicas no XML
        categories = set(root.xpath("//category/text()"))
        print(f"Categorias encontradas: {categories}")

        # Gerar um sub-XML para cada categoria
        for category in categories:
            # Filtrar elementos com base na categoria
            filtered_items = root.xpath(f"//Item[category='{category}']")

            # Criar a estrutura XML para o sub-XML
            sub_root = etree.Element("Items")
            for item in filtered_items:
                sub_root.append(item)

            # Criar a árvore XML
            sub_tree = etree.ElementTree(sub_root)

            # Salvar o sub-XML em um arquivo
            output_file = os.path.join(output_dir, f"{category.replace(' ', '_')}_items.xml")
            sub_tree.write(output_file, encoding="utf-8", xml_declaration=True, pretty_print=True)
            print(f"Sub-XML gerado: {output_file}")

    except Exception as e:
        print(f"Erro ao gerar sub-XMLs: {e}")


# Definir os caminhos dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))
xml_file =  os.path.join(base_dir, "../xml_output/output.xml")
output_dir = os.path.join(base_dir, "../xml_output/sub_xmls")

# Chamar a função
generate_subxmls(xml_file, output_dir)
