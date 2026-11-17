import os, html
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(D)  # la web se genera en la raíz del repositorio
import base64
_raw = open(os.path.join(D, "photo.txt")).read().strip()
open(os.path.join(OUT, "foto.jpg"), "wb").write(base64.b64decode(_raw.split(",", 1)[1]))
PHOTO = "foto.jpg"
import hashlib
def v(path):
    """Añade ?v=<huella> para que el navegador no muestre una versión guardada al cambiar el archivo."""
    return path + "?v=" + hashlib.md5(open(os.path.join(OUT, path), "rb").read()).hexdigest()[:8]

def ul(items): return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ol(items): return '<ol class="ol">' + "".join(f"<li><div>{i}</div></li>" for i in items) + "</ol>"
def p(*xs): return "".join(f"<p>{x}</p>" for x in xs)

CASES = [
dict(
 slug="caso-energia", tag="Energía · B2B y B2C",
 card="De vender productos a vender una relación",
 card_lede="Cómo una estrategia de negocio se convirtió en un backlog priorizado, un customer journey con KPIs y principios de experiencia en cada canal.",
 facts=["38 entrevistas", "3 fases", "Sept. 2024 a mayo 2025"],
 h1="Energética líder en España: de vender productos a vender una relación",
 lede="El research con 38 personas convirtió una estrategia de negocio («Multienergía») en un backlog de oportunidades priorizado con negocio, un customer journey B2B con KPIs y, después, en principios de experiencia aterrizados en cada canal de atención.",
 sheet=[("Cliente","Energética líder en España"),("Sector","Energía B2B y B2C"),("Duración","Fase 1, fase 2 y extensión B2C (septiembre de 2024 a mayo de 2025)"),("Equipo","Otra Service Designer y yo en research y service design, con apoyo de UX")],
 reto=p("La compañía vendía a empresas por verticales (gas, carburantes, luz...), y cada uno tenía su propio flujo, interlocutor y canal de venta. Un mismo cliente podía tener varios gestores y procesos distintos según lo que tuviera contratado.",
        "La nueva estrategia, con visión a 2027, era ofrecer a las empresas <span class='hl'>una solución energética integral con un solo proveedor</span>. Había dos objetivos de negocio: convertir a los clientes actuales en clientes «multienergía» y captar otros nuevos, con foco en pymes, sin aumentar la fuerza comercial y apoyándose más en lo digital."),
 rol=p("Research y Service Design a partes iguales con otra Service Designer: las dos hicimos el mismo trabajo durante todo el proyecto. Diseñamos y realizamos las entrevistas, hicimos la síntesis, mapeamos la experiencia de cliente «AS IS» y facilitamos juntas todos los workshops, tanto los de priorización con negocio como los B2C."),
 enfoque=p("Investigación cualitativa con los tres actores del ecosistema:") + ul([
   "<strong>14 entrevistas a empresas cliente:</strong> pymes de hostelería, industria y agro, con perfiles digitales y no digitales, algunas ya multienergía.",
   "<strong>24 entrevistas internas:</strong> 13 gestores comerciales, 7 personas del canal de distribución y 4 responsables de atención al cliente de distintos verticales.",
   "<strong>Service Design:</strong> mapeo de procesos e interacciones del ecosistema, y comparativa de los funnels de negocio, ventas y cliente.",
   "<strong>Workshops con negocio:</strong> priorización de oportunidades en una matriz y workshop presencial para diseñar escenarios de servicio por tipo de cliente."]),
 hallazgos=ul([
   "<strong>La confianza pesa más que el precio.</strong> Los clientes son «de toda la vida» y no quieren cambiar de proveedor, pero tampoco que se olviden de ellos. El gestor comercial es quien sostiene la relación.",
   "<strong>La segmentación por tamaño y sector no basta.</strong> Definimos tres perfiles de cliente por su relación con el servicio, <em>independiente</em>, <em>pragmático</em> y <em>necesitado</em>, cada uno con un equilibrio distinto entre lo digital y lo humano.",
   "<strong>Las pymes tienen el coste de servicio más alto</strong> y, a la vez, son las que más dependen del gestor en la gestión diaria.",
   "<strong>La oferta multienergía apenas se conoce</strong> entre los clientes: hay un problema claro de awareness.",
   "<strong>Para los equipos internos, Multienergía supone una transformación completa del trabajo diario.</strong> Se sienten sobrepasados por tareas nuevas, temen perder relevancia ante sus clientes y usan el CRM «por obligación».",
   "<strong>El canal quiere ser protagonista</strong> de la estrategia, pero la falta de recursos, control y apoyo le hace sentirse en desventaja.",
   "<strong>El onboarding es el momento clave:</strong> ahí se define el equilibrio entre trato humano y digital de toda la relación."]),
 quote=None,
 entregables=ul([
   "Informe de resultados de las fases 1 y 2.",
   "Customer journey B2B «AS IS», con puntos de contacto, pains y KPIs por fase.",
   "Tres arquetipos de cliente con su propuesta de valor y su estrategia de relación.",
   "Visión comparativa de los funnels de negocio, ventas y cliente, y lifecycle del cliente multienergía.",
   "Backlog de más de 60 oportunidades por ámbito: procesos internos, CRM, digitalización, fidelización, marketing y canal.",
   "Strategic roadmap.",
   "Primeras soluciones digitales: mejoras de usabilidad del CRM para empleados, demo de escenarios multienergía y wireframes del portal unificado de cliente."]),
 traduccion=ul([
   "<strong>De insights a decisiones de negocio:</strong> las oportunidades se priorizaron con negocio en un workshop con matriz. Entre las que salieron están el onboarding digital, la atención al cliente como «gestor remoto» para pymes, un backoffice como facilitador de ventas y la simplificación de la creación de leads en el CRM.",
   "<strong>De arquetipos a escenarios de servicio:</strong> en el workshop presencial, negocio diseñó el servicio por tipo de cliente. El gran reto que se definió fue llevar a los clientes «necesitados» hacia el perfil «pragmático», con más autonomía.",
   "<strong>Del research al diseño:</strong> los hallazgos alimentaron directamente el portal unificado de cliente y las mejoras del CRM.",
   "<strong>Continuidad:</strong> el cliente fue contratando más fases de las iniciales: de la fase 1 a una fase 2 y después a la extensión al cliente particular."]),
 extra=("Extensión B2C", "Principios de experiencia en cada canal",
   p("Con el lanzamiento de la nueva marca, facilitamos <strong>3 workshops de 4 horas</strong> con personas de experiencia de cliente, estaciones de servicio y canal presencial. El objetivo era aterrizar los principios de experiencia de la marca en los momentos clave del customer journey.",
     "Las dinámicas se adaptaron a cada perfil: desde reflexionar sobre cómo otras marcas escuchan y cuidan a sus clientes hasta idear acciones concretas por momento (repostaje, pago, firma de contrato, resolución de dudas...).",
     "<strong>Resultado:</strong> el ADN de marca se tradujo en <strong>decálogos de experiencia por canal</strong> (teléfono, estaciones de servicio y oficinas), con acciones que puede llevar a cabo directamente el empleado. También se acordó en qué formato comunicarlos a los equipos y se elaboró un backlog de mejoras por canal.")),
),
dict(
 slug="caso-ong", tag="Tercer sector · Captación",
 card="Una web que deje de reflejar el organigrama",
 card_lede="De unas 32 secciones organizadas por departamentos a tres bloques pensados para el donante, con toda la organización alineada.",
 facts=["2 fases", "De 32 secciones a 3 bloques", "2026"],
 h1="ONG internacional de infancia: una web que deje de reflejar el organigrama",
 lede="El diagnóstico y el workshop de co-creación alinearon a toda la organización en una visión común de la nueva web. Esa visión se tradujo en una nueva arquitectura de menú validada con las áreas, en wireframes con requisitos claros y en una presentación al comité interno de la organización.",
 sheet=[("Cliente","Delegación española de una ONG internacional de infancia"),("Sector","Tercer sector, captación de fondos"),("Duración","Fase 1 (diagnóstico) y fase 2 (workshop, arquitectura y wireframes), 2026"),("Equipo","Research, análisis y arquitectura de la información llevados por mí")],
 reto=p("La organización iba a rediseñar su web y a migrarla a un nuevo CMS. La web había crecido durante años a base de soluciones puntuales. Su menú tenía unas 32 secciones, cada departamento ocupaba su propio espacio y el 80 % del tráfico llegaba desde móvil, donde la navegación era el punto más crítico.",
        "El reto no era solo cambiar el menú: había que <span class='hl'>reconfigurar cómo se mostraba la organización</span> en un mercado de captación cada vez más saturado."),
 rol=p("Llevé yo todo el trabajo de research y estrategia: entrevistas con stakeholders, auditoría y análisis heurístico, benchmark, diseño y facilitación del workshop, arquetipos y journeys, y la nueva arquitectura de la información con sus requisitos para los wireframes."),
 enfoque="<h3>Fase 1 · Diagnóstico y entendimiento</h3>" + ul([
   "<strong>Entrevistas con stakeholders</strong> de las distintas áreas: captación, comunicación, contenidos, tecnología e influencia.",
   "<strong>Auditoría web y análisis heurístico</strong> de cada área de la web con las 10 heurísticas de Nielsen, puntuadas de 0 a 4 según su gravedad, y análisis de rendimiento.",
   "<strong>Benchmark</strong> con ONG competidoras y otros players, del que salieron unos Do y Don'ts específicos para la organización.",
   "<strong>Diagnóstico emocional y de storytelling</strong>, cruzado con un estudio de perfil del donante de más de 3.000 personas."]) +
   "<h3>Fase 2 · Co-creación y aterrizaje</h3>" + ul([
   "<strong>Workshop de co-creación</strong> con las áreas para construir los arquetipos de donante y su journey.",
   "<strong>Dos arquetipos y sus journeys:</strong> el <em>senior continuista</em>, que paga la cuota y exige transparencia, y la <em>junior concienciada</em>, con menos dinero pero mucha voz y compromiso social.",
   "<strong>Propuesta de arquitectura de la información</strong>, apoyada en datos de mercado sobre el donante en España y validada con las áreas. Después, otra agencia la testó con un card sorting de entre 30 y 50 panelistas."]),
 hallazgos=ul([
   "<strong>«La web refleja cómo estamos organizados, no lo que el usuario necesita.»</strong> Se notaban las costuras de la organización y faltaban criterios comunes para decidir.",
   "<strong>Fragmentación:</strong> colores, CTAs y secciones duplicadas hacían que distintas partes de la web parecieran webs diferentes. El flujo de donación era el punto de mayor fricción.",
   "<strong>Barrera de desconfianza:</strong> el 40 % de los usuarios duda del uso de los fondos y el 41 % teme que la ayuda no llegue a su destino.",
   "<strong>El impacto local no se ve:</strong> mucha gente no sabe que la organización también trabaja en España.",
   "<strong>El equipo editorial depende del código:</strong> crear una landing de emergencia lleva unas 2 horas, y el objetivo es hacerlo en 15 minutos.",
   "<strong>Un deseo unánime:</strong> una web que simplifique la vida al donante, dé autonomía a los editores y muestre el orgullo de pertenecer a la organización."]),
 quote=("La web refleja cómo estamos organizados, no lo que el usuario necesita.", "Stakeholder de la organización"),
 entregables=ul([
   "Informe y executive de la fase 1: diagnóstico, análisis heurístico, benchmark y oportunidades.",
   "Materiales y conclusiones del workshop de co-creación.",
   "Arquetipos de donante con su colaborador journey map.",
   "Nueva arquitectura del menú («Quién / Qué / Cómo») y de la home, bloque a bloque.",
   "Requisitos para los wireframes y primeros wireframes.",
   "Presentación al comité interno: menú actual frente a propuesta.",
   "Piezas derivadas: propuesta de página SEO para una causa, match de contenidos antes y después (el «tetris» de la navegación) y análisis de la landing de microdonaciones."]),
 traduccion=ul([
   "<strong>Un acuerdo de toda la casa:</strong> el workshop logró que áreas con objetivos distintos, desde la captación pura hasta la influencia, compartieran una misma definición de éxito. Esa definición era donar con menos pasos, entender de un vistazo qué hace la organización y publicar sin fricciones.",
   "<strong>Un menú centrado en el usuario:</strong> de unas 32 secciones organizadas por departamentos se pasó a tres bloques (quién somos, qué hacemos y cómo colaborar). La propuesta se validó con las áreas, que aportaron ajustes concretos.",
   "<strong>Requisitos de diseño basados en evidencia:</strong> los fallos heurísticos de la fase 1 se convirtieron en reglas obligatorias para los wireframes. Por ejemplo, un checkout limpio sin imágenes, porque los datos mostraban una caída de conversión del 12,36 % al añadirlas, y máscaras de entrada en campos complejos.",
   "<strong>Nuevas vías de colaboración:</strong> microdonación con pago móvil y campañas de firmas para captar a personas con poca capacidad económica pero mucho compromiso.",
   "<strong>Sistema de diseño como base</strong> de la migración, para dar autonomía a los editores.",
   "<strong>Decisión interna y continuidad:</strong> la propuesta de menú se presentó al comité interno de la organización, y el cliente contrató más fases de las previstas al principio."]),
 extra=None,
),
dict(
 slug="caso-ia", tag="Adopción de IA · Workshop",
 card="Un formato, dos contextos: decidir qué IA construir primero",
 card_lede="Un discovery workshop que parte del día a día real de las personas, aplicado con el equipo de compras de una fintech y con un equipo comercial.",
 facts=["2 equipos", "11 personas", "Sesiones de 90 a 120 min"],
 h1="Workshop de adopción de IA: un formato, dos contextos",
 lede="Diseñé un formato de discovery workshop que parte del día a día real de las personas, y no de la tecnología, para decidir qué IA construir primero. Lo apliqué con el equipo de compras de una fintech y con el equipo comercial de mi consultora, y en ambos casos salió una hoja de prioridades sobre la que construir la solución.",
 sheet=[("Contexto 1","Procurement de una fintech internacional de pagos (4 personas, 90 minutos, septiembre de 2026)"),("Contexto 2","Equipo comercial (SDRs y Business Managers) que vende una suite de IA empresarial (7 personas)"),("Formato","Sesiones de 90 minutos a 2 horas, en cinco bloques"),("Equipo","Senior Researcher (yo) y Senior UX Designer")],
 reto=p("Las empresas tienen acceso a herramientas de IA, pero la adopción se queda en usos sueltos, como redactar correos o resumir textos. El reto era identificar <span class='hl'>dónde aporta valor real la IA en el trabajo de cada equipo</span> y qué debería resolverse primero, antes de construir una solución o una demo a medida.") +
   '<p class="premise">La premisa del formato: «Hoy no venimos a ver otra demo: venimos a construir la vuestra.»</p>',
 rol=p("Diseño del formato y de las dinámicas, facilitación, síntesis y presentación de resultados, junto a una UX Designer."),
 enfoque=p("Cinco bloques que van del día a día a la prioridad:") + ol([
   "<strong>Conversación sobre su día a día:</strong> roles, tareas y una semana tipo. Cada persona señala las 2 o 3 tareas que más tiempo le roban.",
   "<strong>Fricciones:</strong> tareas repetitivas, información dispersa (en cuántas herramientas hay que buscar) y «teléfonos escacharrados» entre áreas. Cierra con votación.",
   "<strong>Su IA hoy:</strong> para qué la usan ya y dónde se queda corta.",
   "<strong>Escenarios de uso:</strong> buscador con citas a documentos internos, agentes de trabajo e IA integrada en reuniones y correo. Se valoran en una escala y en dos lentes («¿me serviría a mí?» y «¿le serviría a un cliente?»).",
   "<strong>Cierre:</strong> su IA ideal, qué no debería hacer nunca y una sola prioridad por persona."]) +
   p("El formato se adaptó a cada equipo. Con procurement, las zonas se centraron en sistemas y aprobaciones. Con el equipo comercial, se añadieron momentos concretos de su día a día («tienes reunión mañana a las 9 con una cuenta que no conoces») y la mirada de lo que piden sus clientes."),
 hallazgos="<h3>Equipo de procurement (fintech)</h3>" + ul([
   "<strong>Sistemas desconectados:</strong> riesgo, gestión legal de contratos y ERP financiero no hablan entre sí. Un contrato no puede aprobarse sin pasar antes el análisis de riesgo en otra herramienta, lo que duplica tareas y resta trazabilidad.",
   "<strong>Alta carga administrativa:</strong> perseguir aprobaciones, revisar facturas y explicar una y otra vez procesos ya documentados. Todo ello para gestionar unos 400 proveedores tecnológicos.",
   "<strong>La IA actual se queda corta:</strong> no conoce el contexto interno, da respuestas genéricas a la primera y no llega al market research profundo."]) +
   "<h3>Equipo comercial</h3>" + ul([
   "<strong>El tiempo se va en tareas administrativas:</strong> actualizar el CRM, rellenar Excel, reclamar facturas y esperar respuestas de fabricantes y aprobaciones internas.",
   "<strong>Preparar una reunión con una cuenta nueva lleva de 30 a 60 minutos</strong> de búsqueda en distintas fuentes y preguntando a compañeros.",
   "<strong>Desconfianza hacia la IA:</strong> «se inventa algo antes de admitir que no sabe». Lo que nunca debería hacer es inventar ni actuar sin supervisión.",
   "<strong>Lo que piden los clientes:</strong> ROI, casos de uso concretos y gobierno de la IA."]),
 quote=("Se inventa algo antes de admitir que no sabe.", "Persona del equipo comercial"),
 entregables=ul([
   "Formato de workshop reutilizable, con agenda, dinámicas, plantillas y escenarios.",
   "Tableros de trabajo de cada sesión.",
   "Informe de resultados del discovery: equipo y tareas, pain points, uso actual de la IA, «IA ideal» y prioridades."]),
 traduccion=ul([
   "<strong>Fintech:</strong> seis prioridades ordenadas por impacto. La primera es una capa de IA que unifique los tres sistemas en una sola interfaz con búsqueda y extracción de datos. Le siguen agentes para recordatorios y seguimientos, un buscador con citas a la fuente y un programa de formación y acompañamiento como elemento diferenciador. A partir de ellas, se entregó a la fintech un documento de adopción y el cliente contrató nuevas fases.",
   "<strong>Equipo comercial:</strong> la demo a medida, que ya está en construcción, parte de los escenarios y tareas que votó el propio equipo. Además, sus aprendizajes alimentan cómo presentan la solución a sus clientes.",
   "<strong>Un formato repetible:</strong> al aplicarlo en dos contextos tan distintos, quedó claro que el método funciona para pasar de «tenemos IA» a «sabemos qué problema resolver primero»."]),
 extra=None,
),
dict(
 slug="caso-farma", tag="Salud · App de pacientes",
 card="Una app que acompañe al paciente, no solo a su tratamiento",
 card_lede="12 entrevistas con pacientes crónicos que dieron mejoras de diseño inmediatas y una hoja de ruta por fases del journey y por arquetipo.",
 facts=["12 entrevistas", "7 enfermedades", "2025"],
 h1="Farmacéutica internacional: una app que acompañe al paciente, no solo a su tratamiento",
 lede="12 entrevistas con pacientes crónicos se tradujeron en dos cosas. A corto plazo, mejoras de diseño concretas para cada sección de la app. A largo plazo, una hoja de ruta de producto organizada por las fases del patient journey y por cuatro arquetipos de paciente.",
 sheet=[("Cliente","Farmacéutica internacional"),("Sector","Salud, app de acompañamiento al paciente"),("Año","2025"),("Equipo","Trabajo individual, de principio a fin")],
 reto=p("La farmacéutica había lanzado una app para pacientes con enfermedades inmunomediadas, como la enfermedad de Crohn, la psoriasis o la dermatitis atópica. Quería saber <span class='hl'>si encajaba con lo que de verdad necesitan estos pacientes</span> y qué mejorar.",
        "El estudio tenía dos objetivos: <strong>entender</strong> las necesidades del paciente desde el diagnóstico hasta hoy y <strong>testar</strong> la app en manos reales."),
 rol=p("Llevé el proyecto sola de principio a fin: diseño del estudio y del perfil de reclutamiento, guion, entrevistas y tests, análisis, construcción del journey y de los arquetipos, recomendaciones y presentación del informe."),
 enfoque=ul([
   "<strong>12 entrevistas en profundidad presenciales de 60 minutos.</strong> El 30 % del tiempo se dedicó a entender el recorrido con la enfermedad y el 70 % al test de usabilidad de la app.",
   "<strong>Muestra diversa:</strong> 7 enfermedades inmunomediadas distintas, de 18 a 55 años, con distinta intensidad y antigüedad (desde diagnosticados hace menos de 3 años hasta pacientes desde el nacimiento), incluida una persona aún sin especialista.",
   "<strong>Test sección a sección:</strong> registro, home, recordatorios de medicación, registro emocional, retos, progreso, ayuda, ajustes e información del tratamiento."]),
 hallazgos=ul([
   "<strong>El journey no es lineal.</strong> Tiene cinco etapas (inicio de síntomas, diagnóstico, adaptación al tratamiento, vida con la enfermedad y brotes) que a partir del tratamiento se repiten y se solapan.",
   "<strong>El objetivo no es superar la enfermedad, sino llevar una vida normal.</strong> La gestión emocional pesa tanto como la física.",
   "<strong>No hay un paciente único.</strong> Cuatro variables determinan qué le sirve a cada uno de la app: estabilidad de la enfermedad, recorrido o expertise, tipo de tratamiento y apertura a aprender.",
   "<strong>De ellas salen cuatro arquetipos:</strong> el <em>evitativo</em>, que quiere que funcione y ya; el <em>autoexigente</em>, que busca rigor y control; el <em>explorador</em>, que quiere aprender y compartir; y el <em>pragmático</em>, que solo usa lo que le ahorra tiempo.",
   "<strong>En la app:</strong> el recordatorio de medicación y el mapa corporal que indica dónde inyectarse generan un «efecto wow». En cambio, varios nombres de sección no anticipan su contenido y el botón clave para registrar emociones pasa desapercibido para todos.",
   "<strong>Lo que más falta:</strong> conexión con el sistema sanitario (historial, centros de referencia, urgencias)."]),
 quote=("Cuando oyes “crónica”, todo se te cae encima.", "Paciente entrevistado"),
 entregables=ul([
   "Informe de resultados de más de 100 diapositivas.",
   "Patient journey en cinco etapas, con emociones, momentos críticos y necesidades por etapa.",
   "Modelo de cuatro variables y cuatro arquetipos de paciente, cada uno con lo que quiere y lo que necesita de la app.",
   "Evaluación de usabilidad por sección, con puntos positivos, fricciones y mejoras.",
   "Oportunidades por fase del journey y funcionalidades por arquetipo."]),
 traduccion=ul([
   "<strong>Mejoras de diseño listas para aplicar:</strong> reforzar el CTA de registro, renombrar las secciones genéricas, unificar en un solo botón las dos rutas de configuración del recordatorio, colocar el registro emocional en el centro y bajar el peso de «ajustes» en la home, entre otras.",
   "<strong>Proteger lo que funciona:</strong> se recomendó dar más protagonismo al mapa corporal y a la información del tratamiento en tono cercano, porque eran los mayores diferenciales de la app.",
   "<strong>Una hoja de ruta de producto:</strong> oportunidades nuevas para cada fase del journey. Por ejemplo, registrar síntomas antes del diagnóstico para evitar el «me lo estoy inventando», un onboarding emocional tras el diagnóstico y un «modo brote» que reduzca notificaciones y dé acceso directo a la ayuda.",
   "<strong>Personalización por arquetipo:</strong> criterios para adaptar el tono, la profundidad del contenido y las funcionalidades a cada tipo de paciente, en lugar de diseñar para un paciente medio que no existe.",
   "<strong>Continuidad:</strong> tras este estudio, el cliente contrató más fases de las previstas al principio."]),
 extra=None,
),
dict(
 slug="caso-diabetes", tag="Salud digital · Diabetes",
 card="Validar una app de diabetes antes de lanzarla",
 card_lede="Un test con usuarias confirmó una necesidad que nadie resolvía y detectó los ajustes de lenguaje, flujo y accesibilidad previos al lanzamiento.",
 facts=["5 usuarias", "2 momentos de uso", "2024"],
 h1="Startup de salud digital: validar una app de diabetes antes de lanzarla",
 lede="Un test con usuarias de un prototipo confirmó que la app cubría una necesidad que nadie estaba resolviendo, saber cuánta insulina te has puesto y cuándo, y detectó los ajustes de lenguaje, flujo y accesibilidad necesarios antes del lanzamiento.",
 sheet=[("Cliente","Startup de salud digital (dispositivo y app para pacientes insulinodependientes)"),("Fecha","Abril de 2024"),("Equipo","Trabajo individual, de principio a fin"),("Idioma del informe","Inglés")],
 reto=p("La startup tenía un prototipo de app que se sincroniza con un dispositivo para la pluma de insulina, con el sensor de glucosa y con el glucómetro. Necesitaba saber, antes de seguir desarrollando, <span class='hl'>si el onboarding y el panel de control se entendían</span> y si respondían a lo que necesitan los pacientes."),
 rol=p("Llevé el proyecto sola de principio a fin: diseño del test y de las tareas, sesiones con usuarias, análisis, informe y recomendaciones."),
 enfoque=ul([
   "<strong>Test de usabilidad con 5 usuarias</strong> insulinodependientes que usan pluma, de distintas edades y niveles de enfermedad.",
   "<strong>Dos tareas que simulan dos momentos de vida del producto:</strong>" + '<ul class="sublist"><li><strong>Onboarding:</strong> entrar por primera vez, crear el perfil y vincular los dispositivos.</li><li><strong>Seguimiento a los 3 meses:</strong> entrar y valorar el panel de control con datos acumulados.</li></ul>',
   "<strong>Conversación de contexto</strong> sobre la experiencia de vivir con diabetes, para entender las necesidades de fondo más allá de la interfaz."]),
 hallazgos=ul([
   "<strong>Un diagnóstico en la edad adulta obliga a «reaprender» el cuerpo y los hábitos con poco apoyo.</strong> Los pacientes se vuelven expertos muy rápido y por su cuenta, porque «su vida depende de ello».",
   "<strong>Su información está dispersa</strong> en varias apps y no la centraliza nadie, ni siquiera la consulta médica. Sienten que se les trata de forma genérica.",
   "<strong>La app cubre una necesidad hasta ahora sin resolver:</strong> controlar cuántas veces y cuánta insulina se han inyectado.",
   "<strong>Onboarding claro y rápido,</strong> que encaja con su modelo mental. La sincronización de dispositivos sorprende por lo fácil que es y la glucosa en tiempo real genera un «efecto wow».",
   "<strong>El lenguaje técnico no funciona:</strong> las siglas de los dispositivos no se reconocen (ninguna usuaria identificó su propio sensor por su sigla) y los recién diagnosticados prefieren «sensor» a «CGM».",
   "<strong>Secciones ambiguas:</strong> no hay consenso sobre qué son «Mi red», «Aprende» o «Informes», y los iconos de la curva personal no se entienden.",
   "<strong>Baja accesibilidad</strong>, un aspecto crítico para un público que tiende a perder visión por la propia enfermedad."]),
 quote=("A menudo no sé si me he pinchado o no.", "Usuaria del test"),
 entregables=ul([
   "Informe de resultados con objetivos, metodología, key insights, evaluación general y detallada pantalla a pantalla, oportunidades y conclusiones.",
   "Notas de cada sesión y análisis de arquitectura de la información."]),
 traduccion=ul([
   "<strong>Validación de la propuesta de valor:</strong> el prototipo encajaba con las necesidades no cubiertas, centralizar los datos y saber cuándo se ha medicado. Esto daba base para seguir desarrollando.",
   "<strong>Ajustes concretos antes del lanzamiento:</strong>" + '<ul class="sublist"><li>agrupar el registro en bloques (perfil, dispositivos y documentación);</li><li>hacer multirrespuesta la pregunta de tratamiento;</li><li>sustituir las siglas por un lenguaje del paciente;</li><li>aclarar con copy y tutorial qué es solo visualización y qué permite añadir datos;</li><li>mejorar la accesibilidad.</li></ul>',
   "<strong>Hoja de ruta de producto:</strong> convertir «Aprende» en un espacio con fuentes médicas fiables desde el diagnóstico, dar acceso al endocrino a los indicadores del paciente, abrir un canal directo de ayuda y valorar una calculadora de carbohidratos, que ya usan en otras apps.",
   "<strong>Oportunidad de engagement:</strong> el acompañamiento personal que piden los pacientes es el elemento que puede convertir una herramienta de registro en una app de referencia.",
   "<strong>Continuidad:</strong> la startup contrató más fases de las previstas al principio."]),
 extra=None,
),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@500&display=swap"><link rel="stylesheet" href="' + v("styles.css") + '"><script>if(\'IntersectionObserver\' in window&&!matchMedia(\'(prefers-reduced-motion: reduce)\').matches)document.documentElement.classList.add(\'anim\')</script>'

# Línea ondulada de las cabeceras de caso (trazo con degradado amanecer, nunca relleno)
WAVE = '''<svg class="wave" viewBox="0 0 1440 600" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="amanecer" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#78BAE6"/><stop offset="1" stop-color="#A99BE8"/></linearGradient></defs><path d="M-20 40 C 400 6, 700 10, 900 130 S 1200 540, 1460 470" fill="none" stroke="url(#amanecer)" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'''

def nav(prefix):
    return f'''<header class="nav"><div class="inner">
  <a class="brand" href="{prefix or '#inicio'}" aria-label="Gema Díez, inicio"><span class="dot" aria-hidden="true"></span>Gema Díez</a>
  <nav aria-label="Principal"><ul>
    <li class="hide-s"><a href="{prefix}#como-trabajo">Cómo trabajo</a></li>
    <li class="hide-s"><a href="{prefix}#casos">Casos</a></li>
    <li class="hide-s"><a href="{prefix}#sobre-mi">Sobre mí</a></li>
    <li><a class="btn btn-primary btn-small" href="{prefix}#contacto">Hablemos</a></li>
  </ul></nav>
</div></header>'''

FOOT = '<footer class="band foot"><div class="inner"><span>© 2026 Gema Díez · Madrid</span><span>Service Designer estratégica</span></div></footer>\n<a class="totop" id="totop" href="#" aria-label="Volver arriba" title="Volver arriba"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></a>\n<script src="' + v('site.js') + '" defer></script>'

ICONS = {
 "sistema": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><path d="M24 8 A16 16 0 0 0 24 40" stroke="#161616"/><path d="M26 8 A16 16 0 0 1 26 40" stroke="#A99BE8" stroke-width="2"/></svg>',
 "piezas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><g stroke="#161616"><path d="M12 12 L36 14 M12 12 L14 36 M36 14 L34 34 M14 36 L34 34 M12 12 L34 34"/><circle cx="12" cy="12" r="4" fill="#FFFFFF"/><circle cx="36" cy="14" r="4" fill="#FFFFFF"/><circle cx="14" cy="36" r="4" fill="#FFFFFF"/></g><circle cx="34" cy="34" r="5" stroke="#78BAE6" stroke-width="2" fill="#FFFFFF"/></svg>',
 "personas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><circle cx="18" cy="24" r="12" stroke="#161616"/><circle cx="30" cy="24" r="12" stroke="#78BAE6" stroke-width="2"/></svg>',
}

# Cifras de la cabecera de cada caso: dato grande + etiqueta, sin caja (no deben parecer botones)
STATS = {
 "caso-energia": [("38", "entrevistas"), ("3", "fases"), ("2024–25", "de septiembre a mayo")],
 "caso-ong": [("2", "fases"), ("32 → 3", "secciones del menú"), ("2026", "año")],
 "caso-ia": [("2", "equipos"), ("11", "personas"), ("90–120", "minutos por sesión")],
 "caso-farma": [("12", "entrevistas"), ("7", "enfermedades"), ("2025", "año")],
 "caso-diabetes": [("5", "usuarias"), ("2", "momentos de uso"), ("2024", "año")],
}

# Trazos "dibujados a mano" (SVG). Se dibujan solos al entrar en pantalla (.draw)
ARROW = '<svg class="doodle draw arrow" viewBox="0 0 120 60" aria-hidden="true"><path pathLength="1" d="M6 50 C 22 18, 58 6, 104 18"/><path pathLength="1" d="M90 6 L106 18 L91 29"/></svg>'
ARROW_DOWN = '<svg class="doodle draw arrow-down" viewBox="0 0 70 90" aria-hidden="true"><path pathLength="1" d="M12 6 C 50 14, 62 46, 40 80"/><path pathLength="1" d="M28 70 L40 82 L52 70"/></svg>'
SCRIBBLE = '<svg class="doodle draw scribble" viewBox="0 0 300 24" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M4 16 C 40 6, 70 20, 110 12 S 190 6, 230 14 S 280 12, 296 8"/></svg>'
LOOP = '<svg class="doodle draw loop" viewBox="0 0 220 120" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M30 70 C 20 30, 90 8, 150 16 C 205 24, 214 70, 170 98 C 120 124, 40 112, 22 80 C 14 64, 30 44, 60 36"/></svg>'
WINK = '<svg class="doodle draw wink" viewBox="0 0 48 48" role="img" aria-label="guiño"><path pathLength="1" d="M24 4 C 36 3, 45 13, 44 25 C 43 37, 33 45, 22 44 C 10 43, 3 33, 4 22 C 5 12, 13 5, 25 5"/><path pathLength="1" d="M15 18 C 16 17, 17 17, 17 19"/><path pathLength="1" d="M28 19 C 30 17, 33 17, 35 19"/><path pathLength="1" d="M13 28 C 18 36, 30 37, 36 27"/></svg>'
# Nota a mano de cada caso, junto a la foto de cabecera
NOTES = {"caso-energia": "de vender productos<br>a vender una relación", "caso-ong": "32 secciones → 3 bloques",
 "caso-ia": "¿qué IA construimos primero?", "caso-farma": "una vida normal,<br>no solo un tratamiento", "caso-diabetes": "«¿me he pinchado o no?»"}

LINES = ["ln-top", "ln-left", "ln-right", "ln-bottom", "ln-top-r"]  # posición de la línea de color de cada tarjeta

def card(c, wide=False, k=0):
    facts = "".join(f"<span>{f}</span>" for f in c["facts"])
    return f'''<a class="case reveal {LINES[k % 5]}{' wide' if wide else ''}" style="--d:{(k % 3)*100}ms" href="{c['slug']}.html">
  <img class="thumb" src="{v('img/' + c['slug'] + '.jpg')}" alt="" width="800" height="800" loading="lazy">
  <span class="tag">{c['tag']}</span>
  <div><h3>{c['card']}</h3><p class="lede">{c['card_lede']}</p></div>
  <div class="facts">{facts}</div>
  <span class="go">Leer el caso</span>
</a>'''

STEP_KIND = {"El reto": "reto", "Mi rol": "rol", "Enfoque": "enfoque", "Hallazgos clave": "hallazgos", "Entregables": "entregables", "En qué se tradujo": "tradujo"}

def step(n, title, body, white):
    kind = STEP_KIND[title]
    tone = " dark" if kind == "hallazgos" else (" white" if white else "")
    chip = "chip-sky" if n % 2 else "chip-lav"
    return f'''<section class="band step step-{kind}{tone}" id="{kind}"><div class="inner">
  <div class="step-head reveal"><span class="bignum" aria-hidden="true">{n:02d}</span><span class="chip {chip}">Paso {n:02d} de 06</span><h2>{title}</h2></div>
  <div class="prose">{body}</div>
</div></section>'''

def case_page(i, c):
    nxt = CASES[(i + 1) % len(CASES)]
    sheet = "".join(f'<div><span class="label">{k}</span><b>{v}</b></div>' for k, v in c["sheet"])
    pills = "".join(f'<div><dt>{l}</dt><dd>{n}</dd></div>' for n, l in STATS[c["slug"]])
    trad = c["traduccion"]
    if c["quote"]:
        q, who = c["quote"]
        pull = f'''<section class="pull"><div class="inner"><figure class="reveal"><span class="qmark" aria-hidden="true">“</span><blockquote><p>{q}</p></blockquote><figcaption><span class="dot" aria-hidden="true"></span>{who}</figcaption></figure></div></section>'''
    else:
        pull = ""
    hall = c["hallazgos"]
    if c["extra"]:
        lab, h, body = c["extra"]
        trad += f'<div class="extra"><span class="label">{lab}</span><h3>{h}</h3>{body}</div>'
    steps = [("El reto", c["reto"]), ("Mi rol", c["rol"]), ("Enfoque", c["enfoque"]), ("Hallazgos clave", hall), ("Entregables", c["entregables"]), ("En qué se tradujo", trad)]
    body = "".join(step(k + 1, t, b, k % 2 == 0) + (pull if t == "Hallazgos clave" else "") for k, (t, b) in enumerate(steps))
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(c['card'])} · Gema Díez</title>
<meta name="description" content="{html.escape(c['lede'])}">
{FONTS}
</head>
<body>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main>
<section class="case-hero">{WAVE}<div class="inner">
  <div class="hero-grid">
    <div class="hero-text">
      <a class="back" href="index.html#casos">← Todos los casos</a>
      <span class="tag">{c['tag']}</span>
      <h1>{c['h1']}</h1>
      <p class="lede">{c['lede']}</p>
      <dl class="stats">{pills}</dl>
    </div>
    <figure class="hero-photo"><img class="float" style="--f:9s" src="{v('img/' + c['slug'] + '.jpg')}" alt="" width="800" height="800"><span class="dot" aria-hidden="true"></span><figcaption class="note n-case">{ARROW}{NOTES[c['slug']]}</figcaption></figure>
  </div>
  <div class="sheet">{sheet}</div>
