---
title: Métricas de desempenho da Web (Web Vitals)
description: Resumo dos Web Vitals e dos critérios de medição do Lighthouse; entenda o que são FCP, LCP, INP, CLS, TBT e SI e como impactam SEO e a experiência do usuário.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Fatores que determinam o desempenho na Web
Ao otimizar desempenho na Web, os fatores que mais pesam podem ser amplamente classificados em desempenho de carregamento e desempenho de renderização.

### Desempenho de carregamento do HTML
- Tempo desde a primeira solicitação da página ao servidor via rede até o momento em que o navegador recebe o documento HTML e inicia a renderização
- Determina quão rapidamente a página começa a ser exibida
- Otimizações: minimizar redirecionamentos, cachear a resposta HTML, comprimir recursos, usar CDN adequadamente, etc.

### Desempenho de renderização
- Tempo que o navegador leva para desenhar o que o usuário vê e tornar a página interativa
- Determina quão suave e rápida é a pintura da tela
- Otimizações: remover CSS e JS desnecessários, evitar atraso no carregamento de fontes e miniaturas, isolar operações pesadas em Web Workers para minimizar a ocupação da thread principal, otimizar animações, etc.

## Métricas de desempenho da Web (Web Vitals)
Com base no [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) do Google e na [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Salvo motivo especial, é melhor mirar uma melhoria global do que focar em apenas uma métrica, e é importante identificar quais partes da página são gargalos. Além disso, quando houver dados reais de usuários, convém olhar para valores do quartil inferior (Q1) em vez de valores de topo ou médios, e garantir que mesmo nesses casos as metas sejam atendidas, melhorando o que for necessário.

### Métricas essenciais da Web (Core Web Vitals)
Há várias métricas nos Web Vitals, como veremos a seguir. Entre elas, o Google considera especialmente importantes as três que se correlacionam fortemente com a experiência do usuário e podem ser medidas em campo (fora de ambiente simulado). Essas são as [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). O Google também as utiliza como sinal na ordenação dos resultados da busca; portanto, para quem administra sites, é crucial observá-las sob a ótica de SEO.
- [Maior pintura com conteúdo (LCP)](#lcp-maior-pintura-com-conteudo): reflete o desempenho de carregamento; deve ficar até 2,5 s
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflete a responsividade; deve ficar até 200 ms
- [Mudança cumulativa de layout (CLS)](#cls-mudanca-cumulativa-de-layout): reflete a estabilidade visual; deve ficar em até 0,1

As Core Web Vitals são concebidas para medição em campo, mas duas delas (exceto INP) podem ser medidas em ambientes simulados como as DevTools do Chrome ou o Lighthouse. Já o INP requer interações reais do usuário e, portanto, não é mensurável em laboratório; nesse caso, o [TBT](#tbt-tempo-total-de-bloqueio) é altamente correlacionado e serve como proxy, e [em geral, melhorar o TBT também melhora o INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pesos da pontuação de desempenho no Lighthouse 10
[A pontuação de desempenho do Lighthouse é a média ponderada das métricas, seguindo os pesos da tabela a seguir](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrica | Peso |
| --- | --- |
| [Primeira exibição com conteúdo](#fcp-primeira-exibicao-com-conteudo) | 10% |
| [Índice de velocidade](#si-indice-de-velocidade) | 10% |
| [Maior pintura com conteúdo](#lcp-maior-pintura-com-conteudo) | 25% |
| [Tempo total de bloqueio](#tbt-tempo-total-de-bloqueio) | 30% |
| [Mudança cumulativa de layout](#cls-mudanca-cumulativa-de-layout) | 25% |

### FCP (Primeira exibição com conteúdo)
- Mede o tempo até a primeira renderização de conteúdo do DOM após a solicitação da página
- Imagens na página, elementos `<canvas>` não brancos, SVG etc. são considerados conteúdo do DOM; conteúdo dentro de `iframe` não é considerado

> Um fator que afeta especialmente o FCP é o tempo de carregamento de fontes; a [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomenda consultar este [post relacionado](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}) para otimizações.
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
Segundo a [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Classificação por cor | FCP móvel (s) | FCP em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–1,8 | 0–0,9 |
| Laranja (médio) | 1,8–3 | 0,9–1,6 |
| Vermelho (lento) | > 3 | > 1,6 |

### LCP (Maior pintura com conteúdo)
- Mede o tempo até a renderização do maior elemento (imagem, bloco de texto, vídeo etc.) dentro da área visível (viewport) quando a página é aberta
- Quanto maior a área ocupada na tela, maior a chance de o usuário percebê-lo como conteúdo principal
- Quando o LCP é uma imagem, o tempo pode ser decomposto em quatro subintervalos; é importante identificar onde está o gargalo:
  1. Time to first byte (TTFB): tempo do início do carregamento da página até o recebimento do primeiro byte da resposta HTML
  2. Atraso de carregamento (Load delay): diferença entre o momento em que o navegador inicia o carregamento do recurso LCP e o TTTB
  3. Tempo de carregamento (Load time): tempo para carregar o recurso LCP em si
  4. Atraso de renderização (Render delay): tempo do fim do carregamento do recurso LCP até a renderização completa do elemento LCP

#### Critérios de avaliação do Lighthouse
Segundo a [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Classificação por cor | FCP móvel (s) | FCP em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–2,5 | 0–1,2 |
| Laranja (médio) | 2,5–4 | 1,2–2,4 |
| Vermelho (lento) | > 4 | > 2,4 |

### TBT (Tempo total de bloqueio)
- Mede o tempo total em que a página não consegue responder a entradas do usuário (cliques, toques, teclado, etc.)
- Entre o FCP e o [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, tarefas com duração superior a 50 ms são consideradas [tarefas longas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}); de cada uma subtrai-se 50 ms para obter a “parte de bloqueio”, e o TBT é a soma dessas partes

> \* O próprio TTI é excessivamente sensível a outliers de rede e a tarefas longas, com baixa consistência e alta variabilidade; por isso, [a partir do Lighthouse 10 foi removido da avaliação de desempenho](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> As causas mais comuns de tarefas longas são carregamento, parsing e execução de JavaScript desnecessário ou ineficiente. A [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) e o [web.dev do Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomendam reduzir o payload de JS e usar [divisão de código](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para que cada parte execute em até 50 ms; se necessário, mover tarefas para um service worker e executá-las em multithread em vez da thread principal.
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
Segundo a [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Classificação por cor | FCP móvel (ms) | FCP em desktop (ms) |
| --- | --- | --- |
| Verde (rápido) | 0–200 | 0–150 |
| Laranja (médio) | 200–600 | 150–350 |
| Vermelho (lento) | > 600 | > 350 |

### CLS (Mudança cumulativa de layout)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemplo de mudança de layout inesperada" autoplay=true loop=true %}
> Fonte do vídeo: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Dá para sentir uma raiva profunda só pelo movimento do cursor~~

- Mudanças inesperadas de layout atrapalham a experiência do usuário de várias formas, como fazer o texto “pular” e perder a linha de leitura, ou induzir cliques errados em links/botões
- O cálculo detalhado da pontuação de CLS está descrito no [web.dev do Google](https://web.dev/articles/cls)
- Como se vê na imagem abaixo, a meta deve ser 0,1 ou menos

![Qual é uma boa pontuação de CLS?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fonte da imagem: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Índice de velocidade)
- Mede quão rapidamente o conteúdo é exibido visualmente durante o carregamento da página
- O Lighthouse grava um vídeo do carregamento no navegador, analisa o progresso entre quadros e usa o [módulo Node.js Speedline](https://github.com/paulirish/speedline) para calcular a pontuação de SI

> Medidas que melhoram a velocidade de carregamento — incluindo as já citadas em [FCP](#fcp-primeira-exibicao-com-conteudo), [LCP](#lcp-maior-pintura-com-conteudo) e [TBT](#tbt-tempo-total-de-bloqueio) — também beneficiam o SI. Ele reflete, em certo grau, o processo de carregamento como um todo, em vez de representar apenas uma etapa.
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
Segundo a [Documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Classificação por cor | SI móvel (s) | SI em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–3,4 | 0–1,3 |
| Laranja (médio) | 3,4–5,8 | 1,3–2,3 |
| Vermelho (lento) | > 5,8 | > 2,3 |
