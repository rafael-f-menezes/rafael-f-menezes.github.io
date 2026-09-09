#!/usr/bin/env python3
"""Generates the HTML pages from Python templates (shared header/footer). Run from the repo root:
    python3 tools/build_pages.py
The generated HTML is committed; this script only keeps the nav/footer consistent across pages."""
import os

SITE = "https://res07.github.io"
NAV = [("index.html", "About"), ("research.html", "Research"), ("publications.html", "Publications"),
       ("animations.html", "Animations"), ("outreach.html", "Outreach"), ("assets/cv/Rafael_Ferreira_de_Menezes_CV.pdf", "CV (PDF)")]
FONTS = "https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Mono:wght@400;500&display=swap"

ICONS = {
 "mail": '<svg viewBox="0 0 24 24"><path d="M2 5h20v14H2zM4 7v.5l8 5 8-5V7l-8 5z"/></svg>',
 "scholar": '<svg viewBox="0 0 24 24"><path d="M12 3 1 9l11 6 9-4.9V17h2V9zM5 13.2V17l7 4 7-4v-3.8l-7 3.8z"/></svg>',
 "orcid": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-3.3 4.4a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM7.9 9.3h1.6v7.5H7.9zm3.3 0h3.3c2.6 0 3.9 1.7 3.9 3.8s-1.3 3.7-3.9 3.7h-3.3zm1.6 1.4v4.7h1.6c1.7 0 2.4-1 2.4-2.3 0-1.4-.8-2.4-2.4-2.4z"/></svg>',
 "linkedin": '<svg viewBox="0 0 24 24"><path d="M4 3.5A1.5 1.5 0 1 1 4 6.5a1.5 1.5 0 0 1 0-3zM2.8 8h2.4v13H2.8zm5 0h2.3v1.8c.5-.9 1.7-2 3.6-2 3.6 0 4.3 2.4 4.3 5.4V21h-2.4v-6.2c0-1.5 0-3.4-2.1-3.4s-2.4 1.6-2.4 3.3V21H7.8z"/></svg>',
 "github": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.2-3.4-1.2-.4-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.7-1.4-2.2-.2-4.6-1.1-4.6-4.9 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.8 1a9.5 9.5 0 0 1 5 0c1.9-1.3 2.8-1 2.8-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.8-2.4 4.7-4.6 4.9.4.3.7.9.7 1.9v2.8c0 .3.2.6.7.5A10 10 0 0 0 12 2z"/></svg>',
 "cv": '<svg viewBox="0 0 24 24"><path d="M6 2h8l5 5v15H6zm7 1.5V8h4.5zM8 11h8v1.5H8zm0 3h8v1.5H8zm0 3h5v1.5H8z"/></svg>',
}

def head(title, desc, page, og_image="assets/img/headshot.jpg"):
    navhtml = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == page else "", l) for h, l in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{'' if page=='index.html' else page}">
<meta property="og:image" content="{SITE}/{og_image}">
<link rel="canonical" href="{SITE}/{'' if page=='index.html' else page}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html">Rafael Ferreira de Menezes</a>
  <nav class="main" aria-label="Main">
    {navhtml}
    <button class="theme-btn" type="button" aria-label="Toggle color theme">Theme</button>
  </nav>
</div></header>
<main id="main" class="wrap">
"""

FOOT = """</main>
<footer class="site-footer"><div class="wrap">
  <span>Rafael Ferreira de Menezes · University of Colorado Boulder · Washington, DC</span>
  <span><a href="mailto:ferreira.rafaeldemenezes@gmail.com">Email</a> · <a href="https://scholar.google.com/citations?user=69vW21YAAAAJ&amp;hl=en">Google Scholar</a> · <a href="https://orcid.org/0000-0002-4908-3391">ORCID</a> · <a href="https://www.linkedin.com/in/rafael-ferreira-de-menezes/">LinkedIn</a> · <a href="https://github.com/RES07">GitHub</a></span>
</div></footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def link(icon, href, label, external=True):
    ext = ' target="_blank" rel="noopener"' if external else ''
    return f'<li><a href="{href}"{ext}>{ICONS[icon]}{label}</a></li>'

LINKS = "\n".join([
    link("mail", "mailto:ferreira.rafaeldemenezes@gmail.com", "Email", False),
    link("cv", "assets/cv/Rafael_Ferreira_de_Menezes_CV.pdf", "CV (PDF)"),
    link("scholar", "https://scholar.google.com/citations?user=69vW21YAAAAJ&amp;hl=en", "Google Scholar"),
    link("orcid", "https://orcid.org/0000-0002-4908-3391", "ORCID"),
    link("linkedin", "https://www.linkedin.com/in/rafael-ferreira-de-menezes/", "LinkedIn"),
    link("github", "https://github.com/RES07", "GitHub"),
])

