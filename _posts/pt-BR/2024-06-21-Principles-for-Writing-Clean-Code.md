---
title: "Princípios para escrever um bom código"
description: >-
  Exploramos a necessidade de escrever um bom código e os principais princípios geralmente aplicados para criar um código de qualidade.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.jpg
---
## A necessidade de escrever um bom código
Se nos concentrarmos apenas em escrever código rapidamente para implementação imediata, a [dívida técnica](/posts/Technical-debt/) pode crescer a níveis incontroláveis, causando problemas de manutenção no futuro. Portanto, ao desenvolver um projeto, é indiscutivelmente importante escrever um bom código desde o início, que seja legível e fácil de manter.

No caso de resolução de problemas algorítmicos (PS, Problem Solving) ou programação competitiva (CP, Competitive Programming), geralmente não há necessidade de reutilizar o código após a conclusão do problema ou da competição. Especialmente em CP, onde há restrições de tempo, alguns argumentam que a implementação rápida é mais importante do que escrever um bom código. Para responder a essa questão, é necessário considerar por que você está fazendo PS/CP e qual direção você está buscando.

Pessoalmente, acredito que os pontos que podem ser aprendidos através de PS/CP são os seguintes:
- Ao resolver problemas dentro de limites de tempo de execução e memória, você pode usar e aprender várias estruturas de dados e algoritmos, o que ajuda a desenvolver intuição sobre quais algoritmos e estruturas de dados usar em situações específicas em projetos reais
- Após escrever e enviar o código, você recebe feedback objetivo imediato sobre acerto/erro, tempo de execução e uso de memória, permitindo praticar a escrita de código preciso, rápido e habilidoso sem perder detalhes
- Você pode comparar seu código com o de outros programadores experientes e identificar áreas de melhoria
- Comparado a projetos de desenvolvimento reais, você escreve repetidamente código de menor escala com funcionalidades similares, permitindo (especialmente ao praticar PS sozinho) exercitar a escrita de código conciso e de qualidade, focando nos detalhes sem se prender a prazos

Embora alguns possam desfrutar de PS/CP apenas como hobby, se você o faz para indiretamente melhorar suas habilidades de programação, a prática de escrever bom código é tão vantajosa quanto os três primeiros pontos mencionados. Escrever bom código não vem naturalmente desde o início, mas requer prática constante e repetitiva. Além disso, código complexo e difícil de ler é complicado de depurar e até mesmo difícil de escrever corretamente de uma vez, então muitas vezes acaba-se perdendo tempo com depuração ineficiente e não implementando tão rapidamente quanto se esperava. Embora PS/CP seja certamente muito diferente do trabalho real, por essas razões, pessoalmente acredito que é melhor se preocupar em escrever código conciso e eficiente mesmo em PS/CP, em vez de focar apenas na implementação imediata, o que seria colocar a carroça na frente dos bois.

> Comentário adicionado em 12/2024:  
> Considerando o clima atual, a menos que você esteja se formando em ciência da computação e planejando fazer do desenvolvimento seu ofício, se você pretende usar programação como uma ferramenta para análise numérica ou interpretação de dados experimentais, talvez seja melhor usar ativamente IA como GitHub Copilot, Cursor, Windsurf, etc., para economizar tempo e usar esse tempo economizado para estudar outras coisas. Se você gosta de PS/CP como hobby, ninguém vai impedi-lo, mas investir tempo e esforço em PS/CP para praticar escrita de código parece ter agora uma relação custo-benefício muito baixa. Mesmo para carreiras de desenvolvimento, espero que a importância dos testes de codificação como exame de admissão provavelmente diminua significativamente em comparação com o passado.
{: .prompt-warning }

## Princípios para escrever um bom código
Seja o código escrito para competições ou para uso profissional, as condições para um bom código não são muito diferentes. Este artigo aborda os principais princípios geralmente aplicados para escrever um bom código. No entanto, em PS/CP, pode haver áreas onde se faz concessões em relação à prática profissional para implementação rápida; esses casos serão mencionados separadamente no texto.

