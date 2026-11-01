"""«Nombra uno de los 1.000 nombres más comunes del mundo» (tanda 6).
La lista es de Norah (datos/siete/fuentes/t6/nombres_mundo.txt, con los puntos que traía). Los niveles se rehacen
pensando en alguien de España: lo español y lo que todo el mundo conoce, abajo; lo que aquí casi nadie diría, arriba.
    python3 nombres_mundo.py   → datos/siete/nombres_mundo.csv"""
import csv
from pathlib import Path
from comun import clave

RAIZ = Path(__file__).resolve().parents[2]
FUENTE = RAIZ / "datos/siete/fuentes/t6/nombres_mundo.txt"
SALIDA = RAIZ / "datos/siete/nombres_mundo.csv"
sp = lambda t: set(t.split())
# los más puestos en España (INE): lo primero que sale
N1 = sp("Maria Jose Juan Antonio Manuel Francisco David Carmen Javier Daniel Carlos Jesus Miguel Ana Laura Isabel Pedro "
        "Alejandro Pablo Luis Sergio Marta Cristina Lucia Elena Sara Paula Rafael Fernando Jorge Angel Mario Andrea Patricia Rosa")
# otros nombres españoles corrientes y los internacionales que conoce cualquiera
N2 = sp("Raul Alberto Diego Adrian Marcos Martin Lucas Hugo Alex Ivan Victor Ruben Oscar Enrique Ramon Teresa Silvia Beatriz "
        "Raquel Eva Irene Claudia Natalia Monica Sandra Julia Sofia Alicia Clara Mercedes Dolores Rosario Josefa Francisca Antonia "
        "Manuela Juana Susana Nicolas Tomas Roberto Ricardo Eduardo Alfredo Gabriel Samuel Rodrigo Guillermo Felipe Salvador Vicente "
        "Julio Arturo Hector Lorena Lidia Esther Ester Marina Andres Cecilia Gloria Martina Valentina Daniela Carolina Victoria Emma "
        "Angela Miriam Yolanda Margarita Luz Veronica Mariana Gabriela Vanessa Jaime Joan Mohamed Fatima Omar Ahmed Ali "
        "John Michael Peter Paul Mary James William Robert Sarah George Thomas Richard Charles Elizabeth Jennifer Jessica Kevin "
        "Christian Cristian Anna Alexander Jack Joseph Steven Patrick Mark Lisa Linda Emily Sophie Nicole Michelle Julio Ernesto "
        "Gustavo Armando Eduardo Fabio Bruno Marco Leonardo Giuseppe Giovanni Pierre Jacques Hans Vladimir Olga Natalia Elena")
# de la lista de +85, los que en España sí suenan
SUENAN = sp("Gerardo Gilberto Josefina Luciano Rodolfo Santos Elvira Raimundo Nestor Paola Joaquim Joao Igor Olivier Monika "
            "Christophe Thierry Pavel Oleg Mehmet Ahmet Hiroshi Kenji Sabina Nathalie Martine Marianne Chantal Brigitte Sylvie "
            "Aleksandra Alexandre Andrei Dmitry Ekaterina Konstantin Kirill Mamadou Moussa Fatoumata Aicha Nour Salma Said Amin "
            "Yousef Karin Sabine Werner Heinz Manfred Tomasz Piotr Katarzyna Galina Oksana Natalya Mercy")
# de la de +60, los que en España casi nadie diría
RAROS = sp("Ajay Amit Arjun Deepak Ganesh Kamala Lakshmi Rajesh Rama Sanjay Sunil Sunita Uma Vijay Eunice Hilda Khadija "
           "Ayesha Iman Imran Umar Yusuf Zahra Ilya Mikhail Sergey Svetlana Tatyana Helga Nguyen")