def video(name, w, h, cls="", poster=None):
    poster = poster or f"assets/video/posters/{name}.jpg"
    return f'<video class="{cls}" muted loop playsinline preload="none" poster="{poster}" data-src="assets/video/{name}.mp4" width="{w}" height="{h}" aria-label="{name.replace("_"," ")} animation"></video>'

pages = {}

# ---------------- index ----------------
pages["index.html"] = head("Rafael Ferreira de Menezes", "Computational chemist and materials scientist. PhD candidate at CU Boulder working on electrochemical interfaces with molecular simulation and synchrotron X-rays.", "index.html") + f"""
<section class="hero">
  <img src="assets/img/headshot.jpg" alt="Rafael Ferreira de Menezes" width="240" height="240">
  <div>
    <div class="kicker">Computational chemistry · Synchrotron X-rays · Energy materials</div>
    <h1>Rafael Ferreira de Menezes</h1>
    <p class="lede">Ph.D. candidate in Chemical Engineering at the University of Colorado Boulder, based in Washington, DC. I study what happens where an electrode meets an electrolyte, one atom at a time, and I check the simulations against operando X-ray experiments.</p>
    <ul class="links">
{LINKS}
    </ul>
  </div>
</section>

<section>
  <h2>About me</h2>
  <p>I am a physicist by training and a battery scientist by practice. I grew up in Brasilia, studied physics at the University of Brasilia, and moved to Boulder in 2022 for a Ph.D. in chemical engineering. There I split my time between the <a href="https://www.colorado.edu/lab/sprenger/" target="_blank" rel="noopener">Sprenger group</a>, which does the simulations, and the <a href="https://www.colorado.edu/lab/toney/" target="_blank" rel="noopener">Toney group</a>, which takes the synchrotron beamtime. I now live in Washington, DC, and expect to defend in Spring 2027.</p>
  <p>My work asks how cathodes, electrolytes, and the thin films between them evolve while a battery runs. I answer with quantum chemistry, classical and reactive molecular dynamics, and machine-learned interatomic potentials, and then test those answers with operando X-ray diffraction, reflectivity, and spectroscopy at the Advanced Photon Source and NSLS-II. The same combination reaches beyond batteries: to ices and minerals under planetary conditions, and to the power systems that keep a spacecraft alive. That is where I want to take it next.</p>
  <p>Outside the lab I volunteer at the Smithsonian National Air and Space Museum, mentor students, learn languages of both the spoken and the programming kind, and meditate. I calculated the probability of understanding this bio after one read to be roughly 1/137, so please read it twice.</p>
</section>

<section>
  <h2>Research interests</h2>
  <div class="grid">
    <div class="card interest"><span class="tag">Modeling</span><h3>Atomic-scale simulation of interfaces</h3><p>DFT and coupled-cluster calculations, classical and reactive (ReaxFF) molecular dynamics, machine-learned potentials, and hybrid molecular dynamics/Monte Carlo sampling of speciation.</p></div>
    <div class="card interest"><span class="tag">Experiment</span><h3>X-ray characterization</h3><p>Operando and in situ synchrotron diffraction, reflectivity, and absorption spectroscopy to follow crystal structure, phase transitions, and oxidation states during cycling.</p></div>
    <div class="card interest"><span class="tag">Next</span><h3>Planetary and space materials</h3><p>Applying the same toolkit to ices, minerals, and electrochemical power systems for space missions, where the environments are extreme and the samples are scarce.</p></div>
  </div>
</section>

<section>
  <h2>Now</h2>
  <div class="card note">
    <p><b>Fall 2026.</b> Writing the thesis, giving invited talks at the 2026 Batteries and Computational Materials Science Gordon Research Conferences, volunteering with K-8 visitors at the National Air and Space Museum, and looking for a postdoctoral position starting mid-2027.</p>
  </div>
</section>

<section>
  <h2>Research groups</h2>
  <p>I hit the lab lottery: two groups at CU Boulder, one that codes and one that runs the beamline.</p>
  <div class="grid">
    <div class="card"><div class="logos"><img src="assets/img/groups/rdi_logo.png" alt="RDI group logo"></div><h3>Sprenger group (RDI)</h3><p>Rationally Designed Immunotherapies and Interfaces. Molecular simulation of interfaces, from proteins to electrodes, with Prof. Kayla G. Sprenger.</p></div>
    <div class="card"><div class="logos"><img src="assets/img/groups/toney_logo.png" alt="Toney group logo"></div><h3>Toney group</h3><p>Synchrotron X-ray scattering and spectroscopy of energy materials with Prof. Michael F. Toney, at the Advanced Photon Source and NSLS-II.</p></div>
  </div>
  <div class="photo-row" style="margin-top:16px">
    <img src="assets/img/groups/group_photo_a.jpg" alt="Group photo outdoors in Boulder" loading="lazy">
    <img src="assets/img/groups/group_photo_b.jpg" alt="Group holiday gathering" loading="lazy">
  </div>
</section>
""" + FOOT

