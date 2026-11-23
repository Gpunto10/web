import os, html
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(D)  # la web se genera en la raíz del repositorio
import base64
_raw = open(os.path.join(D, "photo.txt")).read().strip()
open(os.path.join(OUT, "foto.jpg"), "wb").write(base64.b64decode(_raw.split(",", 1)[1]))
PHOTO = "foto.jpg"
import hashlib
SOBRE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sobre.html"), encoding="utf-8").read()  # bloque personal (19 nov 2026)
MAPA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapa.html"), encoding="utf-8").read()  # mapa de alcance en nodos (prueba 19 nov 2026)
# Imagen del banner «No diseño píxeles». Rosa: img/nubes-pixeles.jpg · Azul: img/nubes-azules.jpg (prueba 20 nov 2026)
PX_IMG = "img/nubes-cobalto.jpg"  # antes img/nubes-azules.jpg (turquesa)
LAB = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab.html"), encoding="utf-8").read()  # sección Laboratorio · Hecho con IA (19 nov 2026)
def v(path):
    """Añade ?v=<huella> para que el navegador no muestre una versión guardada al cambiar el archivo."""
    return path + "?v=" + hashlib.md5(open(os.path.join(OUT, path), "rb").read()).hexdigest()[:8]

def key(x): return f'<p class="key">{x}</p>'
def ul(items): return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def ol(items): return '<ol class="ol">' + "".join(f"<li><div>{i}</div></li>" for i in items) + "</ol>"
def p(*xs): return "".join(f"<p>{x}</p>" for x in xs)

