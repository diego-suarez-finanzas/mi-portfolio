import streamlit as st
import pandas as pd

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
    # PESTAÑA 1: HOJA DE VIDA
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

    # Sección de Propuesta Freelance y Contacto (Visible en el encabezado)
col_info1, col_info2 = st.columns([2, 1])

with col_info1:

    st.image("outputs/diego_suarez.jpg", width=250)

    st.info("🌐 **Servicios Profesionales Freelance:** Ofrezco soluciones estratégicas en **Análisis Financiero** y **Marketing Digital** adaptadas a empresas y emprendimientos en cualquier país de Latinoamérica de forma remota.")

with col_info2:
    st.link_button("📬 Escríbeme un Correo", "mailto:suarezt.diegof@gmail.com", use_container_width=True)

    st.markdown("---")
    st.markdown("<h2 style='font-size: 26px;'>💼 Experiencia Estratégica y Casos de Éxito</h2>", unsafe_allow_html=True)
    col_c1, col_c2 = st.columns(2)
    with col_c1:
            
        with st.container(border=True):
            st.image("outputs/diego_suarez.png", use_container_width=True)

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
    with tab_graphics:
    st.markdown("<h2 style='font-size: 26px;'>🌱 Panel de Control y Rendimiento AgroTech</h2>", unsafe_allow_html=True)
    st.markdown("Visualización completa de indicadores financieros, flujos de caja y proyecciones de cultivos automatizados.")
    st.markdown("---")
    
    # ----------------------------------------------------
    # FILA 1: Comparativos de Capital y Control Operativo
    # ----------------------------------------------------
    f1_col1, f1_col2 = st.columns(2)
    
    with f1_col1:
        with st.container(border=True):
            st.markdown("### 📊 Comparativos de Capital")
            # Ojo: Tu archivo tiene una doble extensión ".png.png" según la imagen
            st.image("outputs/Comparativos de Capital (Dupont vs WACC)png.png", use_container_width=True)
            st.caption("Análisis DuPont estructurado frente al Costo Promedio Ponderado de Capital (WACC).")

    with f1_col2:
        with st.container(border=True):
            st.markdown("### 🎛️ Control Operativo")
            st.image("outputs/Control Operativo y Proyección Interactiva.png", use_container_width=True)
            st.caption("Monitoreo de variables de producción y proyecciones interactivas.")

    # ----------------------------------------------------
    # FILA 2: Evolución Temporal y Valoración Avanzada
    # ----------------------------------------------------
    f2_col1, f2_col2 = st.columns(2)
    
    with f2_col1:
        with st.container(border=True):
            st.markdown("### 📉 Evolución Temporal")
            st.image("outputs/Evolución Temporal del Semestre.png", use_container_width=True)
            st.caption("Comportamiento histórico y tendencias financieras a lo largo del periodo.")

    with f2_col2:
        with st.container(border=True):
            st.markdown("### 💎 Valoración Avanzada")
            st.image("outputs/Módulo de Valoración Avanzada.png", use_container_width=True)
            st.caption("Modelado robusto para la evaluación de activos e indicadores de rendimiento.")

    # ----------------------------------------------------
    # FILA 3: Portafolio de Cultivos y Hoja de Vida Gráfica
    # ----------------------------------------------------
    f3_col1, f3_col2 = st.columns(2)
    
    with f3_col1:
        with st.container(border=True):
            st.markdown("### 🌾 Portafolio de Cultivos")
            # Nota: El nombre en tu imagen termina en tres puntos, asegúrate de escribirlo idéntico o renombrarlo
            st.image("outputs/Portafolio Cultivos Complementarios y Mitigación ...", use_container_width=True)
            st.caption("Estrategia de diversificación agrícola y mitigación de riesgos financieros.")

    with f3_col2:
        with st.container(border=True):
            st.markdown("### 📄 Hoja de Vida Resumida")
            st.image("outputs/Hoja de Vida Diego.png", use_container_width=True)
            st.caption("Infografía ejecutiva con trayectoria, habilidades clave y logros.")

    # Cierre del módulo analítico interactivo
    st.area_chart(datos_meses)
