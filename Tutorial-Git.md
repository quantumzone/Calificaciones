Para comenzar a usar Git y GitHub para versionar tu proyecto y subirlo a tu repositorio en GitHub, sigue estos pasos:
1. Configura Git

    Instala Git si no lo tienes ya:
        Descárgalo de git-scm.com y sigue las instrucciones de instalación.

    Configura tu identidad de usuario en Git: Abre la terminal o el símbolo del sistema y ejecuta los siguientes comandos:

    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_correo@example.com"

2. Inicializa Git en tu carpeta del proyecto

    Abre la terminal y navega a la carpeta de tu proyecto:

cd D:\DC\Code\calif

Inicializa Git en esa carpeta:

    git init

3. Conecta el proyecto a tu repositorio de GitHub

    Configura el repositorio remoto: Agrega la URL del repositorio remoto como origen:

git remote add origin https://github.com/quantumzone/Calificaciones.git

Verifica la conexión:

    git remote -v

4. Prepara tu proyecto para el primer commit

    Agrega todos los archivos del proyecto al área de preparación (staging area):

git add .

Esto incluirá todos los archivos y carpetas dentro de tu proyecto.

Realiza tu primer commit:

    git commit -m "Primera versión del proyecto"

5. Sube el proyecto a GitHub

    Envía los cambios al repositorio remoto:

    git branch -M main
    git push -u origin main

    Esto subirá tu código al repositorio remoto y establecerá la rama main como principal.

6. Usa Git para futuras actualizaciones

    Cada vez que realices cambios en tu proyecto:
        Agrega los archivos modificados:

git add .

Realiza un commit con un mensaje descriptivo:

git commit -m "Descripción de los cambios realizados"

Sube los cambios a GitHub:

git push