# ---------------- research ----------------
pages["research.html"] = head("Research", "Research projects: lithium-sulfur speciation, cathode-electrolyte interphase, electric double layers, hard carbon anodes, and machine-learned interatomic potentials.", "research.html") + f"""
<h1>Research</h1>
<p class="lede muted">The thread through all of it: what happens at the interface between an electrode and an electrolyte while a battery is running, and how to see it both in simulation and at a synchrotron. Every figure and clip below is descriptive; the underlying data live in the papers on the <a href="publications.html">publications page</a>.</p>

<article class="project" id="lis">
  <div>
    <h2>Speciation in lithium-sulfur batteries</h2>
    <p>Lithium-sulfur cells promise about three times the energy density of today's lithium-ion packs from an element that is cheap and abundant. The catch is the chemistry. Sulfur passes through a cascade of soluble polysulfides on its way to Li<sub>2</sub>S, and those intermediates leave the cathode, shuttle to the anode, and quietly destroy the cell.</p>
    <p>I use a hybrid molecular dynamics/Monte Carlo approach to work out which species exist in the electrolyte at each state of charge, and pair that with quantum-chemical predictions of their vibrational fingerprints so they can be identified in operando infrared experiments. The simulated speciation agrees closely with what the experiments see.</p>
  </div>
  <figure class="media dark">{video("lis_speciation", 314, 560, "tall")}<figcaption>Hybrid MD/Monte Carlo snapshot of polysulfides in a Li-S electrolyte.</figcaption></figure>
</article>

<article class="project" id="cei">
  <div>
    <h2>Cathode-electrolyte interphase in lithium-ion batteries</h2>
    <p>The interface is where the battery magic happens. On the anode, a passivating film forms during the first cycles and protects the electrode afterwards. A similar film grows on the cathode, and it is far less understood: how it forms, what it is made of, and how it changes with the electrolyte.</p>
    <p>I combine reactive molecular dynamics with X-ray spectroscopy to follow the cathode-electrolyte interphase as it forms. The clip shows a ReaxFF simulation of a next-generation electrolyte reacting at a lithium manganese oxide surface. Understanding this film is central to fixing capacity fade and extending cycle life, which was the subject of our <em>Advanced Energy Materials</em> paper on Mn dissolution.</p>
  </div>
  <figure class="media dark">{video("cei_reaxff", 360, 812, "tall")}<figcaption>Reactive molecular dynamics of interphase formation on LiMn<sub>2</sub>O<sub>4</sub>.</figcaption></figure>
</article>

<article class="project" id="edl">
  <div>
    <h2>Electric double layer in aqueous electrolytes</h2>
    <p>Within a nanometer of a charged electrode the electric field is enormous, and that field decides which ions and molecules reach the surface and react. The double layer therefore controls the side reactions that limit aqueous batteries and electrocatalysts, yet its role in those reactions has received much less attention than it deserves.</p>
    <p>These molecular dynamics simulations of an aqueous CsCl electrolyte show how charge arranges itself at a negatively and a positively charged graphene electrode. Watch the ions swap places and the water reorient as the sign of the surface charge flips.</p>
  </div>
  <figure class="media dark pair">{video("edl_negative", 370, 406)}{video("edl_positive", 400, 440)}<figcaption>Left: negatively charged electrode. Right: positively charged electrode.</figcaption></figure>
</article>

<article class="project" id="hardcarbon">
  <div>
    <h2>Hard carbon anodes for sodium-ion batteries</h2>
    <p>Sodium-ion cells are the quiet workhorse option for grid storage, and hard carbon is their standard anode. The open question is how sodium fills the pores and defects of this disordered material as the cell charges, and how that depends on the way the carbon was made.</p>
    <p>I build atomistic models of hard carbon by simulated annealing: heating and quenching thousands of carbon atoms until they settle into the curved, layered fragments seen in real samples. The resulting pore size and shape distributions feed the interpretation of X-ray scattering data in our <em>Small</em> paper on microstructure-dependent sodium storage.</p>
  </div>
  <figure class="media dark"><img src="assets/img/research/hardcarbon_anneal.png" alt="Three stages of a simulated annealing run generating a hard carbon model" width="1280" height="311" loading="lazy"><img src="assets/img/research/hardcarbon_thumb.jpg" alt="Slice through a hard carbon model" loading="lazy"><figcaption>Simulated annealing (temperature ramp, then quench) of a hard carbon model, and a slice through the result.</figcaption></figure>
</article>

<article class="project" id="mlip">
  <div>
    <h2>Machine-learned interatomic potentials</h2>
    <p>Quantum chemistry is accurate but slow; classical force fields are fast but rigid. Machine-learned potentials trained on quantum-chemical data close that gap. During a 2024 internship at Lawrence Livermore National Laboratory I worked on such potentials for lithium-ion battery electrolytes, so that solvation and reactivity can be simulated at the size and time scales a real interface demands.</p>
  </div>
  <figure class="media">{video("md_explainer", 1080, 540)}<figcaption>Molecular dynamics in one loop: forces, velocity-Verlet update, repeat. From the <a href="animations.html">animations page</a>.</figcaption></figure>
</article>
""" + FOOT

