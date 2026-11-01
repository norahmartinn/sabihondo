"""«Nombra una de las 100 mejores empresas para trabajar en España en 2026, según Forbes» (tanda 6).
Lista de forbes.es/listas/916499 (13 may 2026; gana JTI y el resto va por orden alfabético). Niveles a mano,
pensando en lo conocida que es la marca en España; alias con las formas de llamarlas.
    python3 forbes_empresas.py   → datos/siete/forbes_empresas.csv"""
import csv
from pathlib import Path
from comun import clave

SALIDA = Path(__file__).resolve().parents[2] / "datos/siete/forbes_empresas.csv"
EMPRESAS = {   # nombre en la lista: (nivel, alias)
 "Inditex": (1, "Zara"), "BBVA": (1, ""), "Mango": (1, ""), "Mahou San Miguel": (1, "Mahou|San Miguel"), "Decathlon": (1, ""),
 "Leroy Merlin España": (1, "Leroy Merlin"), "Endesa": (1, ""), "Deloitte España": (1, "Deloitte"), "Bosch": (1, ""),
 "Accenture": (2, ""), "AXA Seguros": (2, "AXA"), "Allianz Seguros": (2, "Allianz"), "Mutua Madrileña": (2, "Mutua"),
 "Sanitas": (2, ""), "Meliá Hoteles": (2, "Meliá|Meliá Hotels|Melia Hotels International"), "KPMG": (2, ""),
 "PwC": (2, "PricewaterhouseCoopers|Price"), "EY (Ernst & Young) España": (2, "EY|Ernst & Young|Ernst and Young"),
 "Procter & Gamble": (2, "P&G|Procter|Procter and Gamble"), "Danone Iberia": (2, "Danone"), "HP": (2, "Hewlett-Packard|Hewlett Packard"),
 "ING": (2, "ING Direct"), "DHL Supply Chain Iberia": (2, "DHL"), "eDreams Odigeo": (2, "eDreams|Odigeo"),
 "Línea Directa": (2, "Línea Directa Aseguradora"), "Grupo Iberostar": (2, "Iberostar"), "Pastas Gallo": (2, "Gallo"),
 "Freixenet": (2, "Freixenet S.A."), "Raventós Codorníu": (2, "Codorníu|Raventós"), "Verisure España": (2, "Verisure"),
 "Quirónsalud": (2, "Quirón|Quiron Salud"), "Movistar Prosegur Alarmas": (2, "Movistar Prosegur"), "Prosegur": (2, ""),
 "Masorange": (2, "MasOrange|Orange|MásMóvil|Masmovil"), "Moeve": (2, "Cepsa"), "Vorwerk España": (2, "Vorwerk|Thermomix"),
 "Novartis": (3, ""), "Bayer Group Iberia": (3, "Bayer"), "Oracle Ibérica": (3, "Oracle"), "Santalucía": (3, "Santa Lucía"),
 "Generali Group Spain": (3, "Generali"), "Ilunion": (3, ""), "DKV": (3, "DKV Seguros"), "Engel & Völkers": (3, "Engel Völkers|Engel and Völkers"),
 "NTT Data": (3, "NTT|everis"), "AstraZeneca Spain Farmacéutica": (3, "AstraZeneca"), "GSK España": (3, "GSK|GlaxoSmithKline"),
 "Sanofi": (3, ""), "JTI": (3, "Japan Tobacco International|Japan Tobacco"), "Grupo Cosentino": (3, "Cosentino|Silestone"),
 "ISDIN": (3, ""), "Bon Preu": (3, "Bonpreu|Esclat"), "Ametller Origen": (3, "Ametller"), "Feu Vert Ibérica": (3, "Feu Vert"),
 "Takeda Pharmaceutical Iberia": (3, "Takeda"), "Haleon España": (3, "Haleon"), "Schneider Electric Iberia": (3, "Schneider Electric|Schneider"),
 "Tata Consultancy Services": (3, "TCS|Tata"), "Ogilvy": (3, ""), "Reale Seguros": (3, "Reale"), "Aegon Seguros": (3, "Aegon"),
 "Nationale Nederlanden": (3, "Nationale-Nederlanden|NN"), "Minor Hotels": (3, "NH Hotels|NH|Minor"), "Palladium Hotel Group": (3, "Palladium"),
 "TK Elevator": (3, "thyssenkrupp Elevator|Thyssen"), "Pierre Fabre Ibérica": (3, "Pierre Fabre|Avène"),
 "CBRE": (4, ""), "Avoris": (4, "Ávoris|Barceló Viajes"), "B. Braun Group": (4, "B. Braun|B Braun|Braun"), "Covestro": (4, ""),
 "GE Healthcare Iberia": (4, "GE Healthcare"), "Cigna Healthcare": (4, "Cigna"), "Ayesa": (4, ""), "Lyreco Iberia": (4, "Lyreco"),
 "Telpark": (4, ""), "T-Systems Iberia": (4, "T-Systems"), "Kyndryl": (4, ""), "Celonis": (4, ""), "DXC Technology Iberia": (4, "DXC|DXC Technology"),
 "Seidor": (4, ""), "Softtek": (4, ""), "Dräger Hispania": (4, "Dräger|Drager"), "ESIC University": (4, "ESIC"),
 "GMV": (4, ""), "Grupo Oesia": (4, "Oesía|Oesia"), "LLYC": (4, "Llorente y Cuenca|Llorente & Cuenca"), "Hiberus": (4, ""),
 "Serveo": (4, "Ferrovial Servicios"), "Sesé": (4, "Grupo Sesé"), "PreZero Iberia": (4, "PreZero"), "Steelcase Iberia": (4, "Steelcase"),
 "GXO": (4, "GXO Logistics"), "Econocom (Grupo)": (4, "Econocom"), "Arup": (4, ""),
 "Domingo Alonso Group": (5, "Domingo Alonso"), "AQ Acentor": (5, "Acentor"), "Salesland": (5, ""), "Qaracter": (5, ""),
 "Jungle": (5, ""), "World Tech Enterprises": (5, "WTE"),
}
assert len(EMPRESAS) == 100, len(EMPRESAS)
vistos = set()
with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";"); w.writerow(["respuesta", "alias", "nivel", "orden_a_mano"])
    for orden, (n, (nv, al)) in enumerate(sorted(EMPRESAS.items(), key=lambda x: x[1][0])):
        al = [a for a in al.split("|") if a and clave(a) not in vistos and clave(a) != clave(n)]
        vistos.add(clave(n)); vistos.update(clave(a) for a in al)
        w.writerow([n, "|".join(al), nv, 10**9 - orden])
print(SALIDA.name, len(EMPRESAS))
