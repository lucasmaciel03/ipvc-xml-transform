<br />
<p align="center">
  <a href="">
    <img src="images/ipvc.png" alt="Logo" width="auto" height="200">
  </a>

  <h1 align="center">Instituto Politécnico de Viana do Castelo</h1>

  <h3 align="center">Integração de Sistemas</h3>

  <h3 align="center">Lucas Maciel | João Fernandes</h3>

  <h3 align="center">Transformação e Manipulação de XML</h3>
</p>

---

# IPVC XML Transform

Este projeto fornece ferramentas para transformação, validação, manipulação e consulta de dados entre os formatos **CSV** e **XML**. Ele inclui funcionalidades como conversão de CSV para XML, validação com schema XSD, criação de sub-XMLs, transformações com XSLT e consultas XPath.

## Funcionalidades Disponíveis

### 1. Conversão de CSV para XML
- **Descrição:** Converte um ficheiro CSV em um ficheiro XML formatado e estruturado.
- **Requisição:**
    - **Arquivo CSV:** Localizado na pasta `dataset/`.
- **Saída:**
    - **Arquivo XML:** Gerado na pasta `xml_output/`.

### 2. Validação de XML com XSD
- **Descrição:** Valida um ficheiro XML com base em um schema (XSD) definido.
- **Requisição:**
    - **Arquivo XML:** Localizado na pasta `xml_output/`.
    - **Schema XSD:** Localizado na pasta `schemas/`.
- **Saída:**
    - Mensagem indicando sucesso ou falha na validação.

### 3. Criação de Sub-XMLs
- **Descrição:** Gera sub-XMLs a partir de um XML base, filtrando os dados com base em critérios específicos (ex.: categorias).
- **Requisição:**
    - **Arquivo XML:** Localizado na pasta `xml_output/`.
- **Saída:**
    - Sub-XMLs salvos na pasta `xml_output/sub_xmls/`.

### 4. Transformação de XML para HTML (XSLT)
- **Descrição:** Transforma um ficheiro XML em HTML usando um arquivo XSLT.
- **Requisição:**
    - **Arquivo XML:** Localizado na pasta `xml_output/sub_xmls/`.
    - **Arquivo XSLT:** Localizado na pasta `xslt_xquery/`.
- **Saída:**
    - Arquivo HTML gerado na pasta `xml_output/sub_xmls/`.

### 5. Consultas XPath
- **Descrição:** Extrai informações específicas de um XML usando consultas XPath.
- **Exemplos de Consultas:**
    - Itens com preço superior a 10.
    - Listagem de itens por categoria.
    - Contagem total de itens no XML.

---

## Como Utilizar

### Pré-requisitos
- Python 3.8+ instalado.
- Instalar as dependências especificadas no ficheiro `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Fluxo Completo de Execução
1. **Converter CSV para XML:**
    ```bash
    python scripts/csv_to_xml.py
    ```
2. **Validar XML com XSD:**
    ```bash
    python scripts/validate_xml.py
    ```
3. **Gerar Sub-XMLs:**
    ```bash
    python scripts/generate_subxmls.py
    ```
4. **Transformar XML para HTML com XSLT:**
    ```bash
    python scripts/apply_xslt.py
    ```
5. **Consultar XML com XPath:**
    ```bash
    python scripts/query_xml.py
    ```

---

## Logs e Erros

- Logs de operações e mensagens de erro são exibidos no terminal durante a execução de cada script.
- Verifique o terminal para detalhes adicionais sobre falhas ou sucessos em cada etapa do fluxo.

---

## Organização do Projeto

- **`dataset/`**: Contém os ficheiros CSV de entrada.
- **`schemas/`**: Contém os schemas XSD usados para validação.
- **`scripts/`**: Scripts principais do projeto para cada funcionalidade.
- **`xml_output/`**: Saída dos XMLs gerados e processados.
- **`xslt_xquery/`**: Transformações e consultas XSLT/XQuery.

---

## Equipa

- Lucas Maciel
- João Fernandes