# ---------------- publications ----------------
pages["publications.html"] = head("Publications", "Journal articles, preprints, and conference abstracts by Rafael Ferreira de Menezes.", "publications.html") + """
<h1>Publications</h1>
<p id="metrics" class="metrics"></p>
<div id="pub-tabs" class="pub-tabs" role="group" aria-label="Filter publications"></div>
<div id="pubs"><noscript><p>This list needs JavaScript. See my <a href="https://scholar.google.com/citations?user=69vW21YAAAAJ&amp;hl=en">Google Scholar profile</a> instead.</p></noscript></div>
<p class="muted" style="margin-top:24px">Only published work is listed here. Manuscripts in preparation are not.</p>
<script src="assets/js/publications.js"></script>
""" + FOOT

# ---------------- animations ----------------
CLIPS = [
 ("lib_battery", 1080, 560, "Lithium-ion battery: one full cycle",
  "Lithium leaves the graphite, crosses the separator, and slots between the NMC oxide slabs while the electrons take the long way through the external circuit. Then the voltage reverses and everything goes back. Nothing but lithium moves, which is why the cell can do this thousands of times."),
 ("lis_battery", 1080, 560, "Lithium-sulfur battery: discharge",
  "Same cell geometry, different chemistry. The lithium-metal anode is consumed as it works, and sulfur in the cathode steps through the polysulfide cascade from S<sub>8</sub> to Li<sub>2</sub>S. The small clusters drifting toward the anode are the polysulfide shuttle, the central problem in Li-S batteries."),
 ("rdf_explainer", 1080, 540, "Radial distribution function g(r)",
  "How the probability of finding a neighbor at distance r builds up shell by shell around a reference atom, and why the curve plateaus at 1 in a liquid."),
 ("edl_explainer", 1080, 540, "Electric double layer",
  "The Gouy-Chapman-Stern picture: a compact Stern layer of ions at the electrode, then a diffuse layer where the potential decays over a Debye length. The scrubber highlights which ions sit at each distance."),
 ("md_explainer", 1080, 540, "Molecular dynamics",
  "The whole method in one loop: positions and velocities, forces from the potential, a velocity-Verlet update, advance time, repeat. The kinetic energy trace shows equilibration and then fluctuation about its mean."),
 ("dft_explainer", 1080, 540, "Density functional theory",
  "The Kohn-Sham self-consistent field cycle. A guess density builds an effective potential, the Kohn-Sham equations return a new density, and the loop repeats until the energy stops changing."),
 ("tddft_explainer", 1080, 540, "Time-dependent DFT",
  "Linear-response TDDFT on the same molecule. A weak oscillating field scans across photon energies; where it hits an excitation the density responds strongly and a peak grows in the absorption spectrum."),
]
clips_html = "\n".join(f'<figure class="clip">{video(n,w,h)}<figcaption><h3>{t}</h3><p>{d}</p></figcaption></figure>' for n,w,h,t,d in CLIPS)
pages["animations.html"] = head("Animations", "Short teaching animations on battery operation, molecular dynamics, DFT, TDDFT, the radial distribution function, and the electric double layer.", "animations.html", "assets/video/posters/lib_battery.jpg") + f"""
<h1>Animations</h1>
<p class="lede muted">Short explainers I made for lectures and talks, rendered with matplotlib. They play automatically while on screen and pause when scrolled away. Feel free to use them in your own teaching with attribution.</p>
<div class="clips">
{clips_html}
</div>
""" + FOOT

