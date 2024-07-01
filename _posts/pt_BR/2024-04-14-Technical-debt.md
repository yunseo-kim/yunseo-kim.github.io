---
title: "Dívida Técnica (Technical debt)"
description: >-
  Vamos explorar o conceito de dívida técnica, as razões pelas quais ela ocorre e como minimizá-la.
categories: [Programação]
tags: [Codificação]
---

## Dívida Técnica (Technical debt)
Dívida Técnica: O preço a ser pago posteriormente por escolher atalhos que permitem concluir o projeto mais rapidamente para atender às necessidades imediatas durante o processo de desenvolvimento.

Assim como assumir uma dívida financeira permite investir rapidamente onde é necessário, mas resulta em pressão financeira e pagamento do principal mais juros, desenvolver rapidamente para resolver requisitos imediatos, mesmo que de forma um pouco desorganizada, leva a código complexo e redundante, dificultando a implementação ou expansão de novas funcionalidades no futuro.

Assim como uma empresa pode usar dívidas para fazer mais investimentos oportunos, desenvolver novos produtos e aumentar a participação de mercado, ou um indivíduo pode contratar um empréstimo para comprar uma casa, nem sempre é ruim assumir dívida técnica para implementar novas funcionalidades rapidamente. No entanto, é desejável reduzir o acúmulo de dívida técnica e gerenciá-la em um nível administrável.

## Razões para o surgimento da dívida técnica
Mesmo que a capacidade do desenvolvedor seja suficiente, a dívida técnica inevitavelmente surge durante o processo de desenvolvimento de software e é impossível evitá-la completamente.
À medida que o serviço evolui, o código originalmente projetado pode atingir seus limites, e mesmo que o código fosse originalmente legível e funcionasse bem, pode ser necessário modificar o design existente.
Além disso, à medida que a própria tecnologia evolui, bibliotecas/frameworks que antes eram predominantes podem cair em desuso, levando à decisão de mudar a pilha tecnológica para outras bibliotecas/frameworks, e neste caso, o código existente também se torna uma espécie de dívida técnica.

Além disso, a dívida técnica pode surgir pelas seguintes razões:
- Não documentar o design em tempo real durante o projeto, dificultando a interpretação do código por outras pessoas ou até mesmo por si mesmo após algum tempo
- Não remover variáveis ou itens de banco de dados que não são mais utilizados
- Não automatizar tarefas repetitivas (implantação/compilação, etc.), exigindo tempo e esforço adicionais toda vez
- Mudanças urgentes nas especificações

## Métodos para minimizar a dívida técnica
### Estabelecimento de convenções entre desenvolvedores
- Quando não se está desenvolvendo sozinho, é necessário chegar a um acordo sobre a linguagem ou pilha tecnológica a ser usada, a estrutura de diretórios do projeto, o estilo de desenvolvimento, etc., para uma colaboração eficaz
- É preciso decidir até que ponto unificar os métodos de desenvolvimento e a partir de onde deixar para a autonomia individual
- É necessário verificar os estilos de desenvolvimento uns dos outros e trocar opiniões através de revisões de código

### Escrita de código limpo (Clean Code) & Refatoração (Refactoring)
- Se o código existente estiver desorganizado e atrapalhar o desenvolvimento, a dívida técnica pode ser liquidada através da refatoração, que melhora a estrutura do código
- Naturalmente, quanto mais desorganizado for o código existente, mais difícil será a refatoração
- Deve-se esforçar para escrever código legível e fácil de manter desde o início, sempre que possível