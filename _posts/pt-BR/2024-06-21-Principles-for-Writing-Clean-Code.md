---
title: "Princípios para escrever um bom código"
description: >-
  Exploramos a necessidade de escrever um bom código e os principais princípios geralmente utilizados para escrever um bom código.
categories:
  - Programming
tags:
  - Coding
  - PS/CP
---
## A necessidade de escrever um bom código
Se nos concentrarmos apenas em escrever código rapidamente para implementação imediata, a [dívida técnica](/posts/Technical-debt/) pode crescer a níveis incontroláveis, causando problemas de manutenção no futuro. Portanto, ao conduzir um projeto de desenvolvimento, é indiscutivelmente importante escrever um bom código que seja legível e fácil de manter desde o início, sempre que possível.

No caso de resolução de problemas algorítmicos (PS, Problem Solving) ou programação competitiva (CP, Competitive Programming), geralmente não há necessidade de reutilizar o código usado para resolver o problema após o término da resolução ou competição. Especialmente no caso de CP, devido às restrições de tempo, há quem diga que a implementação rápida é mais importante do que escrever um bom código. Para responder a essa questão, é necessário considerar por que você está fazendo PS/CP e qual direção você está buscando.

Pessoalmente, acredito que os pontos que podem ser aprendidos através de PS/CP são os seguintes:
- Ao resolver problemas dentro das restrições de tempo de execução e memória, você pode usar e aprender várias estruturas de dados e algoritmos, e através disso, desenvolver uma intuição sobre quais algoritmos e estruturas de dados usar em situações específicas ao conduzir projetos reais
- Após escrever e enviar o código, você recebe feedback objetivo imediato sobre se está correto/incorreto, tempo de execução e uso de memória, permitindo praticar a escrita de código preciso, rápido e habilidoso sem perder nenhum detalhe
- Você pode ver o código escrito por outros especialistas, comparar com o seu próprio código e encontrar pontos de melhoria
- Como você escreve repetidamente código de escala menor que faz funções semelhantes em comparação com projetos de desenvolvimento reais, (especialmente ao praticar PS sozinho) você pode praticar escrever código conciso e bom, prestando atenção aos detalhes sem estar preso a prazos

Embora possa haver casos em que PS/CP seja simplesmente desfrutado como um hobby, se você, como eu, faz PS/CP para indiretamente melhorar suas habilidades de programação, a "prática de escrever bom código" mencionada por último é uma grande vantagem, não menos importante que as três anteriores. Isso porque escrever bom código não é algo que vem naturalmente desde o início, mas requer prática constante e repetitiva para se tornar proficiente. Além disso, código complexo e difícil de ler é difícil de depurar e não é fácil de escrever corretamente de uma vez, então se você perder tempo com depuração ineficiente, muitas vezes não conseguirá implementar tão rapidamente. Embora PS/CP seja, é claro, muito diferente do trabalho real, por essas razões, pessoalmente, tento esforçar-me para escrever código conciso e eficiente mesmo em PS/CP, em vez de me concentrar apenas na implementação imediata sem me preocupar em escrever bom código.

## Princípios para escrever um bom código
Seja o código escrito em competições ou no trabalho real, as condições para um bom código não são muito diferentes. Este artigo aborda os principais princípios para escrever um bom código em geral. No entanto, em PS/CP, pode haver áreas onde se faz concessões em comparação com o trabalho real para implementação rápida, e esses casos serão mencionados separadamente no artigo.

