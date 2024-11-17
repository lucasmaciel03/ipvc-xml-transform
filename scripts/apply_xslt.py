from lxml import etree
import os


def apply_xslt(xml_file, xslt_file, output_file):
    # Verificar se os arquivos existem
    if not os.path.exists(xml_file):
        print(f"Erro: Arquivo XML '{xml_file}' não encontrado.")
        return
    if not os.path.exists(xslt_file):
        print(f"Erro: Arquivo XSLT '{xslt_file}' não encontrado.")
        return

    try:
        # Parsear o XML e o XSLT
        xml_tree = etree.parse(xml_file)
        xslt_tree = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_tree)

        # Aplicar a transformação
        result_tree = transform(xml_tree)

        # Salvar o resultado
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(result_tree))
        print(f"Transformação XSLT aplicada com sucesso. Resultado salvo em: {output_file}")

    except Exception as e:
        print(f"Erro ao aplicar a transformação XSLT: {e}")


# Definir os caminhos dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))
xml_file = os.path.join(base_dir, "../xml_output/sub_xmls/Category_1_items.xml")
xslt_file = os.path.join(base_dir, "../xslt_xquery/transform_to_html.xslt")
output_file = os.path.join(base_dir, "../xml_output/sub_xmls/Category_1_items.html")

# Chamar a função
apply_xslt(xml_file, xslt_file, output_file)
