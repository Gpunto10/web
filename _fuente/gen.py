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

def key(x): return f'<p class="key">{x}</p>'
def ul(items): return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ol(items): return '<ol class="ol">' + "".join(f"<li><div>{i}</div></li>" for i in items) + "</ol>"
def p(*xs): return "".join(f"<p>{x}</p>" for x in xs)

CASES = [
dict(
 slug="caso-energia", tag="Energía · B2B y B2C",
 card="De vender productos a vender una relación",
 card_lede="Research con clientes, comerciales y canal para convertir una estrategia en decisiones de negocio.",
 facts=["+60 oportunidades priorizadas", "3 decálogos por canal", "2024–25"],
 h1="Empresa energética: de vender productos a vender una relación",
 lede="Convertimos una estrategia de negocio en un backlog priorizado, un customer journey con KPIs y principios de experiencia para cada canal.",
 sheet=[("Cliente","Empresa energética"),("Sector","Energía B2B y B2C"),("Cuándo","De septiembre de 2024 a mayo de 2025, en tres fases"),("Equipo","Otra Service Designer y yo, con apoyo de UX")],
 reto=key("Pasar de vender productos sueltos a ofrecer una solución energética integral, sin más fuerza comercial.") + ul([
   "Cada línea de negocio tenía su flujo, su gestor y su canal.",
   "Un mismo cliente podía tener varios gestores.",
   "Objetivo: que los clientes contrataran más energías y captar pymes, con más peso de lo digital."]),
 rol=key("Research y Service Design a partes iguales con otra Service Designer.") + ul([
   "Entrevistas y síntesis.",
   "Mapa de la experiencia actual del cliente.",
   "Facilitación de todos los workshops con negocio."]),
 enfoque=key("Escuchamos a los tres actores del servicio: clientes, equipos internos y canal.") + ul([
   "Entrevistas a pymes de distintos sectores.",
   "Entrevistas a gestores comerciales, canal de distribución y atención al cliente.",
   "Mapa de procesos y comparativa de los funnels de negocio, ventas y cliente.",
   "Workshops para priorizar oportunidades y diseñar el servicio por tipo de cliente."]),
 hallazgos=key("La confianza pesa más que el precio.") + ul([
   "El cliente no quiere cambiar de proveedor, pero tampoco que se olviden de él.",
   "Segmentar por tamaño y sector no basta: importa cómo se relaciona cada cliente con el servicio.",
   "Para los equipos internos, el cambio transforma todo su día a día.",
   "El onboarding define el equilibrio entre trato humano y digital de toda la relación."]),
 quote=None,
 entregables=ul([
   "Customer journey B2B con KPIs por fase.",
   "Tres arquetipos de cliente con su propuesta de valor.",
   "Backlog de oportunidades y roadmap estratégico.",
   "Primeras soluciones digitales: mejoras del CRM y wireframes del portal de cliente."]),
 traduccion=key("Las oportunidades se convirtieron en decisiones de negocio y en diseño.") + ul([
   "Negocio priorizó las oportunidades en un workshop, como un onboarding digital o una atención remota para pymes.",
   "Los arquetipos sirvieron para diseñar el servicio por tipo de cliente.",
   "Los hallazgos alimentaron el portal de cliente y las mejoras del CRM.",
   "El cliente amplió el proyecto dos veces."]),
 extra=("Extensión B2C", "Principios de experiencia en cada canal",
   key("Tres workshops con equipos de atención telefónica, estaciones de servicio y oficinas.") + ul([
     "Bajamos los principios de la nueva marca a los momentos clave del journey.",
     "Resultado: un decálogo de experiencia por canal, con acciones que el propio empleado puede aplicar."]) + "@@WORKSHOP@@"),
),
dict(
 slug="caso-ong", tag="Tercer sector · Captación",
 card="Una web que deje de reflejar el organigrama",
 card_lede="Diagnóstico y co-creación para que toda la organización compartiera una misma visión de su web.",
 facts=["Menú de 32 secciones a 3 bloques", "5 áreas alineadas", "2026"],
 h1="ONG internacional de infancia: una web que deje de reflejar el organigrama",
 lede="Alineamos a toda la organización en una visión común de su web y la convertimos en un nuevo menú, wireframes con requisitos claros y una propuesta para su comité interno.",
 sheet=[("Cliente","Delegación española de una ONG internacional de infancia"),("Sector","Tercer sector, captación de fondos"),("Cuándo","2026, en dos fases"),("Equipo","Research y estrategia llevados por mí")],
 reto=key("Rediseñar la web para que dejara de reflejar el organigrama.") + ul([
   "La web había crecido a base de soluciones puntuales.",
   "Cada departamento tenía su propio espacio en el menú.",
   "La mayoría de visitas llegaban desde el móvil, donde navegar era lo más difícil."]),
 rol=key("Llevé yo todo el research y la estrategia.") + ul([
   "Entrevistas, auditoría heurística y benchmark.",
   "Diseño y facilitación del workshop.",
   "Arquetipos, journeys y nueva arquitectura de la información."]),
 enfoque="<h3>Fase 1 · Entender</h3>" + ul([
   "Entrevistas con todas las áreas.",
   "Auditoría con las 10 heurísticas de Nielsen.",
   "Benchmark con otras ONG.",
   "Diagnóstico emocional y de storytelling."]) +
   "<h3>Fase 2 · Co-crear</h3>" + ul([
   "Workshop con las áreas para construir arquetipos y journey.",
   "Dos arquetipos de donante: <em>el continuista</em> y <em>la concienciada</em>.",
   "Nueva arquitectura del menú, validada con las áreas y testada después con card sorting."]),
 hallazgos=key("La web reflejaba cómo estaba organizada la ONG, no lo que necesitaba quien quería colaborar.") + ul([
   "Cada parte parecía una web distinta.",
   "Donar era el paso con más fricción.",
   "Había dudas sobre el destino de la ayuda.",
   "El equipo editorial dependía de tecnología para publicar.",
   "Todas las áreas querían lo mismo: facilitar la vida al donante."]),
 quote=("La web refleja cómo estamos organizados, no lo que el usuario necesita.", "Persona de la organización"),
 entregables=ul([
   "Diagnóstico, evaluación heurística y benchmark.",
   "Arquetipos de donante y su journey.",
   "Nueva arquitectura del menú y de la home.",
   "Requisitos y primeros wireframes.",
   "Presentación al comité interno."]) + "@@ONG@@",
 traduccion=key("Un acuerdo de toda la casa y un menú pensado para el donante.") + ul([
   "Todas las áreas compartieron una definición de éxito: donar con menos pasos, entender qué hace la ONG y publicar sin fricción.",
   "El menú pasó de secciones por departamento a tres bloques: quién somos, qué hacemos y cómo colaborar.",
   "Los fallos de la auditoría se convirtieron en reglas para los wireframes.",
   "Nuevas vías de colaboración para quien tiene poco dinero y mucho compromiso.",
   "El comité interno aprobó el nuevo menú y la web nueva sale en 2027.",
   "Sigo trabajando en el proyecto: el cliente ha contratado nuevas fases."]),
 extra=None,
),
dict(
 slug="caso-ia", tag="Adopción de IA · Workshop",
 card="Un formato, dos contextos: decidir qué IA construir primero",
 card_lede="Un workshop que parte del día a día de las personas, no de la tecnología.",
 facts=["5 bloques de trabajo", "6 prioridades por impacto", "2 equipos"],
 h1="Workshop de adopción de IA: un formato, dos contextos",
 lede="Diseñé un formato de workshop que empieza por el trabajo real, no por la tecnología. Lo aplicamos con dos equipos muy distintos y en los dos salió una lista de prioridades.",
 sheet=[("Contexto 1","Equipo de compras de una fintech internacional"),("Contexto 2","Equipo comercial que vende una suite de IA"),("Formato","Sesiones de 90 minutos a 2 horas"),("Equipo","Una Senior UX Designer y yo")],
 reto=key("Las empresas tienen IA, pero la usan para cosas sueltas.") + ul([
   "Redactar correos o resumir textos no cambia el trabajo.",
   "Había que encontrar dónde aporta valor real y qué resolver primero."]) +
   '<p class="premise">«Hoy no venimos a ver otra demo: venimos a construir la vuestra.»</p>',
 rol=key("Diseñé el formato y lo facilité junto a una UX Designer.") + ul([
   "Dinámicas y materiales.",
   "Facilitación.",
   "Síntesis y presentación de resultados."]),
 enfoque=key("Cinco bloques que van del día a día a la prioridad.") + ol([
   "<strong>Su día a día:</strong> las tareas que más tiempo roban.",
   "<strong>Fricciones:</strong> lo repetitivo, lo disperso y lo que se pierde entre áreas.",
   "<strong>Su IA hoy:</strong> para qué la usan y dónde se queda corta.",
   "<strong>Escenarios:</strong> «¿me sirve a mí?» y «¿le serviría a un cliente?».",
   "<strong>Cierre:</strong> su IA ideal, lo que nunca debería hacer y una prioridad por persona."]),
 hallazgos=key("El tiempo se va en tareas administrativas, no en el trabajo de valor.") + ul([
   "Herramientas que no hablan entre sí duplican el trabajo.",
   "Buscar información dispersa ocupa buena parte del día.",
   "La IA genérica se queda corta porque no conoce el contexto interno.",
   "Hay desconfianza: no debe inventar ni actuar sin supervisión."]),
 quote=("Se inventa algo antes de admitir que no sabe.", "Persona del equipo comercial"),
 entregables=ul([
   "Formato de workshop reutilizable: agenda, dinámicas y plantillas.",
   "Tableros de trabajo de cada sesión.",
   "Informe de discovery con dolores, usos actuales y prioridades."]),
 traduccion=key("En los dos equipos salió una hoja de prioridades sobre la que construir.") + ul([
   "<strong>Fintech:</strong> prioridades ordenadas por impacto y un documento de adopción.",
   "<strong>Equipo comercial:</strong> la demo a medida parte de los escenarios que votó el propio equipo.",
   "<strong>En marcha:</strong> ya se están construyendo soluciones a medida.",
   "<strong>Un método repetible</strong> para pasar de «tenemos IA» a «sabemos qué resolver primero»."]),
 extra=None,
),
dict(
 slug="caso-farma", tag="Salud · App de pacientes",
 card="Una app que acompañe al paciente, no solo a su tratamiento",
 card_lede="Entrevistas y test con pacientes crónicos para mejorar la app hoy y orientar su hoja de ruta.",
 facts=["5 etapas de journey", "4 arquetipos de paciente", "2025"],
 h1="Farmacéutica internacional: una app que acompañe al paciente, no solo a su tratamiento",
 lede="Escuchar a pacientes crónicos dio dos resultados: mejoras de diseño inmediatas y una hoja de ruta organizada por etapas del journey y tipos de paciente.",
 sheet=[("Cliente","Farmacéutica internacional"),("Sector","Salud, app para pacientes"),("Año","2025"),("Equipo","Yo, de principio a fin")],
 reto=key("Saber si la app encajaba con lo que de verdad necesitan los pacientes.") + ul([
   "App para pacientes con enfermedades crónicas.",
   "Dos objetivos: entender al paciente y probar la app en manos reales."]),
 rol=key("Llevé el proyecto sola, de principio a fin.") + ul([
   "Diseño del estudio y del reclutamiento.",
   "Entrevistas y tests.",
   "Journey, arquetipos y recomendaciones."]),
 enfoque=key("Entrevistas en profundidad que combinaban la historia del paciente y el test de la app.") + ul([
   "Una parte para entender el recorrido con la enfermedad y la mayor parte para probar la app.",
   "Muestra diversa en enfermedad, edad y tiempo desde el diagnóstico.",
   "Test de cada sección de la app."]),
 hallazgos=key("El paciente no quiere superar la enfermedad. Quiere llevar una vida normal.") + ul([
   "El journey no es lineal: tras el tratamiento, las etapas se repiten.",
   "Lo emocional pesa tanto como lo físico.",
   "No hay un paciente único: lo que le sirve depende de su momento y de su forma de ser.",
   "Valoraban lo que les ahorra esfuerzo y se perdían con los nombres poco claros.",
   "Echaban de menos la conexión con su sistema sanitario."]),
 quote=("Cuando oyes “crónica”, todo se te cae encima.", "Paciente entrevistado"),
 entregables=ul([
   "Patient journey en cinco etapas.",
   "Cuatro arquetipos de paciente.",
   "Evaluación de usabilidad por sección.",
   "Oportunidades por etapa y por arquetipo."]) + "@@FARMA@@",
 traduccion=key("Mejoras para aplicar ya y una hoja de ruta para crecer.") + ul([
   "Cambios de diseño concretos: nombres más claros, un solo camino para los recordatorios y lo emocional en el centro.",
   "Proteger lo que mejor funcionaba.",
   "Nuevas ideas por etapa, como un «modo brote» con menos avisos y ayuda directa.",
   "Criterios para adaptar la app a cada tipo de paciente.",
   "El cliente amplió el proyecto."]),
 extra=None,
),
dict(
 slug="caso-diabetes", tag="Salud digital · Diabetes",
 card="Validar una app de diabetes antes de lanzarla",
 card_lede="Un test con usuarias de un prototipo: qué funcionaba y qué ajustar antes del lanzamiento.",
 facts=["1 necesidad sin cubrir, validada", "5 ajustes antes de lanzar", "2024"],
 h1="Startup de salud digital: validar una app de diabetes antes de lanzarla",
 lede="El test confirmó que la app resolvía una necesidad que nadie cubría y señaló los ajustes de lenguaje, flujo y accesibilidad antes de lanzarla.",
 sheet=[("Cliente","Startup de salud digital"),("Producto","App y dispositivo para pacientes insulinodependientes"),("Año","2024"),("Equipo","Yo, de principio a fin")],
 reto=key("Validar el prototipo antes de seguir desarrollando.") + ul([
   "La app se conecta con la pluma de insulina y con los medidores de glucosa.",
   "¿Se entendían el primer uso y el panel? ¿Respondían a lo que necesita el paciente?"]),
 rol=key("Llevé el proyecto sola, de principio a fin.") + ul([
   "Diseño del test y de las tareas.",
   "Sesiones con usuarias.",
   "Análisis, informe y recomendaciones."]),
 enfoque=key("Un test de usabilidad que simula dos momentos de vida del producto.") + ul([
   "<strong>Primer uso:</strong> crear el perfil y vincular los dispositivos.",
   "<strong>Tres meses después:</strong> entender el panel con datos acumulados.",
   "Conversación sobre cómo es vivir con diabetes."]),
 hallazgos=key("La app resolvía algo que nadie cubría: saber cuándo y cuánto te has medicado.") + ul([
   "Tras el diagnóstico, el paciente reaprende su día a día casi solo.",
   "Su información está repartida en varias apps.",
   "El primer uso era claro y conectar los dispositivos sorprendía para bien.",
   "El lenguaje técnico no funcionaba y algunas secciones eran ambiguas.",
   "La accesibilidad era crítica para este público."]),
 quote=("A menudo no sé si me he pinchado o no.", "Usuaria del test"),
 entregables=ul([
   "Informe con evaluación pantalla a pantalla.",
   "Oportunidades y recomendaciones.",
   "Análisis de la arquitectura de la información."]) + "@@EVAL@@",
 traduccion=key("Base para seguir desarrollando y una lista clara de ajustes.") + ul([
   "La propuesta de valor quedó validada.",
   "Cinco ajustes antes del lanzamiento:" + '<ul class="sublist"><li>agrupar el registro en bloques;</li><li>permitir varias respuestas sobre el tratamiento;</li><li>hablar con palabras del paciente;</li><li>aclarar qué se puede editar y qué no;</li><li>mejorar la accesibilidad.</li></ul>',
   "Ideas para la hoja de ruta: contenido médico fiable, conexión con el especialista y un canal de ayuda.",
   "La startup amplió el proyecto."]),
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
    <li class="show-s"><button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú"><span></span><span></span></button></li>
  </ul></nav>
</div>
<nav class="mnav" id="mnav" aria-label="Menú móvil"><ul>
  <li><a href="{prefix}#como-trabajo">Cómo trabajo</a></li>
  <li><a href="{prefix}#casos">Casos</a></li>
  <li><a href="{prefix}#sobre-mi">Sobre mí</a></li>
</ul></nav>
</header>'''


# Chat de contacto. Para que llegue a tu email, pega aquí la clave de Web3Forms (web3forms.com).
# Mientras esté vacía, el chat abre el programa de correo con el mensaje ya escrito.
CHAT_KEY = "846b664b-7e4f-4e66-84b3-b6f36242411f"
CHAT = ('<div class="chat" id="chat" data-key="' + CHAT_KEY + '" data-mail="gd.glez@gmail.com">'
  '<button class="chat-fab" type="button" aria-expanded="false" aria-controls="chat-panel"><img src="' + v(PHOTO) + '" alt=""><span>Hablemos</span></button>'
  '<section class="chat-panel" id="chat-panel" role="dialog" aria-label="Escríbeme" hidden>'
  '<header class="chat-head"><img src="' + v(PHOTO) + '" alt=""><div><b>Gema Díez</b><span>Te respondo por email</span></div>'
  '<button class="chat-x" type="button" aria-label="Cerrar chat">✕</button></header>'
  '<div class="chat-log" aria-live="polite"><p class="bub them">¡Hola! Soy Gema 👋</p><p class="bub them">Cuéntame tu proyecto, tu reto o tu duda y te contesto por email.</p></div>'
  '<form class="chat-form" novalidate>'
  '<textarea name="message" rows="3" placeholder="Escribe tu mensaje…" required aria-label="Mensaje"></textarea>'
  '<div class="chat-row"><input name="name" placeholder="Tu nombre" autocomplete="name" required aria-label="Nombre"><input name="email" type="email" placeholder="Tu email" autocomplete="email" required aria-label="Email"></div>'
  '<input type="checkbox" name="botcheck" class="chat-hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
  '<p class="chat-err" role="alert"></p>'
  '<button class="btn btn-primary chat-send" type="submit">Enviar</button></form>'
  '</section></div>')

FOOT = '<footer class="band foot"><div class="inner"><span>© 2026 Gema Díez · Madrid</span><span>Service Designer estratégica</span></div></footer>\n<a class="totop" id="totop" href="#" aria-label="Volver arriba" title="Volver arriba"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></a>\n' + CHAT + '\n<script src="' + v('site.js') + '" defer></script>'

ICONS = {
 "sistema": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><path d="M24 8 A16 16 0 0 0 24 40" stroke="#161616"/><path d="M26 8 A16 16 0 0 1 26 40" stroke="#A99BE8" stroke-width="2"/></svg>',
 "piezas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><g stroke="#161616"><path d="M12 12 L36 14 M12 12 L14 36 M36 14 L34 34 M14 36 L34 34 M12 12 L34 34"/><circle cx="12" cy="12" r="4" fill="#FFFFFF"/><circle cx="36" cy="14" r="4" fill="#FFFFFF"/><circle cx="14" cy="36" r="4" fill="#FFFFFF"/></g><circle cx="34" cy="34" r="5" stroke="#78BAE6" stroke-width="2" fill="#FFFFFF"/></svg>',
 "personas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><circle cx="18" cy="24" r="12" stroke="#161616"/><circle cx="30" cy="24" r="12" stroke="#78BAE6" stroke-width="2"/></svg>',
}

# Cifras de la cabecera de cada caso: dato grande + etiqueta, sin caja (no deben parecer botones)
STATS = {
 "caso-energia": [("+60", "oportunidades priorizadas"), ("3", "perfiles de cliente"), ("3", "decálogos por canal")],
 "caso-ong": [("32 → 3", "secciones del menú"), ("5", "áreas alineadas"), ("2", "arquetipos de donante")],
 "caso-ia": [("5", "bloques del formato"), ("6", "prioridades por impacto"), ("2", "equipos, un método")],
 "caso-farma": [("5", "etapas del journey"), ("4", "arquetipos de paciente"), ("2", "horizontes de mejora")],
 "caso-diabetes": [("1", "necesidad validada"), ("2", "momentos de uso"), ("5", "ajustes antes de lanzar")],
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
  <span class="card-top"><span class="cnum">{k+1:02d}</span><span class="tag">{c['tag']}</span></span>
  <div><h3>{c['card']}</h3><p class="lede">{c['card_lede']}</p></div>
  <div class="facts">{facts}</div>
  <span class="card-foot"><span class="go">Leer el caso</span><span class="owner">Proyecto de Sngular</span></span>
</a>'''


EVAL_SCREENS = [
  ("Creación de cuenta", "Crear cuenta", "Accesibilidad", "Contraste y tamaño de letra insuficientes para quien pierde visión.", "hot-a"),
  ("Perfilado", "Tu perfil", "Arquitectura", "Agrupar el registro en bloques: perfil, dispositivos y documentación.", "hot-b"),
  ("Vinculación del dispositivo", "Vincular", "Lenguaje", "Las siglas técnicas confunden: mejor las palabras del paciente.", "hot-c"),
  ("Tratamiento", "Tratamiento", "Interacción", "La pregunta de tratamiento debe permitir varias respuestas.", "hot-d"),
]
def eval_demo():
    screens, notes, dots = [], [], []
    for i, (sec, title, kind, text, hot) in enumerate(EVAL_SCREENS, 1):
        if i == 3:
            body = '<span class="ph-qr"></span><i class="sk w70"></i><i class="sk w50"></i>'
        elif i == 4:
            body = '<span class="ph-opt"></span><span class="ph-opt"></span><span class="ph-opt"></span><i class="sk w60"></i>'
        else:
            body = '<i class="sk w80"></i><i class="sk w60"></i><span class="ph-field"></span><span class="ph-field"></span><span class="ph-field"></span>'
        screens.append(f'<div class="ph-screen e{i}"><span class="ph-bar"></span><b class="ph-title">{title}</b>{body}<span class="ph-btn">Continuar</span><span class="ph-hot {hot}"></span></div>')
        notes.append(f'<div class="ev-note e{i}"><span class="ev-k">Pantalla {i} · {sec}</span><span class="ev-tag">{kind}</span><p>{text}</p><i class="sk w90"></i><i class="sk w60"></i></div>')
        dots.append(f'<span class="e{i}"></span>')
    return ('<figure class="eval" aria-label="Recreación animada de la evaluación pantalla a pantalla">'
            '<div class="eval-stage"><div class="phone" aria-hidden="true">' + "".join(screens) + '</div>'
            '<div class="ev-notes">' + "".join(notes) + '</div></div>'
            '<div class="ev-dots" aria-hidden="true">' + "".join(dots) + '</div>'
            '<figcaption>Así era la evaluación detallada: cada pantalla del prototipo, con lo que falla y cómo mejorarlo. Recreación esquemática.</figcaption></figure>')


def workshop_demo():
    import random
    rnd = random.Random(7)
    cols = ["Repostaje", "Pago", "Contrato", "Dudas"]
    head = '<span class="wk-corner"></span>' + "".join(f'<span class="wk-col">{c}</span>' for c in cols)
    rows = ""
    for r in range(3):
        rows += f'<span class="wk-row"><span class="lng">Principio&nbsp;</span><span class="sht">P</span>{r+1}</span>'
        for c in range(4):
            n = rnd.randint(2, 5)
            its = "".join(f'<i class="pi g{rnd.randint(1,5)}" style="--d:{rnd.uniform(.2,5.2):.2f}s;--r:{rnd.uniform(-7,7):.1f}deg"></i>' for _ in range(n))
            rows += f'<span class="wk-cell">{its}</span>'
    legend = "".join(f'<span><i class="pi g{g}"></i>Grupo {g}</span>' for g in range(1, 6))
    deca = "".join(f'<li style="--d:{5.6 + k*0.32:.2f}s"><b>{k:02d}</b><i class="sk w{rnd.choice([60,70,80,90])}"></i></li>' for k in range(1, 11))
    return ('<figure class="eval wk" aria-label="Recreación animada del workshop: los grupos llenan la matriz y sale el decálogo">'
            '<div class="wk-stage"><div class="wk-board" aria-hidden="true">' + head + rows + '</div>'
            '<div class="wk-flip" aria-hidden="true"><span class="ev-k">Decálogo de experiencia</span><ol>' + deca + '</ol></div></div>'
            '<div class="wk-legend" aria-hidden="true">' + legend + '</div>'
            '<figcaption>Cinco grupos bajan cada principio de marca a los momentos clave, y de ahí sale el decálogo de cada canal. Recreación esquemática.</figcaption></figure>')


def farma_demo():
    stages = ["Inicio de síntomas", "Diagnóstico", "Adaptación al tratamiento", "Vida con la enfermedad", "Brotes y recaídas"]
    st = "".join(f'<li class="jy-s s{i}" style="--d:{(i-1)*0.9:.1f}s"><b>{i}</b><span>{t}</span></li>' for i, t in enumerate(stages, 1))
    journey = ('<figure class="eval jy" aria-label="Journey del paciente en cinco etapas, cíclico desde la tercera">'
               '<span class="ev-k">Patient journey</span><ol class="jy-row">' + st + '</ol>'
               '<svg class="jy-loop" viewBox="0 0 300 40" preserveAspectRatio="none" aria-hidden="true"><path d="M30 6 C 30 34, 270 34, 270 6" pathLength="1"/><path class="jy-head" d="M262 12 L270 4 L276 14" pathLength="1"/></svg>'
               '<p class="jy-note">Hasta el diagnóstico el camino es lineal. Desde el tratamiento, las etapas se repiten y se solapan.</p>'
               '<figcaption>Recreación esquemática del journey.</figcaption></figure>')
    bars = [("Estabilidad", 3), ("Impacto en su vida", 5), ("Expertise", 4), ("Apertura a aprender", 3)]
    br = "".join(f'<div class="ar-v"><span>{n}</span><span class="ar-dots">' + "".join(f'<i class="{"on" if k < v else ""}" style="--d:{0.15*k + 0.4*j:.2f}s"></i>' for k in range(5)) + '</span></div>' for j, (n, v) in enumerate(bars))
    face = ('<svg class="ar-face doodle draw" viewBox="0 0 160 160" aria-hidden="true">'
            '<path pathLength="1" d="M52 70 C 46 36, 74 22, 92 26 C 116 30, 124 52, 116 78 C 112 96, 100 108, 82 108 C 64 108, 56 92, 52 70 Z"/>'
            '<path pathLength="1" d="M48 66 C 50 30, 112 18, 122 62 C 112 46, 86 40, 64 50 C 58 54, 52 60, 48 66"/>'
            '<path pathLength="1" d="M62 68 a 10 10 0 1 0 20 0 a 10 10 0 1 0 -20 0 M 90 68 a 10 10 0 1 0 20 0 a 10 10 0 1 0 -20 0 M 82 68 L 90 68"/>'
            '<path pathLength="1" d="M76 92 C 82 96, 90 96, 96 92"/>'
            '<path pathLength="1" d="M70 106 L 68 120 C 40 124, 26 140, 22 158 M 98 106 L 100 120 C 128 124, 140 140, 144 158"/>'
            '</svg>')
    arch = ('<figure class="eval ar" aria-label="Ficha de arquetipo de paciente">'
            '<div class="ar-id">' + face + '<span class="ev-k">Arquetipo</span><h4>La perfeccionista</h4>'
            '<p>Conoce su enfermedad al detalle, contrasta lo que lee y quiere tenerlo todo bajo control. Cuando algo se le escapa, lo vive con culpa.</p></div>'
            '<div class="ar-body"><div class="ar-q"><span class="ar-k">Quiere</span><p>Una herramienta seria, fiable y exacta.</p></div>'
            '<div class="ar-q"><span class="ar-k">Necesita</span><p>Sentir que tiene el control y confirmar que lo está haciendo bien.</p></div>'
            '<div class="ar-vars">' + br + '</div></div>'
            '<figcaption>Uno de los cuatro arquetipos. Recreación con nombre y datos modificados.</figcaption></figure>')
    return journey + arch


def ong_demo():
    notes = [("La vía para colaborar queda en el tercio inferior, sin el peso que merece.", "d"),
             ("Iconos y botones sin una lógica visual común.", "d"),
             ("Bloques seguidos con el mismo fondo: se lee como texto corrido.", "d"),
             ("En móvil, el scroll es larguísimo y un botón fijo tapa el contenido.", "m"),
             ("El menú apenas se ve y los elementos se apilan.", "m")]
    pins = "".join(f'<span class="ex-pin p{i}" style="--d:{(i-1)*2}s">{i}</span>' for i in range(1, 6))
    nl = "".join(f'<li style="--d:{(i-1)*2}s"><b>{i}</b><span>{t}</span></li>' for i, (t, _) in enumerate(notes, 1))
    desk = ('<div class="ex-desk"><span class="ex-chrome"><i></i><i></i><i></i></span>'
            '<span class="ex-hero"></span><span class="ex-row3"><i></i><i></i><i></i></span>'
            '<span class="ex-band"></span><span class="ex-band"></span><span class="ex-row4"><i></i><i></i><i></i><i></i></span><span class="ex-foot"></span></div>')
    mob = ('<div class="ex-mob"><span class="ex-mbar"></span><span class="ex-hero"></span><span class="ex-band"></span><span class="ex-band"></span>'
           '<span class="ex-band"></span><span class="ex-sticky"></span></div>')
    evalx = ('<figure class="eval ex" aria-label="Recreación animada de la evaluación experta de la home">'
             '<span class="ev-k">Evaluación experta · Home</span>'
             '<div class="ex-stage" aria-hidden="true">' + desk + mob + pins + '</div>'
             '<ol class="ex-notes">' + nl + '</ol>'
             '<figcaption>Cada punto marcado en la home, en escritorio y en móvil, con su explicación. Recreación esquemática.</figcaption></figure>')
    cards = [("Actividad 1", "El futuro colaborador", "Definir quién es, qué le mueve a colaborar y qué le frena."),
             ("Actividad 2", "Happy path", "Dibujar el recorrido ideal, desde que descubre la causa hasta que colabora."),
             ("Actividad 3", "Arquitectura", "Ordenar los contenidos del menú pensando en esa persona, no en los departamentos."),
             ("Cierre", "Puesta en común", "Cada grupo comparte lo suyo y se acuerdan los siguientes pasos.")]
    cs = "".join(f'<div class="fc c{i}"><span class="fc-k">{k}</span><h4>{t}</h4><p>{d}</p><span class="fc-m">Materiales</span><i class="sk w80"></i><i class="sk w60"></i></div>' for i, (k, t, d) in enumerate(cards, 1))
    deck = ('<figure class="eval fcs" aria-label="Fichas de las actividades del workshop">'
            '<span class="ev-k">Fichas del workshop</span><div class="fc-deck">' + cs + '</div>'
            '<figcaption>Las cuatro fichas que guiaron el workshop de co-creación. Recreación con textos resumidos.</figcaption></figure>')
    return evalx + deck


# Impacto de cada caso: solo resultados reales que constan en los documentos de Gema (nada supuesto)
IMPACT = {
 "caso-energia": ("El research se convirtió en la hoja de ruta del negocio.", [
   ("Decisiones de negocio", "Negocio priorizó qué construir a partir de las oportunidades: onboarding digital, atención remota para pymes y un CRM más sencillo."),
   ("Del papel al diseño", "Los hallazgos alimentaron el portal único de cliente y las mejoras del CRM para los equipos."),
   ("Dos ampliaciones", "El cliente amplió el proyecto dos veces, hasta llevar su nueva marca a cada canal de atención.")]),
 "caso-ong": ("El nuevo menú, aprobado. La web nueva, en 2027.", [
   ("Menú aprobado", "El comité interno aprobó el nuevo menú, pensado para el donante y no para el organigrama."),
   ("Web nueva en 2027", "La organización lanza su nueva web en 2027."),
   ("Sigo en el proyecto", "El diagnóstico llevó a nuevas fases, y sigo trabajando mano a mano con la responsable del proyecto.")]),
 "caso-ia": ("De «tenemos IA» a «sabemos qué construir primero».", [
   ("Prioridades claras", "La fintech salió con sus prioridades ordenadas por impacto y un documento de adopción."),
   ("Soluciones en construcción", "Ya se están construyendo soluciones a medida a partir de lo que salió en los workshops."),
   ("Un punto de partida", "Es un formato inicial: en una sola sesión, el equipo pasa de usos sueltos a saber qué resolver primero.")]),
 "caso-farma": ("Mejoras para hoy y una hoja de ruta para mañana.", [
   ("Mejoras listas para aplicar", "Cambios de diseño concretos para cada sección de la app."),
   ("Una hoja de ruta de producto", "Nuevas funcionalidades por etapa del journey y por tipo de paciente."),
   ("Una segunda fase", "El cliente contrató una nueva fase para evaluar también su web.")]),
 "caso-diabetes": ("Luz verde para seguir desarrollando.", [
   ("Propuesta de valor validada", "La app resolvía una necesidad que ninguna otra cubría."),
   ("Ajustes antes de lanzar", "Cinco cambios concretos de lenguaje, flujo y accesibilidad."),
   ("Nuevas fases", "La startup contrató más fases de las previstas.")]),
}

STEP_KIND = {"El reto": "reto", "Mi rol": "rol", "Enfoque": "enfoque", "Hallazgos clave": "hallazgos", "Entregables": "entregables", "En qué se tradujo": "tradujo"}

def step(n, title, body, white):
    kind = STEP_KIND[title]
    tone = " dark" if kind == "hallazgos" else (" white" if white else "")
    chip = "chip-sky" if n % 2 else "chip-lav"
    return f'''<section class="band step step-{kind}{tone}" id="{kind}"><div class="inner">
  <div class="step-head reveal"><span class="bignum" aria-hidden="true">{n:02d}</span><span class="chip {chip}">Paso {n:02d} de 06</span><h2>{title}</h2></div>
  <div class="prose">{body}</div>
</div></section>'''

def impact_html(c):
    head, items = IMPACT[c["slug"]]
    li = "".join(f'<li class="reveal" style="--d:{k*100}ms"><span class="imp-n">{k+1:02d}</span><b>{t}</b><span>{d}</span></li>' for k, (t, d) in enumerate(items))
    return f'''<section class="band impact" id="impacto"><div class="inner">
  <div class="imp-head"><span class="chip chip-sky">Impacto</span><h2>{head}</h2></div>
  <ul class="imp-list">{li}</ul>
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
        lab, h, body = c["extra"]; body = body.replace("@@WORKSHOP@@", workshop_demo())
        trad += f'<div class="extra"><span class="label">{lab}</span><h3>{h}</h3>{body}</div>'
    steps = [("El reto", c["reto"]), ("Mi rol", c["rol"]), ("Enfoque", c["enfoque"]), ("Hallazgos clave", hall), ("Entregables", c["entregables"].replace("@@EVAL@@", eval_demo()).replace("@@FARMA@@", farma_demo()).replace("@@ONG@@", ong_demo())), ("En qué se tradujo", trad)]
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
  <p class="owner-note"><span class="dot" aria-hidden="true"></span>Proyecto realizado como Senior Researcher y Service Designer en Sngular. El trabajo y sus entregables son propiedad de Sngular.</p>
</div></section>
{impact_html(c)}
{body}
<section class="band next"><div class="inner">
  <a class="next-case" href="{nxt['slug']}.html"><span class="label">Siguiente caso</span><h3>{nxt['card']}</h3></a>
  <a class="btn btn-primary" href="{nxt['slug']}.html">Siguiente →</a>
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
  <div class="sec-head"><span class="chip chip-sky">Casos · 2024 a 2026</span><h2>Qué descubrimos y en qué se tradujo</h2><p>Cinco proyectos de Service Design y Research que hice en Sngular. Los cuento por sector, sin marcas ni datos internos.</p></div>
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
      <a class="finding reveal acc-sky" href="caso-energia.html"><span class="fnum">01</span><div><span class="chip chip-sky">Energía</span><h3>La confianza pesa más que el precio.</h3><p>Los clientes valoraban sentirse acompañados más que pagar menos. La relación pasó al centro de la estrategia.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-lav" href="caso-ong.html"><span class="fnum">02</span><div><span class="chip chip-lav">Tercer sector</span><h3>La web estaba ordenada como la organización, no como piensa quien quiere colaborar.</h3><p>Reordenamos los contenidos en tres bloques que cualquiera entiende.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-sky" href="caso-farma.html"><span class="fnum">03</span><div><span class="chip chip-sky">Salud</span><h3>Un paciente crónico no quiere superar la enfermedad. Quiere llevar una vida normal.</h3><p>Lo emocional pesa tanto como lo físico, y la app tenía que reflejarlo.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-lav" href="caso-diabetes.html"><span class="fnum">04</span><div><span class="chip chip-lav">Salud digital</span><h3>El lenguaje técnico no significa nada para quien acaba de recibir un diagnóstico.</h3><p>Hablar con las palabras del paciente fue uno de los ajustes clave antes de lanzar.</p><span class="go">Ver el caso</span></div></a>
      <a class="finding reveal acc-sky" href="caso-ia.html"><span class="fnum">05</span><div><span class="chip chip-sky">Adopción de IA</span><h3>Para decidir qué IA construir, primero hay que ver en qué se va el tiempo.</h3><p>Las prioridades salieron de tareas reales del equipo, no de la tecnología disponible.</p><span class="go">Ver el caso</span></div></a>
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
