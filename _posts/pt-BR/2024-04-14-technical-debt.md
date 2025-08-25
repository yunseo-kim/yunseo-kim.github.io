---
title: Dívida técnica (Technical debt)
description: "Entenda o que é dívida técnica, por que ela surge no desenvolvimento de software e práticas objetivas para reduzir e gerenciar seu impacto ao mínimo."
categories: [Dev, Programming]
tags: [Coding]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Technical-debt/
---

## Dívida técnica
> Dívida técnica (Technical debt)  
> O custo que se paga depois por optar por atalhos para finalizar mais rapidamente um projeto a fim de atender demandas imediatas no desenvolvimento
{: .prompt-info }

Assim como, ao contrair uma dívida financeira, é possível investir rapidamente no que é necessário, mas sofre-se pressão e paga-se juros sobre o principal, avançar rápido no desenvolvimento para resolver exigências imediatas — ainda que de maneira um pouco “suja” — torna o código mais complexo e redundante, dificultando a implementação de novas funcionalidades e a escalabilidade no futuro.

Assumir dívida técnica para entregar novas funcionalidades rapidamente não é intrinsecamente ruim — assim como empresas usam dívida para investir em novos produtos e ganhar mercado, ou indivíduos para financiar um imóvel. O ideal é reduzir seu acúmulo e gerenciá-la em um nível suportável.

## Por que a dívida técnica surge
Mesmo com desenvolvedores competentes, a dívida técnica é inevitável no processo de desenvolvimento; impedi-la totalmente é impossível. À medida que o serviço evolui, o código originalmente projetado pode chegar ao limite, e mesmo uma base legível e funcional pode exigir revisões de arquitetura. Além disso, com a evolução da tecnologia, bibliotecas e frameworks antes predominantes deixam de ser usados; ao decidir migrar o stack para outras opções, o código existente também se torna uma forma de dívida técnica.

Outras razões comuns incluem:
- Não documentar em tempo hábil as decisões de design, dificultando a interpretação por outras pessoas ou por você mesmo no futuro
- Não remover variáveis ou campos de banco de dados que não são mais utilizados
- Não automatizar tarefas repetitivas (deploy/build etc.), exigindo tempo e esforço adicionais a cada ciclo
- Mudanças urgentes de especificação

## Como minimizar a dívida técnica
### Definir convenções entre desenvolvedores
- Quando não se desenvolve sozinho, é necessário alinhar linguagem, stack, estrutura de diretórios do projeto, estilo de desenvolvimento etc. para colaborar bem
- Decidir o que será padronizado e o que ficará sob autonomia individual
- Realizar revisões de código para conhecer os estilos de desenvolvimento e trocar feedbacks

### Escrever código limpo (Clean Code) & refatoração (Refactoring)
- Se o código existente estiver atrapalhando, é possível abater a dívida técnica por meio de refatoração, tornando a estrutura mais limpa
- Quanto mais “código espaguete” for a base, maior a dificuldade de refatorar; em casos extremos, desiste-se da refatoração, descarta-se o código e reescreve-se do zero
- Idealmente, esforçar-se desde o início para escrever código legível e de fácil manutenção