# ---------------- outreach ----------------
pages["outreach.html"] = head("Outreach", "Science outreach: Smithsonian National Air and Space Museum, National Book Festival, the Lindau Nobel Laureate Meeting, and Physics Week.", "outreach.html", "assets/img/outreach/lindau_1.jpg") + """
<h1>Outreach</h1>
<p class="lede muted">Sharing science is half the fun of doing it. A few of the things I do outside the lab.</p>

<section>
  <h2>In Washington, DC</h2>
  <div class="grid">
    <div class="card"><h3>Smithsonian National Air and Space Museum</h3><p>Volunteer educator since 2026. I work with the Museum's K-8 audiences in hands-on activities on satellites, rocketry, writing museum labels, and conservation practice.</p></div>
    <div class="card"><h3>National Book Festival, STEM District</h3><p>Volunteer in 2026 at the Library of Congress festival's STEM District, an interactive space that pairs science, technology, engineering, and mathematics with storytelling for young readers.</p></div>
    <div class="card"><h3>Teaching animations</h3><p>A growing set of short <a href="animations.html">explainer animations</a> on batteries and simulation methods, free to reuse in classrooms with attribution.</p></div>
  </div>
</section>

<section>
  <h2>74th Lindau Nobel Laureate Meeting, 2025</h2>
  <p>I was nominated by the U.S. National Academy of Sciences to attend the 2025 Lindau meeting, a week with young scientists from more than 40 countries and a few dozen Nobel laureates. Some moments that stayed with me:</p>

  <div class="story"><img src="assets/img/outreach/muller.jpg" alt="Rafael with Derek Muller" loading="lazy"><div><h3>Derek Muller (Veritasium)</h3><p>His videos played a big role in getting me into science, not just for the equations but for the stories and history behind them. Watching him moderate a panel on AI in chemistry, and then getting to talk with him, was a highlight of the week.</p></div></div>
  <div class="story"><img src="assets/img/outreach/bawendi.jpg" alt="Rafael with Moungi Bawendi" loading="lazy"><div><h3>Moungi Bawendi</h3><p>In 2021 my undergraduate thesis was on graphene quantum dots as gas sensors. Four years later I got to discuss the future of quantum dots with the person who received the Nobel Prize for them.</p></div></div>
  <div class="story"><img src="assets/img/outreach/klitzing_medal.jpg" alt="Rafael holding Klaus von Klitzing's Nobel medal" loading="lazy"><div><h3>Klaus von Klitzing</h3><p>I first learned about the quantum Hall effect as a physics undergraduate. Hearing from its discoverer how it redefined our fundamental units, and then holding his Nobel medal, was a moment I will not forget.</p></div></div>
  <div class="story"><img src="assets/img/outreach/chu.jpg" alt="Session with Steven Chu at Lindau" loading="lazy"><div><h3>Steven Chu</h3><p>From the Nobel Prize in Physics to U.S. Secretary of Energy. He spoke about embracing interdisciplinary work to tackle big problems, and admitted that even laureates open Khan Academy when learning something new.</p></div></div>
  <div class="story"><img src="assets/img/outreach/jumper.jpg" alt="Rafael with John Jumper" loading="lazy"><div><h3>John Jumper</h3><p>AlphaFold is changing how proteins are discovered. What I liked most was hearing that his favorite part of the job is still writing code.</p></div></div>
  <div class="photo-row" style="margin-top:18px">
    <img src="assets/img/outreach/lindau_1.jpg" alt="Young scientists gathered outdoors at Lindau" loading="lazy">
    <img src="assets/img/outreach/lindau_2.jpg" alt="Panel discussion at the Lindau meeting" loading="lazy">
  </div>
</section>

<section>
  <h2>In Brasilia</h2>
  <div class="grid">
    <div class="card"><h3>Physics Week, 2018 to 2021</h3><p>Co-organized the University of Brasilia's annual week of lectures and short courses in physics, with more than 500 participants each year.</p></div>
    <div class="card"><h3>Computational Quantum Chemistry course, 2021</h3><p>Coordinated a two-week winter course on quantum chemistry methods with the Institute of Physics.</p></div>
    <div class="card"><h3>Introduction to Physics, 2021</h3><p>Designed and taught a calculus-fundamentals course for first-year students to improve retention in the physics program.</p></div>
  </div>
</section>
""" + FOOT

pages["404.html"] = head("Page not found", "Page not found.", "404.html") + """
<h1>Page not found</h1>
<p>That page is not here. Try the <a href="index.html">home page</a> or the <a href="publications.html">publications</a>.</p>
""" + FOOT

for name, html in pages.items():
    with open(name, "w") as f:
        f.write(html)
print("wrote", ", ".join(pages))