CASES = [
dict(
 slug="caso-relacion", tag="Segmentación y propuesta de valor",
 card="De vender productos a vender una relación",
 card_lede="Research con clientes, equipos comerciales y canal para convertir una estrategia en decisiones de negocio.",
 facts=[],
 h1="De vender productos a vender una relación",
 lede="Convertimos una estrategia de negocio en un backlog priorizado, un customer journey con KPIs y principios de experiencia para cada canal.",
 sheet=[("Cliente","Empresa de servicios para particulares y empresas"),("Duración","Tres fases"),("Equipo","Research y Service Design a partes iguales con otra Service Designer, con apoyo de UX")],
 reto=key("Pasar de vender productos sueltos a ofrecer una solución integral, sin más fuerza comercial.") + ul([
   "Cada línea de negocio tenía su flujo, su gestor y su canal.",
   "Un mismo cliente podía tener varios gestores.",
   "Objetivo: que los clientes contrataran más servicios y captar empresas pequeñas, con más peso de lo digital."]),
 decidi=ul([
   "La segmentación por tamaño y tipo de negocio no explicaba cómo se comportaba cada cliente. Propuse segmentar por su relación con el gestor y con lo digital, y construir los arquetipos sobre esa relación.",
   "Señalé que la empresa no tenía una definición común de su propia oferta. Sin ella, cada canal la contaba a su manera y no había una propuesta de valor coherente."]),
 enfoque=key("Escuchamos a los tres actores del servicio: clientes, equipos internos y canal.") + ul([
   "Entrevistas a clientes empresa de distinto perfil.",
   "Entrevistas a gestores comerciales, canal de distribución y atención al cliente.",
   "Mapa de procesos y comparativa de los funnels de negocio, ventas y cliente.",
   "Workshops para priorizar oportunidades y diseñar el servicio por tipo de cliente."]),
 hallazgos=key("La confianza pesa más que el precio.") + ul([
   "El cliente no quiere cambiar de proveedor, pero tampoco que se olviden de él.",
   "Segmentar por tamaño y actividad no basta: importa cómo se relaciona cada cliente con el servicio.",
   "Para los equipos internos, el cambio transforma todo su día a día.",
   "El onboarding define el equilibrio entre trato humano y digital de toda la relación."]),
 quote=None,
 entregables=ul([
   "Customer journey B2B con KPIs por fase.",
   "Arquetipos de cliente con su propuesta de valor.",
   "Backlog de oportunidades y roadmap estratégico.",
   "Primeras soluciones digitales: mejoras del CRM y wireframes del portal de cliente."]),
 deliv="customer journey con KPIs por fase, arquetipos por relación, backlog de oportunidades y roadmap.",
 traduccion=key("Del research al servicio, canal a canal.") + ul([
   "Los arquetipos sirvieron para diseñar el servicio por tipo de cliente: el reto fue llevar a los clientes más dependientes hacia más autonomía."]),
 extra=("Extensión B2C", "Principios de experiencia en cada canal",
   key("Workshops con los equipos que atienden al cliente en cada canal, en persona y por teléfono.") + ul([
     "Bajamos los principios de marca a los momentos clave del journey.",
     "Resultado: un decálogo de experiencia por canal, con acciones que el propio empleado puede aplicar."]) + "@@WORKSHOP@@"),
),
dict(
 slug="caso-web", tag="Ordenar una web por quien llega",
 card="Una web que deje de reflejar el organigrama",
 card_lede="Diagnóstico y co-creación para que toda la organización compartiera una misma visión de su web.",
 facts=[],
 h1="Una web que deje de reflejar el organigrama",
 lede="Alineamos a toda la organización en una visión común de su web y la convertimos en un nuevo menú, wireframes con requisitos claros y una propuesta para su dirección.",
 sheet=[("Cliente","Organización con muchas áreas y una web que había crecido sin un plan común"),("Duración","Dos fases"),("Equipo","Research y estrategia llevados por mí")],
 reto=key("Rediseñar la web para que dejara de reflejar el organigrama.") + ul([
   "La web había crecido a base de soluciones puntuales.",
   "Cada departamento tenía su propio espacio en el menú.",
   "La mayoría de visitas llegaban desde el móvil, donde navegar era lo más difícil."]),
 decidi=ul([
   "Ante un menú ordenado por departamentos, propuse reorganizar la web en tres bloques que cualquiera entiende: quiénes, qué y cómo.",
   "Sin criterios comunes, cada área defendía su espacio. Antes de hablar del menú, diseñé un workshop para que todas acordaran una misma definición de éxito."]),
 enfoque="<h3>Fase 1 · Entender</h3>" + ul([
   "Entrevistas con todas las áreas.",
   "Auditoría con las 10 heurísticas de Nielsen.",
   "Benchmark con organizaciones parecidas.",
   "Diagnóstico emocional y de storytelling."]) +
   "<h3>Fase 2 · Co-crear</h3>" + ul([
   "Workshop con las áreas para construir arquetipos y journey.",
   "Dos territorios de conquista: lo racional y lo emocional.",
   "Nueva arquitectura del menú, validada con las áreas y testada después con card sorting."]),
 hallazgos=key("La web reflejaba cómo estaba organizada la casa, no lo que necesitaba quien llegaba a ella.") + ul([
   "Cada parte parecía una web distinta.",
   "El paso más importante para el usuario era el que tenía más fricción.",
   "Faltaba claridad sobre lo que hace la organización.",
   "El equipo editorial dependía de tecnología para publicar.",
   "Todas las áreas querían lo mismo: ponérselo fácil a quien quiere dar el paso."]),
 quote=None,
 entregables=ul([
   "Diagnóstico, evaluación heurística y benchmark.",
   "Territorios de conquista y su journey.",
   "Nueva arquitectura del menú y de la home.",
   "Requisitos y primeros wireframes.",
   "Presentación a la dirección."]) + "@@ONG@@",
 deliv="diagnóstico, auditoría heurística, nuevo menú, requisitos y primeros wireframes.",
 traduccion=key("Un acuerdo de toda la casa.") + ul([
   "Todas las áreas compartieron una definición de éxito: dar el paso principal con menos fricción, entender qué hace la organización y publicar sin depender de nadie.",
   "El menú pasó de secciones por departamento a tres bloques claros.",
   "Los fallos de la auditoría se convirtieron en reglas para los wireframes.",
   "Nuevas vías de participación para quien quiere implicarse de otras formas."]),
 extra=None,
),
dict(
 slug="caso-ia", tag="Priorizar qué IA construir",
 card="Un formato, dos contextos: decidir qué IA construir primero",
 card_lede="Un workshop que parte del día a día de las personas, no de la tecnología.",
 facts=[],
 h1="Workshop de adopción de IA: un formato, dos contextos",
 lede="Diseñé un formato de workshop que empieza por el trabajo real, no por la tecnología. Lo aplicamos con dos equipos muy distintos y en los dos salió una lista de prioridades.",
 sheet=[("Contextos","Un equipo de compras y un equipo comercial"),("Formato","Sesiones de 90 minutos a 2 horas"),("Equipo","Diseño, moderación y síntesis, de principio a fin")],
 reto=key("Las empresas tienen IA, pero la usan para cosas sueltas.") + ul([
   "Redactar correos o resumir textos no cambia el trabajo.",
   "Había que encontrar dónde aporta valor real y qué resolver primero."]) +
   '<p class="premise">«Hoy no venimos a ver otra demo: venimos a construir la vuestra.»</p>',
 decidi=ul([
   "Ante equipos que esperaban otra demo, decidí empezar por sus tareas reales y no por la tecnología.",
   "Diseñé el cierre para que cada persona eligiera una prioridad. Así la lista salía de su día a día y no de lo que la IA sabe hacer."]),
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
 quote=None,
 entregables=ul([
   "Formato de workshop reutilizable: agenda, dinámicas y plantillas.",
   "Tableros de trabajo de cada sesión, creados con IA y adaptados a cada equipo.",
   "Informe de discovery con dolores, usos actuales y prioridades."]),
 deliv="formato de workshop reutilizable, tableros de cada sesión e informe de discovery.",
 traduccion=key("Lo que se llevó cada equipo.") + ul([
   "<strong>Equipo de compras:</strong> prioridades ordenadas por impacto y un documento de adopción.",
   "<strong>Equipo comercial:</strong> la demo a medida parte de los escenarios que votó el propio equipo."]),
 extra=None,
),
dict(
 slug="caso-app", tag="Orientar la hoja de ruta de un producto",
 card="Una app que acompañe a la persona, no solo a la tarea",
 card_lede="Entrevistas y test con usuarios reales para mejorar la app hoy y orientar su hoja de ruta.",
 facts=[],
 h1="Una app que acompañe a la persona, no solo a la tarea",
 lede="Escuchar a quienes usan la app dio dos resultados: mejoras de diseño inmediatas y una hoja de ruta organizada por etapas del journey y tipos de usuario.",
 sheet=[("Cliente","Empresa con una app de acompañamiento"),("Producto","App para personas que conviven con una situación de larga duración"),("Equipo","Yo, de principio a fin")],
 reto=key("Saber si la app encajaba con lo que de verdad necesitan sus usuarios.") + ul([
   "Dos objetivos: entender a las personas y probar la app en manos reales."]),
 decidi=ul([
   "Propuse perfilar a las personas por su actitud ante su situación, y no por su diagnóstico. Salieron cuatro perfiles, de quien prefiere no pensar en ello a quien ya lo ha integrado en su vida.",
   "Con esos perfiles, cada mejora y cada idea nueva de la hoja de ruta dice a quién sirve."]),
 enfoque=key("Entrevistas en profundidad que combinaban la historia de cada persona y el test de la app.") + ul([
   "Una parte para entender su recorrido y la mayor parte para probar la app.",
   "Muestra diversa en perfil, edad y experiencia.",
   "Test de cada sección de la app."]),
 hallazgos=key("Las personas no quieren gestionar un problema. Quieren llevar una vida normal.") + ul([
   "El journey no es lineal: hay etapas que se repiten.",
   "Lo emocional pesa tanto como lo práctico.",
   "No hay un usuario único: lo que le sirve depende de su momento y de su forma de ser.",
   "Valoraban lo que les ahorra esfuerzo y se perdían con los nombres poco claros.",
   "Echaban de menos más conexión con los profesionales que les acompañan."]),
 quote=None,
 entregables=ul([
   "Journey en cinco etapas.",
   "Arquetipos de usuario.",
   "Evaluación de usabilidad por sección.",
   "Oportunidades por etapa y por arquetipo."]),
 deliv="journey en cinco etapas, perfiles, evaluación por sección y oportunidades por etapa y perfil.",
 traduccion=key("Las mejoras, en concreto.") + ul([
   "Nombres más claros, un solo camino para los recordatorios y lo emocional en el centro.",
   "Proteger lo que mejor funcionaba.",
   "Ideas nuevas por etapa, como un modo para los días difíciles con menos avisos y ayuda directa."]),
 extra=None,
),
dict(
 slug="caso-promesa", tag="Diagnóstico de conversión",
 card="Cuando el nombre promete otra cosa",
 card_lede="Una página con mucho tráfico casi no convertía. El problema estaba en lo que se prometía antes de llegar a ella.",
 facts=[],
 h1="Cuando el nombre promete otra cosa",
 lede="Una página con mucho tráfico de campañas casi no convertía. El problema no estaba en la página, estaba en lo que se prometía antes de llegar a ella.",
 sheet=[("Cliente","Organización con una página de producto muy visitada"),("Equipo","Diagnóstico, research y recomendaciones")],
 reto=key("Saber por qué una página con muchas visitas apenas generaba transacciones."),
 decidi=ul([
   "En lugar de ir directa a la usabilidad, navegué tres hipótesis: el tráfico, la página y el concepto.",
   "Demostré que el problema era de promesa, no de usabilidad. El nombre hacía esperar una cosa y la página ofrecía otra, y esa idea se formaba antes de entrar, en el buscador y en los anuncios.",
   "Por eso la primera recomendación fue cambiar los anuncios, fuera de la web, y después la página."]),
 enfoque=key("Seguir la expectativa desde antes del primer clic hasta la página.") + ul([
   "Analítica y mapas de clics.",
   "Lo que dicen el buscador y los anuncios.",
   "Qué entiende la gente por el nombre.",
   "Evaluación heurística de la página."]),
 hallazgos=key("La gente esperaba elegir libremente una cantidad pequeña y encontraba un catálogo cerrado.") + ul([
   "La expectativa ya venía fijada desde el buscador, antes del primer clic.",
   "Lo más pulsado era «ver más»: no estaba lo que buscaban.",
   "Las preguntas frecuentes no respondían a las dudas de esa página."]),
 quote=None,
 entregables="",
 deliv="diagnóstico de expectativas, evaluación heurística y plan de optimización.",
 traduccion=key("Un plan en cuatro frentes.") + ul([
   "Anuncios que explican lo que hay detrás.",
   "Una forma directa de actuar nada más llegar.",
   "El catálogo visible de un vistazo.",
   "Preguntas frecuentes propias de la página."]),
 extra=None,
),
dict(
 slug="caso-producto", tag="Research integrado en producto",
 card="Research dentro de un equipo de producto",
 card_lede="Los estudios llegaban como encargos concretos. En varios, la respuesta cambió la pregunta de partida.",
 facts=[],
 h1="Research dentro de un equipo de producto",
 lede="Los estudios llegaban como encargos concretos. En varios, la respuesta cambió la pregunta de partida.",
 sheet=[("Cliente","Un e-commerce grande"),("Equipo","Integrada en su equipo de producto, cada estudio llevado sola de principio a fin")],
 owner="Proyecto realizado en Sngular, integrada en el equipo de producto del cliente. El trabajo y sus entregables son propiedad de Sngular.",
 reto=key("Responder a encargos de producto sin perder de vista la pregunta de negocio que había detrás.") + ul([
   "Registro, captación y entrega, entre otros.",
   "Cada estudio con hipótesis ligadas a KPIs desde el kickoff."]),
 decidi=ul([
   "<strong>Registro:</strong> ante un formulario de compra largo, propuse no pedir el registro en ese momento, porque cada vez más gente compra como invitada, y ofrecerlo después con ventajas claras.",
   "<strong>Captar gente joven:</strong> mostré que el problema no era de canal sino de marca. Para la gente joven no era aspiracional, era algo con lo que romper, la ropa que sus padres les compraban para el colegio. Y avisé de que, con el perfil al que se podía llegar, la parte de nuevos clientes necesitaba un estudio aparte.",
   "<strong>Entrega de bajas emisiones:</strong> con un test sin ganador, planteé si tenía sentido cargar más el paso más crítico de la compra."]),
 enfoque=key("Research dentro del día a día del equipo.") + ul([
   "Entrevistas y tests con usuarios.",
   "Analítica, benchmark y tests A/B.",
   "Kickoffs con todas las áreas implicadas para fijar objetivos y riesgos."]),
 hallazgos=key("Quien compra quiere hacerlo en los menos clics posibles.") + ul([
   "La mayoría no lee los mensajes largos y elige el camino que intuye más corto.",
   "Registrarse se asocia a correo no deseado.",
   "Para la gente joven, la marca era la norma de la que querían salir."]),
 quote=None,
 entregables="",
 deliv="planes de research, informes de cada estudio y recomendaciones para el equipo.",
 traduccion=key("Preguntas mejor planteadas para el equipo de producto.") + ul([
   "Cada estudio terminó con recomendaciones concretas y la pregunta de negocio que había detrás."]),
 extra=None,
),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Geist:wght@300;400;500;600;700&family=Geist+Mono:wght@500&display=swap"><link rel="stylesheet" href="' + v("styles.css") + '"><script>if(\'IntersectionObserver\' in window&&!matchMedia(\'(prefers-reduced-motion: reduce)\').matches)document.documentElement.classList.add(\'anim\')</script>'

# Línea ondulada de las cabeceras de caso (trazo con degradado amanecer, nunca relleno)
WAVE = '''<svg class="wave" viewBox="0 0 1440 600" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="amanecer" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#78BAE6"/><stop offset="1" stop-color="#A99BE8"/></linearGradient></defs><path d="M-20 40 C 400 6, 700 10, 900 130 S 1200 540, 1460 470" fill="none" stroke="url(#amanecer)" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>'''

def nav(prefix):
    return f'''<header class="nav"><div class="inner">
  <div class="nav-left">{'<a class="nav-back" id="nav-back" href="index.html">← Atrás</a>' if prefix else ''}
  <a class="brand" href="{prefix or '#inicio'}" aria-label="Gema Díez, inicio"><span class="dot" aria-hidden="true"></span>Gema Díez</a></div>
  <nav aria-label="Principal"><ul>
    <li class="hide-s"><a href="como-trabajo.html">Cómo trabajo</a></li>
    <li class="hide-s"><a href="casos.html">Casos</a></li>
    <li class="hide-s"><a href="ia.html">Con IA</a></li>
    <li class="hide-s"><a href="sobre-mi.html">Sobre mí</a></li>
    <li><a class="btn btn-primary btn-small" href="{prefix}#contacto">Contacto</a></li>
    <li class="show-s"><button class="menu-btn" type="button" aria-expanded="false" aria-controls="mnav" aria-label="Abrir menú"><span></span><span></span></button></li>
  </ul></nav>
</div>
<nav class="mnav" id="mnav" aria-label="Menú móvil"><ul>
  <li><a href="como-trabajo.html">Cómo trabajo</a></li>
  <li><a href="casos.html">Casos</a></li>
  <li><a href="ia.html">Con IA</a></li>
  <li><a href="sobre-mi.html">Sobre mí</a></li>
</ul></nav>
</header>'''


# Chat de contacto. Para que llegue a tu email, pega aquí la clave de Web3Forms (web3forms.com).
# Mientras esté vacía, el chat abre el programa de correo con el mensaje ya escrito.
CHAT_KEY = "846b664b-7e4f-4e66-84b3-b6f36242411f"
CHAT = ('<div class="chat" id="chat" data-key="' + CHAT_KEY + '" data-mail="gd.glez@gmail.com">'
  '<button class="chat-fab" type="button" aria-label="Hablemos: abrir el chat" aria-expanded="false" aria-controls="chat-panel"><img src="' + v(PHOTO) + '" alt=""><span>Hablemos</span></button>'
  '<section class="chat-panel" id="chat-panel" role="dialog" aria-label="Escríbeme" hidden>'
  '<header class="chat-head"><img src="' + v(PHOTO) + '" alt=""><div><b>Gema Díez</b><span>Te respondo por email</span></div>'
  '<button class="chat-x" type="button" aria-label="Cerrar chat">✕</button></header>'
  '<div class="chat-log" aria-live="polite"><p class="bub them">¡Hola! Soy Gema 👋</p><p class="bub them">Cuéntame tu proyecto, tu reto o tu duda y te contesto por email.</p></div>'
  '<form class="chat-form" novalidate><p class="chat-req" aria-hidden="true"><span class="req">*</span> obligatorio</p>'
  '<label class="chat-l" for="chat-msg">Mensaje <span class="req" aria-hidden="true">*</span></label><textarea id="chat-msg" name="message" rows="3" placeholder="Escribe tu mensaje…" required aria-describedby="chat-err"></textarea>'
  '<div class="chat-row"><div><label class="chat-l" for="chat-name">Nombre <span class="req" aria-hidden="true">*</span></label><input id="chat-name" name="name" placeholder="Tu nombre" autocomplete="name" required aria-describedby="chat-err"></div><div><label class="chat-l" for="chat-mail">Email <span class="req" aria-hidden="true">*</span></label><input id="chat-mail" name="email" type="email" placeholder="Tu email" autocomplete="email" required aria-describedby="chat-err"></div></div>'
  '<input type="checkbox" name="botcheck" class="chat-hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
  '<p class="chat-err" id="chat-err" role="alert"></p>'
  '<button class="btn btn-primary chat-send" type="submit">Enviar</button></form>'
  '</section></div>')

FOOT = '<footer class="band foot"><div class="inner"><span>© 2026 Gema Díez · Madrid</span><span>Researcher y Service Design Strategist</span></div>\n<a class="totop" id="totop" href="#" aria-label="Volver arriba" title="Volver arriba"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></a></footer>\n' + CHAT + '\n<script src="' + v('site.js') + '" defer></script>'

ICONS = {
 "sistema": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><path d="M24 8 A16 16 0 0 0 24 40" stroke="#161616"/><path d="M26 8 A16 16 0 0 1 26 40" stroke="#A99BE8" stroke-width="2"/></svg>',
 "piezas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><g stroke="#161616"><path d="M12 12 L36 14 M12 12 L14 36 M36 14 L34 34 M14 36 L34 34 M12 12 L34 34"/><circle cx="12" cy="12" r="4" fill="#FFFFFF"/><circle cx="36" cy="14" r="4" fill="#FFFFFF"/><circle cx="14" cy="36" r="4" fill="#FFFFFF"/></g><circle cx="34" cy="34" r="5" stroke="#78BAE6" stroke-width="2" fill="#FFFFFF"/></svg>',
 "personas": '<svg viewBox="0 0 48 48" width="44" height="44" fill="none" stroke-width="1.5" aria-hidden="true"><circle cx="18" cy="24" r="12" stroke="#161616"/><circle cx="30" cy="24" r="12" stroke="#78BAE6" stroke-width="2"/></svg>',
}

# Cifras de la cabecera de cada caso: dato grande + etiqueta, sin caja (no deben parecer botones)
STATS = {k: [] for k in ["caso-relacion","caso-web","caso-ia","caso-app","caso-promesa","caso-producto"]}  # versión anónima: sin cifras

# Trazos "dibujados a mano" (SVG). Se dibujan solos al entrar en pantalla (.draw)
ARROW = '<svg class="doodle draw arrow" viewBox="0 0 120 60" aria-hidden="true"><path pathLength="1" d="M6 50 C 22 18, 58 6, 104 18"/><path pathLength="1" d="M90 6 L106 18 L91 29"/></svg>'
ARROW_DOWN = '<svg class="doodle draw arrow-down" viewBox="0 0 70 90" aria-hidden="true"><path pathLength="1" d="M12 6 C 50 14, 62 46, 40 80"/><path pathLength="1" d="M28 70 L40 82 L52 70"/></svg>'
SCRIBBLE = '<svg class="doodle draw scribble" viewBox="0 0 300 24" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M4 16 C 40 6, 70 20, 110 12 S 190 6, 230 14 S 280 12, 296 8"/></svg>'
LOOP = '<svg class="doodle draw loop" viewBox="0 0 220 120" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M30 70 C 20 30, 90 8, 150 16 C 205 24, 214 70, 170 98 C 120 124, 40 112, 22 80 C 14 64, 30 44, 60 36"/></svg>'
WINK = '<svg class="doodle draw wink" viewBox="0 0 48 48" role="img" aria-label="guiño"><path pathLength="1" d="M24 4 C 36 3, 45 13, 44 25 C 43 37, 33 45, 22 44 C 10 43, 3 33, 4 22 C 5 12, 13 5, 25 5"/><path pathLength="1" d="M15 18 C 16 17, 17 17, 17 19"/><path pathLength="1" d="M28 19 C 30 17, 33 17, 35 19"/><path pathLength="1" d="M13 28 C 18 36, 30 37, 36 27"/></svg>'
# Nota a mano de cada caso, junto a la foto de cabecera
NOTES = {"caso-relacion": "de vender productos<br>a vender una relación", "caso-web": "del organigrama<br>a tres bloques",
 "caso-ia": "¿qué IA construimos primero?", "caso-app": "una vida normal,<br>no solo una tarea",
 "caso-promesa": "la promesa,<br>no la página", "caso-producto": "cambiar la pregunta<br>de partida"}

LINES = ["ln-top", "ln-left", "ln-right", "ln-bottom", "ln-top-r"]  # posición de la línea de color de cada tarjeta

YEARS = {"caso-relacion": "2024–25", "caso-web": "2026", "caso-ia": "2026", "caso-app": "2025", "caso-promesa": "2026", "caso-producto": "2022–24"}

def row(c, k=0):
    """Fila de la lista de casos de la home (sustituye a las tarjetas, 18 nov 2026)."""
    meta = f"{c['tag']} · {YEARS[c['slug']]}"  # 20 nov 2026: sin cifras en el listado (siguen dentro de cada caso)
    return f'''<a class="crow reveal" style="--d:{k*80}ms" href="{c['slug']}.html">
  <span class="crow-img"><img src="{v('img/' + c['slug'] + '.jpg')}" alt="" width="800" height="800" loading="lazy"><img class="duo" src="{v('img/' + c['slug'] + '.jpg')}" alt="" width="800" height="800" loading="lazy"></span>
  <span class="crow-num" aria-hidden="true">{k+1:02d}</span>
  <span class="crow-text"><span class="crow-title">{c['card']}</span><span class="crow-meta">{meta}</span><span class="crow-lede">{c['card_lede']}</span><span class="owner">Proyecto de Sngular</span></span>
  <span class="crow-go" aria-hidden="true">→</span>
</a>'''

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
  ("Creación de cuenta", "Crear cuenta", "Accesibilidad", "Contraste y tamaño de letra insuficientes para este público.", "hot-a"),
  ("Perfilado", "Tu perfil", "Arquitectura", "Agrupar el registro en bloques: perfil, dispositivos y documentación.", "hot-b"),
  ("Vinculación del dispositivo", "Vincular", "Lenguaje", "Las siglas técnicas confunden: mejor las palabras del usuario.", "hot-c"),
  ("Rutina", "Tu rutina", "Interacción", "La pregunta sobre la rutina debe permitir varias respuestas.", "hot-d"),
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
    cols = ["Llegada", "Uso", "Pago", "Dudas"]
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
            '<div class="ar-id">' + face + '<span class="ev-k">Arquetipo</span><h3>La perfeccionista</h3>'
            '<p>Conoce su enfermedad al detalle, contrasta lo que lee y quiere tenerlo todo bajo control. Cuando algo se le escapa, lo vive con culpa.</p></div>'
            '<div class="ar-body"><div class="ar-q"><span class="ar-k">Quiere</span><p>Una herramienta seria, fiable y exacta.</p></div>'
            '<div class="ar-q"><span class="ar-k">Necesita</span><p>Sentir que tiene el control y confirmar que lo está haciendo bien.</p></div>'
            '<div class="ar-vars">' + br + '</div></div>'
            '<figcaption>Uno de los cuatro arquetipos. Recreación con nombre y datos modificados.</figcaption></figure>')
    return journey + arch


