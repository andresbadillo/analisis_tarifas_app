# 🔧 Guía de Solución de Problemas

## 🚫 Error de Permisos (403 - Access Denied)

### Problema
El usuario ve un mensaje de error indicando que no tiene permisos para acceder al archivo "Tarifas comparativas.xlsm".

### Causas Posibles
1. **Permisos insuficientes**: El usuario no tiene permisos de lectura en la carpeta "Tarifas Reguladas"
2. **Archivo protegido**: El archivo requiere permisos específicos
3. **Rol incorrecto**: El usuario no tiene el rol necesario en la organización
4. **Token expirado**: El token de autenticación ha expirado

### Solución para Usuarios

#### Paso 1: Verificar Autenticación
- Asegúrate de haber iniciado sesión correctamente con tu cuenta de Ruitoque
- Si ves el botón de login, haz clic en "Inicia sesión con tus credenciales de Ruitoque"

#### Paso 2: Solicitar Permisos
1. **Contacta al Analista de Ventas** por correo electrónico
2. **Proporciona la siguiente información:**
   - Tu nombre completo
   - Tu nombre de usuario/correo corporativo
   - El motivo por el que necesitas acceso al archivo
   - La fecha en que necesitas el acceso

#### Paso 3: Esperar Autorización
- El Analista de Ventas revisará tu solicitud
- Una vez autorizado, recibirás confirmación por correo
- El proceso puede tomar hasta 24 horas hábiles

#### Paso 4: Reintentar Acceso
1. Una vez autorizado, regresa a la aplicación
2. Haz clic en el botón **"🔄 Reintentar Carga"**
3. La aplicación debería cargar el archivo correctamente

### Solución para Administradores

#### Verificar Permisos en SharePoint
1. Accede a SharePoint con una cuenta de administrador
2. Navega a la carpeta "Tarifas Reguladas"
3. Haz clic derecho en "Tarifas comparativas.xlsm"
4. Selecciona "Compartir" → "Administrar acceso"
5. Verifica que el usuario tenga permisos de "Lectura"

#### Otorgar Permisos
1. En la ventana de permisos, haz clic en "Agregar personas"
2. Busca el usuario por nombre o correo
3. Asigna el rol "Lector" o "Colaborador"
4. Haz clic en "Compartir"

#### Verificar Configuración de Azure AD
1. Accede al [Portal de Azure](https://portal.azure.com)
2. Ve a "Azure Active Directory" → "Aplicaciones empresariales"
3. Busca la aplicación de análisis de tarifas
4. Verifica que el usuario esté asignado a la aplicación

## 🔄 Otros Errores Comunes

### Error de Conexión
**Síntomas**: Mensaje "Error de conexión al descargar archivo"

**Solución**:
- Verifica tu conexión a internet
- Intenta nuevamente en unos minutos
- Si persiste, contacta al administrador del sistema

### Archivo No Encontrado
**Síntomas**: Error 404 o "Archivo no existe"

**Solución**:
- Verifica que el archivo "Tarifas comparativas.xlsm" existe en SharePoint
- Contacta al administrador si el archivo fue movido o eliminado

### Token Expirado
**Síntomas**: Error de autenticación o redirección al login

**Solución**:
- Cierra la aplicación
- Vuelve a abrir la aplicación
- Inicia sesión nuevamente

## 📞 Contactos de Soporte

### Para Usuarios
- **Analista de Ventas**: [correo del analista]
- **Soporte Técnico**: [correo de soporte]

### Para Administradores
- **Desarrollador**: [andresbadillo.co](https://www.andresbadillo.co/)
- **Equipo de IT**: [correo del equipo IT]

## 📋 Checklist de Verificación

### Antes de Contactar Soporte
- [ ] ¿Iniciaste sesión correctamente?
- [ ] ¿Tienes conexión a internet estable?
- [ ] ¿Intentaste recargar la página?
- [ ] ¿El error persiste después de 24 horas?

### Información para Reportar
- [ ] Tu nombre completo
- [ ] Tu correo corporativo
- [ ] Descripción detallada del error
- [ ] Pasos que seguiste antes del error
- [ ] Captura de pantalla del error (si es posible)
- [ ] Fecha y hora del error

---

**Última actualización**: Agosto 2025  
**Versión**: v2.3.1
