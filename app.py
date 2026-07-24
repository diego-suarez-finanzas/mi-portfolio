import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (SEO Y KEYWORDS SE OCULTAN EN METADATOS)
st.set_page_config(
    page_title="Diego Suárez - Consultor Senior & Freelancer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para mejorar el diseño oscuro y las tarjetas
st.markdown("""
    <style>
    .keyword-tag {
        display: inline-block;
        background-color: #1E293B;
        color: #38BDF8;
        padding: 4px 10px;
        margin: 4px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        border: 1px solid #334155;
    }
    .text-highlight {
        color: #F59E0B;
        font-weight: bold;
    }
    /* Ocultar menú de desarrollo en producción para marca blanca */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 2. SISTEMA DE NAVEGACIÓN SIMPLIFICADO (Pestañas superiores de alto impacto)
tabs = st.tabs([
    "👤 Perfil Profesional", 
    "🌱 Simulador Analítico AgroTech", 
    "⚡ Vectores Emergentes Colombia"
])

# ==========================================
# PESTAÑA 1: PERFIL PROFESIONAL
# ==========================================
with tabs[0]:
    # Estructura en columnas para incluir tu foto (REQUERIMIENTO 2)
    col_foto, col_texto = st.columns([1, 3])
    
    with col_foto:
        try:
            st.image("diego_suarez.jpg", use_container_width=True)
        except:
            # Cuadro de respaldo si la foto no se encuentra en el directorio
            st.info("📸 Espacio para: diego_suarez.jpg")
            
    with col_texto:
        st.title("Perfil Profesional")
        
        # Texto de presentación potente
        st.markdown("""
        Consultor financiero senior y desarrollador de software especializado en el ecosistema corporativo e industrial. 
        Experto en transformar datos transaccionales crudos en Web Apps analíticas interactivas de alto rendimiento. 
        Dominio avanzado de modelos de valoración institucional (DuPont, ROIC, WACC, VAN/TIR), optimización de 
        procesos mediante Inteligencia Artificial y arquitectura de datos aplicada a la toma de decisiones estratégicas de alta gerencia.
        """)
        
        # Especificación de Servicios Freelancer (REQUERIMIENTO 1)
        st.markdown("""
        ---
        ### 🌍 Servicios Freelancer de Disponibilidad Inmediata
        Ofrezco mis servicios especializados como **Freelancer para cualquier país de Latinoamérica**. 
        Mi modalidad de trabajo está diseñada para la agilidad y necesidades de tu negocio:
        * ⏱️ **Contratación por Horas** (Soporte puntual, resolución de bugs o asesorías).
        * 📅 **Contratos Cortos por Entregables** (Desarrollo rápido de MVPs, dashboards o evaluaciones financieras).
        
        *¡Contáctame hoy mismo para acelerar tus proyectos estratégicos sin costos fijos a largo plazo!*
        """, unsafe_allow_html=True)

    # Bloque de Keywords para CEOs y Algoritmos de búsqueda (REQUERIMIENTO 3)
    st.markdown("### 🔍 Especialidades Técnicas y Estratégicas")
    keywords = [
        "Freelancer", "Analista Estratégico Senior", "Consultor de Business Intelligence [BI] (R y Python)", 
        "Análisis Financiero Online", "Marketing Digital", "Evaluación Financiera de Proyectos", 
        "Formulación de Proyectos", "Estrategia y Arquitectura de Datos", "Consultoría de Operaciones y Eficiencia"
    ]
    
    # Renderizado estético de etiquetas HTML para las palabras clave
    kw_html = "".join([f'<span class="keyword-tag">{kw}</span>' for kw in keywords])
    st.markdown(kw_html, unsafe_allow_html=True)
    
    # Sección de experiencia (Versión resumida para mantenerla corta)
    st.markdown("---")
    st.subheader("💼 Experiencia Estratégica y Casos de Éxito")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("**Proyecto Ancla: AgroTech DF-Colombia S.A.S.**")
        st.caption("Rol: Arquitecto Financiero y Desarrollador Líder")
    with col_p2:
        st.markdown("**Americana de Energía SAS ESP**")
        st.caption("Rol: Consultor Senior en Estrategia de Inversión")

# ==========================================
# PESTAÑA 2: SIMULADOR ANALÍTICO AGROTECH
# ==========================================
with tabs[1]:
    st.title("🌱 Simulador Analítico AgroTech")
    st.markdown("Visualización de las interfaces y módulos interactivos desarrollados para el sector agroindustrial.")
    
    # Galería de imágenes agtech_indoor (REQUERIMIENTO 4)
    # Mostramos 5 imágenes organizadas en un grid dinámico para que no ocupe demasiado espacio vertical
    col_ag1, col_ag2 = st.columns(2)
    
    # Diccionario con rutas ordenadas de forma secuencial
    agtech_images = [
        "outputs/agtech_indoor(1).png", 
        "outputs/agtech_indoor(2).png", 
        "outputs/agtech_indoor(3).png",
        "outputs/agtech_indoor(4).png", 
        "outputs/agtech_indoor(5).png"
    ]
    
    for idx, img_name in enumerate(agtech_images):
        # Alterna las capturas entre la columna izquierda y derecha
        target_col = col_ag1 if idx % 2 == 0 else col_ag2
        with target_col:
            try:
                st.image(img_name, caption=f"Módulo Analítico - Vista {idx+1}", use_container_width=True)
            except:
                st.warning(f"No se pudo cargar {img_name}")

# ==========================================
# PESTAÑA 3: VECTORES EMERGENTES MATRÍZ ENERGÉTICA
# ==========================================
with tabs[2]:
    # Nueva sección creada (REQUERIMIENTO 5)
    st.title("⚡ Vectores Emergentes Matríz Energética Colombia")
    st.markdown("Galería de reportes técnicos, modelos analíticos y matrices de evaluación del sector energético.")
    
    # Renderizado directo de las capturas (Word a PNG) sin procesamiento extra
    # Genera la lista consecutiva desde energias_limpias(2).png hasta energias_limpias(13).png
    col_en1, col_en2 = st.columns(2)
    
    for i in range(2, 14):
        img_name = f"outputs/energias_limpias({i}).png"
        target_col = col_en1 if i % 2 == 0 else col_en2
        with target_col:
            try:
                st.image(img_name, caption=f"Reporte Técnico - Folio {i}", use_container_width=True)
            except:
                st.warning(f"No se pudo cargar {img_name}")
