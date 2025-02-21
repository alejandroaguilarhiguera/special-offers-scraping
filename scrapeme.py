import requests
from bs4 import BeautifulSoup
import re
import requests

# URL de la API o sitio donde quieres hacer la solicitud POST
urlLogin = "http://localhost:3000/products"


# Encabezados (si la API lo requiere)
headersLogin = {
    "Content-Type": "application/json",
}








# URL de la tienda
url = "http://scrapeme.live/shop/"

# Encabezados para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar la lista de productos
    products = soup.find_all("li", class_="product")

    # Extraer información de cada producto
    for product in products:
        name = product.find("h2", class_="woocommerce-loop-product__title").text.strip()
        price = product.find("span", class_="woocommerce-Price-amount").text.strip()
        link = product.find("a", class_="woocommerce-LoopProduct-link")["href"]
        image = product.find("img")["src"]
        match = re.match(r"([^\d]+)([\d,.]+)", price)
        if match:
            currency = match.group(1)  # Captura el símbolo de moneda
            amount = match.group(2)  # Captura el valor numérico

        data = {
            "name": name,
            "price": amount,
            "stock": 1,
            "link": link,
            "image": image
        }
        # Hacer la solicitud POST
        response = requests.post(urlLogin, json=data, headers=headersLogin)

        print(f"Nombre: {name}")
        print(f"Precio: {price}")
        print(f"Enlace: {link}")
        print(f"Imagen: {image}")
        print("-" * 40)
else:
    print(f"Error {response.status_code}: No se pudo acceder a la página")