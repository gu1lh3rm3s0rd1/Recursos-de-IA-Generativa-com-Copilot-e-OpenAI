from PIL import Image
import pytesseract

# Atualize o caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text(image_path, output_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='por')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

image_path = 'inputs/imagem.jpg'
output_path = 'outputs/resultado.txt'

recognize_text(image_path, output_path)