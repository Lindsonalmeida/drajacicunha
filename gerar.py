# Site oficial da Clínica Dra. Jaci Cunha (SEO local) + mini site da bio com chat de avaliação · v3, conta Leandro, 04/11/2026 (v1 Solenne em gerar-v1.py, v2 reprovada em gerar-v2.py).
# Composição v3 copiada fielmente de dois shots de estúdios de ponta (lindson/agencia/clientes/jaci-cunha/site/TEMPLATE-V3.md):
# "Seon Clinic" (LAIN, Dribbble, 26,6 mil views) e "Atelier Aesthetica" (Phenomenon Studio, Dribbble, 29,3 mil views), na identidade da Jaci. Método de SEO do site da Desentupidora SF.
# Regras do CFO em tudo: sem preço, sem "grátis", sem promessa de resultado, sem antes e depois, CRO com UF, indicação só após avaliação.
# Uso: python3 gerar.py
import json, html, os, urllib.parse
BASE = 'https://drajacicunha.pages.dev'   # nome do projeto na Cloudflare (trocar se mudar)
WA = ''                                     # WhatsApp da clínica com DDI, ex.: 5598999999999 (PEDIR AO LINDSON). Vazio = botões vão ao direct do Instagram
IG = 'clinica.drajacicunha'
CRO = 'CRO-MA 8514'
END = 'Av. Militar, em frente à Praça do Viva · Zé Doca/MA'
def contato(txt):
    return (f'https://wa.me/{WA}?text=' + urllib.parse.quote(txt)) if WA else f'https://ig.me/m/{IG}'
ROTULO = 'Agendar pelo WhatsApp' if WA else 'Agendar pelo Instagram'
F = '/img/'
AVISO = f'Responsável técnica: Dra. Jaci Cunha · Cirurgiã-dentista · {CRO}. As informações desta página são educativas: a indicação de qualquer procedimento só é feita após avaliação, e os resultados variam de pessoa para pessoa.'