# la cola: nombres chinos compuestos, vietnamitas, birmanos, sílabas sueltas y nombres que aquí no conoce nadie
N5 = sp("Krzysztof Chunhua Chunyan Dongmei Guohua Guoliang Guoqiang Haibo Haitao Haiyan Haiying Hongmei Hongwei Hongyan Huimin "
        "Jianfeng Jianguo Jianhua Jianhui Jianjun Jianmin Jianming Jianping Jianwei Jianxin Jianzhong Jingjing Jinhua Junjie Lihong "
        "Lihua Lijuan Lijun Liming Lingling Liping Lixin Liying Qinghua Shanshan Tingting Weidong Weihua Weimin Weiming Weiping Weiwei "
        "Wenjie Wenjing Wenjun Xiaodong Xiaofeng Xiaohong Xiaohua Xiaohui Xiaojun Xiaoli Xiaolin Xiaoling Xiaomei Xiaomin Xiaoming "
        "Xiaoping Xiaoqing Xiaowei Xiaoxia Xiaoyan Xiaoying Xiaoyu Xuemei Yanhong Yanhua Yanling Yanping Yanyan Yingying Yuanyuan Yuhua "
        "Yumei Yuping Zhenhua Zhigang Zhihong Zhihua Zhihui Zhijian Zhijun Zhiming Zhiping Zhiqiang Zhiwei Zhiyong "
        "Anh Dung Hieu Hoa Hoang Huong Huy Linh Ngoc Nga Phuong Thanh Thao Thu Thuy Trang Tuan Tien "
        "Aung Kyaw Myat Phyo Zaw Lwin Than Tun Zin Wai Ei "
        "A O Ca Ka Pa Ta Ma Na Le Mi Ni Di Tu Ha Om Smt Masmaat Nushi Laoshi Munni Basanti Kamla Sumitra Urmila Shakuntala Savitri "
        "Pramila Punam Saroj Renu Kassa Tadesse Bekele Adamu Aliyu Abdullahi Abubakar Sani Gul Bibi Lal Naseem Sharmin Farzana Nusrat "
        "Sadia Samina Masoumeh Fatemeh Seyyed Lyudmyla Olha Halyna Vasylyi Nykolai Vladymyr Serhei Maryia Kseniya Qiong Qun Rong Shuang")
# cómo se escribe en español, y otras formas de decirlo
TILDE = {"Maria":"María", "Jose":"José", "Jesus":"Jesús", "Lucia":"Lucía", "Angel":"Ángel", "Raul":"Raúl", "Adrian":"Adrián",
  "Martin":"Martín", "Ivan":"Iván", "Victor":"Víctor", "Ruben":"Rubén", "Oscar":"Óscar", "Ramon":"Ramón", "Monica":"Mónica",
  "Sofia":"Sofía", "Nicolas":"Nicolás", "Tomas":"Tomás", "Hector":"Héctor", "Andres":"Andrés", "Veronica":"Verónica",
  "Angela":"Ángela", "Fatima":"Fátima", "Cesar":"César", "Angelica":"Angélica", "Joao":"João", "Nestor":"Néstor",
  "Francois":"François", "Rene":"René", "Elias":"Elías", "Ines":"Inés", "Ayse":"Ayşe", "Lucas":"Lucas"}
ALIAS = {"Mohamed": "Mohammed|Muhammad|Mohamad|Mahoma", "Krzysztof": "Krystof", "Joao": "Joao", "Elizabeth": "Elisabeth",
  "Alexander": "Alexandr", "Dmitry": "Dmitri|Dimitri", "Sergey": "Serguei|Sergei", "Aleksandr": "Aleksander", "Mikhail": "Mijail",
  "Yuriy": "Yuri", "Andrey": "Andrei", "Evgeniy": "Yevgeny|Evgeny", "Ekaterina": "Yekaterina", "Natalya": "Natalia"}
filas, puntos = [], None
for linea in FUENTE.read_text(encoding="utf-8").splitlines():
    linea = linea.strip()
    if not linea or linea.startswith("#"): continue
    if linea.startswith("["): puntos = int(linea[1:-1]); continue
    n = linea
    if n in N1: nv = 1
    elif n in N2: nv = 2
    elif n in N5: nv = 5
    elif puntos == 85: nv = 3 if n in SUENAN else 4
    elif n in RAROS: nv = 4
    else: nv = 3
    filas.append((TILDE.get(n, n), [n] + [a for a in ALIAS.get(n, "").split("|") if a], nv))
# un alias que es también un nombre de la lista no se usa: ese nombre va con su propia entrada
propios = {clave(n) for n, _, _ in filas} | {clave(a[0]) for _, a, _ in filas}
vistos = set()
with open(SALIDA, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=";"); w.writerow(["respuesta", "alias", "nivel", "orden_a_mano"])
    orden = 10**9
    for nombre, al, nv in sorted(filas, key=lambda f: f[2]):
        k = clave(nombre)
        if k in vistos: continue
        al = [a for a in dict.fromkeys(al) if clave(a) and clave(a) != k and clave(a) not in vistos and (a == al[0] or clave(a) not in propios)]
        vistos.add(k); vistos.update(clave(a) for a in al)
        w.writerow([nombre, "|".join(al), nv, orden]); orden -= 1
print(SALIDA.name, len(filas), "nombres")
