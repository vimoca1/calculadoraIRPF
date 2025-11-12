
import streamlit as st
from typing import List, Tuple, Dict, Optional

st.set_page_config(page_title="Calculadora IRPF + PPES · CCAA 2025", page_icon="💶", layout="wide")

STATE_2025: List[Tuple[Optional[float], float]] = [
    (12450, 9.5),
    (20200, 12.0),
    (35200, 15.0),
    (60000, 18.5),
    (300000, 22.5),
    (None, 24.5),
]

CCAA_AUTON_2025: Dict[str, List[Tuple[Optional[float], float]]] = {
    "Andalucía": [
        (12450, 9.5),(13000, 9.5),(20200, 12.0),(21000, 12.0),(35200, 15.0),
        (50000, 18.5),(60000, 22.5),(300000, 22.5),(None, 22.5),
    ],
    "Aragón": [
        (12450, 9.5),(13972.5, 9.5),(20200, 12.0),(21210, 12.0),(35200, 15.0),
        (36960, 15.0),(52500, 18.5),(60000, 20.5),(80000, 23.0),(90000, 24.0),
        (130000, 25.0),(300000, 25.5),(None, 25.5),
    ],
    "Principado de Asturias": [
        (12450, 10.0),(17707, 12.0),(20200, 14.0),(33007, 14.0),(35200, 18.5),
        (53407, 18.5),(60000, 21.5),(70000, 21.5),(90000, 22.5),(175000, 25.0),
        (300000, 25.5),(None, 25.5),
    ],
    "Illes Balears": [
        (10000, 9.0),(12450, 11.25),(18000, 11.25),(20200, 14.25),(30000, 14.25),
        (35200, 17.5),(48000, 17.5),(60000, 19.0),(70000, 19.0),(90000, 21.75),
        (120000, 22.75),(175000, 23.75),(300000, 24.75),(None, 24.75),
    ],
    "Canarias": [
        (12450, 9.0),(17707, 11.5),(20200, 14.0),(33007, 14.0),(35200, 18.5),
        (53407, 18.5),(60000, 23.5),(90000, 23.5),(120000, 25.0),(300000, 26.0),
        (None, 26.0),
    ],
    "Cantabria": [
        (12450, 8.5),(13000, 8.5),(20200, 11.0),(21000, 11.0),(35200, 14.5),
        (60000, 18.0),(90000, 22.5),(300000, 24.5),(None, 24.5),
    ],
    "Castilla-La Mancha": [
        (12450, 9.5),(20200, 12.0),(35200, 15.0),(60000, 18.5),(300000, 22.5),
        (None, 22.5),
    ],
    "Castilla y León": [
        (12450, 9.0),(20200, 12.0),(35200, 14.0),(53407, 18.5),(60000, 21.5),
        (300000, 21.5),(None, 21.5),
    ],
    "Cataluña": [
        (12450, 10.5),(17707, 12.0),(20200, 14.0),(21000, 14.0),(33007, 15.0),
        (35200, 18.8),(53407, 18.8),(60000, 21.5),(90000, 21.5),(120000, 23.5),
        (175000, 24.5),(300000, 25.5),(None, 25.5),
    ],
    "Comunidad de Madrid": [
        (12450, 8.5),(13362, 8.5),(19004, 10.7),(20200, 12.8),(35200, 12.8),
        (35425, 12.8),(57320, 17.4),(60000, 20.5),(300000, 20.5),(None, 20.5),
    ],
    "Extremadura": [
        (12450, 8.0),(20200, 10.0),(24200, 16.0),(35200, 17.5),(60000, 21.0),
        (80200, 23.5),(99200, 24.0),(120200, 24.5),(300000, 25.0),(None, 25.0),
    ],
    "Comunidad Valenciana": [
        (12000, 9.0),(12450, 12.0),(20200, 12.0),(22000, 12.0),(32000, 15.0),
        (35200, 17.5),(42000, 17.5),(52000, 20.0),(65000, 22.5),(72000, 25.0),
        (100000, 26.5),(150000, 27.5),(200000, 28.5),(300000, 29.5),(None, 29.5),
    ],
    "Galicia": [
        (12450, 9.0),(12985, 9.0),(20200, 11.65),(21068, 11.65),(35200, 14.9),
        (47600, 18.4),(60000, 22.5),(300000, 22.5),(None, 22.5),
    ],
    "La Rioja": [
        (12450, 8.0),(20200, 10.6),(35200, 13.6),(40000, 17.8),(50000, 18.5),
        (60000, 19.0),(120000, 24.5),(300000, 27.0),(None, 27.0),
    ],
    "Región de Murcia": [
        (12450, 9.5),(20200, 11.2),(34000, 13.3),(35200, 17.9),(60000, 17.9),
        (300000, 22.5),(None, 22.5),
    ],
}