SERV = [
 dict(slug='harmonizacao-facial-em-ze-doca', nav='Harmonização', kw='Harmonização facial em Zé Doca', foto=F+'jaci-preto-mao-no-cabelo.webp',
  title='Harmonização Facial em Zé Doca (MA) | Clínica Dra. Jaci Cunha',
  desc='Harmonização orofacial em Zé Doca (MA) com a Dra. Jaci Cunha, cirurgiã-dentista (CRO-MA 8514). Toxina botulínica, preenchimento e bioestimulador, sempre com avaliação antes. Agende.',
  h1='Harmonização facial', sub='Natural não é fazer pouco. É fazer certo para você.',
  intro=['A harmonização orofacial é um conjunto de procedimentos que equilibra as proporções do rosto e do sorriso. Na Clínica Dra. Jaci Cunha, tudo começa por uma avaliação: primeiro entender o seu rosto e o que incomoda você, depois montar um plano por etapas.',
         'O objetivo não é mudar quem você é. É cuidar do que você quer melhorar, respeitando os seus traços.'],
  itens=[('Toxina botulínica','suaviza as linhas de expressão (testa, entre as sobrancelhas, ao redor dos olhos)','/botox-em-ze-doca/'),('Preenchimento','repõe volume e contorno com ácido hialurônico (lábios, olheiras, mandíbula)','/preenchimento-labial-em-ze-doca/'),('Bioestimulador de colágeno','estimula a produção natural de colágeno e a firmeza da pele','/bioestimulador-de-colageno-em-ze-doca/')],
  faq=[('Harmonização deixa o rosto artificial?','O resultado depende da indicação e da quantidade. Na clínica, o plano é feito na avaliação, respeitando os seus traços e o que você quer manter.'),
       ('Quem faz a harmonização na clínica?','A Dra. Jaci Cunha, cirurgiã-dentista, CRO-MA 8514, habilitada em harmonização orofacial.'),
       ('Por onde começo?','Pela Avaliação Facial Completa: análise do rosto e do sorriso e um plano por etapas, sem compromisso de fazer tudo de uma vez.')]),
 dict(slug='botox-em-ze-doca', nav='Botox', kw='Botox em Zé Doca', foto=F+'jaci-off-white-frasco-botox.webp',
  title='Botox (Toxina Botulínica) em Zé Doca (MA) | Dra. Jaci Cunha',
  desc='Aplicação de toxina botulínica (botox) em Zé Doca (MA) com a Dra. Jaci Cunha, CRO-MA 8514. Linhas de expressão suavizadas, com avaliação antes e acompanhamento. Agende sua avaliação.',
  h1='Toxina botulínica (botox)', sub='Suavizar as linhas sem perder a expressão.',
  intro=['A toxina botulínica relaxa temporariamente os músculos responsáveis pelas linhas de expressão, como as da testa, entre as sobrancelhas e ao redor dos olhos.',
         'Na avaliação, a Dra. Jaci observa como o seu rosto se movimenta para definir onde e quanto aplicar. A ideia é suavizar, não paralisar.'],
  itens=[('Avaliação','análise dos movimentos do rosto e do que incomoda você',''),('Aplicação','com agulhas finas, em consultório',''),('Acompanhamento','retorno combinado na avaliação; o efeito é temporário e a manutenção é planejada com você','')],
  faq=[('Botox deixa a cara parada?','Quando a dose e os pontos são bem indicados, a expressão continua natural. É isso que é definido na avaliação.'),
       ('Quanto tempo dura?','O efeito é temporário e varia de pessoa para pessoa. A manutenção é combinada com a Dra. Jaci no acompanhamento.'),
       ('Dói?','A aplicação é feita com agulhas finas e costuma ser bem tolerada. Na avaliação, a Dra. Jaci explica cada etapa.')]),
 dict(slug='preenchimento-labial-em-ze-doca', nav='Preenchimento', kw='Preenchimento labial em Zé Doca', foto=F+'jaci-preto-rennova-sorrindo.webp',
  title='Preenchimento Labial e Facial em Zé Doca (MA) | Dra. Jaci Cunha',
  desc='Preenchimento labial e facial com ácido hialurônico em Zé Doca (MA), com a Dra. Jaci Cunha (CRO-MA 8514). Contorno e hidratação respeitando os seus traços. Agende sua avaliação.',
  h1='Preenchimento labial e facial', sub='Volume e contorno na medida do seu rosto.',
  intro=['O preenchimento com ácido hialurônico repõe volume e define contornos. Nos lábios, pode trazer hidratação, contorno e equilíbrio; no rosto, pode suavizar olheiras e marcar a mandíbula e o queixo.',
         'A quantidade e os pontos são definidos na avaliação, olhando o rosto como um todo.'],
  itens=[('Lábios','contorno, hidratação e equilíbrio',''),('Olheiras','suavizar a aparência de cansaço, quando indicado',''),('Mandíbula e queixo','contorno e proporção do rosto','')],
  faq=[('O preenchimento labial fica exagerado?','O volume é definido na avaliação, pensando no equilíbrio do seu rosto. Natural é fazer certo para você.'),
       ('Preenchimento é definitivo?','Não. O ácido hialurônico é absorvido pelo corpo com o tempo, e a duração varia de pessoa para pessoa.'),
       ('Posso fazer lábios e botox no mesmo dia?','Depende da avaliação. A Dra. Jaci monta o plano por etapas.')]),
 dict(slug='bioestimulador-de-colageno-em-ze-doca', nav='Bioestimulador', kw='Bioestimulador de colágeno em Zé Doca', foto=F+'jaci-off-white-sofa-sorrindo.webp',
  title='Bioestimulador de Colágeno em Zé Doca (MA) | Dra. Jaci Cunha',
  desc='Bioestimulador de colágeno em Zé Doca (MA) com a Dra. Jaci Cunha, CRO-MA 8514: estímulo à produção natural de colágeno e à firmeza da pele. Agende sua avaliação.',
  h1='Bioestimulador de colágeno', sub='Estimular o que a sua pele já sabe fazer.',
  intro=['Com o tempo, a pele produz menos colágeno e perde firmeza. O bioestimulador é um procedimento que estimula a produção natural de colágeno, com resultado gradual.',
         'Quando começar e quantas sessões fazer são definidos na avaliação, de acordo com a sua pele e os seus objetivos.'],
  itens=[('Firmeza','estímulo gradual ao colágeno',''),('Qualidade da pele','textura e sustentação ao longo das semanas',''),('Plano','número de sessões definido na avaliação','')],
  faq=[('Bioestimulador ou preenchimento?','São coisas diferentes: o preenchimento repõe volume na hora; o bioestimulador estimula o colágeno aos poucos. A avaliação mostra o que faz sentido para você.'),
       ('Quando começar o bioestimulador?','Não existe uma idade única. Depende da sua pele, e isso é avaliado na consulta.'),
       ('O resultado é imediato?','Não. O bioestimulador age de forma gradual, ao longo das semanas.')]),
 dict(slug='dentista-em-ze-doca', nav='Odontologia', kw='Dentista em Zé Doca', foto=F+'jaci-branco-cadeira-sorrindo.webp',
  title='Dentista em Zé Doca (MA) | Odontologia · Clínica Dra. Jaci Cunha',
  desc='Dentista em Zé Doca (MA): odontologia com a Dra. Jaci Cunha, cirurgiã-dentista (CRO-MA 8514). Cuidado com a saúde e a estética do sorriso. Agende sua consulta.',
  h1='Odontologia', sub='Saúde do sorriso, com o mesmo cuidado.',
  intro=['Além da harmonização orofacial, a Clínica Dra. Jaci Cunha atende odontologia: cuidado com a saúde da boca e com a estética do sorriso.',
         'Na consulta, a Dra. Jaci avalia o seu sorriso e explica as opções de tratamento, por etapas.'],
  itens=[('Consulta e prevenção','avaliação, orientação e limpeza',''),('Estética do sorriso','tratamentos indicados após a avaliação',''),('Plano por etapas','o que fazer primeiro e o que pode esperar','')],
  faq=[('A clínica atende odontologia e harmonização?','Sim. A Dra. Jaci Cunha é cirurgiã-dentista e atende as duas áreas.'),
       ('Onde fica a clínica?', f'Na {END}.'),
       ('Como agendo?', 'Pelo botão de agendamento desta página: você conta o que precisa e a equipe responde com os horários.')]),
]
QUIZ = [('Qual procedimento te interessa?', ['Toxina botulínica (botox)', 'Preenchimento labial', 'Bioestimulador de colágeno', 'Odontologia', 'Ainda não sei: quero a avaliação']),
        ('Você já fez algum procedimento estético?', ['Sim', 'Não, seria a primeira vez']),
        ('Quando você gostaria de vir?', ['Esta semana', 'Este mês', 'Só quero tirar dúvidas']),
        ('Melhor horário', ['Manhã', 'Tarde'])]


