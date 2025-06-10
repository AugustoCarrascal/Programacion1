from datetime import date

Tema = "Bradley Cooper | Lukas Nelson - Shallow"
Vistas = "1900 millones"
Duración = "3:37"
Link = "https://www.youtube.com/watch?v=bo_efYhYU2A"
Fecha_de_Lanzamiento = "2018-09-27"

def obtener_colaboradores(tema: str) -> list:
    tema = tema.split("-")
    colabadores = tema[0].split("|")
    for i in range(len(colabadores)):
        colabadores[i] = colabadores[i].strip()
    print("los colaboradores son: ",colabadores)
    return colabadores

obtener_colaboradores(Tema)

def obtener_nombre_tema(titulo: str) -> str:
    titulo = titulo.split(" - ")
    nombre_cancion = titulo[1].split()
    print("el nombre de la cancion es: ",nombre_cancion)
    return nombre_cancion

obtener_nombre_tema(Tema)

def convertir_visitas_numerico(visitas: str) -> int:
    partes = visitas.split()
    numero = int(partes[0])
    visitas_numeros = numero * 1000000
    print("la visitas del video es de:",visitas_numeros)

convertir_visitas_numerico(Vistas)

def convertir_duracion_numerico(duracion: str) -> int:
    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])
    duracion_total = minutos * 60 + segundos
    print("la duracion en segundos es de:",duracion_total)
    return duracion_total

convertir_duracion_numerico(Duración)

def obtener_codigo(link: str) -> str:
    url = link.split("=")
    codigo = url[1]
    print("el codigo del video es:",codigo)
    return codigo

obtener_codigo(Link)

def formatear_fecha(fecha: str) -> date:
    partes = fecha.split("-")
    anio = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])
    fecha_formateada = date(anio,mes,dia)
    print("la fecha como objeto date es:",fecha_formateada)
    return fecha_formateada

formatear_fecha(Fecha_de_Lanzamiento)
