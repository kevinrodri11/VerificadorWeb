from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

from PaginasWeb import enlaces  # Importa los datos de enlaces, usuarios y contraseñas desde el archivo PaginaWeb.py

def verificar_enlace(enlace, usuario="", contraseña=""):
   
    driver = webdriver.Chrome()   # Inicializa el navegador Chrome con webdriver_manager

    try:
        try:
            driver.get(enlace)
            driver.implicitly_wait(5)  # Pausa para dar tiempo a que la página se cargue completamente

            # Realiza un desplazamiento hacia abajo (scroll)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

            if usuario and contraseña:
                print(f'Enlace: {enlace} - Verificación Exitosa con Usuario: {usuario}')
            else:
                print(f'Enlace: {enlace} - Verificación Exitosa')

        except WebDriverException as e:
            print(f'Enlace: {enlace} - Error: {e.msg}')
            # Si el mensaje de error contiene información sobre la resolución del nombre, muestra un mensaje personalizado
            if 'ERR_NAME_NOT_RESOLVED' in e.msg:
                print('Error: No se pudo resolver el nombre del host. Verifica la validez del enlace.')
            else:
                print('Error no identificado. Consulta el mensaje de error para obtener más detalles.')
                
    finally:
        # Cierra el navegador al final, incluso si hay un error
        driver.quit()

# Itera sobre todos los enlaces desde el archivo PaginaWeb.py
for nombre_pagina, datos_pagina in enlaces.items():
    enlace = datos_pagina["enlace"]
    usuario = datos_pagina.get("usuario", "")
    contraseña = datos_pagina.get("contraseña", "")

    # Llama a la función para verificar el enlace
    verificar_enlace(enlace, usuario, contraseña)
