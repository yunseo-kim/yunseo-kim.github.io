---
title: Métricas de Performance Web (Web Vitals)
description: Resumo das métricas de performance web (Web Vitals) e critérios de medição e avaliação do Lighthouse, explorando o que cada métrica de performance significa.
categories: [Dev, Web Dev]
tags: [Web Performance, Web Vitals]
image: /assets/img/technology.webp
---

## Fatores que Determinam a Performance Web
Os fatores que determinam a performance web a serem considerados na otimização podem ser amplamente classificados em dois tipos: performance de carregamento e performance de renderização.

### Performance de Carregamento HTML
- Tempo desde a primeira solicitação de uma página web ao servidor através da rede até o navegador receber o documento HTML e começar a renderização
- Determina quão rapidamente a página começa a ser exibida
- Otimizada através de métodos como minimização de redirecionamentos, cache de resposta HTML, compressão de recursos e uso adequado de CDN

### Performance de Renderização
- Tempo necessário para o navegador desenhar a tela que o usuário vê e torná-la interativa
- Determina quão suave e rapidamente a tela é desenhada
- Otimizada através de métodos como remoção de CSS e JS desnecessários, prevenção de carregamento tardio de fontes e miniaturas, separação de operações pesadas para Web Workers separados para minimizar a ocupação da thread principal, otimização de animações, etc.