CCAA_LIST = sorted(CCAA_AUTON_2025.keys())

MIN_EST = {
    "personal": {"base": 5550, "mas65": 1150, "mas75": 1400},
    "desc": {"primero": 2400, "segundo": 2700, "tercero": 4000, "cuarto_y_sig": 4500, "menor3": 2800},
    "asc": {"mas65": 1150, "mas75": 1400},
    "disc": {"33": 3000, "65": 9000, "ayuda": 3000}
}

MIN_AUTON = {
    "Andalucía": {
        "personal": {"base": 5790, "mas65": 1200, "mas75": 1460},
        "desc": {"primero": 2510, "segundo": 2820, "tercero": 4170, "cuarto_y_sig": 4700, "menor3": 2920},
        "asc": {"mas65": 1200, "mas75": 1460},
        "disc": {"33": 3130, "65": 9390, "ayuda": 3130},
    },
    "Illes Balears": {
        "personal": {"base": 5550, "mas65": 1265, "mas75": 1540},
        "desc": {"primero": 2400, "segundo": 2970, "tercero": 4400, "cuarto_y_sig": 4950, "menor3": 2800},
        "asc": {"mas65": 1265, "mas75": 1540},
        "disc": {"33": 3300, "65": 9900, "ayuda": 3300},
    },
    "Canarias": {
        "personal": {"base": 5606, "mas65": 1162, "mas75": 1414},
        "desc": {"primero": 2424, "segundo": 2727, "tercero": 4040, "cuarto_y_sig": 4545, "menor3": 2828},
        "asc": {"mas65": 1162, "mas75": 1414},
        "disc": {"33": 3030, "65": 9090, "ayuda": 3030},
    },
    "Castilla y León": "estatales",
    "Cataluña": "estatales",
    "Galicia": {
        "personal": {"base": 5789, "mas65": 1199, "mas75": 1460},
        "desc": {"primero": 2503, "segundo": 2816, "tercero": 4172, "cuarto_y_sig": 4694, "menor3": 2920},
        "asc": {"mas65": 1199, "mas75": 1460},
        "disc": {"33": 3129, "65": 9387, "ayuda": 3129},
    },
    "Comunidad de Madrid": {
        "personal": {"base": 5956.65, "mas65": 1234.26, "mas75": 1502.58},
        "desc": {"primero": 2575.85, "segundo": 2897.83, "tercero": 4400, "cuarto_y_sig": 4950, "menor3": 3005.16},
        "asc": {"mas65": 1234.26, "mas75": 1502.58},
        "disc": {"33": 3219.81, "65": 9659.44, "ayuda": 3219.81},
    },
    "La Rioja": {"extra_ayuda": 3000},
    "Comunidad Valenciana": {
        "personal": {"base": 6105, "mas65": 1265, "mas75": 1540},
        "desc": {"primero": 2640, "segundo": 2970, "tercero": 4400, "cuarto_y_sig": 4950, "menor3": 3080},
        "asc": {"mas65": 1265, "mas75": 1540},
        "disc": {"33": 3300, "65": 9900, "ayuda": 3300},
    }
}

