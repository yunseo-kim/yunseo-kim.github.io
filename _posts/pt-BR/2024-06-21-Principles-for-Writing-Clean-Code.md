---
title: Princípios para escrever um bom código
description: Exploramos a necessidade de escrever um bom código e os principais princípios geralmente aplicados para criar código de qualidade.
categories: [Programming]
tags: [Coding, PS/CP]
image: /assets/img/technology.webp
---
## A necessidade de escrever um bom código
Se nos concentrarmos apenas em escrever código rapidamente para implementação imediata, a [dívida técnica](/posts/Technical-debt/) pode crescer a níveis incontroláveis, causando problemas de manutenção no futuro. Portanto, ao desenvolver projetos, é indiscutivelmente importante escrever código legível e de fácil manutenção desde o início.

No caso de Resolução de Problemas (PS, Problem Solving) ou Programação Competitiva (CP, Competitive Programming), geralmente não reutilizamos o código após a conclusão do problema ou competição. Especialmente em CP, devido às restrições de tempo, alguns argumentam que a implementação rápida é mais importante que escrever código de qualidade. Para responder a essa questão, é necessário refletir sobre por que você pratica PS/CP e qual direção deseja seguir.

Na minha opinião, os benefícios que podemos obter com PS/CP incluem:
- Praticar e aprender diversos algoritmos e estruturas de dados dentro de limites de tempo de execução e memória, desenvolvendo intuição sobre quais usar em situações específicas em projetos reais
- Receber feedback objetivo imediato sobre a correção, tempo de execução e uso de memória do código, permitindo praticar a escrita de código preciso e eficiente
- Comparar seu código com o de programadores mais experientes para identificar pontos de melhoria
- Praticar a escrita de código conciso e de qualidade, trabalhando com códigos de escala menor que projetos reais, mas com funcionalidades similares, sem a pressão de prazos (especialmente quando praticando PS sozinho)

Embora alguns pratiquem PS/CP apenas como hobby, para quem busca indiretamente melhorar suas habilidades de programação, o último ponto - "praticar a escrita de bom código" - é uma vantagem tão importante quanto as três primeiras. Escrever bom código não é algo natural desde o início, mas uma habilidade que requer prática constante. Além disso, código complexo e difícil de ler é mais difícil de depurar e mais propenso a erros, o que pode acabar consumindo tempo em depuração ineficiente. Embora PS/CP seja diferente do desenvolvimento profissional, negligenciar completamente a qualidade do código em favor da implementação rápida é, pelos motivos mencionados, contraproducente. Por isso, pessoalmente, acredito que escrever código conciso e eficiente é importante mesmo em PS/CP.

> Comentário adicionado em 12024.12:  
> Considerando o cenário atual, a menos que você esteja estudando ciência da computação e planeje seguir carreira em desenvolvimento, se você usa programação apenas como ferramenta para análise numérica ou processamento de dados experimentais, talvez seja mais eficiente utilizar ferramentas de IA como GitHub Copilot, Cursor ou Windsurf para economizar tempo e dedicar-se a outros estudos. Se você gosta de PS/CP como hobby, não há problema, mas investir tempo e esforço em PS/CP apenas para praticar codificação parece ter uma relação custo-benefício baixa atualmente. Prevejo que mesmo para carreiras de desenvolvimento, a importância dos testes de codificação em processos seletivos provavelmente diminuirá em comparação com o passado.
{: .prompt-warning }

## Princípios para escrever um bom código
Os critérios para um bom código não diferem muito entre código escrito para competições ou para uso profissional. Este artigo aborda os principais princípios para escrever bom código em geral. No entanto, em PS/CP, pode haver compromissos para implementação rápida que serão mencionados quando relevantes.

### Escrever código conciso
> "KISS (Keep It Simple, Stupid)"

- Código mais curto e conciso naturalmente reduz a chance de erros de digitação ou bugs simples, facilitando a depuração
- Escreva código que possa ser facilmente interpretado sem comentários extensos, adicionando comentários apenas quando realmente necessário. É preferível manter a estrutura do código concisa a depender de comentários.
- Quando escrever comentários, seja claro e conciso
- Limite o número de argumentos em uma função a três ou menos; se precisar passar mais argumentos, agrupe-os em um único objeto
- Evite aninhamento profundo de condicionais, pois isso reduz a legibilidade. 
  Ex: O código abaixo usando cláusulas de guarda (Guard Clause) é mais legível que o anterior

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
- Em PS/CP, às vezes são usadas macros em C/C++ para reduzir ainda mais o tamanho do código e acelerar a escrita. Isso pode ser útil em competições com tempo limitado, mas geralmente o uso de macros em C++ deve ser evitado em desenvolvimento normal.  
  Ex:  

  ```c++
  #define FOR(i,n) for(int i=0; i<n; i++)
  ```

### Modularização de código
> "DRY (Don't Repeat Yourself)"

- Quando o mesmo código é usado repetidamente, separe-o em funções ou classes para reutilização
- A modularização melhora a legibilidade e facilita a manutenção, pois modificações futuras precisam ser feitas em apenas um lugar
- Idealmente, uma função deve realizar apenas uma tarefa. No entanto, em PS/CP, onde os programas geralmente são menores e o tempo é limitado, pode ser difícil seguir este princípio tão rigorosamente quanto em ambiente profissional.

### Utilização de bibliotecas padrão
> "Don't reinvent the wheel"

- Embora seja útil implementar estruturas de dados como filas e pilhas ou algoritmos de ordenação para entender seus princípios durante o aprendizado, é melhor utilizar bibliotecas padrão em outros casos
- As bibliotecas padrão são bem testadas, otimizadas e amplamente utilizadas, tornando-as mais eficientes que implementações próprias
- Usar bibliotecas existentes economiza tempo e torna o código mais compreensível para outros desenvolvedores

### Uso de nomenclatura consistente e clara
> "Follow standard conventions"

- Use nomes de variáveis e funções não ambíguos
- Aprenda e aplique consistentemente as convenções de nomenclatura da linguagem que está usando
- Nomeie variáveis, funções e classes de forma que sua finalidade seja clara, incluindo quando uma variável booleana retorna verdadeiro

### Normalização de todos os dados
- Processe todos os dados em um formato consistente e normalizado
- Dados com múltiplos formatos podem causar bugs sutis, como diferenças em representações de string ou valores hash
- Ao armazenar e processar dados como fusos horários ou strings, converta-os imediatamente para um formato padrão (UTC, codificação UTF-8, etc.). Isso pode ser feito no construtor da classe que representa os dados ou na função que recebe os dados.

### Separação entre lógica e dados
- Separe dados que não estão relacionados à lógica do código em tabelas separadas, em vez de incluí-los diretamente em condicionais  
  Ex: O código abaixo é preferível ao anterior.

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
