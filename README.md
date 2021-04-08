# Poshibot
Yet Another Bot para manejar los grupos de FIUBAVerse

# Instalación
1. Clonar el repo
2. Crear el enviroment ``poshibot`` con: ``conda env create -f environment.yml``
3. Crear un archivo de texto llamado ``.env`` con los siguientes datos:
```
POSHIBOT_TOKEN = "<TOKEN DE BOTFATHER>" 
SMTP_USER = "<USER>@gmail.com"
SMTP_PASSWORD = "<PASSWORD>"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
```

Reemplace **cuando menos** todos los campos entre ``<>``

# Uso
3. Activar el enviroment con ``conda activate poshibot``
4. Ejecutar el bot: ``python poshibot.py``