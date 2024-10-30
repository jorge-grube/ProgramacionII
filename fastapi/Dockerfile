# Dockerfile para FastAPI
FROM tiangolo/uvicorn-gunicorn

# Crear el directorio de trabajo
RUN mkdir /fastapi

# Copiar el archivo de requisitos
COPY requirements.txt /fastapi

# Establecer el directorio de trabajo
WORKDIR /fastapi

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el código completo
COPY . /fastapi  # Esto incluye la carpeta `veterinaria`

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]