EMP = {"@type": ["Dentist", "MedicalClinic"], "@id": BASE + "/#clinica", "name": "Clínica Dra. Jaci Cunha", "alternateName": "Dra. Jaci Cunha · Harmonização Orofacial e Odontologia",
       "url": BASE + "/", "image": BASE + "/img/jaci-off-white-sofa-sorrindo.webp", "logo": BASE + "/img/avatar.webp", "sameAs": [f"https://www.instagram.com/{IG}/"],
       "address": {"@type": "PostalAddress", "streetAddress": "Av. Militar, em frente à Praça do Viva", "addressLocality": "Zé Doca", "addressRegion": "MA", "addressCountry": "BR"},
       "areaServed": {"@type": "City", "name": "Zé Doca"}, "medicalSpecialty": ["Dentistry", "Dermatology"],
       "employee": {"@type": "Person", "name": "Dra. Jaci Cunha", "jobTitle": "Cirurgiã-dentista", "identifier": CRO}}
if WA: EMP["telephone"] = "+" + WA
def migalha(itens):
    vis = ' / '.join(f'<a href="{u}">{n}</a>' if i < len(itens) - 1 else n for i, (n, u) in enumerate(itens))
    return f'<div class="migalha">{vis}</div>', {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(itens)]}
def faqs(fq):
    return '<div class="faq">' + ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in fq) + '</div>', \
           {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in fq]}


# ---------- v3: "Seon Clinic" (LAIN) + "Atelier Aesthetica" (Phenomenon Studio) ----------
FOTO_T = {'harmonizacao-facial-em-ze-doca': 'v3-t-harm', 'botox-em-ze-doca': 'v3-t-botox', 'preenchimento-labial-em-ze-doca': 'v3-t-preench', 'bioestimulador-de-colageno-em-ze-doca': 'v3-t-bio', 'dentista-em-ze-doca': 'v3-t-odonto'}
for s_ in SERV: s_['foto'] = F + FOTO_T[s_['slug']] + '.webp'
SETA = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11 11 5M6 5h5v5" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'
def bt(txt, href, cls=''): return f'<a class="bt {cls}" href="{href}"><span>{txt}</span><i>{SETA}</i></a>'
def nav(claro=False):
    itens = '<span>·</span>'.join(f'<a href="{u}">{t}</a>' for t, u in [('Início', '/'), ('Tratamentos', '/#tratamentos'), ('A Dra. Jaci', '/#dra'), ('Avaliação', '/avaliacao/'), ('Como chegar', '/#como-chegar')])
    return (f'<header class="nav {"claro" if claro else ""}"><a class="logo" href="/">Dra. Jaci Cunha</a><nav aria-label="Páginas">{itens}</nav>{bt("Agendar avaliação", "/avaliacao/#agendar", "pq")}'
            f'<button class="mn" type="button" aria-label="Abrir menu" onclick="document.body.classList.toggle(\'menu-aberto\')"><i></i><i></i></button></header>'
            f'<div class="menu-cel">{"".join(f"<a href=\"{u}\">{t}</a>" for t, u in [("Início", "/"), ("Tratamentos", "/#tratamentos"), ("A Dra. Jaci", "/#dra"), ("Avaliação", "/avaliacao/"), ("Como chegar", "/#como-chegar")])}</div>')
