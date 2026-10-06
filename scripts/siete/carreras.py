"""Carreras: todos los grados oficiales en alta del Registro de Universidades, Centros y Títulos (RUCT,
Ministerio de Universidades), bajados de https://www.educacion.gob.es/ruct/consultaestudios.
Nivel: en cuántas universidades se puede estudiar cada grado, con una corrección a mano para
una docena de carreras clásicas (ver CLASICAS)."""
import collections
from comun import *

def nombre(t):
    t = re.sub(r"^Graduad[oa] o Graduad[oa] en |^Grado en ", "", t)
    t = re.sub(r" por (la|el|les?|las|los) .*$", "", t)
    t = re.split(r"\s*/\s*", t)[0]                       # fuera el nombre en inglés
    t = re.sub(r"\s*\((ADE|Big Data)\)", "", t)
    return re.sub(r"^Maestro en ", "", t).strip()

# lo que la gente dice de verdad → nombre oficial
ALIAS = {
 "Administración y Dirección de Empresas": ["ADE", "Empresariales", "Administración de Empresas", "Dirección de Empresas", "Business"],
 "Ingeniería Informática": ["Informática", "Ingeniería de Software"],
 "Ciencias de la Actividad Física y del Deporte": ["INEF", "CAFD", "CAFYD", "Educación Física", "Ciencias del Deporte"],
 "Educación Primaria": ["Magisterio", "Magisterio de Primaria", "Maestro", "Profesor de Primaria", "Primaria"],
 "Educación Infantil": ["Magisterio de Infantil", "Infantil"],
 "Nutrición Humana y Dietética": ["Nutrición", "Dietética"],
 "Relaciones Laborales y Recursos Humanos": ["Relaciones Laborales", "Recursos Humanos", "RRHH", "Graduado Social"],
 "Estudios Ingleses": ["Filología Inglesa", "Inglés"],
 "Publicidad y Relaciones Públicas": ["Publicidad"],
 "Ingeniería Electrónica Industrial y Automática": ["Ingeniería Electrónica", "Electrónica"],
 "Ingeniería en Tecnologías Industriales": ["Ingeniería Industrial", "Industriales"],
 "Ingeniería de Tecnologías de Telecomunicación": ["Teleco", "Telecomunicaciones", "Ingeniería de Telecomunicaciones", "Ingeniería de Telecomunicación"],
 "Traducción e Interpretación": ["Traducción"],
 "Ciencia y Tecnología de los Alimentos": ["Tecnología de los Alimentos"],
 "Fundamentos de la Arquitectura": ["Arquitectura"],
 "Ingeniería Aeroespacial": ["Aeronáutica", "Ingeniería Aeronáutica", "Aeroespacial"],
 "Ingeniería Civil": ["Caminos", "Ingeniería de Caminos", "Ingeniería de Caminos, Canales y Puertos"],
 "Óptica y Optometría": ["Óptica", "Optometría"],
 "Finanzas y Contabilidad": ["Finanzas", "Contabilidad"],
 "Antropología Social y Cultural": ["Antropología"],
 "Geografía y Ordenación del Territorio": ["Geografía"],
 "Gestión y Administración Pública": ["Administración Pública"],
 "Ciencias Políticas y de la Administración": ["Ciencias Políticas", "Políticas"],
 "Ciencias Ambientales": ["Ambientales", "Medio Ambiente"],
 "Comunicación Audiovisual": ["Audiovisuales"],
 "Ingeniería Agroalimentaria y del Medio Rural": ["Agrónomos", "Ingeniería Agrónoma", "Ingeniería Agrícola"],
 "Arquitectura Técnica": ["Aparejadores", "Aparejador"],
 "Ciencia e Ingeniería de Datos": ["Ciencia de Datos", "Data Science", "Big Data"],
 "Información y Documentación": ["Biblioteconomía", "Documentación"],
 "Filología Hispánica": ["Filología", "Lengua y Literatura"],
 "Lengua y Literatura Españolas": ["Hispánicas"],
 "Ingeniería Mecánica": ["Mecánica"],
 "Ingeniería Química": [], "Ingeniería Eléctrica": ["Electricidad"],
 "Ingeniería Biomédica": ["Biomédica"], "Historia del Arte": ["Arte"],
 "Ingeniería de Diseño Industrial y Desarrollo del Producto": ["Diseño Industrial"],
 "Ingeniería Forestal y del Medio Natural": ["Montes", "Ingeniería de Montes", "Forestales"],
 "Ingeniería Naval y Oceánica": ["Ingeniería Naval", "Naval"],
 "Ingeniería de Minas": ["Minas"], "Náutica y Transporte Marítimo": ["Náutica"],
 "Cine": ["Cinematografía"], "Diseño de Moda": ["Moda"],
 "Negocios Internacionales": ["International Business", "Negocios"],
}

# Grados que existen y el registro lista con otro nombre o dentro de un doble grado: (nombre, universidades)
A_MANO = [("Economía y Negocios Internacionales", 1)]

# Carreras de toda la vida que pocas universidades ofrecen (plazas limitadas, facultades caras).
# El recuento las dejaría como raras y no lo son: se quedan como mucho en nivel 2.
CLASICAS = ["Farmacia", "Veterinaria", "Fundamentos de la Arquitectura", "Bellas Artes", "Sociología",
            "Filología Hispánica", "Ingeniería de Tecnologías de Telecomunicación", "Ingeniería Civil",
            "Traducción e Interpretación", "Ingeniería Aeroespacial", "Ciencias Políticas y de la Administración"]

cuenta = collections.Counter()
with open(FUENTES / "grados_ruct.csv", encoding="utf-8") as f:
    for cod, titulo, uni in csv.reader(f): cuenta[nombre(titulo)] += 1

for n, c in A_MANO: cuenta[n] += c

# juntar variantes que solo cambian en mayúsculas o tildes
grupos = {}
for n, c in cuenta.items():
    g = grupos.setdefault(clave(n), [n, 0])
    g[1] += c
    if cuenta[n] > cuenta.get(g[0], 0): g[0] = n
al = {clave(k): v for k, v in ALIAS.items()}
sin = [k for k in ALIAS if clave(k) not in grupos]
clasicas = {clave(c) for c in CLASICAS}
filas = [(n, al.get(k, []), min(nivel_por_umbral(c, [45, 25, 10, 3]), 2 if k in clasicas else 5), c)
         for k, (n, c) in grupos.items()]
guarda("carreras", filas, "universidades_que_lo_ofrecen")
print("alias sin grado en el registro:", sin)