def get_minimos(ccaa: str):
    cfg = MIN_AUTON.get(ccaa, "estatales")
    if cfg == "estatales":
        return {k: v.copy() if isinstance(v, dict) else v for k, v in MIN_EST.items()}
    base = {k: v.copy() if isinstance(v, dict) else v for k, v in MIN_EST.items()}
    if isinstance(cfg, dict):
        for k in ["personal","desc","asc","disc"]:
            if k in cfg and isinstance(cfg[k], dict):
                base[k].update(cfg[k])
        base["extra_ayuda"] = cfg.get("extra_ayuda", 0)
    return base

def aplicar_tarifa(base: float, tramos: List[Tuple[Optional[float], float]]) -> float:
    cuota = 0.0
    prev = 0.0
    rem = max(0.0, base)
    for limite, tipo in tramos:
        t = tipo / 100.0
        if limite is None:
            cuota += rem * t
            break
        tramo = min(rem, max(0.0, limite - prev))
        cuota += tramo * t
        rem -= tramo
        prev = limite
        if rem <= 0:
            break
    return cuota

def cuota_total(base_liquidable: float, ccaa: str) -> float:
    if base_liquidable <= 0: return 0.0
    auton = CCAA_AUTON_2025.get(ccaa, STATE_2025)
    return aplicar_tarifa(base_liquidable, STATE_2025) + aplicar_tarifa(base_liquidable, auton)

def minimo_total(ccaa: str, edad:int, hijos:int, menores3:int, asc65:int, asc75:int,
                 disc_contrib: str, disc_fam_33:int, disc_fam_65:int, ayuda_terceras: bool=False) -> float:
    m = get_minimos(ccaa)
    total = m["personal"]["base"]
    if edad >= 65: total += m["personal"]["mas65"]
    if edad >= 75: total += m["personal"]["mas75"]
    if hijos > 0:
        escalas = [m["desc"]["primero"], m["desc"]["segundo"], m["desc"]["tercero"]]
        if hijos > 3:
            escalas += [m["desc"]["cuarto_y_sig"]] * (hijos - 3)
        total += sum(escalas[:hijos])
        total += m["desc"]["menor3"] * min(menores3, hijos)
    total += m["asc"]["mas65"] * asc65
    total += m["asc"]["mas75"] * asc75
    if disc_contrib == "≥65%":
        total += m["disc"]["65"]
    elif disc_contrib == "≥33%":
        total += m["disc"]["33"]
    total += m["disc"]["33"] * disc_fam_33
    total += m["disc"]["65"] * disc_fam_65
    if ayuda_terceras and "extra_ayuda" in m:
        total += float(m["extra_ayuda"] or 0)
    return total

def anos_hasta_67(edad: int) -> int:
    return max(0, 67 - int(edad))

def tasa_asumida(edad: int) -> float:
    n = anos_hasta_67(edad)
    return 0.05 if n <= 10 else 0.07

def fv_aportaciones_anuales(aporte_anual: float, n: int, r: float) -> float:
    if n <= 0 or aporte_anual <= 0:
        return 0.0
    if r == 0:
        return aporte_anual * n
    return aporte_anual * (((1 + r) ** n - 1) / r)

st.title("💶 Calculadora de ahorro IRPF por aportación a PPES (España)")
st.caption("Escalas estatal y autonómicas (régimen común) 2025 + mínimos personales/familiares. Proyección de inversión hasta los 67 (5%/7%).")

left, right = st.columns([0.62, 0.38])

