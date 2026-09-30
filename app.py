import streamlit as st

# ESTA DEBE SER LA PRIMERA LÍNEA DE CÓDIGO ACTIVO
st.set_page_config(
    page_title="Ruta de la Seda Analytics", 
    page_icon="🚢", 
    layout="wide"
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
    "⚡ Vectores Emergentes Colombia",
    "🚢 Conectividad Comercial BRICS-Seda"
])
# --- INYECCIÓN DE ESTILOS DE GAMA ALTA (24PX GLOBAL) ---
st.markdown("""
    <style>
    /* Tamaño gigante para textos de párrafos y viñetas en todas las pestañas */
    div[data-testid="stMarkdownContainer"] p, 
    div[data-testid="stMarkdownContainer"] li {
        font-size: 24px !important;
        line-height: 1.7 !important;
    }
    /* Tamaño macro para subtítulos técnicos e idiomas (H3) */
    div[data-testid="stMarkdownContainer"] h3 {
        font-size: 32px !important;
        font-weight: bold !important;
    }
    /* Ajuste homogéneo para los cuadros informativos inferiores */
    .stAlert p {
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# PESTAÑA 1: PERFIL PROFESIONAL
# ==========================================
with tabs[0]:

    # Estructura en columnas para incluir tu foto
    col_foto, col_texto = st.columns([1, 3])
    
    with col_foto:
        try:
            # Opción 1: Buscar en la carpeta outputs
            st.image("outputs/diego_suarez.jpg", use_container_width=True)
        except:
            try:
                # Opción 2: Buscar en la raíz por si acaso
                st.image("diego_suarez.jpg", use_container_width=True)
            except:
                st.info("📸 Espacio para: diego_suarez.jpg")
            
    with col_texto:
        st.title("Perfil Profesional")
        
        # CORREO EN ALTO IMPACTO VISUAL
        st.markdown("### 📧 Contacto Inmediato: **suarezt.diego.f@gmail.com**")
        
        # Texto de presentación potente
        st.markdown("""
        Consultor financiero senior y desarrollador de software especializado en el ecosistema corporativo e industrial. 
        Experto en transformar datos transaccionales crudos en Web Apps analíticas interactivas de alto rendimiento. 
        Dominio avanzado de modelos de valoración institucional (DuPont, ROIC, WACC, VAN/TIR), optimización de 
        procesos mediante Inteligencia Artificial y arquitectura de datos aplicada a la toma de decisiones estratégicas de alta gerencia.
        """)
        
        # Especificación de Servicios Freelancer
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



# ==============================================================================
# PESTAÑA 4: PROPUESTA FREELANCER BRICS LATAM-CHINA
# ==============================================================================
# ==============================================================================
# PESTAÑA 4: PROPUESTA FREELANCER BRICS LATAM-CHINA
# ==============================================================================
with tabs[3]:
    # --- INYECCIÓN DE ESTILOS SEGURA (AFECTA SOLO AL TEXTO INTERNO, NO AL MENÚ) ---
    st.markdown("""
        <style>
        /* Engorda y agranda el texto de los párrafos y listas internas */
        div[data-testid="stMarkdownContainer"] p, 
        div[data-testid="stMarkdownContainer"] li {
            font-size: 24px !important;
            line-height: 1.7 !important;
        }
        /* Agranda los subtítulos de los idiomas (H3) */
        div[data-testid="stMarkdownContainer"] h3 {
            font-size: 32px !important;
            font-weight: bold !important;
        }
        /* Ajuste de tamaño para los bloques informativos inferiores */
        .stAlert p {
            font-size: 24px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.header("🚢 Servicios de Inteligencia Comercial e Intermediación Global")
    st.caption("Estructuración de Operaciones Bilaterales de Comercio Exterior — Diego Suárez")
    st.markdown("---")
    
    st.markdown("""
    ### 🤝 El Puente de Conectividad Comercial
    Consultoría estratégica orientada a actuar como un **Zhōngjiè (仲介 - Intermediario de Confianza)** de alta eficiencia, 
    vinculando de forma directa a empresas de tecnología, logística y manufactura en Asia con los mercados emergentes 
    de América Latina. 
    
    Esta propuesta está diseñada con un enfoque analítico estricto para mitigar barreras culturales, logísticas y 
    operativas, agilizando el flujo de transacciones y optimizando la cadena de suministro en destino.
    """)
    
    st.markdown("### 🌐 Portafolio de Gestión Homologada (Trilingüe)")
    
    # Tres columnas para el despliegue idiomático regional y asiático
    col_esp, col_por, col_pin = st.columns(3)
    
    with col_esp:
        st.subheader("🇨🇴 Español")
        st.markdown("""
        *   **Auditoría Documental y Costos:** Validación de Facturas Comerciales y Certificados de Origen bajo términos Incoterms (**EXW, FOB, CIF**) para contención de sobrecostos y demoras (*Demurrage*).
        *   **Ingeniería de Costos de Aterrizaje:** Precosteo detallado de aranceles locales, tarifas portuarias y gravámenes específicos, asegurando la viabilidad financiera antes del embarque.
        *   **Monitoreo de Ventana Logística:** Supervisión analítica de tiempos en terminales (*Berth Windows*, procesos de *Gate-in* y *Gate-out*) para la agilización del despacho anticipado y nacionalización de contenedores.
        """)
        
    with col_por:
        st.subheader("🇧🇷 Português")
        st.markdown("""
        *   **Auditoria de Custos de Desembarque:** Análise analítica e validação crítica de documentos internacionais de frete e conformidade tarifária para o mercado bilateral China-Brasil.
        *   **Mitigação de Riscos Portuários:** Avaliação estratégica de custos logísticos de ponta a ponta e controle do impacto tributário do **AFRMM** nos principais portos de entrada da América do Sul.
        *   **Eficiência alfandegária:** Estruturação documental cênica para acelerar os processos de nacionalização e liberação ágil de contêineres e cargas consolidadas.
        """)
        
    with col_pin:
        st.subheader("🇨🇳 Pīnyīn (pīnyīn)")
        st.markdown("""
        *   **海关清关数据审计 (Hǎiguān qīngguān shùjù shěnjié):** 
            国际贸易清关管理。全面审核和验证商业发票、货运合同和符合贸易术语 (**EXW, FOB, CIF**) 的原产地证书，防止目的地港口产生额外关税或滞期费滞箱费 (*Demurrage*)。
        *   **到岸成本与关税工程 (Dào'àn chéngběn yǔ guānshuì gōngchéng):** 
            精算当地进口税率、港口规费及各项特定税费。在货物启运前，提供精准的集装箱预估成本核算矩阵，确保供应链资金流的财务可行性。
        *   **港口物流窗口监控 (Gǎngkǒu wùliú chuāngkǒu jiānkòng):** 
            深度分析码头靠泊窗口 (*Berth Windows*)、进港 (*Gate-in*) 与出港 (*Gate-out*) 流程。通过数据化追踪提高集装箱提前申报与快速放行通关效率。
        """)
        
    st.markdown("---")
    
    st.subheader("💼 Canales de Intermediación Estratégica")
    st_col1, st_col2 = st.columns(2)
    
    with st_col1:
        st.info("""
        **🔗 Soporte en Origen para Agencias de Sourcing y PYMES**
        Revisión minuciosa de catálogos industriales, coordinación analítica de auditorías de calidad en fábricas aliadas de China y resolución inmediata de inconsistencias comerciales e impositivas.
        """)
        
    with st_col2:
        st.success("""
        **📊 Soluciones de Viabilidad de Contenedores**
        Estructuración en sesiones privadas de análisis de márgenes brutos de ganancia, establecimiento del punto de equilibrio por contenedor (*FCL/LCL*) y proyección de retorno de inversión (ROI) antes del embarque.
        """)
