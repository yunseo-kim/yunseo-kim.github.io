---
title: "Dívida técnica (Technical debt)"
description: >-
  Vamos explorar o conceito de dívida técnica, as razões pelas quais ela ocorre e como minimizá-la.
categories: [Programming]
tags: [Coding]
---

## Dívida técnica (Technical debt)
Dívida técnica: O preço a ser pago posteriormente por escolher atalhos que permitem concluir o projeto mais rapidamente para atender às necessidades imediatas durante o processo de desenvolvimento.

Assim como assumir uma dívida financeira permite investir rapidamente onde é necessário, mas resulta em pressão financeira e pagamento do principal com juros, desenvolver rapidamente para resolver requisitos imediatos, mesmo que de forma um pouco desorganizada, leva a código complexo e redundante, dificultando a implementação ou expansão de novas funcionalidades no futuro.

Assumir dívida técnica para implementar rapidamente novas funcionalidades não é necessariamente ruim, assim como empresas usam dívidas para investir oportunamente no desenvolvimento de novos produtos e aumentar a participação de mercado, ou indivíduos fazem empréstimos para comprar casas. No entanto, é desejável reduzir o acúmulo de dívida técnica e gerenciá-la em um nível administrável.

## Razões para o surgimento da dívida técnica
A dívida técnica surge inevitavelmente no processo de criação de software, mesmo com desenvolvedores competentes, e é impossível evitá-la completamente.
À medida que um serviço evolui, o código originalmente projetado pode atingir seus limites, exigindo modificações no design existente, mesmo que o código fosse inicialmente legível e funcional.
Além disso, com o avanço da tecnologia, bibliotecas/frameworks antes populares podem cair em desuso, levando à decisão de mudar para outras tecnologias, transformando o código existente em uma forma de dívida técnica.

Outras razões para o surgimento da dívida técnica incluem:
- Não documentar o design do projeto em tempo real, dificultando a interpretação do código por outros ou pelo próprio autor após algum tempo
- Não remover variáveis ou itens de banco de dados que não são mais utilizados
- Não automatizar tarefas repetitivas (como implantação/compilação), exigindo tempo e esforço adicionais a cada vez
- Mudanças urgentes nas especificações

## Métodos para minimizar a dívida técnica
### Estabelecimento de convenções entre desenvolvedores
- Quando o desenvolvimento não é individual, é necessário chegar a um acordo sobre linguagens, pilhas tecnológicas, estrutura de diretórios do projeto e estilos de desenvolvimento para uma colaboração eficaz
- Decidir até que ponto os métodos serão unificados e onde começará a autonomia individual
- É importante realizar revisões de código para verificar os estilos de desenvolvimento uns dos outros e trocar opiniões

### Escrita de código limpo (Clean Code) & Refatoração (Refactoring)
- Se o código existente estiver desorganizado e atrapalhar o desenvolvimento, a dívida técnica pode ser liquidada através da refatoração, que melhora a estrutura do código
- Naturalmente, quanto mais desorganizado o código existente (código espaguete), mais difícil será a refatoração
- Deve-se esforçar para escrever código legível e fácil de manter desde o início