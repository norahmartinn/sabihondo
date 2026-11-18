"""Descarga los datos en bruto de la octava tanda (semana del 16 al 22 de noviembre de 2026) a datos/siete/fuentes/t8/.
Mismo sistema que baja_tanda5.py (QLever y, si falla, el servicio oficial de Wikidata). Se puede relanzar: lo bajado no se vuelve a pedir."""
from comun import *
import baja_tanda4 as b4
import baja_tanda5 as b5
D8 = FUENTES / "t8"; D8.mkdir(exist_ok=True)
b5.D5 = D8
q = b4.q
CONSULTAS = {
 "portugal":    q("{ ?x wdt:P31 wd:Q13217644 } UNION { ?x wdt:P31/wdt:P279* wd:Q515 ; wdt:P17 wd:Q45 }"),
 "andalucia":   q("?x wdt:P31 wd:Q2074737 ; wdt:P131+ wd:Q5783 ."),
 "perros":      q("?x wdt:P31 wd:Q39367 ."),
 "realmadrid":  q("?x wdt:P31 wd:Q5 ; wdt:P54 wd:Q8682 ."),
 "rios":        q("?x wdt:P31/wdt:P279* wd:Q4022 ; wdt:P17 wd:Q29 ."),
 "museos":      q("?x wdt:P31/wdt:P279* wd:Q33506 ; wikibase:sitelinks ?s0 . FILTER(?s0 > 14)"),
 "euskadi":     b4.PRE + """SELECT ?x (SAMPLE(?es) AS ?xLabel) (SAMPLE(?e) AS ?en) (SAMPLE(?l) AS ?links) (GROUP_CONCAT(DISTINCT ?alt;separator="|") AS ?alts) WHERE {
  ?x wdt:P31 wd:Q2074737 ; wdt:P131+ wd:Q3995 ; wikibase:sitelinks ?l .
  OPTIONAL { ?x rdfs:label ?es FILTER(LANG(?es)="es") }
  OPTIONAL { ?x rdfs:label ?e FILTER(LANG(?e)="eu") }
  OPTIONAL { ?x skos:altLabel ?alt FILTER(LANG(?alt)="es" || LANG(?alt)="eu") }
} GROUP BY ?x""",
 "amenazados_animales": q("VALUES ?st { wd:Q11394 wd:Q219127 wd:Q278113 } ?x wdt:P141 ?st ; wdt:P171+ wd:Q729 ; wikibase:sitelinks ?s0 . FILTER(?s0 > 9)"),
 "amenazados":  q("VALUES ?st { wd:Q11394 wd:Q219127 wd:Q278113 } ?x wdt:P141 ?st ; wikibase:sitelinks ?s0 . FILTER(?s0 > 9)"),
}
if __name__ == "__main__":
    for n, c in CONSULTAS.items(): b5.sparql(n, c)
