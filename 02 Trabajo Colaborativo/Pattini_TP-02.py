# Trabajo Práctico Git y GitHub
## Actividad 1 

# ¿Qué es GitHub?
## GitHub es una plataforma en el internet donde la comunidad, sus usuarios pueden comparar y compartir sus repositorios y/o codigos de manera publica o privada (a selección).

# ¿Cómo crear un repositorio en GitHub?
## Dentro de la página GitHub hay un boton con el símbolo "+", se aprieta y selecciona la opción nuevo repositorio. Se le asigna un numbre, que puede coincider o no con el repositorio local.
## Se utiliza el comando para que la configuración de Git local use el repositorio remoto "git remote add origin (pegar el url del repositorio remoto)".

# ¿Cómo crear una rama en Git?
## Se abre la terminal, y se utiliza el comando "git branch (escribir nombre de la rama)".

# ¿Cómo cambiar a una rama en Git?
## Se abre la terminal, y se utiliza el comando "git checkout (escribir el nombre de la rama a la que quiera reubicarse)".

# ¿Cómo fusionar ramas en Git?
## Se abre la terminal, usando el comando checkout se posiciona en la rama que va a adquirir los cambios de ambas ramas a fusionarse; y se utiliza el comando "git merge (el nombre de la otra rama con la que se fusionará)".
## Si se generase un conflicto, ya sea por que una o ambas posean distintos contenidos, habrá que solucionarlo salvando el contenido de ambas ramas, o eliminando las discrepancias marcadas.

# ¿Cómo crear un commit en Git?
## Se abre la terminal, primero se agregan los cambios realizados al archivo usando el comando "git add ."; y luego se utiliza el comando "git commit -m (escribir un mensaje o recordatorio del cambio cometido)".

# ¿Cómo enviar un commit a GitHub?
## Se abre la terminal, y se utiliza el comando "git push -u origin (nombre de la rama)", en mi caso se llama MASTER, para otros usuarios puede ser MAIN.

# ¿Qué es un repositorio remoto?
## Es una carpeta que contiene los archivos de nuestros proyectos, el repositorio que se encuentra en la plataforma en la web, en nuestro caso es GitHub.

# ¿Cómo agregar un repositorio remoto a Git?
## Se abre la terminal, y se utiliza el comando "git pull origin master".

# ¿Cómo empujar cambios a un repositorio remoto?
## Se abre la terminal, y se utiliza el comando "git push"; si es la primera vez que se hace, el comando a usar es "git push -u origin master".

# ¿Cómo tirar de cambios de un repositorio remoto?
## Se abre la terminal, y se utiliza el comando "git fetch".

# ¿Qué es un fork de repositorio?
## Es hacer una copia exacta de un repositorio en una cuenta diferente del original, obteniendo un repositorio idéntico para hacer cambios sin modificar el original en la cuenta del usuario.

# ¿Cómo crear un fork de un repositorio? 
## En la plataforma GitHub hay un boton destinado a crear un fork de ese repositorio, en el cual nos va a pedir un nombre, puede ser el mismo del repositorio original o el que queramos.

# ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
## Cuando se decide y abre el repositorio al que se le realizará la solicitud de extracción (suyo, o de otra persona), se apreta en la parte superior de la pagina, en "Pull requests", seguido de apretar en "New pull request".
## Se seleccionará entre dos ramas para hacer una comparación, y se aprieta en "Create pull request". Se agrega un titulo y si se quiere una descripción. Se puede cerrar y reabrir varias veces la misma solicitud de extracción. 

# ¿Cómo aceptar una solicitud de extracción?
## En nuestra cuenta de GitHub hay un icono que indica si nos han hecho una solicitud de extracción, si hay una o varias solicitudes podemos elegir a cual haremos revisión.
## Se apreta en files changed (archivos cambiados), se puede hacer un comentario sobre lo propuesto, continuamente se aprieta en "Aprobar" y seguido en (Enviar revisión).

# ¿Qué es un etiqueta en Git?
## Una etiqueta (o tag) en git permite tener un nombre que apunta a un commit, esto marcar un punto específico en la historia de un repositorio.
## Git utiliza dos tipos principales de etiquetas: ligeras y anotadas. Una etiqueta ligera es muy parecido a una rama que no cambia; las etiquetas anotadas se guardan en la base de datos de Git como objetos enteros.

# ¿Cómo crear una etiqueta en Git?
## Se abre la terminal, y se utiliza el comando "git tag (nombre de la etiqueta)". También se le puede agregar un mensaje haciendo "git tag -a (nombre) -m (mensaje)".

# ¿Cómo enviar una etiqueta a GitHub?
## Para enviar etiquetas en GitHub se las envían de forma explícita al servidor luego de crearlas. Es un proceso similar al de compartir ramas remotas, puedes ejecutar "git push (nombre del repositorio remoto) --tags".

# ¿Qué es un historial de Git?
## El historial de Git es el listado de los commits, lo cometido. Se hace un guardado en el historial cada vez que se realiza el comando "git commit".

# ¿Cómo ver el historial de Git?
## Se puede ver el historial de los commits usando el comando "git log".

# ¿Cómo buscar en el historial de Git?
## Una forma mas comoda para ver la informacion del historial es usando el comando "git log --oneline", muestra la información de commits en una única línea para que sea más fácil examinar las confirmaciones de un vistazo. 

# ¿Cómo borrar el historial de Git?
## En la terminal se escribe "cls", de la palabra cleanse.

# ¿Qué es un repositorio privado en GitHub?
## Es una configuración para repositorios, donde solo se encuentran disponibles para el propietario de dicho repositorio y quienes el o ella elija.

# ¿Cómo crear un repositorio privado en GitHub?
## De la misma forma que se crea un repositorio público, solo cambiando esta opcion a privado.

# ¿Cómo invitar a alguien a un repositorio privado en GitHub?
## Dentro del repositorio privado, se apreta en "Add collaborators to this repository", te va a pedir hacer la verificación con la app de teléfono; una vez hecho se apreta en "add people", y se puede buscar por nombre de usuario, nombre completo o correo.

# ¿Qué es un repositorio público en GitHub?
## Un repositorio publico en GitHub es un repositorio en la plataforma en la cual cualquier usuario puede ver tus archivos publicados y clonarlos (o le pueden hacer un fork), y sugerir cambios, correcciones, o avances de tu codigo para que la utilices.

# ¿Cómo crear un repositorio público en GitHub?
## Una vez se tiene una cuenta de usuario en GitHub, se aprieta en el icono "mas" (+), y se aprieta "New repository".
## Nos va a mostrar como dueños del mismo y elejiremos un nombre y una descripción, se deja la opción en publico, y se aprieta en "Create repository".

# ¿Cómo compartir un repositorio público en GitHub?
## Se abre el repositorio a compartir, en la parte superior del sitio web va a haber un boton de configuración, dentro se aprieta en "collaborators" (colaboradores), y se aprieta en agregar personas.