## Métricas de Performance Web (Web Vitals)
Baseado no [web.dev](https://web.dev/performance?hl={{ site.active_lang }}) do Google e na [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}). A menos que haja uma razão específica, é melhor visar uma melhoria geral em vez de focar em apenas uma métrica de performance, e é importante identificar quais partes da página web que você deseja otimizar estão causando gargalos na performance. Além disso, quando há estatísticas de dados reais de usuários, é recomendável focar nos valores do quartil inferior (Q1) em vez dos valores médios ou do quartil superior, verificando e melhorando se os critérios-alvo são atendidos mesmo nesses casos.

### Métricas Principais de Performance Web (Core Web Vitals)
Como abordaremos em breve, existem várias métricas de performance web (Web Vitals). No entanto, entre elas, o Google considera especialmente importantes as seguintes 3 métricas que estão intimamente relacionadas à experiência do usuário e podem ser medidas em ambientes reais, não simulados, chamando-as de [Métricas Principais de Performance Web (Core Web Vitals)](https://web.dev/articles/vitals?hl={{ site.active_lang }}#core-web-vitals). Como o Google também reflete as métricas principais de performance web dos sites de destino na ordem dos resultados de busca de seu mecanismo de busca, do ponto de vista dos operadores de sites, essas métricas devem ser cuidadosamente examinadas do aspecto de otimização para mecanismos de busca (SEO).
- [Large Contentful Paint (LCP)](#lcp-largest-contentful-paint): Reflete *performance de carregamento*, deve ser dentro de 2,5 segundos
- [Interaction to Next Paint (INP)](https://web.dev/articles/inp?hl={{ site.active_lang }}): Reflete *responsividade*, deve ser 200ms ou menos
- [Cumulative Layout Shift (CLS)](#cls-cumulative-layout-shift): Reflete *estabilidade visual*, deve ser mantido em 0,1 ou menos

As métricas principais de performance web são basicamente destinadas à medição em ambientes reais, mas exceto pelo INP, as outras duas podem ser medidas também em ambientes simulados como Chrome DevTools ou Lighthouse. No caso do INP, como requer entrada real do usuário para ser medido, não pode ser medido em ambientes simulados, mas nesse caso, [TBT](#tbt-total-blocking-time) tem uma correlação muito alta com INP e é uma métrica de performance similar, então pode ser usado como referência, e [geralmente melhorar o TBT também melhora o INP](https://web.dev/articles/vitals?hl={{ site.active_lang }}#lab_tools_to_measure_core_web_vitals).

### Pesos da Pontuação de Performance do Lighthouse 10
[A pontuação de performance do Lighthouse é calculada como uma média ponderada das pontuações de cada item de medição, seguindo os pesos da tabela a seguir](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring?hl={{ site.active_lang }}).

| Item de Medição | Peso |
| --- | --- |
| [First Contentful Paint](#fcp-first-contentful-paint) | 10% |
| [Speed Index](#si-speed-index) | 10% |
| [Largest Contentful Paint](#lcp-largest-contentful-paint) | 25% |
| [Total Blocking Time](#tbt-total-blocking-time) | 30% |
| [Cumulative Layout Shift](#cls-cumulative-layout-shift) | 25% |

### FCP (First Contentful Paint)
- Mede o tempo necessário para renderizar o primeiro conteúdo DOM após a solicitação da página
- Considera imagens, elementos `<canvas>` não brancos, SVG, etc. como conteúdo DOM, mas não considera conteúdo dentro de `iframe`

> Um dos fatores que afeta particularmente o FCP é o tempo de carregamento de fontes, e para otimização relacionada a isso, a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}) recomenda consultar o [post relacionado](https://developer.chrome.com/docs/lighthouse/performance/font-display?hl={{ site.active_lang }}).
{: .prompt-tip }

#### Critérios de Avaliação do Lighthouse
De acordo com a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/first-contentful-paint/?hl={{ site.active_lang }}), os critérios de avaliação do Lighthouse são os seguintes:

| Classificação por Cor | FCP Móvel (segundos) | FCP Desktop (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-1.8 | 0-0.9 |
| Laranja (médio) | 1.8-3 | 0.9-1.6 |
| Vermelho (lento) | Mais de 3 | Mais de 1.6 |

### LCP (Largest Contentful Paint)
- Mede o tempo necessário para renderizar o maior elemento (imagens, blocos de texto, vídeos, etc.) dentro da área de visualização (viewport) que aparece primeiro na tela quando uma página web é aberta pela primeira vez
- Quanto maior a área ocupada na tela, maior a probabilidade de ser percebido como conteúdo principal pelo usuário
- Quando o LCP é uma imagem, o tempo necessário pode ser dividido em 4 subintervalos, e é importante identificar onde ocorre o gargalo
  1. Time to first byte (TTFB): Tempo desde o início do carregamento da página até receber o primeiro byte da resposta do documento HTML
  2. Atraso de carregamento (Load delay): Diferença entre o momento em que o navegador começou a carregar o recurso LCP e o TTFB
  3. Tempo de carregamento (Load time): Tempo necessário para carregar o próprio recurso LCP
  4. Atraso de renderização (Render delay): Tempo desde a conclusão do carregamento do recurso LCP até a conclusão completa da renderização do elemento LCP

#### Critérios de Avaliação do Lighthouse
De acordo com a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint/?hl={{ site.active_lang }}), os critérios de avaliação do Lighthouse são os seguintes:

| Classificação por Cor | FCP Móvel (segundos) | FCP Desktop (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-2.5 | 0-1.2 |
| Laranja (médio) | 2.5-4 | 1.2-2.4 |
| Vermelho (lento) | Mais de 4 | Mais de 2.4 |

### TBT (Total Blocking Time)
- Mede o tempo total em que uma página web não consegue responder a entradas do usuário como cliques do mouse, toques na tela e entrada do teclado
- Entre as tarefas entre FCP e [TTI (Time to Interactive)](https://developer.chrome.com/docs/lighthouse/performance/interactive?hl={{ site.active_lang }})\*, considera tarefas executadas por 50ms ou mais como [tarefas longas](https://web.dev/articles/long-tasks-devtools?hl={{ site.active_lang }}), e define a *porção de bloqueio (blocking portion)* como o tempo excedente após subtrair 50ms do tempo gasto em cada uma dessas tarefas longas, sendo o TBT a soma de todas as porções de bloqueio

> \* O próprio TTI é excessivamente sensível a anomalias de resposta de rede e tarefas longas, resultando em baixa consistência e alta variabilidade, e por isso [foi excluído dos itens de avaliação de performance a partir do Lighthouse 10](https://developer.chrome.com/blog/lighthouse-10-0#scoring-changes).
{: .prompt-info }

> Geralmente, a causa mais comum de tarefas longas é o carregamento, análise e execução desnecessários ou ineficientes de JavaScript, e a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}) e o [web.dev do Google](https://web.dev/articles/long-tasks-devtools#what_is_causing_my_long_tasks?hl={{ site.active_lang }}) recomendam considerar reduzir o tamanho do payload JavaScript através de [divisão de código](https://web.dev/articles/reduce-javascript-payloads-with-code-splitting?hl={{ site.active_lang }}) para que cada um possa ser executado dentro de 50ms, e se necessário, separar para service workers separados em vez da thread principal para execução multithread.
{: .prompt-tip }

#### Critérios de Avaliação do Lighthouse
De acordo com a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time/?hl={{ site.active_lang }}), os critérios de avaliação do Lighthouse são os seguintes:

| Classificação por Cor | FCP Móvel (milissegundos) | FCP Desktop (milissegundos) |
| --- | --- | --- |
| Verde (rápido) | 0-200 | 0-150 |
| Laranja (médio) | 200-600 | 150-350 |
| Vermelho (lento) | Mais de 600 | Mais de 350 |

### CLS (Cumulative Layout Shift)
{% include embed/video.html src='https://web.dev/static/articles/cls/video/web-dev-assets/layout-instability-api/layout-instability2.webm' title="Exemplo de mudança súbita de layout" autoplay=true loop=true %}
> Fonte do vídeo: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls?hl={{ site.active_lang }})

~~Uma profunda raiva pode ser sentida no movimento do cursor~~

- Mudanças inesperadas de layout prejudicam a experiência do usuário de várias maneiras, como fazer o texto se mover repentinamente fazendo perder a posição de leitura, ou causar cliques errados em links ou botões
- O método específico para calcular a pontuação CLS está descrito no [web.dev do Google](https://web.dev/articles/cls)
- Como pode ser visto na imagem abaixo, deve-se visar 0,1 ou menos

![What is a good CLS score?](/assets/img/about-web-vitals/good-cls-values.svg)
> Fonte da imagem: [Cumulative Layout Shift (CLS) \| Articles \| web.dev](https://web.dev/articles/cls#what-is-a-good-cls-score?hl={{ site.active_lang }})

### SI (Speed Index)
- Mede quão rapidamente o conteúdo é exibido visualmente durante o carregamento da página
- O Lighthouse grava em vídeo o processo de carregamento da página no navegador, analisa o vídeo para calcular o progresso entre frames e usa o [módulo Speedline Node.js](https://github.com/paulirish/speedline) para calcular a pontuação SI

> Incluindo as coisas mencionadas ao resumir [FCP](#fcp-first-contentful-paint), [LCP](#lcp-largest-contentful-paint) e [TBT](#tbt-total-blocking-time) anteriormente, qualquer medida que melhore a velocidade de carregamento da página também afeta positivamente a pontuação SI. Pode ser vista como uma métrica de performance que reflete todo o processo de carregamento em certo nível, em vez de representar apenas um processo específico do carregamento da página.
{: .prompt-tip }

#### Critérios de Avaliação do Lighthouse
De acordo com a [documentação do desenvolvedor Chrome](https://developer.chrome.com/docs/lighthouse/performance/speed-index/?hl={{ site.active_lang }}), os critérios de avaliação do Lighthouse são os seguintes:

| Classificação por Cor | SI Móvel (segundos) | SI Desktop (segundos) |
| --- | --- | --- |
| Verde (rápido) | 0-3.4 | 0-1.3 |
| Laranja (médio) | 3.4-5.8 | 1.3-2.3 |
| Vermelho (lento) | Mais de 5.8 | Mais de 2.3 |