with left:
    st.subheader("Datos del contribuyente")
    situacion = st.selectbox("Situación laboral", ["Autónomo", "Autónomo + Asalariado"])
    ccaa = st.selectbox("Comunidad Autónoma de residencia", CCAA_LIST, index=CCAA_LIST.index("Comunidad de Madrid") if "Comunidad de Madrid" in CCAA_LIST else 0)
    declaracion = st.radio("Tipo de declaración", ["Individual", "Conjunta"], horizontal=True)
    edad = st.number_input("Edad", min_value=18, max_value=100, value=35, step=1)
    base_imponible = st.number_input("Base imponible general (todas tus rentas netas) €", min_value=0.0, value=45000.0, step=100.0, format="%.2f")
    aportacion = st.number_input("Aportación anual a PPES (€)", min_value=0.0, value=3000.0, step=100.0, format="%.2f")

    st.markdown("**Mínimos personales y familiares**")
    c1, c2 = st.columns(2)
    with c1:
        hijos = st.number_input("Nº hijos (<25 o con discapacidad)", min_value=0, max_value=10, value=0, step=1)
        menores3 = st.number_input("De ellos, <3 años", min_value=0, max_value=10, value=0, step=1)
        asc65 = st.number_input("Ascendientes ≥65 a cargo", min_value=0, max_value=5, value=0, step=1)
        asc75 = st.number_input("Ascendientes ≥75 (de los anteriores)", min_value=0, max_value=5, value=0, step=1)
    with c2:
        disc_contrib = st.selectbox("Discapacidad contribuyente", ["No", "≥33%", "≥65%"])
        disc_fam_33 = st.number_input("Familiares con discapacidad ≥33%", min_value=0, max_value=10, value=0, step=1)
        disc_fam_65 = st.number_input("Familiares con discapacidad ≥65%", min_value=0, max_value=10, value=0, step=1)
        ayuda = st.checkbox("Necesita ayuda de terceras personas / movilidad reducida (cuando proceda)", value=False)

    M = minimo_total(ccaa, int(edad), int(hijos), int(menores3), int(asc65), int(asc75),
                     disc_contrib, int(disc_fam_33), int(disc_fam_65), ayuda)

    tope_ppes = min(aportacion, 5750.0, 0.30 * base_imponible)

    BLG_sin = max(0.0, base_imponible)
    BLG_con = max(0.0, base_imponible - tope_ppes)

    base_tarifa_sin = max(0.0, BLG_sin - M)
    base_tarifa_con = max(0.0, BLG_con - M)

    cuota_sin = cuota_total(base_tarifa_sin, ccaa)
    cuota_con = cuota_total(base_tarifa_con, ccaa)
    ahorro = max(0.0, cuota_sin - cuota_con)

    n_years = anos_hasta_67(int(edad))
    r = tasa_asumida(int(edad))
    capital_jubilacion = fv_aportaciones_anuales(aportacion, n_years, r)

with right:
    st.subheader("Resultado (año actual)")
    st.metric("Tope fiscal PPES aplicable", f"{tope_ppes:,.2f} €")
    st.metric("Mínimos aplicados", f"{M:,.2f} €")
    st.metric("Base sujeta a tarifa (antes)", f"{base_tarifa_sin:,.2f} €")
    st.metric("Base sujeta a tarifa (después)", f"{base_tarifa_con:,.2f} €")
    st.metric("Ahorro IRPF estimado (año)", f"{ahorro:,.2f} €")

    st.divider()
    st.subheader("Proyección a jubilación (67 años)")
    st.metric("Años hasta 67", f"{n_years} años")
    st.metric("Rentabilidad asumida", f"{r*100:.2f}% anual")
    st.metric("Capital estimado a los 67", f"{capital_jubilacion:,.2f} €")
    st.caption("FV de aportación anual constante (no descuenta inflación ni variación salarial).")

st.divider()
with st.expander("Ver escalas usadas (2025)"):
    st.write("**Estatal (común)**:", STATE_2025)
    st.write(f"**Autonómica - {ccaa}**:", CCAA_AUTON_2025.get(ccaa))

st.caption("Cálculo orientativo. La liquidación real puede variar por deducciones específicas, familia numerosa, vivienda, etc.")
