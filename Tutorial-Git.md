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
-----
ERRORES COMUNIES
1. Asegúrate de que el Repositorio Local Está Conectado al Remoto
Verifica si el repositorio remoto (origin) está configurado correctamente:

bash
Copiar código
git remote -v
Deberías ver algo como esto:

perl
Copiar código
origin  https://github.com/usuario/repositorio.git (fetch)
origin  https://github.com/usuario/repositorio.git (push)
Si no aparece, agrega el repositorio remoto:

bash
Copiar código
git remote add origin https://github.com/usuario/repositorio.git
2. Verifica si la Rama main Existe
Si estás intentando renombrar la rama actual a main, asegúrate de estar en la rama correcta:

bash
Copiar código
git branch
Si estás en otra rama (por ejemplo, master), cámbiala antes de renombrarla:

bash
Copiar código
git checkout master
git branch -M main
3. Subir la Nueva Rama al Remoto
Una vez que la rama main esté configurada, súbela al repositorio remoto con:

bash
Copiar código
git push -u origin main
4. Cambiar la Rama Predeterminada en GitHub (Si Aplica)
Si el repositorio remoto está en GitHub y su rama predeterminada es master, necesitas cambiarla manualmente a main en la configuración del repositorio:

Ve a tu repositorio en GitHub.
Haz clic en Settings > Branches.
Cambia la rama predeterminada a main.
5. Forzar la Creación de la Rama main Remota
Si los pasos anteriores no funcionan, fuerza la creación de la rama remota con:

bash
Copiar código
git push origin HEAD:main
Esto crea la rama main en el remoto, incluso si no existía.

6. Eliminar Conflictos con la Rama master (Opcional)
Si la rama master existe tanto en local como en remoto y ya no la necesitas, elimínala:

En el repositorio remoto:

bash
Copiar código
git push origin --delete master
En el repositorio local:

bash
Copiar código
git branch -d master

-----
El error indica que el repositorio remoto ya tiene un historial de commits en la rama main que no coincide con tu repositorio local. Esto ocurre porque estás intentando sobrescribir el historial remoto sin haber sincronizado primero.

Para solucionar este problema, puedes seguir los pasos que se indican a continuación según tus necesidades.

Opción 1: Traer y Fusionar Cambios Remotos
Si quieres integrar los cambios remotos en tu repositorio local antes de empujar:

Descarga los cambios remotos:

bash
Copiar código
git pull origin main --rebase
Esto intentará aplicar tus cambios locales sobre los cambios remotos.

Sube los cambios nuevamente:

bash
Copiar código
git push -u origin main
Opción 2: Sobrescribir el Repositorio Remoto
Si no necesitas los cambios que están en el repositorio remoto y quieres sobrescribirlos con tu repositorio local:

Fuerza el push:

bash
Copiar código
git push -u origin main --force
Esto sobrescribirá el historial remoto con el historial de tu repositorio local. Nota: Esta acción eliminará cualquier cambio remoto que no esté en tu repositorio local.

Opción 3: Clonar Cambios Remotos (Si los Necesitas)
Si decides conservar los cambios remotos y trabajar desde ahí:

Descarga los archivos remotos:

bash
Copiar código
git pull origin main
Si hay conflictos, Git te pedirá que los resuelvas manualmente.

Sube los cambios una vez resueltos:

bash
Copiar código
git push -u origin main
Opción 4: Verificar Conflictos
Si no estás seguro de qué cambios remotos están causando el problema, revisa el historial remoto:

Verifica el historial remoto:

bash
Copiar código
git log origin/main
Compara con el historial local:

bash
Copiar código
git log
Esto te permitirá entender las diferencias entre los repositorios antes de decidir qué acción tomar.