### Escrevendo código conciso
> "KISS (Keep It Simple, Stupid)"

- Quanto mais curto e conciso o código, naturalmente menor é o risco de erros de digitação ou bugs simples, e mais fácil é a depuração
- Escreva de forma que possa ser facilmente interpretado sem comentários adicionais sempre que possível, adicionando comentários apenas quando realmente necessário para explicações detalhadas. É preferível manter a estrutura do código concisa em vez de depender de comentários.
- Se escrever comentários, faça-o de forma clara e concisa
- Limite o número de argumentos passados para uma função a três ou menos; se precisar passar mais argumentos juntos, agrupe-os em um único objeto
- Evite aumentar a profundidade das declarações condicionais, pois isso reduz a legibilidade quando se torna duplo ou triplo. 
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
- No entanto, em PS/CP, às vezes se usa o truque de usar macros em C/C++ para reduzir ainda mais o comprimento do código e escrevê-lo rapidamente. Isso pode ser útil ocasionalmente em competições com tempo limitado, mas é uma técnica que só funciona em PS/CP e geralmente o uso de macros em C++ deve ser evitado.  
  ex)  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularização do código
> "DRY (Don't Repeat Yourself)"

- Quando o mesmo código é usado repetidamente, separe essa parte em funções ou classes para reutilização
- A modularização ativa através da reutilização de código melhora a legibilidade e facilita a manutenção, pois quando surge a necessidade de modificar o código posteriormente, basta modificar a função ou classe uma vez
- Em princípio, é ideal que uma função execute apenas uma funcionalidade e não faça duas ou mais coisas. No entanto, o código escrito em PS/CP geralmente é um programa de pequena escala que executa funcionalidades simples, então há limitações na reutilização, e devido às restrições de tempo, pode ser difícil seguir os princípios tão estritamente quanto na prática profissional.

### Utilização de bibliotecas padrão
> "Don't reinvent the wheel"

- Ao estudar algoritmos ou estruturas de dados, é útil implementar diretamente estruturas de dados como filas ou pilhas e algoritmos de ordenação para entender os princípios, mas caso contrário, é melhor utilizar ativamente as bibliotecas padrão
- As bibliotecas padrão já foram usadas e verificadas inúmeras vezes, e são bem otimizadas, sendo mais eficientes do que implementar novamente por conta própria
- Como você pode simplesmente usar bibliotecas já existentes, não há necessidade de desperdiçar tempo implementando diretamente código com a mesma funcionalidade, e é mais fácil para outros membros da equipe entenderem o código que você escreveu durante a colaboração

### Uso de nomenclatura consistente e clara
> "Follow standard conventions"

- Use nomes de variáveis e funções que não sejam ambíguos
- Geralmente, cada linguagem de programação tem suas próprias convenções de nomenclatura, então aprenda as convenções usadas nas bibliotecas padrão da linguagem que você está usando e aplique-as consistentemente ao declarar classes, funções, variáveis, etc.
- Nomeie de forma que fique claro qual é a função de cada variável, função e classe, e no caso de tipos booleanos, em que condições retornam verdadeiro (True)

### Armazenamento de todos os dados de forma normalizada
- Processe todos os dados em um formato consistente e normalizado
- Se o mesmo dado tiver mais de um formato, podem ocorrer bugs sutis e difíceis de detectar, como pequenas diferenças na representação de strings ou valores de hash diferentes
- Ao armazenar e processar dados como fusos horários e strings, eles devem ser convertidos para um formato padrão único, como UTC ou codificação UTF-8, assim que forem recebidos ou calculados. É bom realizar a normalização desde o início no construtor da classe que representa os dados ou na função que recebe os dados.

### Separação da lógica do código e dos dados
- Dados não relacionados à lógica do código não devem ser colocados diretamente em declarações condicionais, mas separados em tabelas distintas  
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
