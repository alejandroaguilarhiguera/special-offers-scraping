import requests
from bs4 import BeautifulSoup
import time

# URL de la tienda
url = "http://scrapeme.live/shop/"

# Encabezados para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Realizar la solicitud HTTP request
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

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Buscar la lista de productos
#     products = soup.find_all("li", class_="product")

#     for product in products:
#         product_link = product.find("a", class_="woocommerce-LoopProduct-link")
#         if product_link:
#             links.append(product_link["href"])

# for link in links:
#     print(f"Scrapeando: {link}")
#     time.sleep(5)
    
#     response = requests.get(link, headers=headers, verify=False)  # <-- Aquí está el cambio

#     if response.status_code == 200:
#         soupPage = BeautifulSoup(response.text, "html.parser")

#         # Extraer el nombre correctamente
#         nombre_element = soupPage.find("h1", class_="product_title entry-title")
#         nombre = nombre_element.text.strip() if nombre_element else "No encontrado"

#         print(f"Nombre del producto: {nombre}")
        
#         producto = {
#             "Nombre": nombre,
#         }
#         print(producto)

#         time.sleep(10)