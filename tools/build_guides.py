#!/usr/bin/env python3
"""Generate the translated usage guides (guide/en, guide/es, guide/pt, guide/zh).

The Japanese guide (guide/index.html) is written by hand; the other languages are
generated from the shared template below so that their structure stays in sync.
Run:  python3 tools/build_guides.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://fouritre.vercel.app'
UPDATED = '2026-10-13'

LANGS = [  # code, path, hreflang, label
    ('en', '/guide/en/', 'en', 'English'),
    ('es', '/guide/es/', 'es', 'Español'),
    ('pt', '/guide/pt/', 'pt', 'Português'),
    ('zh', '/guide/zh/', 'zh-Hans', '中文'),
    ('ja', '/guide/', 'ja', '日本語'),
]


def hreflang_links():
    out = [f'<link rel="alternate" hreflang="{h}" href="{SITE}{p}">' for _, p, h, _ in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/guide/en/">')
    return '\n'.join(out)


def lang_switch(cur):
    items = []
    for c, p, h, label in LANGS:
        cur_attr = ' aria-current="page"' if c == cur else ''
        items.append(f'<a href="{p}" hreflang="{h}" lang="{h}"{cur_attr}>{label}</a>')
    return '<div class="langs">' + ''.join(items) + '</div>'


TEMPLATE = '''<!DOCTYPE html>
<html lang="{htmllang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
{hreflang}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#05070d">
<meta property="og:type" content="article">
<meta property="og:site_name" content="FouriTre">
<meta property="og:locale" content="{oglocale}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:image" content="{site}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogtitle}">
<meta name="twitter:description" content="{ogdesc}">
<meta name="twitter:image" content="{site}/assets/og.jpg">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%23060a14'/><circle cx='50' cy='50' r='35' fill='none' stroke='%233d8bfd' stroke-width='3'/><circle cx='50' cy='15' r='5' fill='%23fcd34d'/></svg>">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;500{extrafont}&display=swap">
<script type="application/ld+json">
{jsonld}
</script>
<link rel="stylesheet" href="/guide/guide.css">
</head>
<body>
<nav class="nav"><div class="in">
  <a class="brand" href="{app}"><span class="logo"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8" stroke="#3b4a7a" stroke-width="1.4"/><line x1="12" y1="12" x2="17.5" y2="6.5" stroke="#6d8cff" stroke-width="1.6" stroke-linecap="round"/><circle cx="17.5" cy="6.5" r="2.2" fill="#fcd34d"/></svg></span>FouriTre</a>
  <a class="lk" href="#quickstart">{nav_start}</a>
  <a class="lk" href="#math">{nav_math}</a>
  <a class="lk" href="#faq">FAQ</a>
  <a class="cta" href="{app}">{nav_open}</a>
</div></nav>

<header class="hero">
  <div>
    <div class="eyebrow">{eyebrow}</div>
    <h1><span>{h1}</span></h1>
    <p class="lead">{lead}</p>
    <a class="cta lg" href="{app}">{cta}</a>
    <div class="badges">{badges}</div>
    {langs}
  </div>
  <img src="/assets/screenshot-app-{code}.jpg" width="1400" height="860" alt="{hero_alt}" fetchpriority="high">
</header>

<div class="wrap">
  <aside class="toc">
    <p>{toc_title}</p>
{toc}
  </aside>
  <main>
    <section id="what">
      <h2><small>About</small>{what_h}</h2>
{what}
    </section>

    <section id="quickstart">
      <h2><small>Quick start</small>{qs_h}</h2>
      <ol class="steps">
{qs_steps}
      </ol>
      {demo_qs}
      <div class="note">{qs_note}</div>
    </section>

    <section id="modes">
      <h2><small>Input modes</small>{modes_h}</h2>
      <p>{modes_intro}</p>
      <div class="cards">
{modes_cards}
      </div>
      <div class="demo2">{demo_img}{demo_text}</div>
      <h3>{img_tips_h}</h3>
      <ul>
{img_tips}
      </ul>
      <h3>{open_h}</h3>
      <p>{open_p}</p>
    </section>

    <section id="settings">
      <h2><small>Settings</small>{settings_h}</h2>
      <table>
{settings}
      </table>
    </section>

    <section id="effects">
      <h2><small>Effects</small>{effects_h}</h2>
      {demo_fx}
      <table>
{effects}
      </table>
    </section>

    <section id="edit">
      <h2><small>Editing</small>{edit_h}</h2>
      <ul>
{edit}
      </ul>
      <h3>{keys_h}</h3>
      <table>
{keys}
      </table>
      <p>{keys_note}</p>
    </section>

    <section id="export">
      <h2><small>Export</small>{export_h}</h2>
      <p>{export_intro}</p>
      <ul>
{export}
      </ul>
    </section>

    <section id="mobile">
      <h2><small>Mobile</small>{mobile_h}</h2>
      <div class="mob">
        <div>
{mobile}
        </div>
        <img src="/assets/screenshot-mobile-{code}.jpg" width="780" height="1600" alt="{mobile_alt}" loading="lazy">
      </div>
    </section>

    <section id="math">
      <h2><small>Math</small>{math_h}</h2>
      <h3>{m1_h}</h3>
      <p>{m1}</p>
      <h3>{m2_h}</h3>
      <div class="fm">X[k] = (1/N) · Σ<sub>n=0..N−1</sub> z[n] · e<sup>−i2πkn/N</sup></div>
      <p>{m2}</p>
      <table>
{m2_table}
      </table>
      <h3>{m3_h}</h3>
      <div class="fm">z(t) = Σ<sub>k</sub> X[k] · e<sup>ikt</sup>　(0 ≤ t &lt; 2π)</div>
      <p>{m3}</p>
      {demo_conv}
      <div class="note">{m3_note}</div>
    </section>

    <section id="faq">
      <h2><small>FAQ</small>{faq_h}</h2>
{faq_html}
    </section>

    <div class="end">
      <h2>{end_h}</h2>
      <p>{end_p}</p>
      <a class="cta lg" href="{app}">{end_cta}</a>
    </div>
  </main>
</div>

<footer>
  {langs}
  <p>&copy; Ike mfr ・ <a href="{app}">FouriTre</a> ・ <a href="https://buymeacoffee.com/ike_mfr">Buy Me a Coffee</a></p>
</footer>
{demo_js}
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
'''

DEMO_SIZE = {'quickstart': (960, 560), 'image': (720, 528), 'text': (720, 528), 'effects': (720, 528), 'converge': (720, 528)}


def demo(name, caption, src=None):
    w, h = DEMO_SIZE[name]
    src = src or name
    return (f'<figure class="demo"><video poster="/assets/demo/{src}.jpg" '
            f'width="{w}" height="{h}" muted loop playsinline preload="none" aria-label="{caption}">'
            f'<source src="/assets/demo/{src}.webm" type="video/webm"><source src="/assets/demo/{src}.mp4" type="video/mp4">'
            f'</video><figcaption>{caption}</figcaption></figure>')


# Play demo videos only while visible; respect reduced motion.
DEMO_JS = """<script>
(function () {
  var vids = document.querySelectorAll('.demo video');
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    vids.forEach(function (v) { v.controls = true; v.preload = 'metadata'; });
    return;
  }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.play().catch(function () {}); } else { e.target.pause(); } });
  }, { threshold: 0.35 });
  vids.forEach(function (v) { io.observe(v); });
})();
</script>"""


TOC_IDS = ['what', 'quickstart', 'modes', 'settings', 'effects', 'edit', 'export', 'mobile', 'math', 'faq']


def rows(pairs):
    return '\n'.join(f'        <tr><th>{a}</th><td>{b}</td></tr>' for a, b in pairs)


def lis(items, indent=8):
    return '\n'.join(' ' * indent + f'<li>{x}</li>' for x in items)


def paras(items, indent=6):
    return '\n'.join(' ' * indent + f'<p>{x}</p>' for x in items)


def build(code, t):
    path = dict((c, p) for c, p, _, _ in LANGS)[code]
    htmllang = dict((c, h) for c, _, h, _ in LANGS)[code]
    url = SITE + path
    app = f'/?lang={code}'
    faq_html = '\n'.join(
        f'      <details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(t['faq']))
    jsonld = {
        '@context': 'https://schema.org',
        '@graph': [
            {
                '@type': 'TechArticle', '@id': url + '#article', 'headline': t['ld_headline'],
                'description': t['description'], 'inLanguage': htmllang, 'image': SITE + '/assets/og.jpg',
                'author': {'@type': 'Person', 'name': 'Ike mfr'}, 'publisher': {'@type': 'Person', 'name': 'Ike mfr'},
                'dateModified': UPDATED, 'mainEntityOfPage': url,
                'about': [{'@type': 'Thing', 'name': n} for n in t['ld_about']],
            },
            {
                '@type': 'BreadcrumbList', 'itemListElement': [
                    {'@type': 'ListItem', 'position': 1, 'name': 'FouriTre', 'item': SITE + '/'},
                    {'@type': 'ListItem', 'position': 2, 'name': t['ld_crumb'], 'item': url},
                ]
            },
            {
                '@type': 'FAQPage', 'mainEntity': [
                    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                    for q, a in t['faq']
                ]
            },
        ],
    }
    v = dict(t)
    v.update(
        htmllang=htmllang, url=url, app=app, site=SITE, code=code,
        hreflang=hreflang_links(), langs=lang_switch(code),
        extrafont='&family=Noto+Sans+SC:wght@400;500;700' if code == 'zh' else '',
        jsonld=json.dumps(jsonld, ensure_ascii=False, indent=2),
        badges=''.join(f'<span>{b}</span>' for b in t['badges']),
        toc='\n'.join(f'    <a href="#{i}">{n}</a>' for i, n in zip(TOC_IDS, t['toc'])),
        what=paras(t['what']),
        qs_steps='\n'.join(f'        <li><b>{a}</b><br>{b}</li>' for a, b in t['qs_steps']),
        modes_cards='\n'.join(f'        <div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in t['modes_cards']),
        img_tips=lis(t['img_tips']), settings=rows(t['settings']), effects=rows(t['effects']),
        edit=lis(t['edit']), keys=rows(t['keys']), export=lis(t['export']),
        mobile=paras(t['mobile'], 10), m2_table=rows(t['m2_table']), faq_html=faq_html,
        demo_qs=demo('quickstart', t['cap_qs'], 'quickstart-' + code), demo_img=demo('image', t['cap_img']),
        demo_text=demo('text', t['cap_text']), demo_fx=demo('effects', t['cap_fx']), demo_conv=demo('converge', t['cap_conv']),
        demo_js=DEMO_JS,
    )
    html = TEMPLATE.format(**v)
    out = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', os.path.relpath(out, ROOT))


KBD_UNDO = '<kbd>Ctrl</kbd> + <kbd>Z</kbd>'
KBD_REDO = '<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd> / <kbd>Ctrl</kbd> + <kbd>Y</kbd>'
KBD_CP = '<kbd>Ctrl</kbd> + <kbd>C</kbd> / <kbd>Ctrl</kbd> + <kbd>V</kbd>'

T = {}

T['en'] = dict(
    cap_qs='Draw one stroke and the chain of circles redraws it. Lower “Circles” and the shape gets rounder.', cap_img='Contours extracted from an image, drawn with epicycles (the “Fourier” preset).', cap_text='The text “Fourier ♥” turned into outlines.', cap_fx='Mirror + Rainbow + Sparkle.', cap_conv='The more circles (n), the closer the shape gets to the original cat.',
    oglocale='en_US',
    title='How to Use FouriTre | Draw with Fourier Transform Epicycles',
    description='Learn how to use FouriTre, a free web tool that turns your drawings, images and text into rotating circles (epicycles) using the Fourier transform. Covers drawing, image import, text, effects, video export and how the discrete Fourier transform works.',
    ogtitle='FouriTre Guide | Fourier Transform Epicycle Drawing Tool',
    ogdesc='How to use FouriTre, the free web tool that redraws your sketches with rotating circles, and how the Fourier transform behind it works.',
    ld_headline='How to use FouriTre', ld_crumb='Guide',
    ld_about=['Fourier transform', 'Discrete Fourier transform', 'Epicycles'],
    nav_start='Get started', nav_math='How it works', nav_open='Open the app',
    eyebrow='How to use FouriTre',
    h1='Redraw any line<br>with spinning circles.',
    lead='<b>FouriTre</b> takes a hand-drawn line, an image or text, runs a <b>Fourier transform</b> on it, and redraws it by chaining together many rotating circles called <b>epicycles</b>. This guide covers how to use it and the math behind it.',
    cta='Start drawing →',
    badges=['Free', 'No sign-up or install', 'Desktop / phone / tablet', '5 languages'],
    hero_alt='The FouriTre app redrawing contours extracted from a portrait of Fourier with colorful epicycle traces',
    toc_title='Contents',
    toc=['What is FouriTre', 'Get started in 3 steps', 'Four input modes', 'Epicycle settings', 'Effects', 'Editing', 'Saving and export', 'On mobile', 'How the Fourier transform works', 'FAQ'],
    what_h='What is FouriTre?',
    what=[
        'Any closed curve can be described as the path traced by the tip of a chain of circles, each spinning at a different speed. That is the idea behind the <b>Fourier series</b>, and FouriTre is a visualizer that lets you see it and play with it.',
        'When you draw a single stroke on the canvas, the line is decomposed into frequency components by the <b>discrete Fourier transform (DFT)</b>. Each component becomes one circle; linking the circles from largest to smallest makes the tip retrace your line. Lower the number of circles and the shape becomes round and blurry; raise it and every detail comes back, in real time.',
        'Use it as a math teaching aid, to build intuition for the Fourier transform, or just to make mesmerizing animations.',
    ],
    qs_h='Get started in 3 steps',
    qs_steps=[
        ('Open the app', 'Open <a href="/?lang=en">fouritre.vercel.app</a> in your browser. You start in Draw mode.'),
        ('Draw a single stroke', 'Drag with your mouse or finger and release. A chain of circles appears and redraws your line.'),
        ('Adjust circles and speed', 'In the right-hand panel (the settings button at the top right on phones), change “Circles” and “Draw time”. When you like the result, use “Export” to save an image or a video.'),
    ],
    qs_note='Tip: don’t feel like drawing? Pick a heart or star from the Presets tab, or press “Random” at the bottom of the screen.',
    modes_h='Four input modes', modes_intro='Use the tabs at the top of the panel to choose what to turn into epicycles.',
    modes_cards=[
        ('Draw', 'Draw freely with a mouse or finger. “Stabilizer” reduces hand jitter and “Smoothing” evens out the finished line.'),
        ('Image', 'Load a photo or illustration; edges are detected and converted into several lines. “Threshold” sets the edge sensitivity and “Contours” the number of lines used.'),
        ('Text', 'Draw the outline of letters or emoji. Multiple lines are supported, and you can load your own font file (TTF / OTF / WOFF).'),
        ('Presets', 'One click for a star, heart, infinity sign, π, butterfly, square wave, cat, spiral, DNA or a portrait of Fourier.'),
    ],
    img_tips_h='Tips for converting images',
    img_tips=[
        'Images with a plain background and clear outlines give the most stable results.',
        'If there are too many messy lines, raise “Threshold” or lower “Contours”.',
        'After changing settings, press “Re-detect” to process the same image again. “Mono” draws every trace in one color.',
    ],
    open_h='Lines that don’t close are fine',
    open_p='A Fourier series assumes a shape that comes back to where it started, so transforming an open line directly would join its two ends with a straight segment and cause ripples (the Gibbs phenomenon). FouriTre computes open lines internally as a there-and-back path and stops drawing at the end point, so your open line is reproduced exactly as drawn.',
    settings_h='Epicycle settings',
    settings=[
        ('Circles (1–2000)', 'The number of frequency components used. Fewer gives a simpler, rounder shape; more follows the original line closely. Changing it restarts the drawing.'),
        ('Draw time (0.5–60 s)', 'How many seconds one full pass takes. It runs at the same speed on 60 Hz and 120 Hz screens.'),
        ('Width (0.5–16)', 'The thickness of the trace.'),
        ('Colors', 'Change the trace, circle, background and grid colors. The background can be “Grid”, “Dots” or “None”, with the slider next to it setting the spacing.'),
    ],
    effects_h='Effects',
    effects=[
        ('Rainbow', 'Draws the trace with a rainbow gradient.'),
        ('Persist', 'Keeps finished traces on screen. Turn it off to redraw the same shape over and over.'),
        ('Reveal', 'Starts with one circle and adds more little by little, so you can watch the shape converge to your line. A great way to feel how a Fourier series converges.'),
        ('Mirror', 'Also draws the reflection across an axis. You can set the axis angle and position and show or hide the axis.'),
        ('Sparkle', 'Particles of light fly from the pen tip.'),
        ('Sync', 'With several contours, makes them all finish at the same time. When off, smaller contours finish sooner.'),
    ],
    edit_h='Editing',
    edit=[
        '<b>Move</b>: turn it on and drag near a shape to move it.',
        '<b>Copy / Paste</b>: press “Copy” and click a shape to copy it, then “Paste” to place a slightly offset duplicate. The thumbnail in the header shows what is on the clipboard.',
        '<b>Delete</b>: turn it on and click to delete the nearest shape. “Clear all” erases everything.',
        '<b>Undo / Redo</b>: up to 30 steps of history.',
    ],
    keys_h='Keyboard shortcuts',
    keys=[(KBD_UNDO, 'Undo'), (KBD_REDO, 'Redo'), (KBD_CP, 'Copy / paste the shape under the cursor')],
    keys_note='On a Mac, use <kbd>⌘</kbd> instead of <kbd>Ctrl</kbd>. While you are typing in a text field, these keys copy and paste text as usual.',
    export_h='Saving and export', export_intro='Use “Export” in the header to save with a file name of your choice.',
    export=[
        '<b>PNG / JPEG</b>: saves the current canvas as an image.',
        '<b>PNG (transparent)</b>: an image with a transparent background, handy for video editing and design.',
        '<b>WebM video</b>: records the animation from start to finish.',
        '<b>JSON project</b>: saves your lines and settings. Open it later with “Load” at the bottom of the screen to keep editing.',
    ],
    mobile_h='Using it on phones and tablets',
    mobile=[
        'On phones the settings panel is hidden so the canvas can fill the screen. Tap the <b>settings button at the top right</b> to slide the panel up from the bottom. Touching the canvas closes it automatically so you can start drawing right away.',
        'Trace with one finger to draw a line. For fine detail, a tablet with a stylus works best.',
    ],
    mobile_alt='FouriTre on a smartphone with the settings panel open',
    math_h='How the Fourier transform works',
    m1_h='1. Turn the line into a sequence of complex numbers',
    m1='The line you draw is resampled into N evenly spaced points. Treating each point (x, y) as a complex number <b>z = x + iy</b> turns the line into the sequence z[0], z[1], …, z[N−1].',
    m2_h='2. Split it into frequencies with the discrete Fourier transform',
    m2='Each resulting X[k] corresponds to one circle, defined by three properties:',
    m2_table=[('Amplitude |X[k]|', 'The radius of the circle'), ('Frequency k', 'How many turns it makes per cycle (negative means it spins the other way)'), ('Phase arg X[k]', 'The angle it starts from')],
    m3_h='3. Chain the circles to redraw the line',
    m3='Place each circle’s center on the tip of the previous one, from the largest radius down, and the tip of the last circle traces z(t). These are the <b>epicycles</b>. Large components shape the result the most, so a handful of circles already shows the rough form, and more circles add detail. <b>JPEG image compression</b> rests on the same idea of discarding the frequency components that matter least.',
    m3_note='Epicycles were first used in ancient Greek astronomy to explain the motion of the planets. Seen through the Fourier series, stacking enough circles can describe any periodic path.',
    faq_h='Frequently asked questions',
    faq=[
        ('Is FouriTre free?', 'Yes. There is nothing to sign up for or install; just open it in your browser.'),
        ('Are my drawings or images uploaded to a server?', 'No. The Fourier transform and edge detection run entirely in your browser, and your drawings and images are never sent to a server.'),
        ('What changes when I add more circles?', 'The number of circles is the number of frequency components used. With few circles the shape is round and blurry; with more, corners and fine details match the original line. You can use up to 2000.'),
        ('Does it work on smartphones?', 'Yes. Draw on the canvas with your finger and open the settings panel with the button at the top right.'),
        ('Can I save my animation?', 'From the Export menu you can save PNG, transparent PNG and JPEG images, WebM video, and a JSON project file you can edit again later.'),
    ],
    end_h='Give it a try', end_p='One stroke is all it takes to make the Fourier transform click.', end_cta='Open FouriTre →',
)

T['es'] = dict(
    cap_qs='Dibuja un trazo y la cadena de círculos lo redibuja. Al bajar «Círculos», la forma se redondea.', cap_img='Contornos extraídos de una imagen y dibujados con epiciclos (plantilla «Fourier»).', cap_text='El texto «Fourier ♥» convertido en contornos.', cap_fx='Espejo + Arcoíris + Destellos.', cap_conv='Cuantos más círculos (n), más se parece la forma al gato original.',
    oglocale='es_ES',
    title='Cómo usar FouriTre | Dibuja con epiciclos y la transformada de Fourier',
    description='Guía de FouriTre, una herramienta web gratuita que convierte tus dibujos, imágenes y textos en círculos giratorios (epiciclos) mediante la transformada de Fourier. Aprende a dibujar, importar imágenes, convertir texto, aplicar efectos, exportar vídeo y cómo funciona la transformada discreta de Fourier.',
    ogtitle='Guía de FouriTre | Dibujo con epiciclos y transformada de Fourier',
    ogdesc='Cómo usar FouriTre, la herramienta web gratuita que redibuja tus trazos con círculos que giran, y cómo funciona la transformada de Fourier que hay detrás.',
    ld_headline='Cómo usar FouriTre', ld_crumb='Guía',
    ld_about=['Transformada de Fourier', 'Transformada discreta de Fourier', 'Epiciclos'],
    nav_start='Primeros pasos', nav_math='Cómo funciona', nav_open='Abrir la app',
    eyebrow='Cómo usar FouriTre',
    h1='Redibuja cualquier trazo<br>con círculos que giran.',
    lead='<b>FouriTre</b> toma un trazo a mano alzada, una imagen o un texto, le aplica la <b>transformada de Fourier</b> y lo vuelve a dibujar encadenando muchos círculos giratorios llamados <b>epiciclos</b>. Esta guía explica cómo usarlo y las matemáticas que hay detrás.',
    cta='Empezar a dibujar →',
    badges=['Gratis', 'Sin registro ni instalación', 'PC / móvil / tableta', '5 idiomas'],
    hero_alt='FouriTre redibujando con epiciclos de colores los contornos extraídos de un retrato de Fourier',
    toc_title='Contenido',
    toc=['Qué es FouriTre', 'Empieza en 3 pasos', 'Cuatro modos de entrada', 'Ajustes de los epiciclos', 'Efectos', 'Edición', 'Guardar y exportar', 'En el móvil', 'Cómo funciona la transformada de Fourier', 'Preguntas frecuentes'],
    what_h='¿Qué es FouriTre?',
    what=[
        'Cualquier curva cerrada puede describirse como la trayectoria de la punta de una cadena de círculos que giran a distintas velocidades. Esa es la idea de las <b>series de Fourier</b>, y FouriTre es un visualizador que te permite verla y experimentar con ella.',
        'Cuando dibujas un trazo en el lienzo, se descompone en componentes de frecuencia con la <b>transformada discreta de Fourier (DFT)</b>. Cada componente se convierte en un círculo; al unirlos de mayor a menor, la punta vuelve a recorrer tu trazo. Con pocos círculos la forma queda redondeada y borrosa; con más, aparecen todos los detalles, en tiempo real.',
        'Sirve como material para clases de matemáticas, para entender la transformada de Fourier de forma intuitiva o simplemente para crear animaciones hipnóticas.',
    ],
    qs_h='Empieza en 3 pasos',
    qs_steps=[
        ('Abre la app', 'Abre <a href="/?lang=es">fouritre.vercel.app</a> en el navegador. Empiezas en el modo Dibujar.'),
        ('Dibuja un solo trazo', 'Arrastra con el ratón o el dedo y suelta. Aparece una cadena de círculos que redibuja tu trazo.'),
        ('Ajusta los círculos y la velocidad', 'En el panel de la derecha (en el móvil, el botón de ajustes arriba a la derecha) cambia «Círculos» y «Tiempo de dibujo». Cuando te guste, usa «Exportar» para guardar una imagen o un vídeo.'),
    ],
    qs_note='Consejo: ¿no te apetece dibujar? Elige un corazón o una estrella en la pestaña Plantillas o pulsa «Aleatorio» en la parte inferior.',
    modes_h='Cuatro modos de entrada', modes_intro='Con las pestañas de la parte superior del panel eliges qué convertir en epiciclos.',
    modes_cards=[
        ('Dibujar', 'Dibuja libremente con el ratón o el dedo. El «Estabilizador» reduce el temblor de la mano y el «Suavizado» alisa el trazo terminado.'),
        ('Imagen', 'Carga una foto o ilustración; se detectan los bordes y se convierten en varias líneas. El «Umbral» fija la sensibilidad y «Contornos», cuántas líneas se usan.'),
        ('Texto', 'Dibuja el contorno de letras o emojis. Admite varias líneas y puedes cargar tu propia fuente (TTF / OTF / WOFF).'),
        ('Plantillas', 'Con un clic: estrella, corazón, infinito, π, mariposa, onda cuadrada, gato, espiral, ADN o un retrato de Fourier.'),
    ],
    img_tips_h='Consejos para convertir imágenes',
    img_tips=[
        'Las imágenes con fondo liso y contornos nítidos dan los resultados más estables.',
        'Si salen demasiadas líneas, sube el «Umbral» o baja «Contornos».',
        'Tras cambiar los ajustes, pulsa «Volver a detectar» para procesar la misma imagen. «Monocromo» dibuja todos los trazos de un solo color.',
    ],
    open_h='No importa si el trazo no se cierra',
    open_p='Una serie de Fourier supone una forma que vuelve a su punto de partida, así que transformar un trazo abierto tal cual uniría sus extremos con una recta y provocaría ondulaciones (el fenómeno de Gibbs). FouriTre calcula internamente los trazos abiertos como un camino de ida y vuelta y deja de dibujar en el punto final, de modo que tu trazo abierto se reproduce tal como lo dibujaste.',
    settings_h='Ajustes de los epiciclos',
    settings=[
        ('Círculos (1–2000)', 'El número de componentes de frecuencia. Menos da una forma más simple y redonda; más sigue fielmente el trazo original. Al cambiarlo, el dibujo se reinicia.'),
        ('Tiempo de dibujo (0,5–60 s)', 'Los segundos que tarda una vuelta completa. Va a la misma velocidad en pantallas de 60 Hz y de 120 Hz.'),
        ('Grosor (0,5–16)', 'El grosor del trazo.'),
        ('Colores', 'Cambia el color del trazo, los círculos, el fondo y la rejilla. El fondo puede ser «Rejilla», «Puntos» o «Ninguno», y el control deslizante de al lado ajusta la separación.'),
    ],
    effects_h='Efectos',
    effects=[
        ('Arcoíris', 'Dibuja el trazo con un degradado de arcoíris.'),
        ('Persistir', 'Mantiene en pantalla los trazos terminados. Si lo desactivas, la misma forma se dibuja una y otra vez.'),
        ('Revelar', 'Empieza con un círculo y añade más poco a poco para que veas cómo la forma se acerca a tu trazo. Ideal para sentir cómo converge una serie de Fourier.'),
        ('Espejo', 'Dibuja también el reflejo respecto a un eje. Puedes ajustar el ángulo y la posición del eje y mostrarlo u ocultarlo.'),
        ('Destellos', 'Saltan partículas de luz desde la punta del lápiz.'),
        ('Sincronizar', 'Con varios contornos, hace que todos terminen a la vez. Desactivado, los contornos pequeños terminan antes.'),
    ],
    edit_h='Edición',
    edit=[
        '<b>Mover</b>: actívalo y arrastra cerca de una figura para moverla.',
        '<b>Copiar / Pegar</b>: pulsa «Copiar» y haz clic en una figura para copiarla; «Pegar» coloca un duplicado ligeramente desplazado. La miniatura del encabezado muestra lo que hay en el portapapeles.',
        '<b>Borrar</b>: actívalo y haz clic para borrar la figura más cercana. «Borrar todo» lo elimina todo.',
        '<b>Deshacer / Rehacer</b>: hasta 30 pasos de historial.',
    ],
    keys_h='Atajos de teclado',
    keys=[(KBD_UNDO, 'Deshacer'), (KBD_REDO, 'Rehacer'), (KBD_CP, 'Copiar / pegar la figura bajo el cursor')],
    keys_note='En Mac usa <kbd>⌘</kbd> en lugar de <kbd>Ctrl</kbd>. Mientras escribes en un campo de texto, estas teclas copian y pegan texto como siempre.',
    export_h='Guardar y exportar', export_intro='Con «Exportar» en el encabezado puedes guardar con el nombre de archivo que quieras.',
    export=[
        '<b>PNG / JPEG</b>: guarda el lienzo actual como imagen.',
        '<b>PNG (transparente)</b>: imagen con fondo transparente, útil para edición de vídeo y diseño.',
        '<b>Vídeo WebM</b>: graba la animación de principio a fin.',
        '<b>Proyecto JSON</b>: guarda tus trazos y ajustes. Ábrelo luego con «Abrir» en la parte inferior para seguir editando.',
    ],
    mobile_h='En el móvil y la tableta',
    mobile=[
        'En el móvil, el panel de ajustes se oculta para que el lienzo ocupe toda la pantalla. Toca el <b>botón de ajustes arriba a la derecha</b> y el panel sube desde abajo. Al tocar el lienzo se cierra solo, así puedes empezar a dibujar enseguida.',
        'Desliza un dedo para dibujar. Para trazos finos, lo mejor es una tableta con lápiz óptico.',
    ],
    mobile_alt='FouriTre en un smartphone con el panel de ajustes abierto',
    math_h='Cómo funciona la transformada de Fourier',
    m1_h='1. Convertir el trazo en una serie de números complejos',
    m1='El trazo se vuelve a muestrear en N puntos equidistantes. Si cada punto (x, y) se trata como el número complejo <b>z = x + iy</b>, el trazo se convierte en la sucesión z[0], z[1], …, z[N−1].',
    m2_h='2. Descomponerlo en frecuencias con la transformada discreta de Fourier',
    m2='Cada X[k] resultante corresponde a un círculo, definido por tres propiedades:',
    m2_table=[('Amplitud |X[k]|', 'El radio del círculo'), ('Frecuencia k', 'Cuántas vueltas da por ciclo (si es negativa, gira al revés)'), ('Fase arg X[k]', 'El ángulo desde el que empieza')],
    m3_h='3. Encadenar los círculos para redibujar el trazo',
    m3='Coloca el centro de cada círculo en la punta del anterior, del radio mayor al menor, y la punta del último dibuja z(t). Esos son los <b>epiciclos</b>. Los componentes grandes son los que más influyen en la forma, así que con unos pocos círculos ya aparece la silueta y con más se añaden los detalles. La <b>compresión JPEG</b> se basa en la misma idea de descartar los componentes de frecuencia menos importantes.',
    m3_note='Los epiciclos se usaron por primera vez en la astronomía de la antigua Grecia para explicar el movimiento de los planetas. Desde el punto de vista de las series de Fourier, con suficientes círculos se puede describir cualquier trayectoria periódica.',
    faq_h='Preguntas frecuentes',
    faq=[
        ('¿FouriTre es gratis?', 'Sí. No hace falta registrarse ni instalar nada: basta con abrirlo en el navegador.'),
        ('¿Se suben mis dibujos o imágenes a un servidor?', 'No. La transformada de Fourier y la detección de bordes se calculan por completo en tu navegador, y tus dibujos e imágenes nunca se envían a un servidor.'),
        ('¿Qué cambia si añado más círculos?', 'El número de círculos es el número de componentes de frecuencia. Con pocos, la forma queda redondeada y borrosa; con más, las esquinas y los detalles se ajustan al trazo original. Puedes usar hasta 2000.'),
        ('¿Funciona en el móvil?', 'Sí. Dibuja en el lienzo con el dedo y abre el panel de ajustes con el botón de arriba a la derecha.'),
        ('¿Puedo guardar mi animación?', 'Desde el menú Exportar puedes guardar imágenes PNG, PNG transparente y JPEG, vídeo WebM y un proyecto JSON que podrás volver a editar.'),
    ],
    end_h='Pruébalo ahora', end_p='Un solo trazo basta para entender la transformada de Fourier.', end_cta='Abrir FouriTre →',
)

T['pt'] = dict(
    cap_qs='Desenhe um traço e a corrente de círculos o redesenha. Ao diminuir “Círculos”, a forma fica arredondada.', cap_img='Contornos extraídos de uma imagem, desenhados com epiciclos (modelo “Fourier”).', cap_text='O texto “Fourier ♥” convertido em contornos.', cap_fx='Espelho + Arco-íris + Brilhos.', cap_conv='Quanto mais círculos (n), mais a forma se aproxima do gato original.',
    oglocale='pt_BR',
    title='Como usar o FouriTre | Desenhe com epiciclos e a transformada de Fourier',
    description='Guia do FouriTre, uma ferramenta web gratuita que transforma seus desenhos, imagens e textos em círculos giratórios (epiciclos) usando a transformada de Fourier. Aprenda a desenhar, importar imagens, converter texto, aplicar efeitos, exportar vídeo e como funciona a transformada discreta de Fourier.',
    ogtitle='Guia do FouriTre | Desenho com epiciclos e transformada de Fourier',
    ogdesc='Como usar o FouriTre, a ferramenta web gratuita que redesenha seus traços com círculos que giram, e como funciona a transformada de Fourier por trás dele.',
    ld_headline='Como usar o FouriTre', ld_crumb='Guia',
    ld_about=['Transformada de Fourier', 'Transformada discreta de Fourier', 'Epiciclos'],
    nav_start='Primeiros passos', nav_math='Como funciona', nav_open='Abrir o app',
    eyebrow='Como usar o FouriTre',
    h1='Redesenhe qualquer traço<br>com círculos que giram.',
    lead='O <b>FouriTre</b> pega um traço feito à mão, uma imagem ou um texto, aplica a <b>transformada de Fourier</b> e o redesenha encadeando vários círculos giratórios chamados <b>epiciclos</b>. Este guia mostra como usá-lo e a matemática por trás dele.',
    cta='Começar a desenhar →',
    badges=['Grátis', 'Sem cadastro nem instalação', 'PC / celular / tablet', '5 idiomas'],
    hero_alt='O FouriTre redesenhando com epiciclos coloridos os contornos extraídos de um retrato de Fourier',
    toc_title='Conteúdo',
    toc=['O que é o FouriTre', 'Comece em 3 passos', 'Quatro modos de entrada', 'Ajustes dos epiciclos', 'Efeitos', 'Edição', 'Salvar e exportar', 'No celular', 'Como funciona a transformada de Fourier', 'Perguntas frequentes'],
    what_h='O que é o FouriTre?',
    what=[
        'Qualquer curva fechada pode ser descrita como o caminho traçado pela ponta de uma corrente de círculos, cada um girando numa velocidade diferente. Essa é a ideia das <b>séries de Fourier</b>, e o FouriTre é um visualizador que permite ver e brincar com ela.',
        'Quando você desenha um traço na tela, ele é decomposto em componentes de frequência pela <b>transformada discreta de Fourier (DFT)</b>. Cada componente vira um círculo; ligando os círculos do maior para o menor, a ponta refaz o seu traço. Com poucos círculos a forma fica arredondada e borrada; com mais, todos os detalhes voltam, em tempo real.',
        'Use como material para aulas de matemática, para entender a transformada de Fourier de forma intuitiva ou só para criar animações hipnotizantes.',
    ],
    qs_h='Comece em 3 passos',
    qs_steps=[
        ('Abra o app', 'Abra <a href="/?lang=pt">fouritre.vercel.app</a> no navegador. Você começa no modo Desenhar.'),
        ('Desenhe um único traço', 'Arraste com o mouse ou o dedo e solte. Uma corrente de círculos aparece e redesenha o seu traço.'),
        ('Ajuste os círculos e a velocidade', 'No painel à direita (no celular, o botão de ajustes no canto superior direito), mude “Círculos” e “Tempo de desenho”. Quando gostar do resultado, use “Exportar” para salvar uma imagem ou um vídeo.'),
    ],
    qs_note='Dica: sem vontade de desenhar? Escolha um coração ou uma estrela na aba Modelos, ou toque em “Aleatório” na parte de baixo da tela.',
    modes_h='Quatro modos de entrada', modes_intro='Use as abas no topo do painel para escolher o que transformar em epiciclos.',
    modes_cards=[
        ('Desenhar', 'Desenhe livremente com o mouse ou o dedo. O “Estabilizador” reduz o tremor da mão e a “Suavização” deixa o traço final mais liso.'),
        ('Imagem', 'Carregue uma foto ou ilustração; as bordas são detectadas e convertidas em várias linhas. O “Limiar” define a sensibilidade e “Contornos”, quantas linhas são usadas.'),
        ('Texto', 'Desenhe o contorno de letras ou emojis. Aceita várias linhas e você pode carregar sua própria fonte (TTF / OTF / WOFF).'),
        ('Modelos', 'Com um clique: estrela, coração, infinito, π, borboleta, onda quadrada, gato, espiral, DNA ou um retrato de Fourier.'),
    ],
    img_tips_h='Dicas para converter imagens',
    img_tips=[
        'Imagens com fundo liso e contornos nítidos dão os resultados mais estáveis.',
        'Se aparecerem linhas demais, aumente o “Limiar” ou diminua “Contornos”.',
        'Depois de mudar os ajustes, toque em “Detectar de novo” para processar a mesma imagem. “Monocromático” desenha todos os traços numa só cor.',
    ],
    open_h='Tudo bem se o traço não fechar',
    open_p='Uma série de Fourier pressupõe uma forma que volta ao ponto de partida, então transformar um traço aberto diretamente ligaria as duas pontas com uma reta e causaria ondulações (o fenômeno de Gibbs). O FouriTre calcula internamente os traços abertos como um caminho de ida e volta e para de desenhar no ponto final, reproduzindo o traço aberto exatamente como você o desenhou.',
    settings_h='Ajustes dos epiciclos',
    settings=[
        ('Círculos (1–2000)', 'O número de componentes de frequência. Menos dá uma forma mais simples e arredondada; mais segue fielmente o traço original. Ao mudar, o desenho recomeça.'),
        ('Tempo de desenho (0,5–60 s)', 'Quantos segundos leva uma volta completa. A velocidade é a mesma em telas de 60 Hz e de 120 Hz.'),
        ('Espessura (0,5–16)', 'A espessura do traço.'),
        ('Cores', 'Mude a cor do traço, dos círculos, do fundo e da grade. O fundo pode ser “Grade”, “Pontos” ou “Nenhum”, e o controle deslizante ao lado ajusta o espaçamento.'),
    ],
    effects_h='Efeitos',
    effects=[
        ('Arco-íris', 'Desenha o traço com um degradê de arco-íris.'),
        ('Manter', 'Mantém na tela os traços concluídos. Desligado, a mesma forma é desenhada repetidamente.'),
        ('Revelar', 'Começa com um círculo e acrescenta mais aos poucos, para você ver a forma se aproximar do seu traço. Ótimo para sentir como uma série de Fourier converge.'),
        ('Espelho', 'Desenha também o reflexo em relação a um eixo. Dá para ajustar o ângulo e a posição do eixo e mostrá-lo ou ocultá-lo.'),
        ('Brilhos', 'Partículas de luz saem da ponta da caneta.'),
        ('Sincronizar', 'Com vários contornos, faz todos terminarem ao mesmo tempo. Desligado, os contornos menores terminam antes.'),
    ],
    edit_h='Edição',
    edit=[
        '<b>Mover</b>: ative e arraste perto de uma figura para movê-la.',
        '<b>Copiar / Colar</b>: toque em “Copiar” e clique numa figura para copiá-la; “Colar” cria uma cópia levemente deslocada. A miniatura no cabeçalho mostra o que está copiado.',
        '<b>Apagar</b>: ative e clique para apagar a figura mais próxima. “Limpar tudo” apaga tudo.',
        '<b>Desfazer / Refazer</b>: até 30 passos de histórico.',
    ],
    keys_h='Atalhos de teclado',
    keys=[(KBD_UNDO, 'Desfazer'), (KBD_REDO, 'Refazer'), (KBD_CP, 'Copiar / colar a figura sob o cursor')],
    keys_note='No Mac, use <kbd>⌘</kbd> no lugar de <kbd>Ctrl</kbd>. Enquanto você digita num campo de texto, essas teclas copiam e colam texto normalmente.',
    export_h='Salvar e exportar', export_intro='Use “Exportar” no cabeçalho para salvar com o nome de arquivo que quiser.',
    export=[
        '<b>PNG / JPEG</b>: salva a tela atual como imagem.',
        '<b>PNG (transparente)</b>: imagem com fundo transparente, útil para edição de vídeo e design.',
        '<b>Vídeo WebM</b>: grava a animação do início ao fim.',
        '<b>Projeto JSON</b>: salva seus traços e ajustes. Abra depois com “Abrir” na parte de baixo para continuar editando.',
    ],
    mobile_h='No celular e no tablet',
    mobile=[
        'No celular, o painel de ajustes fica escondido para a tela de desenho ocupar todo o espaço. Toque no <b>botão de ajustes no canto superior direito</b> e o painel sobe por baixo. Ao tocar na tela de desenho ele fecha sozinho, para você começar a desenhar na hora.',
        'Deslize um dedo para desenhar. Para detalhes finos, um tablet com caneta é o ideal.',
    ],
    mobile_alt='O FouriTre num smartphone com o painel de ajustes aberto',
    math_h='Como funciona a transformada de Fourier',
    m1_h='1. Transformar o traço numa sequência de números complexos',
    m1='O traço é reamostrado em N pontos igualmente espaçados. Tratando cada ponto (x, y) como o número complexo <b>z = x + iy</b>, o traço vira a sequência z[0], z[1], …, z[N−1].',
    m2_h='2. Separar em frequências com a transformada discreta de Fourier',
    m2='Cada X[k] obtido corresponde a um círculo, definido por três propriedades:',
    m2_table=[('Amplitude |X[k]|', 'O raio do círculo'), ('Frequência k', 'Quantas voltas dá por ciclo (negativa significa girar ao contrário)'), ('Fase arg X[k]', 'O ângulo de partida')],
    m3_h='3. Encadear os círculos para redesenhar o traço',
    m3='Coloque o centro de cada círculo na ponta do anterior, do maior raio para o menor, e a ponta do último desenha z(t). Esses são os <b>epiciclos</b>. Os componentes grandes são os que mais definem a forma, então poucos círculos já mostram o contorno geral, e mais círculos acrescentam detalhes. A <b>compressão JPEG</b> se baseia na mesma ideia de descartar os componentes de frequência menos importantes.',
    m3_note='Os epiciclos foram usados pela primeira vez na astronomia da Grécia antiga para explicar o movimento dos planetas. Do ponto de vista das séries de Fourier, com círculos suficientes é possível descrever qualquer trajetória periódica.',
    faq_h='Perguntas frequentes',
    faq=[
        ('O FouriTre é gratuito?', 'Sim. Não é preciso cadastro nem instalação: basta abrir no navegador.'),
        ('Meus desenhos ou imagens são enviados para um servidor?', 'Não. A transformada de Fourier e a detecção de bordas são calculadas inteiramente no seu navegador, e seus desenhos e imagens nunca são enviados para um servidor.'),
        ('O que muda quando aumento o número de círculos?', 'O número de círculos é o número de componentes de frequência. Com poucos, a forma fica arredondada e borrada; com mais, cantos e detalhes ficam iguais ao traço original. Dá para usar até 2000.'),
        ('Funciona no celular?', 'Sim. Desenhe na tela com o dedo e abra o painel de ajustes pelo botão no canto superior direito.'),
        ('Posso salvar minha animação?', 'Pelo menu Exportar você salva imagens PNG, PNG transparente e JPEG, vídeo WebM e um projeto JSON que pode ser editado de novo depois.'),
    ],
    end_h='Experimente agora', end_p='Um único traço basta para a transformada de Fourier fazer sentido.', end_cta='Abrir o FouriTre →',
)

T['zh'] = dict(
    cap_qs='一笔画出线条，旋转的圆就会把它重新画出来。减少“圆的数量”，形状会变圆。', cap_img='从图片中提取轮廓，再用本轮画出来（“傅里叶”模板）。', cap_text='把文字“Fourier ♥”转换成轮廓。', cap_fx='镜像 + 彩虹 + 闪光。', cap_conv='圆的数量 n 越多，形状越接近原来的猫。',
    oglocale='zh_CN',
    title='FouriTre 使用指南 | 用傅里叶变换和本轮（周转圆）画画',
    description='FouriTre 是一款免费的网页工具，用傅里叶变换把手绘线条、图片和文字变成一串旋转的圆（本轮）重新画出来。本指南介绍绘制、导入图片、文字转换、效果、视频导出等操作，以及离散傅里叶变换（DFT）的原理。',
    ogtitle='FouriTre 使用指南 | 傅里叶变换本轮绘图工具',
    ogdesc='介绍免费网页工具 FouriTre 的用法：用旋转的圆重新画出你的线条，并讲解背后的傅里叶变换原理。',
    ld_headline='FouriTre 使用指南', ld_crumb='使用指南',
    ld_about=['傅里叶变换', '离散傅里叶变换', '本轮'],
    nav_start='快速上手', nav_math='原理', nav_open='打开应用',
    eyebrow='How to use FouriTre',
    h1='用旋转的圆，<br>把你画的线重新画出来。',
    lead='<b>FouriTre</b> 会对手绘线条、图片或文字进行<b>傅里叶变换</b>，再把许多旋转的圆（<b>本轮</b>，也叫周转圆）首尾相连，重新画出原来的形状。本指南介绍它的用法和背后的数学原理。',
    cta='马上开始画 →',
    badges=['免费', '无需注册和安装', '电脑 / 手机 / 平板', '支持 5 种语言'],
    hero_alt='FouriTre 用彩色的本轮轨迹重新画出从傅里叶肖像中提取的轮廓',
    toc_title='目录',
    toc=['FouriTre 是什么', '三步上手', '四种输入模式', '本轮设置', '效果', '编辑操作', '保存与导出', '在手机上使用', '傅里叶变换的原理', '常见问题'],
    what_h='FouriTre 是什么？',
    what=[
        '任何一条闭合曲线，都可以看成一串以不同速度旋转的圆的末端所描出的轨迹。这就是<b>傅里叶级数</b>的思想，而 FouriTre 是一个让你亲眼看到、亲手体验这一思想的可视化工具。',
        '在画布上一笔画出线条后，它会通过<b>离散傅里叶变换（DFT）</b>被分解成各个频率分量。每个分量对应一个圆，把圆按半径从大到小首尾相连，末端就会重新描出你的线条。减少圆的数量，形状会变圆、变模糊；增加圆的数量，细节会一点点回来，一切都是实时的。',
        '它可以用作数学课的教具，帮助直观理解傅里叶变换，也可以用来制作有趣的动画。',
    ],
    qs_h='三步上手',
    qs_steps=[
        ('打开应用', '在浏览器中打开 <a href="/?lang=zh">fouritre.vercel.app</a>，默认是“绘制”模式。'),
        ('一笔画出线条', '用鼠标或手指拖动后松开，一串旋转的圆就会出现，并重新画出你的线条。'),
        ('调整圆的数量和速度', '在右侧面板（手机上点右上角的设置按钮）中修改“圆的数量”和“绘制时间”。满意后，用“导出”保存为图片或视频。'),
    ],
    qs_note='提示：不想自己画？在“模板”选项卡里选择爱心或星星，或者点击屏幕下方的“随机生成”就能看到效果。',
    modes_h='四种输入模式', modes_intro='用面板顶部的选项卡选择要变成本轮的内容。',
    modes_cards=[
        ('绘制', '用鼠标或手指自由绘画。“防抖”可以减少手抖，“平滑”会让画好的线条更顺滑。'),
        ('图片', '载入照片或插图，自动检测边缘并转换成多条线。“阈值”决定检测灵敏度，“轮廓数”决定使用多少条线。'),
        ('文字', '画出文字或表情符号的轮廓。支持多行，也可以载入自己的字体文件（TTF / OTF / WOFF）。'),
        ('模板', '一键调出星星、爱心、无穷符号、π、蝴蝶、方波、猫、螺旋、DNA 和傅里叶肖像。'),
    ],
    img_tips_h='让图片转换效果更好的技巧',
    img_tips=[
        '背景单一、轮廓清晰的图片效果最稳定。',
        '线条太多太乱时，可以调高“阈值”或减少“轮廓数”。',
        '修改设置后，点击“重新检测”即可重新处理同一张图片。“单色”会把所有轨迹统一成一种颜色。',
    ],
    open_h='线条首尾不相连也没关系',
    open_p='傅里叶级数假定图形会回到起点，所以如果直接变换一条不闭合的线，两端会被一条直线连起来，并在那里出现波纹（吉布斯现象）。FouriTre 在内部把不闭合的线当作“去了再回来”的路径来计算，并在终点停止绘制，因此会按你画的样子还原这条开放的线。',
    settings_h='本轮设置',
    settings=[
        ('圆的数量（1–2000）', '使用的频率分量个数。越少形状越简单、越圆；越多越接近原来的线条。修改后会重新开始绘制。'),
        ('绘制时间（0.5–60 秒）', '画完一整圈所需的秒数。无论屏幕刷新率是 60Hz 还是 120Hz，速度都一样。'),
        ('线宽（0.5–16）', '轨迹线条的粗细。'),
        ('颜色', '可以自由修改轨迹、圆、背景和网格的颜色。背景可选“网格”“圆点”或“无”，旁边的滑块用来调整间距。'),
    ],
    effects_h='效果',
    effects=[
        ('彩虹', '用彩虹渐变色画出轨迹。'),
        ('保留轨迹', '把画完的轨迹留在画面上。关闭后会反复画同一个图形。'),
        ('渐显', '从 1 个圆开始逐渐增加，让你看到形状一点点接近原来的线条。很适合体会傅里叶级数的收敛。'),
        ('镜像', '同时画出关于某条轴对称的轨迹。可以调整轴的角度和位置，也可以显示或隐藏轴。'),
        ('闪光', '笔尖会飞出闪亮的粒子。'),
        ('同步绘制', '有多个轮廓时，让它们同时画完。关闭时，越小的轮廓越早画完。'),
    ],
    edit_h='编辑操作',
    edit=[
        '<b>移动</b>：打开后在图形附近拖动，就能移动该图形。',
        '<b>复制 / 粘贴</b>：点击“复制”后再点击图形即可复制，点击“粘贴”会稍微错开位置贴上一份。顶部的缩略图会显示当前复制的图形。',
        '<b>选择删除</b>：打开后点击，会删除离点击位置最近的图形。“全部清除”会删除所有内容。',
        '<b>撤销 / 重做</b>：最多可追溯 30 步。',
    ],
    keys_h='键盘快捷键',
    keys=[(KBD_UNDO, '撤销'), (KBD_REDO, '重做'), (KBD_CP, '复制 / 粘贴鼠标所在位置的图形')],
    keys_note='在 Mac 上请用 <kbd>⌘</kbd> 代替 <kbd>Ctrl</kbd>。在文本框中输入时，这些按键会像平常一样复制、粘贴文字。',
    export_h='保存与导出', export_intro='点击顶部的“导出”，可以自定义文件名后保存。',
    export=[
        '<b>PNG / JPEG</b>：把当前画布保存为图片。',
        '<b>PNG（透明）</b>：背景透明的图片，适合用作视频剪辑或设计素材。',
        '<b>WebM 视频</b>：录制从开始到画完的整个动画。',
        '<b>JSON 项目</b>：保存线条数据和设置。之后用屏幕下方的“打开”载入，就能继续编辑。',
    ],
    mobile_h='在手机和平板上使用',
    mobile=[
        '在手机上，为了让画布占满屏幕，设置面板默认是隐藏的。点击<b>右上角的设置按钮</b>，面板会从下方滑出。触碰画布时面板会自动关闭，可以马上开始画。',
        '用一根手指滑动即可画线。想画精细的线条，推荐使用平板和触控笔。',
    ],
    mobile_alt='在智能手机上打开 FouriTre 设置面板的画面',
    math_h='傅里叶变换的原理',
    m1_h='1. 把线条变成一串复数',
    m1='先把线条按等长重新取样成 N 个点。把每个点的坐标 (x, y) 看作复数 <b>z = x + iy</b>，线条就变成了复数序列 z[0], z[1], …, z[N−1]。',
    m2_h='2. 用离散傅里叶变换分解成频率',
    m2='得到的每个 X[k] 对应一个圆，由以下三个属性决定：',
    m2_table=[('振幅 |X[k]|', '圆的半径'), ('频率 k', '每个周期转几圈（负数表示反向旋转）'), ('相位 arg X[k]', '开始旋转时的角度')],
    m3_h='3. 把圆连起来重新画线',
    m3='按半径从大到小，把每个圆的圆心放在前一个圆的末端，最后一个圆的末端就会画出 z(t)。这就是<b>本轮</b>（周转圆）。半径越大的分量对形状影响越大，所以只用前几个圆就能看出大致轮廓，圆越多细节越丰富。<b>JPEG 图片压缩</b>也基于同样的思想：舍弃影响较小的频率分量。',
    m3_note='本轮最早是古希腊天文学为了解释行星运动而提出的。从傅里叶级数的角度看，只要叠加足够多的圆，就能表示任何周期性的轨迹。',
    faq_h='常见问题',
    faq=[
        ('FouriTre 是免费的吗？', '是的，完全免费。无需注册或安装，用浏览器打开即可使用。'),
        ('我画的图或图片会上传到服务器吗？', '不会。傅里叶变换和边缘检测都在你的浏览器中完成，画的线条和载入的图片不会被发送到服务器。'),
        ('增加圆的数量会有什么变化？', '圆的数量就是使用的频率分量个数。圆少时形状又圆又模糊；圆越多，棱角和细节越接近原来的线条。最多可以设置 2000 个。'),
        ('手机上能用吗？', '可以。用手指在画布上画即可，设置可以通过右上角的按钮打开面板进行修改。'),
        ('可以保存做好的动画吗？', '在“导出”菜单中，可以保存为 PNG、透明 PNG、JPEG 图片，WebM 视频，以及可以再次编辑的 JSON 项目文件。'),
    ],
    end_h='马上来试试吧', end_p='只要画一笔，傅里叶变换就会变得亲切起来。', end_cta='打开 FouriTre →',
)


if __name__ == '__main__':
    for code in ['en', 'es', 'pt', 'zh']:
        build(code, T[code])