### Escrever código conciso
> "KISS (Keep It Simple, Stupid)"
- Quanto mais curto e conciso o código, naturalmente menor é o risco de erros de digitação ou bugs simples, e mais fácil é a depuração
- Escreva de forma que possa ser facilmente interpretado sem comentários separados sempre que possível, e adicione explicações detalhadas com comentários apenas quando realmente necessário. É preferível manter a própria estrutura do código concisa do que depender de comentários.
- Ao escrever comentários, faça-o de forma clara e concisa
- Limite o número de argumentos passados para uma função a três ou menos, e se mais argumentos precisarem ser passados juntos, agrupe-os em um único objeto
- A profundidade (depth) de declarações condicionais que se aprofundam em duplo ou triplo reduz a legibilidade, portanto, aumentar a profundidade das declarações condicionais deve ser evitado sempre que possível. 
  ex) O código abaixo usando a cláusula de guarda (Guard Clause) é mais favorável em termos de legibilidade do que o código acima  

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
- No entanto, em PS/CP, às vezes se usa o truque de usar macros em C/C++ para reduzir ainda mais o comprimento do código e escrevê-lo rapidamente. Isso pode ser útil ocasionalmente em competições com tempo limitado, mas é uma técnica que funciona apenas para PS/CP e geralmente o uso de macros em C++ deve ser evitado.  
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularização do código
> "DRY (Don't Repeat Yourself)"
- Quando o mesmo código é usado repetidamente, separe essa parte em uma função ou classe para reutilização
- A reutilização ativa do código através da modularização melhora a legibilidade e facilita a manutenção, pois quando surge a necessidade de modificar o código posteriormente, basta modificar a função ou classe relevante uma vez
- Em princípio, é ideal que uma função execute apenas uma funcionalidade e não faça duas ou mais coisas. No entanto, o código escrito em PS/CP geralmente é um programa de pequena escala que executa funções simples, então há limites na reutilização, e devido às restrições de tempo, pode ser difícil seguir os princípios tão estritamente quanto no trabalho real.

### Utilização de bibliotecas padrão
> "Don't reinvent the wheel"
- Na fase de estudo de algoritmos ou estruturas de dados, é útil implementar diretamente estruturas de dados como filas e pilhas, algoritmos de ordenação, etc., para entender os princípios, mas caso contrário, é melhor utilizar ativamente as bibliotecas padrão
- As bibliotecas padrão já foram usadas e verificadas inúmeras vezes, e são bem otimizadas, tornando-as mais eficientes do que implementar diretamente novamente
- Como você pode simplesmente usar bibliotecas já existentes, não há necessidade de desperdiçar tempo implementando diretamente código que faz a mesma função desnecessariamente, e é mais fácil para outros membros da equipe entenderem o código que você escreveu durante a colaboração

### Uso de nomenclatura consistente e clara
> "Follow standard conventions"
- Use nomes de variáveis e funções que não sejam ambíguos
- Geralmente, cada linguagem de programação tem suas próprias convenções de nomenclatura, então aprenda as convenções de nomenclatura usadas na biblioteca padrão da linguagem que você está usando e aplique-as consistentemente ao declarar classes, funções, variáveis, etc.
- Nomeie de forma que fique claro qual função cada variável, função e classe desempenha, e no caso de tipos booleanos, em que condições retornam verdadeiro (True)

### Armazenar todos os dados de forma normalizada
- Processe todos os dados em um formato consistente e normalizado
- Se os mesmos dados tiverem dois ou mais formatos, podem ocorrer bugs sutis e difíceis de detectar, como representações de strings ligeiramente diferentes ou valores de hash diferentes
- Ao armazenar e processar dados como fusos horários, strings, etc., eles devem ser convertidos para um formato padrão único, como UTC, codificação UTF-8, etc., assim que forem recebidos ou calculados. É bom realizar a normalização desde o início no construtor da classe que representa os dados ou realizar a normalização imediatamente na função que recebe os dados.

### Separar a lógica do código e os dados
- Dados que não estão relacionados à lógica do código não devem ser colocados diretamente em declarações condicionais, mas separados em uma tabela separada  
  ex) É preferível escrever como o código abaixo em vez do código acima.

  ```c++
  string getMonthName(int month){
    if(month == 1) return "January";
    if(month == 2) return "February";
    ...
    if(month == 12) return "December";
  }
  ```
  ```c++
  const string monthName[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

  string getMonthName(int month){
    return monthName[month-1];
  }
  ```