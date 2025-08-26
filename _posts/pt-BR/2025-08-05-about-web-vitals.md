---
title: Métricas de desempenho da web (Web Vitals)
description: "Resumo dos Web Vitals e dos critérios de medição e pontuação do Lighthouse; entenda FCP, LCP, INP, CLS, TBT e SI e como eles afetam o desempenho e o SEO."
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Fatores que determinam o desempenho da web
Ao otimizar a performance na web, os fatores que a determinam podem ser classificados em dois grandes grupos: desempenho de carregamento e desempenho de renderização.

### Desempenho de carregamento do HTML
- Tempo desde a primeira solicitação da página ao servidor pela rede até o momento em que o navegador recebe o documento HTML e começa a renderizar
- Determina quão rápido a página começa a ser exibida
- Otimização por meio de minimizar redirecionamentos, cachear a resposta HTML, comprimir recursos e usar um CDN de forma adequada, entre outros

### Desempenho de renderização
- Tempo que o navegador leva para desenhar a interface que o usuário vê e torná-la interativa
- Determina quão suave e rapidamente a tela é desenhada
- Otimização removendo CSS e JS desnecessários, evitando atraso no carregamento de fontes e miniaturas, separando operações pesadas em Web Workers para minimizar a ocupação da thread principal, e otimizando animações, entre outros

## Métricas de desempenho da web (Web Vitals)
Com base no [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) do Google e na [documentação para desenvolvedores do Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). Em geral, salvo motivo específico, é melhor mirar melhorias holísticas do que focar em uma única métrica, identificando quais partes da página estão causando gargalos. Se você tiver estatísticas de dados reais de usuários, é recomendável observar valores do quartil inferior (Q1), em vez de médias ou topos, e garantir que, mesmo nesses casos, as metas sejam atingidas.

