'''
Descripción del proyecto
Crear un programa de línea de comandos que simule un sistema de facturación básico para un supermercado. 
El usuario puede ingresar los artículos comprados (por ejemplo, manteca, huevos, etc.), sus precios y 
cantidades. La aplicación calculará la factura total, aplicará los descuentos correspondientes y mostrará 
un resumen detallado de la factura. Este proyecto se centra en bucles, diccionarios y cálculos aritméticos.
'''

def main():
    print("Welcome to the Supermarket Billing System!")
    item_count = int(input("Enter the number of items: "))
    
    items = {}
    
    for i in range(item_count):
        print(f"\nItem {i + 1}:")
        name = input("Name: ")
        price_per_unit = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))
        
        items[name] = {
            "price_per_unit": price_per_unit,
            "quantity": quantity
        }
    
    # Cálculo de la factura
    subtotal = 0
    for name, details in items.items():
        total_price = details["price_per_unit"] * details["quantity"]
        subtotal += total_price
    
    discount = 0
    # Aquí puedes aplicar condiciones para el descuento si es necesario
    sales_tax = subtotal * 0.05
    total = subtotal - discount + sales_tax
    
    # Resumen de la factura
    print("\n--- Bill Summary ---")
    for name, details in items.items():
        total_price = details["price_per_unit"] * details["quantity"]
        print(f"{name}: {details['quantity']} x ${details['price_per_unit']:.2f} = ${total_price:.2f}")
    
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Sales Tax (5%): ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("\nThank you for shopping with us!")

if __name__ == "__main__":
    main()

