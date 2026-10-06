"""Apellidos: todos los que llevan 20 personas o más en España (INE, censo a 1-1-2025).
Fuente: https://www.ine.es/daco/daco42/nombyapel/apellidos_frecuencia.xls
Nivel: cuánta gente lo lleva de primer apellido."""
import csv, re
from comun import *

TILDES = """García Rodríguez González Fernández López Martínez Sánchez Pérez Gómez Martín Jiménez Hernández Díaz Álvarez
Gutiérrez Ramírez Vázquez Domínguez Suárez Méndez Núñez Giménez Márquez León Durán Benítez Vélez Román Sáez Sáenz Velázquez
Bermúdez Cortés Garzón Guillén Marín Rincón Galán Beltrán Roldán Millán Simón Pavón Chacón Calderón Ibáñez Yáñez Estévez
Meléndez Menéndez Avilés Valdés Andrés Ginés Farré Solé Córdoba Mejía Macías Cárdenas Ávila Águila Ángel Jesús Tomás Lázaro
Cáceres Cánovas Córdova Dávila Gálvez Girón Gascón Morán Barragán Alarcón Aragón Colón Cerdán Jordán Julián Adán Germán
Farfán Luján Villalón Bazán Terán Tristán Sebastián Cebrián Albarrán Zaldívar Narváez Peláez Páez Báez Laínez Ordóñez
Antúnez Fernán Güell Pérez Bolívar Céspedes Míguez Bárcena Rodón Capdevila Juárez Chávez Ordóñez Yagüe Agüero Argüelles
Agüera Sanjuán Sanmartín Santamaría Rubén Zurbarán Quirós Solís Quílez Ródenas Mármol Fábregas Fábrega
Cuéllar Tévar Escámez Almodóvar Bécquer Azcárate Zárate Arévalo Ávalos Álamo Úbeda Árbol Íñiguez Íñigo
Garcés Arnáiz Sáinz Montón Borrás Ferrándiz Hernándiz Fernándiz Pérez Mínguez Diéguez Rodrígues Gonzálvez
Garví Martí Mulé Pallarés Cervelló Feliú Subirá Abellán Catalán Guzmán Santillán Sultán Blázquez""".split()
MAPA = {clave(a): a for a in TILDES}
AGUDOS_EZ = {"jerez", "cortez", "valdez", "ortez", "alférez"}
TILDE = dict(zip("aeiou", "áéíóú"))

def tilde_ez(p):
    """Los patronímicos en -ez son llanos: Blazquez → Blázquez, Dieguez → Diéguez."""
    m = re.fullmatch(r"(.*?)([aeiou])((?:qu|gu|[^aeiou])*)ez", p.lower())
    if not m or p.lower() in AGUDOS_EZ or not re.search(r"[a-zñ]", m.group(1) + m.group(3)): return p
    q = m.group(1) + TILDE[m.group(2)] + m.group(3) + "ez"
    return q[0].upper() + q[1:]
MINUS = {"DE", "DEL", "LA", "LAS", "LOS", "Y", "I"}

def bonito(s):
    partes = []
    for i, p in enumerate(s.split()):
        if p in MINUS and i: partes.append(p.lower()); continue
        p2 = "-".join(x.capitalize() for x in p.split("-"))
        partes.append(MAPA.get(clave(p2)) or (tilde_ez(p2) if "-" not in p2 else p2))
    return " ".join(partes)

filas = []
with open(FUENTES / "apellidos_ine.csv", encoding="utf-8") as f:
    for ap, n in csv.reader(f, delimiter=";"):
        n = int(n)
        filas.append((bonito(ap), [], nivel_por_umbral(n, [150000, 30000, 5000, 700]), n))
guarda("apellidos", filas, "personas_primer_apellido")