### Métricas essenciais da web (Core Web Vitals)
Há várias métricas de Web Vitals. Entre elas, três têm relação direta com a experiência do usuário e podem ser medidas em campo (e não apenas em laboratório). O Google as considera especialmente importantes e as denomina [Core Web Vitals](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Como o Google também reflete essas métricas nos rankings de resultados de busca, administradores de sites devem observá-las atentamente sob a ótica de SEO.
- [Maior exibição de conteúdo (LCP)](#lcp-maior-exibicao-de-conteudo): reflete o *desempenho de carregamento*; deve ser de até 2,5 s
- [Interação até a próxima pintura (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): reflete a *responsividade*; deve ser ≤ 200 ms
- [Mudança cumulativa de layout (CLS)](#cls-mudanca-de-layout-cumulativa): reflete a *estabilidade visual*; deve permanecer ≤ 0,1

As Core Web Vitals são, por definição, métricas de campo. Porém, exceto pelo INP, as outras duas podem ser medidas em ambientes de laboratório como as DevTools do Chrome ou o Lighthouse. O INP requer entradas reais do usuário e, portanto, não é medido em laboratório. Nesses casos, como [o TBT](#tbt-tempo-total-de-bloqueio) é altamente correlacionado ao INP e é uma métrica semelhante, pode ser usado como referência; [em geral, ao melhorar o TBT, o INP também melhora](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pesos da pontuação de desempenho no Lighthouse 10
[A pontuação de desempenho do Lighthouse é calculada como a média ponderada das pontuações de cada métrica, seguindo os pesos da tabela a seguir](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Métrica | Peso |
| --- | --- |
| [Primeira exibição com conteúdo](#fcp-primeira-exibicao-com-conteudo) | 10% |
| [Índice de Velocidade](#si-indice-de-velocidade) | 10% |
| [Maior exibição de conteúdo](#lcp-maior-exibicao-de-conteudo) | 25% |
| [Tempo total de bloqueio](#tbt-tempo-total-de-bloqueio) | 30% |
| [Mudança cumulativa de layout](#cls-mudanca-de-layout-cumulativa) | 25% |

### FCP (Primeira exibição com conteúdo) {#fcp-primeira-exibicao-com-conteudo}
- Mede o tempo até a renderização do primeiro conteúdo do DOM após a solicitação da página
- Imagens na página, elementos `<canvas>` não brancos, SVG etc. são considerados conteúdo do DOM; conteúdo dentro de `iframe` não é considerado

> Um dos fatores que mais impactam o FCP é o tempo de carregamento de fontes. Para otimizações a esse respeito, a [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomenda consultar [este post relacionado](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
De acordo com a [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Cor/nível | FCP em dispositivos móveis (s) | FCP em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–1,8 | 0–0,9 |
| Laranja (médio) | 1,8–3 | 0,9–1,6 |
| Vermelho (lento) | acima de 3 | acima de 1,6 |

### LCP (Maior exibição de conteúdo) {#lcp-maior-exibicao-de-conteudo}
- Toma como referência a área visível inicial (viewport) quando a página é aberta e mede o tempo até a renderização do maior elemento exibido nessa área (imagem, bloco de texto, vídeo etc.)
- Quanto maior a área ocupada na tela, maior a probabilidade de o usuário percebê-lo como conteúdo principal
- Quando o LCP é uma imagem, o tempo pode ser decomposto em 4 subperíodos; identificar onde está o gargalo é fundamental:
  1. Time to first byte (TTFB): tempo do início do carregamento da página até o recebimento do primeiro byte da resposta do documento HTML
  2. Atraso de carregamento (Load delay): diferença entre o momento em que o navegador começa a carregar o recurso LCP e o TTFB
  3. Tempo de carregamento (Load time): tempo necessário para carregar o próprio recurso LCP
  4. Atraso de renderização (Render delay): tempo do término do carregamento do recurso LCP até a renderização completa do elemento LCP

#### Critérios de avaliação do Lighthouse
De acordo com a [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Cor/nível | LCP em dispositivos móveis (s) | LCP em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–2,5 | 0–1,2 |
| Laranja (médio) | 2,5–4 | 1,2–2,4 |
| Vermelho (lento) | acima de 4 | acima de 2,4 |

### TBT (Tempo total de bloqueio) {#tbt-tempo-total-de-bloqueio}
- Mede o tempo total em que a página não consegue responder a entradas do usuário (cliques, toques, teclado etc.)
- Entre o FCP e o [TTI (Tempo até interativo, Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }}), tarefas que executam por 50 ms ou mais são consideradas [tarefas longas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}). De cada tarefa longa, subtrai-se 50 ms para obter a sua *porção de bloqueio (blocking portion)*, e o TBT é a soma de todas as porções de bloqueio

> O próprio TTI é excessivamente sensível a outliers de rede e a tarefas longas, apresentando baixa consistência e alta variabilidade; por isso, [a partir do Lighthouse 10 foi removido da pontuação de performance](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Em geral, as causas mais comuns de tarefas longas são o carregamento, parsing e execução de JavaScript desnecessário ou ineficiente. A [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) e o [web.dev do Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomendam usar [code splitting](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para reduzir o payload de JS de modo que cada parte execute em ≤ 50 ms e, se necessário, mover trabalho para fora da thread principal, executando em múltiplas threads (por exemplo, em um Service Worker).
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
De acordo com a [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Cor/nível | TBT em dispositivos móveis (ms) | TBT em desktop (ms) |
| --- | --- | --- |
| Verde (rápido) | 0–200 | 0–150 |
| Laranja (médio) | 200–600 | 150–350 |
| Vermelho (lento) | acima de 600 | acima de 350 |

### CLS (Mudança cumulativa de layout) {#cls-mudanca-de-layout-cumulativa}
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemplo de mudança inesperada de layout" autoplay=true loop=true %}
> Fonte do vídeo: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Sinto uma fúria profunda no movimento do cursor~~

- Mudanças inesperadas de layout prejudicam a experiência do usuário de várias formas: o texto se desloca e você perde o ponto de leitura, clica no link ou botão errado, etc.
- O cálculo detalhado da pontuação de CLS está descrito no [web.dev do Google](https://web.dev/articles/cls)
- Como se vê na imagem abaixo, a meta deve ser ≤ 0,1

![Qual é uma boa pontuação de CLS?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fonte da imagem: [Cumulative Layout Shift (CLS) | Articles | web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Índice de Velocidade) {#si-indice-de-velocidade}
- Mede quão rapidamente o conteúdo é exibido visualmente durante o carregamento da página
- O Lighthouse grava em vídeo o processo de carregamento no navegador, analisa o progresso entre quadros e usa o [Speedline (módulo Node.js)](https://github.com/paulirish/speedline) para calcular a pontuação de SI

> Medidas que aceleram o carregamento da página — incluindo as já citadas em [FCP](#fcp-primeira-exibicao-com-conteudo), [LCP](#lcp-maior-exibicao-de-conteudo) e [TBT](#tbt-tempo-total-de-bloqueio) — também beneficiam o SI. Ele não representa apenas um estágio do carregamento, mas reflete o processo como um todo em certo grau.
{: .prompt-tip }

#### Critérios de avaliação do Lighthouse
De acordo com a [documentação do Chrome para desenvolvedores](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), os critérios do Lighthouse são:

| Cor/nível | SI em dispositivos móveis (s) | SI em desktop (s) |
| --- | --- | --- |
| Verde (rápido) | 0–3,4 | 0–1,3 |
| Laranja (médio) | 3,4–5,8 | 1,3–2,3 |
| Vermelho (lento) | acima de 5,8 | acima de 2,3 |
