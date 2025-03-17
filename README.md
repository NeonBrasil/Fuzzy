# Relatório: Sistema de Controle Fuzzy para Previsão de Peso
## Descrição do Projeto

Este projeto consiste em um sistema de controle fuzzy que prevê o peso de uma pessoa com base na quantidade de comida consumida e no nível de atividade física. Utilizando a biblioteca skfuzzy, o sistema é capaz de classificar as entradas em categorias fuzzy e aplicar regras para determinar a saída.

***

A variável "atividade" é uma parte crucial do sistema, pois reflete o nível de atividade física do usuário. Ela é categorizada em três conjuntos fuzzy:

+ Baixa: Representa um nível de atividade física muito baixo, onde a pessoa não se exercita ou se movimenta pouco.
+ Média: Refere-se a um nível moderado de atividade, onde a pessoa se exercita de forma regular, mas não intensamente.
+ Alta: Indica um nível elevado de atividade física, onde a pessoa se exercita com frequência e intensidade.

A inclusão dessa variável permite que o sistema leve em consideração não apenas a quantidade de comida consumida, mas também o impacto da atividade física no peso da pessoa. Por exemplo, uma pessoa que consome uma grande quantidade de comida, mas se exercita intensamente, pode ter um peso previsto diferente em comparação a alguém que consome a mesma quantidade, mas não se exercita.

### Experiência Resolvendo o Problema

Durante o desenvolvimento deste projeto, encontramos alguns desafios, especialmente na geração de gráficos (o que era opcional mas achamos que era legal). A lógica fuzzy é uma abordagem que permite lidar com incertezas e variáveis subjetivas, o que é muito útil em situações do mundo real. A criação de regras que considerassem tanto a quantidade de comida quanto o nível de atividade foi um aspecto interessante, pois exigiu uma compreensão profunda de como essas variáveis interagem. Conseguimos imaginar outras situações e problemas que podemos aplicar a regra Fuzzy.

### Exemplos de Aplicação da Lógica Fuzzy

A lógica fuzzy pode ser aplicada em diversas áreas além da previsão de peso. Um exemplo interessante é no controle de temperatura em sistemas de climatização. Em vez de definir uma temperatura exata, um sistema fuzzy pode considerar variáveis como:
***
+ Temperatura ambiente: Fria, agradável, quente.
+ Nível de conforto: Desconfortável, confortável, muito confortável.
***
Ou até mesmo um exemplo de sistema de aquecedor levando em consideração as seguintes variavéis:
+ Temperatura do lado de fora
+ Sensação térmica atual
+ Nível de conforto
+ Vai sair de casa em quanto tempo (nesse caso, se o usuário for sair de casa em pouco tempo o sistema não daria um valor muito alto para não causar choque térmico).

Com essas variáveis, o sistema pode ajustar a temperatura de forma mais eficiente, proporcionando um ambiente mais agradável para os usuários sem existir riscos para a saúde dos usuários.

### Membros do Grupo
+ Cayque Cicarelli - 22.221.005-6
+ Bruna Paz - 22.121.020-6
+ Matheus Miranda - 22.22.0017-2
***
## Conclusão

Este mini projeto demonstrou a aplicação da lógica fuzzy para resolver problemas do mundo real, como a previsão de peso com base em variáveis subjetivas. A utilização de regras fuzzy permite uma abordagem mais flexível e intuitiva em comparação com métodos tradicionais, mostrando o potencial dessa técnica em diversas áreas.
