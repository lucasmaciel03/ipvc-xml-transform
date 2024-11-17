from lxml import etree
import os


def validate_xml(xml_file, xsd_file):
    # Verificar se os arquivos existem
    if not os.path.exists(xml_file):
        print(f"Erro: Arquivo XML '{xml_file}' não encontrado.")
        return False
    if not os.path.exists(xsd_file):
        print(f"Erro: Arquivo XSD '{xsd_file}' não encontrado.")
        return False

    # Carregar o XML e o XSD
    try:
        with open(xsd_file, 'r') as schema_file:
            schema_root = etree.XML(schema_file.read().encode())  # Converte o conteúdo para bytes
        schema = etree.XMLSchema(schema_root)
        with open(xml_file, 'rb') as xml_file_data:  # Leia o XML como bytes
            xml_tree = etree.parse(xml_file_data)

        # Validar o XML
        if schema.validate(xml_tree):
            print(f"O arquivo XML '{xml_file}' é válido.")
            return True
        else:
            print(f"O arquivo XML '{xml_file}' é inválido. Erros:")
            for error in schema.error_log:
                print(error.message)
            return False

    except Exception as e:
        print(f"Erro ao validar XML: {e}")
        return False

# Definir os caminhos dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))
xml_file = os.path.join(base_dir, "../xml_output/output.xml")
xsd_file = os.path.join(base_dir, "../schemas/validation.xsd")

# Chamar a função
validate_xml(xml_file, xsd_file)
