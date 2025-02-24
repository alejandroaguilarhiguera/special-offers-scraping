import requests
from bs4 import BeautifulSoup
import re
import requests
import time

# URL de la API o sitio donde quieres hacer la solicitud POST
urlProduct = "http://localhost:3000/products"


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
# response = requests.get(url, headers=headers,verify=False)
# links = []

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Buscar la lista de productos
#     products = soup.find_all("li", class_="product")

#     for product in products:
#         links.append(product.find("a", class_="woocommerce-LoopProduct-link")["href"])


response = requests.get(url, headers=headers, verify=False)
links = []

last_page = 1
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")


    # Obtener todos los elementos de paginación
    pagination_links = soup.select(".page-numbers")

    # Seleccionar el penúltimo elemento (índice -2)
    last_page_element = pagination_links[-2]
    last_page = int(last_page_element.text) 


for page in range(1, last_page +1):
    response = requests.get(url + "page/"+str(page), headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("li", class_="product")

    for product in products:
        product_link = product.find("a", class_="woocommerce-LoopProduct-link")
        if product_link:
            links.append(product_link["href"])

print(links)




for link in links:
    print(link)

    response = requests.get(link, headers=headers, verify=False)  # <-- Aquí está el cambio
    
    if response.status_code == 200:
        soupPage = BeautifulSoup(response.text, "html.parser")

        name = soupPage.find("h1").text.strip()

        # test
        price = soupPage.find("span", class_="amount").text.strip()
        
        
        match = re.match(r"([^\d]+)([\d,.]+)", price)
        if match:
            currency = match.group(1)  # Captura el símbolo de moneda
            amount = match.group(2)  # Captura el valor numérico



        description = soupPage.find("div", class_="woocommerce-product-details__short-description").find('p').text.strip()
        # stock = soupPage.find("p", class_="stock in-stock").text.strip()
        # stock_element = soupPage.find("p", class_="stock in-stock")
        # stock = ""
        # if stock_element:
        #     stock_text = stock_element.get_text(strip=True)  # "125 in stock"
        #     stock_number = ''.join(filter(str.isdigit, stock_text))  # Extrae solo los números
        #     stock = stock_number
        # else:
        #     print("No se encontró el stock.")
    
    
        # sku = ""
        
        # sku_element = soupPage.find("span", class_="sku")

        # if sku_element:
        #     sku = sku_element.get_text(strip=True)
        # else:
        #     print("No se encontró el SKU.")
        
        # categorias = [cat.text for cat in soupPage.select(".posted_in a")]
        # tags = [tag.text for tag in soupPage.select(".tagged_as a")]
        # imagen = soupPage.find("div", class_="woocommerce-product-gallery__image").find("a")["href"]


        # image_div = soupPage.find("div", class_="woocommerce-product-gallery__image")

        # if image_div:
        #     image_link = image_div.find("a")
        #     print(image_link)
        # else:
        #     print("No se encontró el div de la imagen.")
    
    
    

        # Extraer información adicional
        # peso = soupPage.select_one(".product_weight").text.strip()
        # dimensiones = soupPage.select_one(".product_dimensions").text.strip()

        # Mostrar los datos obtenidos
        product = {
            "name": name,
            "price": amount,
            "currencyName": currency,
            # "Precio": "precio",
            "description": description,
            # "Stock": stock,
            # "SKU": sku,
            # "Categorías": categorias,
            # "Tags": tags,
            # "Imagen": imagen,
            # "Peso": peso,
            # "Dimensiones": dimensiones,
        }
        print(product)
        response = requests.post(urlProduct, json=product, headers=headersLogin)
        



# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Buscar la lista de productos
#     products = soup.find_all("li", class_="product")

#     # Extraer información de cada producto
#     for product in products:
#         name = product.find("h2", class_="woocommerce-loop-product__title").text.strip()
#         price = product.find("span", class_="woocommerce-Price-amount").text.strip()
#         link = product.find("a", class_="woocommerce-LoopProduct-link")["href"]
#         image = product.find("img")["src"]
#         match = re.match(r"([^\d]+)([\d,.]+)", price)
#         if match:
#             currency = match.group(1)  # Captura el símbolo de moneda
#             amount = match.group(2)  # Captura el valor numérico

#         data = {
#             "name": name,
#             "price": amount,
#             "stock": 1,
#             "link": link,
#             "image": image
#         }
#         # Hacer la solicitud POST
#         response = requests.post(urlProduct, json=data, headers=headersLogin)

#         print(f"Nombre: {name}")
#         print(f"Precio: {price}")
#         print(f"Enlace: {link}")
#         print(f"Imagen: {image}")
#         print("-" * 40)
# else:
#     print(f"Error {response.status_code}: No se pudo acceder a la página")