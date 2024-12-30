import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice(data):
    client = data['client']
    items = data['items']
    tax_rate = data['tax_rate']

    total = sum(item['price'] * item['quantity'] for item in items)
    tax = total * tax_rate
    grand_total = total + tax

    pdf_file = "Invoice.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    # Configuración de márgenes
    margin = 50
    width, height = letter

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, height - margin, "Factura")
    
    c.setFont("Helvetica", 12)
    c.drawString(margin, height - margin - 30, f"Cliente: {client['name']}")
    c.drawString(margin, height - margin - 50, f"Dirección: {client['address']}")

    # Cabecera de la tabla
    c.drawString(margin, height - margin - 90, "Descripción")
    c.drawString(margin + 250, height - margin - 90, "Cantidad")
    c.drawString(margin + 350, height - margin - 90, "Precio Unitario")
    c.drawString(margin + 450, height - margin - 90, "Total")

    # Detallar los artículos
    y_position = height - margin - 110
    for item in items:
        c.drawString(margin, y_position, item['description'])
        c.drawString(margin + 250, y_position, str(item['quantity']))
        c.drawString(margin + 350, y_position, f"${item['price']:.2f}")
        c.drawString(margin + 450, y_position, f"${item['price'] * item['quantity']:.2f}")
        y_position -= 20

    # Línea divisoria
    c.line(margin, y_position + 10, width - margin, y_position + 10)

    # Totales
    y_position -= 20
    c.drawString(margin + 350, y_position, "Subtotal:")
    c.drawString(margin + 450, y_position, f"${total:.2f}")

    y_position -= 20
    c.drawString(margin + 350, y_position, "Impuesto:")
    c.drawString(margin + 450, y_position, f"${tax:.2f}")

    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin + 350, y_position, "Total a Pagar:")
    c.drawString(margin + 450, y_position, f"${grand_total:.2f}")

    c.save()
    print(f"Factura guardada como '{pdf_file}'.")

def main():
    input_file = './facturas/invoice_data.json'

    with open(input_file, 'r') as f:
        data = json.load(f)

    generate_invoice(data)

if __name__ == "__main__":
    main()