def rodape():
    s1 = ''.join(f'<a href="/{s["slug"]}/">{s["h1"]}</a>' for s in SERV)
    return f'''<footer class="rod"><div class="w"><div class="rod-top"><h2>Uma boa avaliação começa <em>com a conversa certa.</em></h2>{bt("Agendar avaliação", "/avaliacao/#agendar", "claro")}</div>
<div class="cols"><div><b>Clínica</b>{END}<br>@{IG}</div><div><b>Tratamentos</b>{s1}</div><div><b>Páginas</b><a href="/avaliacao/">Avaliação</a><a href="/#como-chegar">Como chegar</a><a href="/bio/">Links da bio</a></div><div><b>Responsável técnica</b>Dra. Jaci Cunha<br>Cirurgiã-dentista · {CRO}</div></div>
<div class="marca-g" aria-hidden="true">Jaci Cunha</div><div class="leg">{AVISO} · © 2026 Clínica Dra. Jaci Cunha</div></div></footer>'''
def doc(path, title, desc, corpo, ld, img=BASE + '/img/v3-heroi.webp', robots='index,follow,max-image-preview:large', classe='', claro=False):
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{BASE}{path}"><meta name="robots" content="{robots}">
<meta name="geo.region" content="BR-MA"><meta name="geo.placename" content="Zé Doca"><meta name="theme-color" content="#F4F2EF">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Clínica Dra. Jaci Cunha"><meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{img}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/avatar.webp"><link rel="apple-touch-icon" href="/img/avatar.webp"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False)}</script></head>
<body class="{classe}">{nav(claro)}<main>{corpo}</main>{rodape()}
<script>(()=>{{const r=matchMedia('(prefers-reduced-motion: reduce)').matches;const o=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('ok');o.unobserve(e.target)}}}}),{{threshold:.15}});document.querySelectorAll('.rv').forEach(el=>r?el.classList.add('ok'):o.observe(el));
const n=document.querySelector('.nav');addEventListener('scroll',()=>n.classList.toggle('fixo',scrollY>40),{{passive:true}});
document.querySelectorAll('[data-sl]').forEach(sl=>{{const it=[...sl.querySelectorAll('.sl-i')];let k=0;const ir=d=>{{it[k].classList.remove('on');k=(k+d+it.length)%it.length;it[k].classList.add('on');sl.querySelector('.sl-n').textContent=String(k+1).padStart(2,'0')+'/'+String(it.length).padStart(2,'0')}};sl.querySelector('[data-a]').onclick=()=>ir(-1);sl.querySelector('[data-p]').onclick=()=>ir(1)}});}})();</script></body></html>'''
def quiz_html(id='agendar'):
    dados = json.dumps({"quiz": QUIZ, "wa": WA, "ig": IG}, ensure_ascii=False)
    return f'''<section class="quiz" id="{id}"><div class="w q-grid"><div class="rv"><span class="eti">Avaliação</span><h2>Quatro perguntas. <em class="cz">Um começo</em> claro.</h2><p class="mut">A mensagem vai pronta para a equipe da clínica, que confirma o horário com você. Não pedimos informações de saúde aqui.</p></div>
