---
title: Princípios para escrever um bom código
description: "Por que escrever um bom código importa e os princípios‑chave: KISS, DRY, modularização, convenções de nomes, biblioteca padrão, normalização e separar lógica de dados."
categories: [Dev, Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
redirect_from:
  - /posts/Principles-for-Writing-Clean-Code/
---

## A necessidade de escrever um bom código
Se você se apressa apenas para implementar algo rapidamente, a [dívida técnica](/posts/Technical-debt/) pode crescer a um nível difícil de sustentar e causar problemas de manutenção depois. Portanto, ao conduzir um projeto de desenvolvimento, escrever desde o início um bom código, legível e fácil de manter, é algo que dispensa justificativas.

No caso de resolução de problemas com algoritmos (PS, Problem Solving) ou programação competitiva (CP, Competitive Programming), costuma-se dizer que o código usado para resolver o problema raramente será reutilizado após o fim do problema/competição e, especialmente em CP, como há limite de tempo, a implementação rápida seria mais importante do que escrever um bom código. Para responder a isso, vale refletir por que você faz PS/CP e qual direção está buscando.

Na minha visão, restringindo-nos ao aspecto relacionado à programação (fora do desenvolvimento de uma capacidade genérica de resolução de problemas), é possível aprender o seguinte por meio de PS/CP:
- Dentro de restrições como tempo de execução e memória, você pode usar e dominar diversos algoritmos e estruturas de dados, e com isso ganhar intuição sobre o que usar em situações específicas em projetos reais.
- Ao submeter o código, você recebe feedback objetivo imediato sobre certo/errado, tempo de execução e uso de memória, o que ajuda a treinar a escrita de código correto, de forma rápida e habilidosa, sem deixar pontas soltas.
- É possível comparar seu código com o de pessoas mais experientes e identificar pontos de melhoria.
- Como, em comparação com projetos reais, você escreve repetidamente códigos menores com funções semelhantes, (especialmente quando treina PS sozinho) pode praticar escrever código enxuto e bom, cuidando de detalhes sem ficar amarrado a prazos.

É claro que você pode fazer PS/CP apenas como hobby; mas, se o objetivo é desenvolver habilidades de programação, então o último ponto — “praticar escrever um bom código” — é uma vantagem tão grande quanto os três anteriores. Escrever bom código não surge naturalmente desde o início: requer prática repetida e melhoria contínua. Além disso, código confuso e difícil de ler é mais complicado de depurar e também é mais difícil de acertar de primeira; muitas vezes você acaba perdendo tempo com depuração ineficiente e nem implementa tão rápido assim. PS/CP é diferente do trabalho do dia a dia, mas, ainda assim, ignorar totalmente a qualidade e focar apenas em “fazer funcionar agora” me parece inverter prioridades; pessoalmente, acredito que em PS/CP também é melhor escrever código conciso e eficiente.

> 12024.12 Comentário adicional:  
> Pelo cenário atual, construir base de conhecimento em algoritmos e estruturas de dados para escrever programas eficientes e desenvolver capacidade de resolução de problemas seguirá sendo valioso, mas, na etapa de transformar isso em código executável, talvez não valha insistir em escrever tudo à mão. Usar ativamente IA como GitHub Copilot, Cursor ou Windsurf pode poupar tempo, e você pode investir o tempo ganho em outras tarefas ou estudos. Para praticar resolução de problemas de forma geral ou estudar algoritmos/estruturas de dados — ou simplesmente por hobby —, PS/CP continua válido; porém, dedicar tempo e esforço a PS/CP apenas para treinar digitação de código parece hoje ter uma relação custo‑benefício bem menor. Arrisco dizer que, mesmo em carreiras de desenvolvimento, os testes de código como prova de entrada provavelmente terão importância bem menor do que no passado.
{: .prompt-warning }

## Princípios para escrever um bom código
Os critérios de um bom código não diferem muito entre o que você escreve em competições e o que escreve no trabalho. Aqui trato dos principais princípios para, em geral, escrever um bom código. Em PS/CP, pode haver concessões em prol da velocidade de implementação; nesses casos, menciono explicitamente no texto.

### Escreva código conciso
> "KISS (Keep It Simple, Stupid)"

- Quanto mais curto e conciso o código, menor a chance de typos ou bugs triviais e mais fácil a depuração.
- Sempre que possível, escreva de modo que o código se explique sozinho, sem precisar de comentários; adicione comentários apenas quando realmente necessário. Em vez de depender de comentários, é preferível manter a estrutura do código simples por si só.
- Quando escrever comentários, seja claro e direto.
- Prefira no máximo 3 argumentos por função; se precisar de mais, agrupe-os em um único objeto.
- Condicionais aninhadas em vários níveis prejudicam a legibilidade; evite aumentar a profundidade de ifs.  
  Exemplo: usar guard clause melhora a leitura:

  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if user:
          token = await user_service.get_token(user)
  
          if token :
              if token.purpose == 'reset':
                  return True
      return False
  ```
  ```python
  async def verify_token(email: str, token: str, purpose: str):
      user = await user_service.get_user_by_email(email)
  
      if not user:
          return False
    
      token = await user_service.get_token(user)
  
      if not token or token.purpose != 'reset':
          return False
    
    return True
  ```
- Em PS/CP, às vezes se recorre a artifícios para reduzir o tamanho e escrever mais rápido, como macros em C/C++. Podem ser úteis em competições com tempo apertado, mas funcionam só nesse contexto; no geral, o uso de macros em C++ deve ser evitado.  
  Exemplo:

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularização do código
> "DRY (Don't Repeat Yourself)"

- Se trechos de código se repetem, extraia-os para funções ou classes reutilizáveis.
- Modularizar e reutilizar ativamente melhora a legibilidade e facilita a manutenção: para mudanças futuras, basta alterar a função ou classe em um único lugar.
- Idealmente, uma função deve fazer apenas uma coisa. Em PS/CP, porém, os programas costumam ser pequenos e com funcionalidades simples, e o tempo é limitado; portanto, pode não ser viável seguir o princípio com o mesmo rigor do mundo real.

### Use a biblioteca padrão
> "Não reinvente a roda"

- Na fase de estudo de algoritmos e estruturas de dados, é útil implementar por conta própria filas, pilhas, ordenações etc. para entender os princípios. Fora isso, use a biblioteca padrão ativamente.
- Bibliotecas padrão já foram amplamente usadas e validadas, além de bem otimizadas, sendo mais eficientes do que reimplementar do zero.
- Reaproveitar o que já existe evita perder tempo implementando funcionalidade redundante e facilita que colegas entendam seu código em colaboração.

### Use nomenclaturas consistentes e claras
> "Siga as convenções padrão"

- Use nomes de variáveis e funções não ambíguos.
- Cada linguagem costuma ter convenções de nomenclatura; aprenda as usadas na biblioteca padrão da linguagem e aplique-as de forma consistente a classes, funções e variáveis.
- Deixe claro pelo nome o que cada variável, função ou classe faz e, no caso de booleanos, em que condição retornam verdadeiro (True).

### Normalize todos os dados ao armazenar
- Trate todos os dados em um formato único e consistente.
- Se o mesmo dado existir em dois ou mais formatos, podem surgir bugs sutis e difíceis de detectar, como diferenças na representação em string ou nos valores de hash.
- Ao armazenar/tratar datas, strings etc., converta imediatamente, na entrada ou no cálculo, para um formato padrão único, como UTC ou codificação UTF-8. É recomendável realizar a normalização já no construtor da classe que representa o dado, ou diretamente na função que recebe a entrada.

### Separe a lógica do código dos dados
- Não coloque dados que não dizem respeito à lógica dentro de condicionais; separe-os em uma tabela/estrutura própria.  
  Exemplo: em vez do código abaixo, prefira o seguinte.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ~~~c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ~~~
