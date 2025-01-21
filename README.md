# Laboratorio 2: Rendimiento de Bases de Datos NoSQL

Este repositorio contiene toda la documentación y los archivos necesarios para replicar el laboratorio de evaluación del rendimiento de dos bases de datos NoSQL: **MongoDB** (documentos) y **Redis** (clave-valor). También se incluye un script en Python para realizar las pruebas CRUD.

## Índice
- [Requisitos Previos](#requisitos)
- [Instalación de MongoDB](#instalación-de-mongodb)
- [Instalación de Redis](#instalación-de-redis)
- [Instalación de Dependencias de Python](#instalación-de-paquetes-de-python)
- [Ejecución del Script](#ejecución-del-script)

---

## Requisitos
- Python 3.8 o superior.
- MongoDB instalado localmente.
- Redis instalado localmente.

---

## Instalación de MongoDB
1. Descarga el instalador de MongoDB desde la página oficial: [MongoDB Community Server](https://www.mongodb.com/try/download/community).
2. Sigue los pasos del instalador.
3. Verificar la instalación ejecutando en la terminal: "mongod --version"

---

## Instalación de Redis
1. Descargar Redis desde el repositorio de Microsoft Open Tech: [Redis para Windows](https://github.com/microsoftarchive/redis/releases).
2. Descomprimir el archivo descargado.
3. Añadir la ruta del descomprimido al path del sistema.
4. Verificar la instalacion ejecutando en la terminal: "redis-server"

---

## Instalación de Paquetes de Python
1. Instalar el paquete de mongo para python utilizando el comando en la terminal: "pip install pymongo"
2. Instalar el paquete de redis para python utilizando el comando en la terminal: "pip install redis"
3. De ser necesario, instalar el paquete de tiempo para python utilizando el comando en la terminal: "pip install time"

---

## Ejecución del Script
1. Asegurarse de que los servicios de MongoDB y Redis esten eejectuandose.
2. Ejecutar el archivo 'prueba.py'
3. Los tiempos de ejecución para ambas bases se mostraran en la terminal.