<div id="qz" class="qz rv" aria-live="polite"></div></div></section>
<script>(()=>{{const D={dados},R=[];const el=document.getElementById('qz');
function passo(i){{if(i<D.quiz.length){{const[p,ops]=D.quiz[i];el.innerHTML=`<div class="q-top"><span>${{String(i+1).padStart(2,'0')}}/${{String(D.quiz.length+1).padStart(2,'0')}}</span><i style="--p:${{(i+1)/(D.quiz.length+1)}}"></i></div><h3>${{p}}</h3><div class="op">${{ops.map(o=>`<button type="button">${{o}}<span>→</span></button>`).join('')}}</div>`;
 el.querySelectorAll('button').forEach(b=>b.onclick=()=>{{R[i]=b.firstChild.textContent;passo(i+1)}})}}
 else{{el.innerHTML=`<div class="q-top"><span>${{D.quiz.length+1}}/${{D.quiz.length+1}}</span><i style="--p:1"></i></div><h3>Seu nome e sua cidade</h3><input id="qn" placeholder="Nome" autocomplete="given-name"><input id="qc" placeholder="Cidade" value="Zé Doca"><button type="button" id="qe" class="bt"><span>Enviar para a clínica</span><i>{SETA}</i></button>`;
 document.getElementById('qe').onclick=()=>{{const n=document.getElementById('qn').value.trim()||'(sem nome)',c=document.getElementById('qc').value.trim();
  const t=`Oi! Vim pelo site da Clínica Dra. Jaci Cunha.\\nNome: ${{n}}\\nCidade: ${{c}}\\nInteresse: ${{R[0]}}\\nJá fez procedimento: ${{R[1]}}\\nQuando: ${{R[2]}}\\nHorário: ${{R[3]}}`;
  if(D.wa)location.href='https://wa.me/'+D.wa+'?text='+encodeURIComponent(t);
  else{{try{{navigator.clipboard.writeText(t)}}catch(e){{}}el.innerHTML='<h3>Mensagem copiada.</h3><p class="mut" style="margin:10px 0 18px">Abra o direct da clínica e cole a mensagem.</p><a class="bt" href="https://ig.me/m/'+D.ig+'"><span>Abrir o direct</span><i>{SETA}</i></a>'}}}}}}}}
passo(0)}})();</script>'''
def cards_trat(excluir=None):   # LAIN: cartões de foto com nome por cima
    return '<div class="cards">' + ''.join(f'<a class="card rv" href="/{s["slug"]}/"><img src="{s["foto"]}" alt="{s["h1"]} em Zé Doca" loading="lazy" width="900" height="1200"><div class="card-t"><b>{s["h1"]}</b><small>{s["sub"]}</small></div><span class="card-n">{i:02d}</span></a>' for i, s in enumerate([x for x in SERV if x is not excluir], 1)) + '</div>'
def dra_card():   # Phenomenon: cartão taupe com nome, formação e selos + recorte da Dra.
    selos = ''.join(f'<span>{x}</span>' for x in [CRO, 'Cirurgiã-dentista', 'Harmonização orofacial', 'Odontologia', 'Zé Doca · MA'])
    return f'''<section class="sec" id="dra"><div class="w"><span class="eti c">Quem cuida de você</span><h2 class="h2c rv">Onde o cuidado técnico encontra <em>um olhar individual</em></h2>
<div class="dra rv"><div class="dra-t"><h3><em>Dra.</em> Jaci Cunha</h3><p>Cirurgiã-dentista com atuação em harmonização orofacial e odontologia, em Zé Doca (MA). Cada plano começa por uma avaliação: entender o rosto, o sorriso e o que você quer manter, antes de qualquer procedimento.</p>
<div class="selos">{selos}</div><p class="cit"><em>“Natural não é fazer pouco. É fazer certo pra você.”</em></p></div><img class="dra-f" src="/img/v3-dra-recorte.webp" alt="Dra. Jaci Cunha, cirurgiã-dentista" loading="lazy" width="900" height="1153"></div></div></section>'''

os.makedirs('img', exist_ok=True)
for s in SERV:
    mg, ldm = migalha([('Início', '/'), (s['nav'], f'/{s["slug"]}/')]); fh, ldf = faqs(s['faq'])
    itens = ''.join(f'<div class="env-i rv"><span>{i:02d}</span><b>{a}</b><p>{b}</p>{f"<a href=\"{u}\">Saiba mais →</a>" if u else ""}</div>' for i, (a, b, u) in enumerate(s['itens'], 1))
    corpo = f'''<section class="pg-h"><div class="w pg-g"><div class="rv">{mg}<span class="eti">{s["kw"]}</span><h1>{s["h1"]}<em> em Zé Doca</em></h1><p class="lead">{s["sub"]}</p>{bt("Agendar avaliação", "/avaliacao/#agendar")}</div><div class="pg-f rv"><img src="{s["foto"]}" alt="Dra. Jaci Cunha, cirurgiã-dentista em Zé Doca" width="900" height="1200"><span class="pg-cro">{CRO}</span></div></div></section>
