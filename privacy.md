
# Política de Privacidad — `ivec-zotero-api`

**Última actualización:** 29 de julio de 2025

## 1. ¿Quiénes somos?

`ivec-zotero-api` es una API personalizada que permite acceder a una biblioteca Zotero privada para recuperar citas bibliográficas en formato BibTeX. Esta API ha sido creada y es mantenida por [Tu nombre o alias].

## 2. ¿Qué datos recogemos?

La API **no recoge, almacena ni procesa datos personales de los usuarios**. Las únicas solicitudes procesadas son:

- Términos de búsqueda enviados como parámetros en la URL (`?q=`).
- Solicitudes GET anónimas para recuperar citas desde Zotero.

## 3. ¿Qué hace la API con los datos?

La API:

- **Consulta tu biblioteca Zotero personal** mediante una clave API privada.
- Devuelve **únicamente los metadatos bibliográficos** de los ítems que coincidan con la consulta.
- **No registra ni guarda consultas** ni resultados en ninguna base de datos.

## 4. ¿Qué datos personales están protegidos?

La clave Zotero (`ZOTERO_API_KEY`) está almacenada de forma segura como variable de entorno en el servidor (Render). **Nunca se expone al usuario final ni se transmite en la respuesta.**

## 5. Seguridad

- El servidor no guarda registros.
- La API no tiene acceso de escritura ni privilegios administrativos sobre Zotero.
- Se emplea HTTPS para todas las comunicaciones.

## 6. Terceros

No compartimos ninguna información con terceros. Esta API no utiliza cookies, ni rastrea, ni integra servicios analíticos de terceros.

## 7. Cambios en la política

Nos reservamos el derecho de modificar esta política en cualquier momento. Las actualizaciones se publicarán en esta sección con la nueva fecha de entrada en vigor.

## 8. Contacto

Para preguntas sobre esta política o el funcionamiento de la API, puedes escribir a:  
📧 `tu-correo@ejemplo.com`
