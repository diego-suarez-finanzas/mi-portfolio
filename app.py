import streamlit as st

# Configuración de la plataforma web en modo ancho
st.set_page_config(
    page_title="Portfolio Profesional - Diego Fernando Suárez",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Título de impacto del sitio web público
st.markdown("<h1 style='font-size: 38px;'>🚀 PORTFOLIO PROFESIONAL E INTERACTIVO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-size: 24px;'><b>Diego Fernando Suárez Toscano</b> | Consultor Financiero & Programador Analítico</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 18px; color: #b2bec3;'>📍 Distrito Capital, Colombia | ✉️ suarezt.diegof@gmail.com</p>", unsafe_allow_html=True)
st.markdown("---")

# Sistema de pestañas para dividir el Currículum de las Gráficas
tab_cv, tab_graphics = st.tabs(["👔 Currículum Vitae Ejecutivo", "📊 Simulador Analítico AgroTech"])

with tab_cv:
    # -------------------------------------------------------------
    # PESTAÑA 1: TU HOJA DE VIDA OPTIMIZADA
    # -------------------------------------------------------------
    st.markdown("<h2 style='font-size: 26px;'>🎯 Perfil Profesional</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 19px; line-height: 1.6;'>Consultor financiero senior y desarrollador de software "
        "especializado en el ecosistema corporativo e industrial. Experto en transformar datos transaccionales "
        "crudos en Web Apps analíticas interactivas de alto rendimiento. Dominio avanzado de modelos de valoración "
        "institucional (DuPont, ROIC, WACC, VAN/TIR), optimización de procesos mediante Inteligencia Artificial y "
        "arquitectura de datos aplicada a la toma de decisiones estratégicas de alta gerencia.</p>", 
        unsafe_allow_html=True
    )
    st.markdown("---")

    st.markdown("<h2 style='font-size: 26px;'>💼 Experiencia Estratégica y Casos de Éxito</h2>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        with st.container(border=True):
            st.markdown("<h3 style='font-size: 22px;'>🥬 Proyecto Ancla: AgroTech DF-Colombia S.A.S.</h3>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 16px; color: #e67e22;'><b>Rol:</b> Arquitecto Financiero y Desarrollador Líder</p>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("<ul style='font-size: 17px; line-height: 1.5;'>"
                        "<li><b>Automatización Analítica:</b> Creación de aplicaciones web interactivas (Python + Streamlit) para control operativo.</li>"
                        "<li><b>Modelado Avanzado:</b> Implementación del despiece del Sistema DuPont, ROIC y mitigación de riesgo de portafolio dual.</li>"
                        "<li><b>Simulación Predictiva:</b> Diseño de motores predictivos a 5 años (VAN de $105,168.29 USD y TIR de 84.11%) para blindar caja.</li>"
                        "</ul>", unsafe_allow_html=True)
    with col_c2:
        with st.container(border=True):
            st.markdown("<h3 style='font-size: 22px;'>⚡ Americana de Energía SAS ESP</h3>", unsafe_allow_html=True)
            st.markdown("<p style='font-size: 16px; color: #3498db;'><b>Rol:</b> Consultor Senior en Estrategia de Inversión</p>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("<ul style='font-size: 17px; line-height: 1.5;'>"
                        "<li><b>Optimización de Activos:</b> Análisis financiero avanzado frente a sistemas híbridos y vectores energéticos emergentes.</li>"
                        "<li><b>Evaluación de Proyectos:</b> Modelado global de CAPEX/OPEX en el ecosistema energético colombiano (TIR del 11.5% al 16.8%).</li>"
                        "<li><b>Mitigación de Riesgos:</b> Estructuración de matrices DOFA equilibradas y narrativas de viabilidad para mesas de inversión.</li>"
                        "</ul>", unsafe_allow_html=True)

    st.markdown("")
    with st.container(border=True):
        st.markdown("<h3 style='font-size: 22px;'>🏢 Conserse Ltda. (Consultores en Servicios y Seguros)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 16px; color: #9b59b6;'><b>Rol:</b> Asistente de IA e Informática Operativa</p>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("<ul style='font-size: 17px; line-height: 1.5;'>"
                    "<li><b>Optimización de Procesos:</b> Diseño e implementación de herramientas de IA aplicadas a la eficiencia operativa interna.</li>"
                    "<li><b>Marketing de Rendimiento:</b> Automatización de flujos de datos comerciales y analítica de conversión para el sector.</li>"
                    "</ul>", unsafe_allow_html=True)

with tab_graphics:
    # -------------------------------------------------------------
    # PESTAÑA 2: GRÁFICOS Y ANÁLISIS FINANCIERO DE AGROTECH
    # -------------------------------------------------------------
    st.markdown("<h2 style='font-size: 26px;'>📊 Cuadro de Mando Integral - AgroTech Semestral</h2>", unsafe_allow_html=True)
    
    f1_col1, f1_col2 = st.columns(2)
    
    with f1_col1:
        with st.container(border=True):
            st.markdown("### ### 📊 Comparativos de Rentabilidad")
            datos_capital = {
                "ROE (Patrimonio)": -64.23,
                "ROA (Activos)": -64.23,
                "ROIC (Capital)": -41.75,
                "WACC (Meta)": 7.50
            }
            st.bar_chart(datos_capital)
            st.caption("Análisis DuPont y Costo de Capital Aplicado")
            
    with f1_col2:
        with st.container(border=True):
            st.markdown("### 📊 Control Operativo Semestral")
            datos_meses = {
                "Enero": -6710.44, 
                "Febrero": 1121.92, 
                "Marzo": -8422.25, 
                "Abril": -7346.33, 
                "Mayo": 1120.06, 
                "Junio": -5038.48
            }
            st.area_chart(datos_meses)
            st.caption("Monitoreo de Flujo de Caja e Indicadores Dinámicos")