<section class="sec"><div class="w"><h2 class="h2c rv">{s["intro"][0]}</h2><p class="mut c rv" style="max-width:640px;margin:18px auto 0">{s["intro"][1]}</p><div class="env">{itens}</div><p class="aviso c">{AVISO}</p></div></section>
<section class="sec cinza"><div class="w duas"><div class="rv"><span class="eti">Perguntas frequentes</span><h2 class="h2">Antes de <em>decidir</em></h2></div><div class="rv">{fh}</div></div></section>
{quiz_html()}<section class="sec"><div class="w"><span class="eti">Outros tratamentos</span>{cards_trat(s)}</div></section>'''
    ld = [EMP, ldm, ldf, {"@type": "MedicalProcedure", "name": s['h1'], "description": s['desc'], "url": f'{BASE}/{s["slug"]}/', "provider": {"@id": BASE + "/#clinica"}}]
    os.makedirs(s['slug'], exist_ok=True); open(f'{s["slug"]}/index.html', 'w').write(doc(f'/{s["slug"]}/', s['title'], s['desc'], corpo, ld, BASE + s['foto']))

# avaliação (Phenomenon "Private Consultation 01/04" com as fotos do consultório e da recepção)
mg, ldm = migalha([('Início', '/'), ('Avaliação', '/avaliacao/')])
fh, ldf = faqs([('Quanto tempo dura a avaliação?', 'Cerca de 30 minutos.'), ('Preciso decidir o procedimento antes?', 'Não. A avaliação existe justamente para entender o seu rosto e montar o plano com você.'), ('Vou sair com um plano?', 'Sim: um plano por etapas, explicando o que faz sentido para você e em que ordem.')])
etapas = [('Conversa', 'O que incomoda você e o que você quer manter.', 'v3-cons1'), ('Análise', 'Rosto, expressão e sorriso, com fotos para o prontuário.', 'v3-cons2'), ('Plano', 'As etapas que fazem sentido para você, explicadas uma a uma.', 'v3-cons3'), ('Acompanhamento', 'Retorno combinado para cuidar do resultado com você.', 'v3-cons4')]
sl = ''.join(f'<div class="sl-i {"on" if k == 0 else ""}"><div class="sl-t"><h3><em>{t}</em></h3></div><img src="/img/{f}.webp" alt="Clínica Dra. Jaci Cunha em Zé Doca" loading="lazy" width="1000" height="1250"><p class="sl-d">{d}</p></div>' for k, (t, d, f) in enumerate(etapas))
corpo = f'''<section class="pg-h"><div class="w">{mg}<span class="eti">Avaliação Facial Completa · {CRO}</span><h1 class="pg-h1c">A sua primeira consulta <em>é uma conversa.</em></h1><p class="lead c">Cerca de 30 minutos para entender o seu rosto e o seu sorriso, registrar fotos no prontuário e montar um plano por etapas. Sem pressa e sem decidir nada na hora.</p></div></section>
<section class="sec"><div class="w"><div class="sl rv" data-sl>{sl}<div class="sl-c"><span class="sl-n">01/04</span><button type="button" data-a aria-label="Anterior">←</button><button type="button" data-p aria-label="Próxima">→</button></div></div></div></section>
{quiz_html()}<section class="sec cinza"><div class="w duas"><div class="rv"><span class="eti">Dúvidas</span><h2 class="h2">Sobre a <em>avaliação</em></h2></div><div class="rv">{fh}</div></div></section>'''
os.makedirs('avaliacao', exist_ok=True)
open('avaliacao/index.html', 'w').write(doc('/avaliacao/', 'Avaliação Facial Completa em Zé Doca (MA) | Clínica Dra. Jaci Cunha', 'Agende sua Avaliação Facial Completa com a Dra. Jaci Cunha (CRO-MA 8514) em Zé Doca (MA): análise do rosto e do sorriso e um plano por etapas.', corpo, [EMP, ldm, ldf]))

# home
fh, ldf = faqs([('Onde fica a clínica?', f'Na {END}.'), ('A clínica faz odontologia e harmonização?', 'Sim. A Dra. Jaci Cunha é cirurgiã-dentista e atende harmonização orofacial e odontologia.'),
                ('Como agendo?', 'Pelo agendamento deste site: você responde quatro perguntas e a mensagem vai pronta para a equipe, que confirma o horário.'), ('Preciso saber qual procedimento quero?', 'Não. Comece pela Avaliação Facial Completa.')])
mapa = 'https://www.google.com/maps?q=' + urllib.parse.quote('Clínica Dra. Jaci Cunha, Av. Militar, Zé Doca - MA') + '&output=embed'
ic = {'plano': '<svg viewBox="0 0 24 24"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 17h6M17 14v6" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>',
      'escudo': '<svg viewBox="0 0 24 24"><path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z M9 12l2 2 4-4" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>',
      'olho': '<svg viewBox="0 0 24 24"><path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6S2 12 2 12z" fill="none" stroke="currentColor" stroke-width="1.3"/><circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>',
      'folha': '<svg viewBox="0 0 24 24"><path d="M5 19C5 10 11 5 20 4c-1 9-6 15-15 15zM5 19l7-7" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>',
      'relogio': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M12 7v5l3 2" fill="none" stroke="currentColor" stroke-width="1.3"/></svg>'}
pilares = ''.join(f'<div class="pil rv"><i>{ic[k]}</i><b>{t}</b><small>{d}</small></div>' for k, t, d in [('olho', 'Avaliação antes de tudo', 'Nenhum procedimento sem entender o rosto primeiro.'), ('escudo', f'Registro {CRO}', 'Cirurgiã-dentista habilitada em harmonização.'), ('folha', 'Resultado natural', 'Respeitar os seus traços e o seu jeito.'), ('relogio', 'Acompanhamento', 'Retorno combinado depois de cada etapa.')])
jorn = [('01', 'Conversa', 'v3-j1'), ('02', 'Plano personalizado', 'v3-j2'), ('03', 'Procedimento', 'v3-j3'), ('04', 'Acompanhamento', 'v3-j4')]
jornada = ''.join(f'<div class="jp jp{k}"><img src="/img/{f}.webp" alt="" loading="lazy" width="400" height="400"><span>{n}</span><b>{t}</b></div>' for k, (n, t, f) in enumerate(jorn, 1))
corpo = f'''<section class="heroi"><div class="mancha m1"></div><div class="mancha m2"></div><picture><source media="(max-width:760px)" srcset="/img/v3-heroi-cel.webp"><img class="h-img" src="/img/v3-heroi.webp" alt="Dra. Jaci Cunha, cirurgiã-dentista em Zé Doca" width="2400" height="1348"></picture>
<div class="h-in"><div class="h-top rv"><p class="h-frase">A confiança começa com um rosto que <em>continua sendo seu.</em></p>{bt("Ver tratamentos", "#tratamentos", "pq")}</div>
<div class="h-feat rv"><div><i>{ic['plano']}</i><b>Plano personalizado</b><small>Cada indicação é feita para o seu rosto, os seus objetivos e o seu momento.</small></div><div><i>{ic['escudo']}</i><b>Cuidado com segurança</b><small>Cirurgiã-dentista {CRO}, avaliação e acompanhamento em cada etapa.</small></div></div>
<a class="selo-g" href="/avaliacao/" aria-label="Avaliação antes de tudo"><svg viewBox="0 0 200 200"><defs><path id="cir" d="M100,100 m-78,0 a78,78 0 1,1 156,0 a78,78 0 1,1 -156,0"/></defs><text><textPath href="#cir">AVALIAÇÃO ANTES DE TUDO · {CRO} · ZÉ DOCA · </textPath></text></svg><span>✦</span></a>
<h1 class="h-nome"><span class="sr">Harmonização facial e dentista em Zé Doca · </span>Jaci Cunha</h1></div></section>
<div class="faixa"><div>{"".join(f"<span>{p}</span><i>✦</i>" for p in ["Harmonização orofacial", "Natural é fazer certo pra você", "Odontologia", "Avaliação antes de tudo", "Zé Doca · Maranhão"] * 3)}</div></div>
<section class="sec"><div class="w c"><h2 class="h2c rv">A beleza começa <span class="cz">por</span> entender <span class="cz">o seu</span> rosto.</h2>{bt("Conhecer a Dra. Jaci", "#dra", "pq centro rv")}
<div class="largo rv"><img src="/img/v3-beleza.webp" alt="Dra. Jaci Cunha" loading="lazy" width="1800" height="1200"></div></div></section>
<section class="sec escuro" id="tratamentos"><div class="w"><div class="tt-cab"><h2 class="h2 rv">Tratamentos <em>para o seu</em> rosto e sorriso</h2><p class="mut rv">Harmonização orofacial e odontologia em Zé Doca. Cada tratamento é indicado na avaliação.</p></div>{cards_trat()}</div></section>
<section class="sec rose"><div class="w"><h2 class="h2 rv" style="max-width:620px">Um cuidado pensado <span class="cz">para o que torna</span> você única.</h2><div class="pils">{pilares}</div></div></section>
<section class="sec"><div class="w c"><h2 class="h2c rv">Uma jornada pensada <span class="cz">para o seu rosto,</span> <span class="cz">os seus objetivos e o</span> resultado no tempo.</h2>{bt("Agendar avaliação", "/avaliacao/#agendar", "pq centro rv")}
<div class="jorn rv"><div class="j-anel"></div><div class="j-meio"><b>Seu rosto</b><span>merece um cuidado que dura.</span></div>{jornada}</div></div></section>
{dra_card()}
<section class="conversa"><img src="/img/v3-conversa.webp" alt="Dra. Jaci Cunha na recepção da clínica em Zé Doca" loading="lazy" width="2400" height="1348"><div class="w cv-in rv"><h2>Um bom resultado começa <span class="cz2">com a conversa certa.</span></h2><div class="tags"><span>Escuta</span><span>Avaliação</span><span>Plano por etapas</span><span>Resultado natural</span><span>Acompanhamento</span></div></div></section>
<section class="objetivos"><div class="ob-f f1"><img src="/img/v3-j1.webp" alt="" loading="lazy" width="400" height="400"></div><div class="ob-f f2"><img src="/img/v3-t-harm.webp" alt="" loading="lazy" width="900" height="1200"></div><div class="ob-f f3"><img src="/img/v3-j4.webp" alt="" loading="lazy" width="400" height="400"></div><div class="ob-f f4"><img src="/img/v3-t-odonto.webp" alt="" loading="lazy" width="900" height="1200"></div>
<div class="w c rv"><span class="eti claro">Sua avaliação</span><h2 class="ob-t">Fale dos seus objetivos <em>com toda a confiança.</em></h2>{bt("Começar a avaliação", "#agendar", "ouro centro")}</div></section>
{quiz_html()}
<section class="sec" id="como-chegar"><div class="w duas"><div class="rv"><span class="eti">Como chegar</span><h2 class="h2">A clínica fica <em>em Zé Doca</em></h2><p class="mut">{END}.</p><p class="mut">Agendamento pelo site ou pelo Instagram @{IG}.</p>{bt("Ver rota no mapa", "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Clínica Dra. Jaci Cunha Zé Doca"))}</div>
<iframe class="mapa rv" src="{mapa}" loading="lazy" title="Mapa da Clínica Dra. Jaci Cunha" referrerpolicy="no-referrer-when-downgrade"></iframe></div></section>
<section class="sec cinza"><div class="w duas"><div class="rv"><span class="eti">Dúvidas</span><h2 class="h2">Perguntas <em>frequentes</em></h2><p class="aviso">{AVISO}</p></div><div class="rv">{fh}</div></div></section>'''
open('index.html', 'w').write(doc('/', 'Harmonização Facial e Dentista em Zé Doca (MA) | Clínica Dra. Jaci Cunha',
     'Clínica Dra. Jaci Cunha em Zé Doca (MA): harmonização orofacial (toxina botulínica, preenchimento, bioestimulador) e odontologia com a Dra. Jaci Cunha, CRO-MA 8514. Agende sua avaliação.',
     corpo, [EMP, {"@type": "WebSite", "url": BASE + "/", "name": "Clínica Dra. Jaci Cunha", "inLanguage": "pt-BR"}, ldf], classe='home'))

# bio do Instagram (mesma linguagem: foto de estúdio grande com o nome por cima, lista com seta, chat)
botoes = [('Agendar avaliação', 'Quatro perguntas e a mensagem vai pronta', '#agendar')] + [(s['h1'], s['sub'], f'/{s["slug"]}/') for s in SERV] + [('Como chegar', 'Av. Militar, em frente à Praça do Viva', '/#como-chegar'), ('Site completo', 'Tratamentos, dúvidas e a clínica', '/')]
bts = ''.join(f'<a class="{"b1" if i == 0 else ""}" href="{u}"><span><b>{t}</b><small>{d}</small></span><i>{SETA}</i></a>' for i, (t, d, u) in enumerate(botoes))
corpo = f'''<section class="bio"><div class="bio-h"><img src="/img/v3-bio.webp" alt="Dra. Jaci Cunha, cirurgiã-dentista" width="1100" height="1375"><div class="bio-ht"><span class="eti claro">Cirurgiã-dentista · {CRO}</span><h1>Jaci<br>Cunha</h1></div></div>
<div class="bio-w"><p class="bio-f">Harmonização orofacial e odontologia em Zé Doca/MA. <em>Natural é fazer certo pra você.</em></p><div class="bio-l">{bts}</div></div></section>{quiz_html()}'''
os.makedirs('bio', exist_ok=True)
open('bio/index.html', 'w').write(doc('/bio/', 'Dra. Jaci Cunha · Links | Harmonização e Odontologia em Zé Doca', 'Agende sua avaliação com a Dra. Jaci Cunha (CRO-MA 8514) em Zé Doca (MA).', corpo, [EMP], robots='noindex,follow', classe='pg-bio'))

urls = ['/'] + [f'/{s["slug"]}/' for s in SERV] + ['/avaliacao/']
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{BASE}{u}</loc><changefreq>monthly</changefreq><priority>{"1.0" if u == "/" else "0.8"}</priority></url>\n' for u in urls) + '</urlset>\n')
open('robots.txt', 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n')
open('_redirects', 'w').write('/links /bio/ 301\n')
print('páginas:', len(urls), '+ bio/ · WhatsApp:', WA or 'AINDA NÃO (botões vão ao direct do Instagram)')