</div></section>
{body}
<section class="band next"><div class="inner">
  <a class="next-case" href="{nxt['slug']}.html"><span class="label">Siguiente caso</span><h3>{nxt['card']}</h3></a>
  <a class="btn btn-primary" href="index.html#contacto">Cuéntame tu proyecto</a>
</div></section>
</main>
{FOOT}
</body>
</html>
'''

cards = "".join(card(c, wide=(k >= 3), k=k) for k, c in enumerate(CASES))

INDEX = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Gema Díez · Service Designer</title>
<meta name="description" content="Gema Díez, Service Designer estratégica. Hago que lo fragmentado funcione como un solo servicio.">
{FONTS}
</head>
<body>
{nav('')}
<main>
<section class="hero" id="inicio">
<div class="orbits" aria-hidden="true"><span class="orbit o1"></span><span class="orbit o2"></span></div>
<div class="inner">
  <span class="chip chip-sky">Service Designer estratégica</span>
  <h1 class="bigtype" aria-label="Entiendo el sistema. Uno las piezas. Pienso en las personas y en el negocio.">
    <span class="row" style="--d:0ms" aria-hidden="true"><span>Entiendo el sistema.</span></span>
    <span class="row" style="--d:120ms" aria-hidden="true"><span class="accent">Uno las piezas.</span><span class="note n-hero">lo que mejor<br>se me da{ARROW}</span></span>
    <span class="row" style="--d:240ms" aria-hidden="true"><span>Pienso en las personas</span></span>
    <span class="row" style="--d:360ms" aria-hidden="true"><span>y en el negocio.</span></span>
  </h1>
  <p class="sub">Hago que lo fragmentado funcione como un solo servicio.</p>
  <div class="ctas"><a class="btn btn-secondary" href="#contacto">Cuéntame tu proyecto</a><a class="btn btn-primary" href="#casos">Ver casos</a></div>
  <p class="proof"><span class="dot" aria-hidden="true"></span><span>En 2025 y 2026, <b>todos mis clientes han vuelto a contar conmigo</b> para nuevas fases y proyectos. {WINK}</span></p>
</div></section>

<section class="band white" id="como-trabajo"><div class="inner">
  <div class="sec-head"><span class="chip chip-lav">Cómo trabajo</span><h2>Tres pasos para que un servicio <span class="hand-u">complejo{SCRIBBLE}</span> funcione</h2><p>La investigación es mi punto de partida, no mi entregable. Escucho a las personas y leo los datos para decidir qué hacer.</p></div>
  <div class="pillars">
    <div class="pillar reveal" style="--d:0ms"><div class="pillar-top">{ICONS['sistema']}<span class="pnum">01</span></div><h3>Entiendo el sistema</h3><p>Mapeo cómo funcionan las cosas de verdad: quién las sostiene, qué herramientas usa cada equipo y dónde se rompe la experiencia.</p></div>
    <div class="pillar reveal" style="--d:120ms"><div class="pillar-top">{ICONS['piezas']}<span class="pnum">02</span></div><h3>Uno las piezas</h3><p>Decido qué importa y qué no puede fallar en cada flujo y punto de contacto, para que todo funcione como un solo servicio.</p></div>
    <div class="pillar reveal" style="--d:240ms"><div class="pillar-top">{ICONS['personas']}<span class="pnum">03</span></div><h3>Pienso en las personas y en el negocio</h3><p>Alineo a los equipos en torno a los mensajes que hay que transmitir, para que lo bueno para las personas también lo sea para el negocio.</p></div>
  </div>
  <div class="statement reveal">
    <p>No diseño píxeles.<br>Diseño lo que hace que esos píxeles <span class="hand-u light">tengan sentido.{SCRIBBLE}</span></p>
  </div>
</div></section>



<section class="band" id="casos"><div class="inner">
  <div class="sec-head"><span class="chip chip-sky">Casos · 2024 a 2026</span><h2>Qué descubrimos y en qué se tradujo</h2><p>Cinco proyectos de Service Design y Research contados por sector, sin nombres de marca ni datos internos, por confidencialidad.</p></div>
  <div class="cases">{cards}</div>
</div></section>

<section class="band white" id="hallazgos"><div class="inner">
  <div class="findings-wrap">
    <div class="findings-head">
      <span class="chip chip-lav">Hallazgos</span>
      <h2>A veces el problema <span class="hand-o">no es{LOOP}</span> el que parece</h2>
      <p>Cinco cosas que solo aparecieron al escuchar a las personas que usan y sostienen el servicio, y lo que cambiaron.</p>
    </div>
    <div class="findings">
      <a class="finding reveal acc-sky" href="caso-energia.html"><span class="fnum">01</span><div><span class="chip chip-sky">Energía</span><h3>En energía, la confianza pesaba más que el precio.</h3><p>Las pymes no querían cambiar de proveedor, pero sí sentir que su gestor no se olvidaba de ellas. Por eso una de las prioridades fue convertir la atención al cliente en un «gestor remoto».</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-lav" href="caso-ong.html"><span class="fnum">02</span><div><span class="chip chip-lav">Tercer sector</span><h3>La web estaba ordenada como la ONG, no como piensa quien quiere donar.</h3><p>Tenía unas 32 secciones repartidas por departamentos. Las reordenamos en tres bloques que cualquiera entiende: quién somos, qué hacemos y cómo colaborar.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-sky" href="caso-farma.html"><span class="fnum">03</span><div><span class="chip chip-sky">Salud</span><h3>Un paciente crónico no quiere superar la enfermedad. Quiere llevar una vida normal.</h3><p>Lo emocional pesa tanto como lo físico. De ahí salieron un registro de emociones en el centro de la app y un «modo brote» con menos avisos y ayuda directa.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-lav" href="caso-diabetes.html"><span class="fnum">04</span><div><span class="chip chip-lav">Salud digital</span><h3>Ninguna usuaria reconoció su propio sensor por su sigla.</h3><p>Quien acaba de recibir el diagnóstico no habla en siglas técnicas. Antes del lanzamiento, la app cambió «CGM» por palabras del paciente, como «sensor».</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-sky" href="caso-ia.html"><span class="fnum">05</span><div><span class="chip chip-sky">Adopción de IA</span><h3>Para decidir qué IA construir, primero hay que ver en qué se va el tiempo.</h3><p>Preparar una reunión con una cuenta nueva llevaba de 30 a 60 minutos de búsqueda. Las prioridades salieron de tareas reales como esa, no de la tecnología disponible.</p><span class="go">Ver el caso</span></div></a>
    </div>
  </div>
</div></section>

<section class="band" id="sobre-mi"><div class="inner">
  <div class="about">
    <div class="photo"><img src="{v(PHOTO)}" alt="Retrato de Gema Díez sonriendo" width="400" height="400"><span class="note n-about">¡hola, soy yo!{ARROW_DOWN}</span></div>
    <div class="bio">
      <span class="chip chip-lav">Sobre mí</span>
      <p class="lead">Soy Gema Díez, Service Designer estratégica con más de 8 años trabajando en servicios complejos.</p>
      <p>He trabajado en energía, banca, salud, seguros, retail y tercer sector. Mi trabajo empieza donde las cosas están fragmentadas, con plataformas que no se hablan, equipos con visiones distintas y mensajes que no llegan, y termina cuando funcionan como un solo servicio.</p>
      <p>Mapeo cómo son las cosas de verdad, escuchando a las personas y leyendo los datos, decido qué no puede fallar y ayudo a que todo el equipo empuje en la misma dirección.</p>
      <ul class="facts-list">
        <li><b>+8 años</b><span>En diseño de servicios, investigación y experiencia de cliente</span></li>
        <li><b>Docente desde 2023</b><span>Mentora de Design y User Research en Uxer School</span></li>
        <li><b>4 países europeos</b><span>Investigación internacional con equipos y usuarios en varios mercados</span></li>
        <li><b>Ciencias Políticas</b><span>De ahí viene mi forma de pensar en sistemas</span></li>
      </ul>
    </div>
  </div>
  <div class="mentor reveal">
    <div class="mentor-score">
      <span class="chip chip-lav">Como docente</span>
      <b>9,58</b>
      <p>de valoración de mi alumnado en las clases de research.</p>
      <span class="note n-mentor">lo dicen mis alumnos/as{ARROW_DOWN}</span>
    </div>
    <div class="mentor-quotes">
      <blockquote><p>Es muy atenta y divertida, se nota que se preocupa por cada uno y dedica tiempo a cada grupo!</p></blockquote>
      <blockquote><p>Lo mejor de esta materia, da gusto encontrarse con una persona con tanto conocimiento</p></blockquote>
      <blockquote><p>Genial instrucciones, explicaciones, actitud... Mis dieses</p></blockquote>
      <a class="link mentor-src" href="https://lnkd.in/p/dmYyr5pn" target="_blank" rel="noopener">Ver la publicación de la escuela en LinkedIn ↗</a>
    </div>
  </div>
</div></section>

<section class="band white" id="contacto"><div class="inner">
  <div class="sec-head"><span class="chip chip-sky">Contacto</span><h2>Si tu servicio tiene muchas piezas y no sabes por dónde empezar, empiezo yo.</h2></div>
  <div class="doors">
    <div class="door">
      <span class="label">Para proyectos</span>
      <h3>Cuéntame tu proyecto</h3>
      <p>Escríbeme con el reto que tienes entre manos. Te respondo con una primera idea de por dónde empezaría.</p>
      <div class="mail"><code id="email">gd.glez@gmail.com</code><button class="btn btn-primary" id="copy-email" type="button">Copiar email</button></div>
      <p class="copy-status" id="copy-status" aria-live="polite"></p>
    </div>
    <div class="door">
      <span class="label">Para empresas</span>
      <h3>Ver mi trayectoria</h3>
      <p>Si buscas una Service Designer senior que piense en negocio y lidere proyectos de principio a fin, aquí tienes mi recorrido.</p>
      <div class="ctas"><a class="btn btn-secondary" href="https://www.linkedin.com/in/gema-d%C3%ADez-gonz%C3%A1lez-74157943/" target="_blank" rel="noopener">LinkedIn</a><span class="soon">CV en PDF, próximamente</span></div>
    </div>
  </div>
</div></section>
</main>
<div class="solo-back"><div class="inner"><a class="btn btn-secondary" href="#inicio">← Ver la web completa</a></div></div>
{FOOT}
<script>
(function(){{
  var b=document.getElementById('copy-email'), s=document.getElementById('copy-status'), e=document.getElementById('email');
  function fallback(){{var r=document.createRange();r.selectNodeContents(e);var sel=window.getSelection();sel.removeAllRanges();sel.addRange(r);s.textContent='Email seleccionado. Cópialo con Ctrl+C o Cmd+C.';}}
  b.addEventListener('click',function(){{
    if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(e.textContent).then(function(){{s.textContent='Email copiado.';}}).catch(fallback);}} else {{fallback();}}
  }});
}})();
</script>
</body>
</html>
'''

open(os.path.join(OUT, "index.html"), "w").write(INDEX)
for i, c in enumerate(CASES):
    open(os.path.join(OUT, c["slug"] + ".html"), "w").write(case_page(i, c))
print("ok")
