# OCR com Tesseract e Python

Este projeto utiliza o Tesseract OCR para reconhecer texto em imagens e salvar o texto reconhecido em um arquivo de saída.

## Pré-requisitos

- Python 3.6 ou superior
- Tesseract OCR

## Instalação

### Passo 1: Instalar o Python

Certifique-se de que você tem o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

### Passo 2: Instalar o Tesseract OCR

1. **Baixe o instalador do Tesseract OCR**:

   - Acesse a página de [lançamentos do Tesseract OCR no GitHub](https://github.com/tesseract-ocr/tesseract/releases).
   - Baixe o instalador apropriado para o seu sistema operacional (Windows).
2. **Instale o Tesseract OCR**:

   - Execute o instalador baixado e siga as instruções na tela para completar a instalação.
   - Anote o diretório de instalação (por padrão, é `C:\Program Files\Tesseract-OCR\`).
3. **Adicionar o Tesseract ao PATH do Sistema**:

   - Abra as Configurações do Sistema.
   - Vá para "Configurações avançadas do sistema".
   - Clique em "Variáveis de Ambiente".
   - Na seção "Variáveis do sistema", encontre a variável `Path` e clique em "Editar".
   - Adicione o caminho para o diretório onde o Tesseract está instalado, por exemplo: `C:\Program Files\Tesseract-OCR\`.
   - Clique em "OK" para salvar as alterações.
4. **Baixar os dados de treinamento para o idioma português**:

   - Acesse o repositório oficial do Tesseract [aqui](https://github.com/tesseract-ocr/tessdata).
   - Baixe o arquivo `por.traineddata`.
   - Coloque o arquivo `por.traineddata` no diretório `tessdata` do Tesseract (por padrão, `C:\Program Files\Tesseract-OCR\tessdata`).

### Passo 3: Instalar as Dependências do Python

No terminal, navegue até o diretório do projeto e execute:

```sh
pip install pillow pytesseract
```

## Uso

1. **Atualize o caminho para o executável do Tesseract no script** :

**pytesseract.pytesseract.tesseract_cmd **=** **r**'**C:\Program Files\Tesseract-OCR\tesseract.exe**'**

2. **Execute o script** :

```
py index.py`
```

O script irá reconhecer o texto na imagem especificada e salvar o texto em um arquivo de saída.


## Estrutura do Projeto

.
├── inputs
│   └── imagem.jpg          # Imagem de entrada
├── output
│   └── resultado.txt       # Arquivo de saída com o texto
├── index.py                # Script principal
└── README.md               # Este arquivo