def ong_demo():
    notes = [("La acción principal queda en el tercio inferior, sin el peso que merece.", "d"),
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
    cards = [("Actividad 1", "La persona usuaria", "Definir quién es, qué le mueve a dar el paso y qué le frena."),
             ("Actividad 2", "Happy path", "Dibujar el recorrido ideal, desde que descubre la organización hasta que da el paso."),
             ("Actividad 3", "Arquitectura", "Ordenar los contenidos del menú pensando en esa persona, no en los departamentos."),
             ("Cierre", "Puesta en común", "Cada grupo comparte lo suyo y se acuerdan los siguientes pasos.")]
    cs = "".join(f'<div class="fc c{i}"><span class="fc-k">{k}</span><h3>{t}</h3><p>{d}</p><span class="fc-m">Materiales</span><i class="sk w80"></i><i class="sk w60"></i></div>' for i, (k, t, d) in enumerate(cards, 1))
    deck = ('<figure class="eval fcs" aria-label="Fichas de las actividades del workshop">'
            '<span class="ev-k">Fichas del workshop</span><div class="fc-deck">' + cs + '</div>'
            '<figcaption>Las cuatro fichas que guiaron el workshop de co-creación. Recreación con textos resumidos.</figcaption></figure>')
    return evalx + deck


# Impacto de cada caso: solo resultados reales que constan en los documentos de Gema (nada supuesto)
IMPACT = {
 "caso-relacion": ("El research se convirtió en la hoja de ruta del negocio.", [
   ("Decisiones de negocio", "Negocio priorizó qué construir a partir de las oportunidades: onboarding digital, atención remota para empresas y un CRM más sencillo."),
   ("Del papel al diseño", "Los hallazgos alimentaron el portal de cliente y las mejoras del CRM para los equipos."),
   ("Dos ampliaciones", "El cliente amplió el proyecto dos veces, hasta llevar sus principios de marca a cada canal de atención.")]),
 "caso-web": ("El nuevo menú, aprobado.", [
   ("Menú aprobado", "La dirección aprobó el nuevo menú, pensado para el usuario y no para el organigrama."),
   ("Base de la web nueva", "El diagnóstico y el nuevo menú son la base de su próxima web."),
   ("Sigo en el proyecto", "El diagnóstico llevó a nuevas fases, y sigo trabajando mano a mano con la responsable del proyecto.")]),
 "caso-ia": ("De «tenemos IA» a «sabemos qué construir primero».", [
   ("Prioridades claras", "Ya se están construyendo soluciones a medida a partir de lo que salió en los workshops."),
   ("Un formato que crece", "Del primer workshop salió el segundo, adaptado a otro equipo, y el formato se ha compartido con más clientes."),
   ("Un método repetible", "Construcción de un método para pasar de «tenemos IA» a «sabemos qué resolver primero».")]),
 "caso-app": ("Mejoras para hoy y una hoja de ruta para mañana.", [
   ("Mejoras listas para aplicar", "Cambios de diseño concretos para cada sección de la app."),
   ("Una hoja de ruta de producto", "Nuevas funcionalidades por etapa del journey y por tipo de usuario."),
   ("Una segunda fase", "El cliente contrató una nueva fase para evaluar también su web.")]),
}

STEP_KIND = {"El reto": "reto", "Lo que decidí": "decidi", "Enfoque": "enfoque", "Hallazgos clave": "hallazgos", "En qué se tradujo": "tradujo"}

def step(n, title, body, white, total=5):
    kind = STEP_KIND[title]
    tone = " dark" if kind == "hallazgos" else (" white" if white else "")
    chip = "chip-sky" if n % 2 else "chip-lav"
    return f'''<section class="band step step-{kind}{tone}" id="{kind}"><div class="inner">
  <div class="step-head reveal"><span class="bignum" aria-hidden="true">{n:02d}</span><span class="chip {chip}">Paso {n:02d} de {total:02d}</span><h2>{title}</h2></div>
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
    sheet = "".join(f'<div><span class="label">{k}</span><b>{v}</b></div>' for k, v in c["sheet"][:1] + [("Año", YEARS[c["slug"]])] + c["sheet"][1:])
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
    # 23 nov 2026: «Mi rol» pasa a la ficha y entra «Lo que decidí». Los entregables son una línea dentro de «En qué se tradujo»
    demo = c["entregables"].replace("@@EVAL@@", eval_demo()).replace("@@FARMA@@", farma_demo()).replace("@@ONG@@", ong_demo())
    demo = demo[demo.index("<figure"):] if "<figure" in demo else ""
    trad += f'<p class="deliv"><strong>Entregables:</strong> {c["deliv"]}</p>' + demo
    steps = [("El reto", c["reto"]), ("Lo que decidí", '<div class="decidi">' + c["decidi"] + '</div>'), ("Enfoque", c["enfoque"]), ("Hallazgos clave", hall), ("En qué se tradujo", trad)]
    toc = ('<nav class="case-toc" aria-label="En este caso"><span class="label">En este caso</span><ol>'
           + ('<li><a href="#impacto">Impacto</a></li>' if c["slug"] in IMPACT else '') + "".join(f'<li><a href="#{STEP_KIND[t]}">{t}</a></li>' for t, _ in steps) + '</ol></nav>')
    body = "".join(step(k + 1, t, b, k % 2 == 0, len(steps)) + (pull if t == "Hallazgos clave" else "") for k, (t, b) in enumerate(steps))
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(c['card'])} · Gema Díez</title>
<meta name="description" content="{html.escape(c['lede'])}">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main id="contenido">
<section class="case-hero">{WAVE}<div class="inner">
  <div class="hero-grid">
    <div class="hero-text">
      <span class="tag">{c['tag']}</span>
      <h1>{c['h1']}</h1>
      <p class="lede">{c['lede']}</p>
      <dl class="stats">{pills}</dl>
    </div>
    <figure class="hero-photo"><img class="float" style="--f:9s" src="{v('img/' + c['slug'] + '.jpg')}" alt="" width="800" height="800"><span class="dot" aria-hidden="true"></span><figcaption class="note n-case">{ARROW}{NOTES[c['slug']]}</figcaption></figure>
  </div>
  <div class="sheet">{sheet}</div>
  {toc}
  <p class="owner-note"><span class="dot" aria-hidden="true"></span>{c.get("owner", "Proyecto realizado como Senior Researcher y Service Designer en Sngular. El trabajo y sus entregables son propiedad de Sngular.")}</p>
</div></section>
{impact_html(c) if c["slug"] in IMPACT else ""}
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

# 23 nov 2026 (tarde): primero los casos con más peso estratégico
_ORDEN = ["caso-relacion", "caso-web", "caso-promesa", "caso-ia", "caso-app", "caso-producto"]
CASES.sort(key=lambda c: _ORDEN.index(c["slug"]))
cards = "".join(row(c, k=k) for k, c in enumerate(CASES))

INDEX = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Gema Díez · Researcher y Service Design Strategist</title>
<meta name="description" content="Gema Díez, Researcher y Service Design Strategist. Hago que lo fragmentado funcione como un solo servicio.">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{nav('')}
<main id="contenido">
<section class="hero hero-big" id="inicio">
<div class="orbits" aria-hidden="true"><span class="orbit o1"></span><span class="orbit o2"></span></div>
<div class="inner">
  <span class="chip chip-sky">Researcher y Service Design Strategist</span>
  <h1 class="hero-phrases">
    <span class="hp" style="--d:0ms">Entiendo el sistema. <span class="accent">Uno las piezas.</span></span>
    <span class="hp" style="--d:900ms">Pienso en las personas y en el negocio.</span>
    <span class="hp hp-3" style="--d:1800ms">Hago que lo fragmentado funcione como un solo servicio.</span>
  </h1>
  <p class="proof"><span class="dot" aria-hidden="true"></span><span>En 2025 y 2026, <b>todos mis clientes han vuelto a contar conmigo</b> para nuevas fases y proyectos. {WINK}</span></p>
  <a class="scroll-hint" href="casos.html"><span class="note">mira los casos de éxito</span><svg class="sh-right" viewBox="0 0 60 30" aria-hidden="true"><path d="M4 18 C 18 10, 34 22, 54 14"/><path d="M45 7 L55 14 L46 22"/></svg></a>
  <figure class="hero-cut"><div class="hc-block"><a class="hc-more" href="sobre-mi.html">Más sobre mí →</a></div><img class="hc-photo" src="img/gema-recorte.webp" alt="Retrato de Gema Díez sonriendo" width="800" height="769"><span class="note hc-note" aria-hidden="true">esta soy yo{ARROW_DOWN}</span></figure>
</div></section>

<section class="band white" id="como-trabajo"><div class="inner">
  <div class="sec-head"><span class="chip chip-lav">Cómo trabajo</span><h2>Tres pasos para que un servicio <span class="hand-u">complejo{SCRIBBLE}</span> funcione</h2><p>La investigación es mi punto de partida, no mi entregable. Escucho a las personas y leo los datos para decidir qué hacer.</p></div>
  <div class="pillars">
    <div class="pillar reveal" style="--d:0ms"><div class="pillar-top">{ICONS['sistema']}<span class="pnum">01</span></div><h3>Entiendo el sistema</h3><p>Mapeo cómo funcionan las cosas de verdad: quién las sostiene, qué herramientas usa cada equipo y dónde se rompe la experiencia.</p></div>
    <div class="pillar reveal" style="--d:120ms"><div class="pillar-top">{ICONS['piezas']}<span class="pnum">02</span></div><h3>Uno las piezas</h3><p>Decido qué importa y qué no puede fallar en cada flujo y punto de contacto, para que todo funcione como un solo servicio.</p></div>
    <div class="pillar reveal" style="--d:240ms"><div class="pillar-top">{ICONS['personas']}<span class="pnum">03</span></div><h3>Pienso en las personas y en el negocio</h3><p>Alineo a los equipos en torno a los mensajes que hay que transmitir, para que lo bueno para las personas también lo sea para el negocio.</p></div>
  </div>
  <div class="statement statement-px reveal" id="statement-px" data-img="{PX_IMG}" style="--px-img:url({PX_IMG})">
    <canvas class="px-canvas" aria-hidden="true"></canvas>
    <p>No diseño píxeles.<br>Diseño lo que hace que esos píxeles <span class="hand-u light">tengan sentido.{SCRIBBLE}</span></p>
  </div>
</div></section>

<section class="band impact decisions" id="decisiones"><div class="inner">
  <div class="imp-head"><span class="chip chip-sky">Decisiones</span><h2>Decisiones que salieron de mi trabajo</h2></div>
  <ul class="imp-list">
    <li class="reveal" style="--d:0ms"><span class="imp-n">01</span><b>Un menú pensado para quien llega</b><span>La dirección aprobó un menú pensado para quien llega, no para el organigrama.</span><a class="link" href="caso-web.html">Ver el caso →</a></li>
    <li class="reveal" style="--d:100ms"><span class="imp-n">02</span><b>Qué construir primero</b><span>Negocio priorizó qué construir a partir de las oportunidades del research.</span><a class="link" href="caso-relacion.html">Ver el caso →</a></li>
    <li class="reveal" style="--d:200ms"><span class="imp-n">03</span><b>IA a partir de tareas reales</b><span>Dos equipos construyen su IA a partir de las prioridades que salieron de sus workshops.</span><a class="link" href="caso-ia.html">Ver el caso →</a></li>
  </ul>
</div></section>

<section class="band white" id="hallazgos"><div class="inner">
  <div class="findings-wrap">
    <div class="findings-head">
      <span class="chip chip-lav">Hallazgos</span>
      <h2>A veces el problema <span class="hand-o">no es{LOOP}</span> el que parece</h2>
      <p>Cinco cosas que solo aparecieron al escuchar a las personas que usan y sostienen el servicio, y lo que cambiaron.</p>
    </div>
    <div class="findings">
      <a class="finding reveal acc-sky" href="caso-relacion.html"><span class="fnum">01</span><div><span class="chip chip-sky">Segmentación y propuesta de valor</span><h3>La confianza pesa más que el precio.</h3><p>Los clientes valoraban sentirse acompañados más que pagar menos. La relación pasó al centro de la estrategia.</p></div></a>
      <a class="finding reveal acc-lav" href="caso-web.html"><span class="fnum">02</span><div><span class="chip chip-lav">Ordenar una web por quien llega</span><h3>La web estaba ordenada como la organización, no como piensa quien llega a ella.</h3><p>Reordenamos los contenidos en tres bloques que cualquiera entiende.</p></div></a>
      <a class="finding reveal acc-sky" href="caso-promesa.html"><span class="fnum">03</span><div><span class="chip chip-sky">Diagnóstico de conversión</span><h3>El problema no era la página, era la promesa.</h3><p>El nombre hacía esperar una cosa y la página ofrecía otra.</p></div></a>
      <a class="finding reveal acc-lav" href="caso-ia.html"><span class="fnum">04</span><div><span class="chip chip-lav">Priorizar qué IA construir</span><h3>Para decidir qué IA construir, primero hay que ver en qué se va el tiempo.</h3><p>Las prioridades salieron de tareas reales del equipo, no de la tecnología disponible.</p></div></a>
      <a class="finding reveal acc-sky" href="caso-app.html"><span class="fnum">05</span><div><span class="chip chip-sky">Orientar la hoja de ruta de un producto</span><h3>Nadie quiere gestionar un problema. Quiere llevar una vida normal.</h3><p>Lo emocional pesa tanto como lo práctico, y la app tenía que reflejarlo.</p></div></a>
    </div>
  </div>
</div></section>

<section class="band" id="sobre-mi"><div class="inner">
  <div class="about">
    <div class="photo"><img src="{v(PHOTO)}" alt="Retrato de Gema Díez sonriendo" width="400" height="400"><span class="note n-about">¡hola, soy yo!{ARROW_DOWN}</span></div>
    <div class="bio">
      <span class="chip chip-lav">Sobre mí</span>
      <p class="lead">Soy Gema Díez, Researcher y Service Design Strategist con más de 8 años trabajando en servicios complejos.</p>
      <p>He trabajado en energía, banca, salud, seguros, retail y tercer sector. Mi trabajo empieza donde las cosas están fragmentadas, con plataformas que no se hablan, equipos con visiones distintas y mensajes que no llegan, y termina cuando funcionan como un solo servicio.</p>
      <p>Mapeo cómo son las cosas de verdad, escuchando a las personas y leyendo los datos, decido qué no puede fallar y ayudo a que todo el equipo empuje en la misma dirección.</p>
      <ul class="facts-list">
        <li><b>+8 años</b><span>En diseño de servicios, investigación y experiencia de cliente</span></li>
        <li><b>Docente desde 2023</b><span>Mentora de Design y User Research en Uxer School</span></li>
        <li><b>4 países europeos</b><span>Investigación internacional con equipos y usuarios en varios mercados</span></li>
        <li><b>Ciencias Políticas</b><span>De ahí viene mi forma de pensar en sistemas</span></li>
      </ul>
      <a class="link about-more" href="sobre-mi.html">Más sobre Gema, fuera del trabajo →</a>
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
      <p>Mi recorrido y dónde trabajo.</p>
      <div class="ctas"><a class="btn btn-secondary" href="https://www.linkedin.com/in/gema-d%C3%ADez-gonz%C3%A1lez-74157943/" target="_blank" rel="noopener">Mi LinkedIn</a><a class="btn btn-secondary" href="https://www.sngular.com/" target="_blank" rel="noopener">Web de Sngular</a><span class="soon">CV en PDF, próximamente</span></div>
    </div>
    <div class="door door-chat">
      <span class="label">Para algo rápido</span>
      <h3>Escríbeme por el chat {WINK.replace('role="img" aria-label="guiño"', 'aria-hidden="true" focusable="false"')}</h3>
      <p>Lo que escribas llega directamente a mi email.</p>
      <div class="ctas"><button class="btn btn-secondary" id="open-chat" type="button">Abrir el chat</button></div>
</div>
  </div>
</div></section>
</main>
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

# 20 nov 2026: la sección «Sobre mí» ya no sale en la home (sigue generándose para sobre-mi.html)
import re as _re0
# 23 nov 2026: Hallazgos sale de la home y pasa a casos.html, tras el listado
_HALL = _re0.search(r'<section class="band white" id="hallazgos">.*?</section>', INDEX, _re0.S).group(0)
_idx = _re0.sub(r'\n?<section class="band" id="sobre-mi">.*?</div></section>\n?', '\n', INDEX, count=1, flags=_re0.S).replace(_HALL, '')
open(os.path.join(OUT, "index.html"), "w").write(_idx)

# Página propia «Con IA» (19 nov 2026): el Laboratorio sale de la home a ia.html
IA_PAGE = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Con IA · Gema Díez</title>
<meta name="description" content="Diseño con IA de principio a fin: investigo, sintetizo, facilito y construyo.">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main id="contenido">
{LAB}
</main>
{FOOT}
</body>
</html>
'''
open(os.path.join(OUT, "ia.html"), "w").write(IA_PAGE.replace('<a href="ia.html">Con IA</a>', '<a href="ia.html" class="active" aria-current="page">Con IA</a>'))
for i, c in enumerate(CASES):
    open(os.path.join(OUT, c["slug"] + ".html"), "w").write(case_page(i, c).replace('<a href="casos.html">Casos</a>', '<a href="casos.html" class="active">Casos</a>'))
print("ok")

# Página «Sobre mí» (19 nov 2026): la sección de la home + bloque personal «Fuera del trabajo»
import re as _re
_home = INDEX
_about = _re.search(r'<section class="band" id="sobre-mi">.*?</div></section>', _home, _re.S).group(0)
_about = _about.replace('\n      <a class="link about-more" href="sobre-mi.html">Más sobre Gema, fuera del trabajo →</a>', '')
_about = _about.replace('<p class="lead">', '<h1 class="sr-only">Sobre mí</h1><p class="lead">', 1)
# Plegado (19 nov 2026): visible solo la primera frase + «Leer más», el resto se despliega
_about = _re.sub(r'(<p class="lead">.*?</p>)', r'\1\n      <button type="button" class="more-toggle" id="more-toggle" aria-expanded="true" aria-controls="about-rest about-mentor" hidden><span class="mt-t">Leer menos</span><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 6 8 10.5 12.5 6"/></svg></button>\n      <div class="about-rest" id="about-rest">', _about, count=1)
_about = _about.replace('</ul>\n    </div>\n  </div>\n  <div class="mentor reveal">', '</ul>\n      </div>\n    </div>\n  </div>\n  <div class="mentor reveal" id="about-mentor">', 1)
SOBRE_PAGE = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Sobre mí · Gema Díez</title>
<meta name="description" content="Gema Díez, Researcher y Service Design Strategist. Y fuera del trabajo: cine, música electrónica, libros, exposiciones y dos gatos.">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body class="sobre-page">
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main id="contenido">
{_about}
{SOBRE}
</main>
{FOOT}
</body>
</html>
'''
open(os.path.join(OUT, "sobre-mi.html"), "w").write(SOBRE_PAGE.replace('<a href="sobre-mi.html">Sobre mí</a>', '<a href="sobre-mi.html" class="active" aria-current="page">Sobre mí</a>'))

# Página propia de casos (20 nov 2026): la sección sale de la home y «Casos» del menú lleva aquí
CASOS_SECTION = f'''<section class="band" id="casos"><div class="inner">
  <div class="sec-head"><span class="chip chip-sky">Casos · 2022 a 2026</span><h1 class="h2like">Qué vi, qué propuse y qué cambió</h1><p>Seis proyectos de Service Design y Research que hice en Sngular. Los cuento sin marcas, sectores ni datos de los clientes.</p></div>
  <div class="case-list">{cards}</div>
  <svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="duo" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values=".2126 .7152 .0722 0 0 .2126 .7152 .0722 0 0 .2126 .7152 .0722 0 0 0 0 0 1 0"/><feComponentTransfer><feFuncR type="table" tableValues=".086 .961"/><feFuncG type="table" tableValues=".086 .937"/><feFuncB type="table" tableValues=".086 .894"/></feComponentTransfer></filter></svg>
</div></section>'''
CASOS_PAGE = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Casos · Gema Díez</title>
<meta name="description" content="Seis proyectos de Service Design y Research hechos en Sngular: qué vi, qué propuse y qué cambió.">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body class="casos-page">
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main id="contenido">
{CASOS_SECTION}
{_HALL}
</main>
{FOOT}
</body>
</html>
'''
open(os.path.join(OUT, "casos.html"), "w").write(CASOS_PAGE.replace('<a href="casos.html">Casos</a>', '<a href="casos.html" class="active" aria-current="page">Casos</a>'))

# Página «Cómo trabajo» (23 nov 2026): desde el menú se ve solo esta sección, sin Hallazgos ni Contacto
_CT = _re.search(r'<section class="band white" id="como-trabajo">.*?</div></section>', INDEX, _re.S).group(0)
CT_PAGE = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Cómo trabajo · Gema Díez</title>
<meta name="description" content="Tres pasos para que un servicio complejo funcione: entender el sistema, unir las piezas y pensar en las personas y en el negocio.">
{FONTS}
<script data-goatcounter="https://gemadiez.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</head>
<body class="ct-page">
<a class="skip" href="#contenido">Saltar al contenido</a>
<div class="progress" aria-hidden="true"><span id="progress"></span></div>
{nav('index.html')}
<main id="contenido">
<h1 class="sr-only">Cómo trabajo</h1>
{_CT}
</main>
{FOOT}
</body>
</html>
'''
open(os.path.join(OUT, "como-trabajo.html"), "w").write(CT_PAGE.replace('<a href="como-trabajo.html">Cómo trabajo</a>', '<a href="como-trabajo.html" class="active" aria-current="page">Cómo trabajo</a>'))
