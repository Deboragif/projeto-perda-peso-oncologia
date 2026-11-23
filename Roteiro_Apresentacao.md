# Roteiro da apresentação

Apresentação em sequência única. As explicações integram os assuntos correspondentes.

## Slide 1

UFPE  /  INTRODUÇÃO À CIÊNCIA DE DADOS

Perda de peso em

pacientes oncológicos

Uma base brasileira real

Comparação entre Lasso e floresta aleatória

Débora de Cássia de Morais

23 de novembro de 2026

01

### Explicação para a fala

Fala: meu trabalho investiga quanto as características e os sintomas de pacientes com câncer ajudam a estimar a perda de peso já registrada. Comparei Lasso e floresta aleatória com uma referência simples. Autora: Débora de Cássia de Morais, Introdução à Ciência de Dados, UFPE. Base: Viana et al. (2020).

## Slide 2

De onde vêm os dados?

Característica

Base utilizada

Pacientes

135 adultos com câncer

Local

Hospital público de Vitória, ES

Coleta

Março/2017 a outubro/2019

Publicação

Viana et al., PLOS ONE, 2020

Banco original

44 variáveis, arquivo público SAV

Dados reais de pacientes cirúrgicos de um único hospital.

02

### Explicação para a fala

Os dados são de um estudo brasileiro publicado, disponibilizados individualmente no suplemento S 1 Data. O ano da coleta é diferente do ano de publicação. Conferimos registros repetidos, ausências e codificação. Não há ausências nas variáveis selecionadas, nem linhas duplicadas ou IDs repetidos. Não afirmamos que a base representa o Brasil inteiro. Fonte: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0241305

## Slide 3

O que queremos estimar?

Resposta do modelo (Y)

Percentual de peso perdido nos seis meses anteriores à avaliação

Entradas do modelo (X)

Características do paciente e sintomas

Exemplo hipotético

Valor

Peso habitual

80 kg

Peso atual

72 kg

Perda

8 kg = 10%

Estimamos uma quantidade. Por isso, usamos regressão.

03

### Explicação para a fala

Y é o que queremos estimar. X são as informações usadas para essa estimativa. O exemplo 80 kg para 72 kg é inventado apenas para explicar o percentual: (80−72)/80 × 100=10%. Não foi calculado com esses pesos no banco, que já fornece weight_loss. Não estamos diagnosticando desnutrição ou prevendo perda futura. A resposta registrada refere-se aos seis meses anteriores, avaliada na mesma ocasião dos sintomas. Fonte: artigo e dicionário de Viana et al. (2020).

## Slide 4

p.p. significa pontos percentuais

Erro médio de 5,43 p.p. não significa 5,43% de erros nem 94,57% de acertos.

04

Exemplo hipotético

João pesava 100 kg e perdeu 14 kg: perda real de 14%.

O modelo estimou uma perda de 10%.

A distância entre 14% e 10% é de 4 pontos percentuais.

Escrevemos esse erro como 4 p.p.

O MAE é a média dessas distâncias para todos os pacientes do teste.

### Explicação para a fala

p.p. é a abreviação de pontos percentuais. Usamos essa unidade quando calculamos a diferença entre dois percentuais. Exemplo hipotético: se a pessoa pesava 100 kg e perdeu 14 kg, perdeu 14% do peso inicial. Se o modelo estimou 10%, a diferença absoluta é 4 pontos percentuais. Se o peso inicial fosse outro, 14 kg não corresponderiam necessariamente a 14%. No nosso trabalho o alvo é o percentual e não a perda em kg. Para calcular o MAE, tiramos a distância de cada previsão ao percentual real, sem considerar o sinal, somamos essas distâncias e dividimos pelo número de pacientes. O MAE da floresta no teste foi aproximadamente 5,43 p.p. Alguns erros foram menores e outros maiores. Esse número não é uma taxa de erros, e não se pode calcular uma taxa de acertos subtraindo-o de 100. Fonte: definição das métricas e exemplo didático hipotético.

## Slide 5

A maioria das perdas é pequena

Amostra completa

4,54% de perda média

2,40% de perda mediana

51 pacientes sem perda

37,8% da amostra

No treino, o máximo foi 23,59%. Valores extremos foram mantidos.

05

### Explicação para a fala

O gráfico usa somente os 108 pacientes do treino. Faixas de 5 pontos percentuais, com frequências 73,18,10,4,3. A concentração em valores baixos e a cauda à direita ajudam a explicar por que a média supera a mediana. A mediana é o valor central após ordenar os registros. Ausência de perda registrada não significa ausência de câncer ou garantia de bom estado nutricional. Fonte: banco de Viana et al. (2020) e divisão do notebook.

## Slide 6

Dicionário do banco

Coluna

Como interpretar

Age

Idade em anos

Sex

1 = feminino; 2 = masculino

tumor_location

1 = GI superior; 2 = GI inferior

tumor_location

3 = glândulas anexas; 6 = outros

Sintomas

1 = sim; 2 = não

Cada linha representa um paciente. Os códigos não são medidas.

06

### Explicação para a fala

GI significa gastrointestinal. Glândulas anexas agrupam fígado, pâncreas e vias biliares, conforme o artigo. O código 6 não significa tumor seis vezes maior, nem maior gravidade. ID é um identificador e não uma característica explicativa. Fonte: dicionárioSAV publicado com Viana et al.2020.

## Slide 7

Quais informações entram no modelo?

Tipo

Variáveis

Quantitativa

Idade

Categóricas

Sexo e localização do tumor

Sintomas (12)

Apetite, náusea, dor e outros

Preparação

15 variáveis resultam em 17 colunas

Fora do modelo

ID, desfechos e escores com perda de peso

Categorias viraram indicadores de 0 e 1, conforme a orientação do professor.

07

### Explicação para a fala

Os 12 sintomas são falta de apetite, náusea, constipação, feridas na boca, alteração do paladar, incômodo com odores, saciedade precoce, vômito, diarreia, boca seca, dificuldade para engolir e dor. Foram 15 variáveis originais: idade+sexo+tumor+12 sintomas. Após codificação: idade 1+sexo 1+tumor 3+sintomas 12=17 colunas. Os escores nutricionais que incorporam a própria resposta foram excluídos para evitar vazamento. Peso atual e IMC também ficaram fora da seleção conceitual. Os códigos estão explicados nos slides 9 e 10.

## Slide 8

Por que não usar todas as 44 variáveis?

ID identifica a pessoa, mas não explica a perda.

Escores podem conter a própria resposta.

Desfechos posteriores não pertencem à avaliação inicial.

Escolhemos 15 variáveis por critérios conceituais,

sem selecionar pelo resultado no teste.

Incluir mais colunas pode introduzir vazamento ou ruído.

08

### Explicação para a fala

Vazamento de informação ocorre quando o ajuste recebe uma informação que não estaria disponível no uso pretendido ou que incorpora a própria resposta. Classificação da perda de peso é uma transformação direta deweight_loss. Escores comoASG/SGAincorporam componentes relacionados ao peso perdido. Tempo de internação e óbito são desfechos posteriores ao momento de avaliação nutricional. PesoatualeIMCtambém ficaram fora da proposta; não afirmamos que são vazamento direto, apenas que não foram selecionados. Não usar rótulo de perda como preditor da perda.

## Slide 9

Como ler os indicadores dos sintomas

No banco original

Significado

Na coluna absence_appetite_2.0

1

Tem falta de apetite

0

2

Não tem falta de apetite

1

A coluna representa a AUSÊNCIA do sintoma, porque “sim” é a referência.

09

### Explicação para a fala

É uma escolha do codificador utilizado: drop='first' omite a categoria 1. Portanto, a coluna 2.0 recebe 1 quando o código original era 2, isto é, ausência do sintoma. Isso é matematicamente válido. O mesmo raciocínio vale para náusea e demais sintomas. EmSex_2.0,1 significa masculino e 0 feminino. Importante:0 nessa nova coluna não é dado ausente. O zero representa a categoria de referência. Se o professor perguntar por que não usar presença=1, explicar que seria outra codificação possível, mas mantivemos o procedimento aplicado sem alterar depois do teste.

## Slide 10

Localização do tumor em três indicadores

Categoria original

GI inferior

Glândulas

Outros

GI superior

0

0

0

GI inferior

1

0

0

Glândulas anexas

0

1

0

Outros

0

0

1

Quatro categorias precisam de três indicadores com uma referência.

10

### Explicação para a fala

GI superior é a categoria de referência. Quando os três indicadores são zero, o paciente está no grupoGI superior, não significa que falta localização. A localização original tinha quatro categorias. OOneHotEncoder(drop='first') transforma em três colunas. Assim: idade 1+sexo 1+localização 3+sintomas 12=17. Essa transformação impede que os números sejam lidos como uma escala contínua. Fonte: dicionário e notebook.

## Slide 11

Como separamos aprender de avaliar?

Etapa

Pacientes e finalidade

Treino

108 pacientes para aprender as relações

Validação cruzada

5 partes dentro do treino para escolher ajustes

Teste

27 pacientes reservados para avaliar

Reprodutibilidade

Semente 42 mantém a mesma divisão

Proteção

Preparação refeita dentro de cada parte

Depois de observar o teste, não mudamos a divisão nem os ajustes.

11

### Explicação para a fala

Treino é a parte usada para ajustar. Validação cruzada divide os 108 em cinco grupos e alterna o grupo usado para validar. Os outros quatro servem para ajustar em cada rodada. A transformação das categorias e a padronização do Lasso são aprendidas apenas com cada parte de ajuste. Depois da escolha, cada modelo é ajustado aos 108 e avaliado nos 27. A resposta do teste não participa do fit. Conferência descritiva inicial do banco não foi utilizada para selecionar ajustes. Fonte: notebook e documentação Pipeline/GridSearchCV, https://scikit-learn.org/stable/.

## Slide 12

O que significam fit, predict e pipeline?

Comando ou etapa

O que faz

fit

Aprende com os dados de treino

predict

Estima a resposta usando o modelo ajustado

Pipeline

Encadeia preparação e modelo

GridSearchCV

Compara combinações de ajustes por validação

random_state = 42

Permite repetir a mesma aleatoriedade

A preparação aprende com o treino e é aplicada ao teste.

12

### Explicação para a fala

NoLasso, oPipelineencadeiaOneHotEncoder,StandardScaler eLasso. Na floresta, codificação eRandomForestRegressor. GridSearchCVusa cinco partes para avaliar cada combinação. Depois refaz o ajuste da melhor configuração nos 108 pacientes, porrefit=Truepadrão. Predictnos 27 pacientes aplica as transformações já aprendidas. Random_state 42 é uma escolha fixa para reprodução, não tem significado clínico. Fonte: código do notebook e https://scikit-learn.org/stable/.

## Slide 13

Dois modelos e uma referência

Método

Como produz a estimativa

Lasso

Equação linear com penalização dos coeficientes

Floresta aleatória

Média das previsões de 300 árvores

Referência

Sempre prevê a mediana do treino: 2,675%

A referência permite verificar se a complexidade trouxe algum ganho.

13

### Explicação para a fala

Lasso é uma regressão linear que reduz coeficientes, podendo zerar alguns. O alpha escolhido foi 0,43444. Todos os 17 preditores foram padronizados dentro do pipeline. Floresta é um conjunto de árvores: cada uma faz divisões dos pacientes conforme os preditores. O resultado é a média. Ajustes:300 árvores, mínimo 3 pacientes/folha, max_features 0,7 e sem limite explícito de profundidade. A referência não recebe características para produzir estimativas diferentes: usa o valor constante da mediana do treino. Fontes: Tibshirani 1996, doi:10.1111/j.2517-6161.1996.tb 02080.x; Breiman 2001, doi:10.1023/A:1010933404324.

## Slide 14

Média e mediana não são iguais

Exemplo hipotético ordenado: 0, 0, 2, 4, 14

Média = (0 + 0 + 2 + 4 + 14) ÷ 5 = 4

Mediana = valor central = 2

O valor alto aumenta a média mais do que a mediana.

Na base completa: média 4,54% e mediana 2,40%.

14

### Explicação para a fala

A média soma todos os valores e divide pelo número de registros. A mediana é o valor central da lista ordenada. Quando a quantidade é par, é a média dos dois centrais. A mediana do treino é 2,675%, arredondada para 2,68%. Esse único valor vira a previsão da referência para cada paciente no teste. A mediana é adequada como referência paraMAE porque minimiza a soma de erros absolutos no treino. Exemplo 0,0,2,4,14 é didático, não dados da amostra.

## Slide 15

Lasso: o que a penalização faz?

O modelo combina as entradas em uma equação linear.

A penalização reduz os coeficientes.

Alguns podem chegar a zero.

Alpha controla a intensidade dessa redução.

Selecionamos alpha = 0,43444 dentro do treino.

Padronizamos os preditores para controlar diferenças de escala.

15

### Explicação para a fala

Coeficiente é o peso de uma variável na equação. Penalização é um custo adicional para coeficientes grandes. Alpha pequeno permite menos redução; alpha grande aplica mais redução. Não é porcentagem, probabilidade, acurácia nem número de variáveis. A padronização usa média e desvio-padrão do treino de cada parte daCV. Na nossa pipeline, foi aplicada a todas as 17 colunas, inclusive indicadores. Não apresentamos coeficientes específicos ou afirmamos quantos zeraram, pois isso não foi analisado no relatório. Fonte: Tibshirani 1996 e notebook.

## Slide 16

Floresta: como várias árvores estimam?

Cada árvore divide pacientes conforme os preditores.

A folha produz uma estimativa a partir do treino.

Exemplo hipotético de três árvores:

2%, 4% e 6% → média de 4%

Nosso modelo combina 300 árvores.

Mais árvores não garantem melhor previsão para esta amostra.

16

### Explicação para a fala

As árvores recebem amostras com reposição do treino. Nas divisões, a floresta usa subconjuntos aleatórios de preditores. Em cada folha de uma árvore de regressão com critério padrão de erro quadrático, a previsão é a média das respostas dos pacientes de treino naquela folha. A floresta calcula a média das previsões das árvores. Os números 2,4,6 são exemplo inventado. Nosso min_samples_leaf 3 significa que folhas precisam conter pelo menos 3 amostras segundo o ajuste. Não confundir com 3 pacientes previstos ou 3 árvores. Fonte: Breiman 2001 e documentação scikit-learn.

## Slide 17

Ajustes escolhidos na validação

Método

Configuração selecionada

Lasso

alpha ≈ 0,43444

Floresta: árvores

300

Floresta: profundidade

Sem limite explícito

Floresta: folha mínima

3 amostras

Floresta: preditores

Fração 0,7 em cada divisão

Escolhemos os ajustes pelo menor MAE na validação interna.

17

### Explicação para a fala

O grid doLassoavaliou 30 alphas logaritmicamente espaçados entre 0,001 e 31,62. A floresta avaliou 3 profundidades× 2 mínimosfolha× 2 fraçõespreditores=12 combinações. O número de árvores 300 foi fixo, não selecionado por grid. ProfundidadeNonepermite crescer até os outros critérios de parada. O mínimo por folha ajuda a limitar árvores excessivamente específicas. A fração 0,7 é transformada em quantidade inteira pela implementação. Não corresponde a 70%dos pacientes. Fonte: notebook.

## Slide 18

Como medimos o tamanho do erro?

Métrica

Em linguagem simples

Melhor direção

MAE

Erro absoluto médio

Menor

RMSE

Pesa mais os erros grandes

Menor

R²

Compara erros com a média do teste

Maior

Exemplo: real 10%, estimado 5% = erro de 5 pontos percentuais.

18

### Explicação para a fala

Leia MAE como as letras M,A,E. Não é uma porcentagem de acertos. Exemplo simples: se o paciente perdeu 10% e estimamos 5%, erramos 5 pontos percentuais. MAE calcula a média desses erros sem sinal. RMSE eleva os erros ao quadrado, tira a média e depois a raiz, de modo que erros grandes pesam mais. R² usa a soma dos erros quadráticos comparada à soma dos desvios em torno da média do próprio teste. Pode ser negativo. Não confundir essa referência matemática do R² com o nosso modelo constante de mediana. Há exemplos completos nos slides 16 a 18. Fonte: scikit-learn, documentação das métricas de regressão.

## Slide 19

MAE: exemplo calculado passo a passo

Paciente hipotético

Perda real

Estimativa

Erro absoluto

A

0%

2%

2 p.p.

B

5%

4%

1 p.p.

C

10%

7%

3 p.p.

MAE = (2 + 1 + 3) ÷ 3 = 2 pontos percentuais

19

### Explicação para a fala

Exemplo didático inventado, não são pacientes do banco. Primeiro subtraímos previsto de observado:0−2=−2,5−4=1,10−7=3. Como interessa o tamanho do erro, tomamos valor absoluto:2,1,3. Somamos 6 e dividimos por 3 pacientes. MAE=2 p.p. No teste real, MAE da referência 5,375, floresta 5,429, Lasso 5,619. Não interpretarMAE como porcentagem de acertos. A sigla pode ser lida letra por letra: M,A,E.

## Slide 20

RMSE: por que erros grandes pesam mais?

Usando os mesmos erros hipotéticos: 2, 1 e 3 p.p.

1. Elevar ao quadrado: 4, 1 e 9

2. Calcular a média: (4 + 1 + 9) ÷ 3 = 4,67

3. Tirar a raiz: √4,67 ≈ 2,16 p.p.

Um erro de 10 contribui com 100 antes da raiz. Um erro de 2 contribui com 4.

20

### Explicação para a fala

Exemplo didático inventado. RMSE é a raiz do erro quadrático médio. O quadrado dá maior peso aos erros grandes. A raiz faz a unidade voltar a pontos percentuais. No exemplo,MAE 2 eRMSE 2,16. No teste real, a floresta teveRMSE 9,356, menor que os 10,200 da referência. Ao mesmo tempo, seuMAE foi maior. Isso é possível porque as métricas priorizam aspectos diferentes dos erros. Não concluir que uma das métricas está errada.

## Slide 21

R²: uma comparação com a média

R² = 1 − (soma dos erros² do modelo ÷ soma dos desvios² da média)

1: estimativas perfeitas

0: mesmo erro quadrático de usar a média do teste

Negativo: erro maior que essa comparação

Floresta: R² = 0,100. Isso não significa 10% de acertos.

21

### Explicação para a fala

O R² do teste pode ser negativo. Ele usa a média das respostas do próprio teste apenas para calcular a referência matemática, não para treinar o modelo. SeSSE do modelo=90 eSST=100, entãoR²=1−90/100=0,10. Isso equivale a redução 10%da soma de erros quadráticos em relação à previsão constante pela média desse conjunto. Esses 90 e 100 são exemplo inventado. Nosso DummyRegressor é diferente: aprende mediana no treino. Por isso, não esperar queR² dele seja 0. Valores reais: referência−0,069; floresta 0,100; Lasso 0,011.

## Slide 22

Validação interna e teste final

Modelo

MAE da validação

MAE do teste

Referência

3,849 p.p.

5,375 p.p.

Floresta

3,838 p.p.

5,429 p.p.

Lasso

3,979 p.p.

5,619 p.p.

A diferença interna entre floresta e referência foi só 0,011 p.p.

22

### Explicação para a fala

Os valores da validação são médias das cinco partes. ParaLasso e floresta, são os melhores escores após pesquisar ajustes e podem estar otimistas. Não equivalem a teste externo. A referência também foi avaliada em cinco partes, mas sem busca de hiperparâmetros. No teste, os erros aumentaram. Possíveis razões são composição da amostra, perdas altas e limitações dos preditores, mas não calculamos uma decomposição dessas causas. Não mudar a semente buscando um resultado melhor. Fonte: resultados do notebook.

## Slide 23

Os resultados dependem da métrica

Modelo

MAE (p.p.)

RMSE (p.p.)

R²

Referência

5,375

10,200

−0,069

Floresta

5,429

9,356

0,100

Lasso

5,619

9,810

0,011

Referência: menor MAE. Floresta: menor RMSE, sem vantagem geral.

23

### Explicação para a fala

Esta é a avaliação nos 27 pacientes reservados. O critério de escolha dos ajustes foi MAE. A floresta não superou a mediana nessa métrica final:5,429 contra 5,375 p.p. A floresta teve menor RMSE e R²0,100, ainda modesto. Não escolhemos só uma métrica que favoreça um método. Na validação interna, a floresta teve 3,838 e a mediana 3,849: diferença mínima 0,011 p.p. Os escores internos serviram para ajustar e podem estar otimistas após seleção. Não calculamos teste formal de diferenças nem intervalos. Fonte: saídas originais do Colab.

## Slide 24

Por que os maiores casos foram difíceis?

Perda real

Lasso

Floresta

45,94%

4,68%

5,42%

22,46%

5,11%

8,03%

19,76%

4,68%

7,09%

O maior valor do teste supera o máximo de 23,59% visto no treino.

24

### Explicação para a fala

Para 45,94%, o erro absoluto doLassoé 41,26 p.p.e o da floresta 40,52 p.p. Ambos subestimaram. Uma floresta de regressão faz médias dos valores das folhas e não extrapola a resposta para acima do maior valor de treino, no procedimento padrão utilizado. Isso restringe o tratamento desse extremo. O Lasso pode extrapolar pela forma linear, mas nesse caso não produziu uma estimativa alta. Não concluímos que o valor 45,94%éerro; foi mantido como publicado. Não estamos dizendo que esse único paciente explica toda a métrica. Fonte: resultados originais.

## Slide 25

O que podemos concluir e o que falta?

Pergunta

Resposta defensável

A floresta foi a melhor?

Só no RMSE e R² desta divisão

O Lasso falhou como método?

Não; teve desempenho limitado nesta análise

Sintomas causam emagrecimento?

O estudo não permite concluir causalidade

Serve para uso clínico?

Não houve validação suficiente para isso

Próximo estudo

Maior amostra, evolução temporal e outros centros

Não demonstramos diferenças significativas nem validação externa.

25

### Explicação para a fala

O teste tem apenas 27 pacientes. Um único hospital e pacientes cirúrgicos limitam generalização. Não há intervalo de confiança calculado, comparação estatística formal ou avaliação em outro serviço. Não apresentar nenhuma diferença como estatisticamente significativa. O resultado negativo não invalida o trabalho: ele responde honestamente à pergunta sobre capacidade preditiva do procedimento adotado. Associaçãoestatística, desempenho preditivo e causalidade são conceitos diferentes.

## Slide 26

Conclusão: desempenho limitado

Testamos se idade, sexo, localização do tumor e sintomas ajudavam a estimar a perda de peso.

Nos 27 pacientes do teste, usar essas informações não reduziu o erro absoluto médio em relação a estimar 2,68% para todos.

Os modelos subestimaram principalmente as maiores perdas. A floresta teve o menor RMSE, mas não foi melhor em todas as medidas.

Conclusão: a capacidade de estimar a perda individual foi limitada nesta análise.

Não demonstramos vantagem consistente sobre a referência simples nem identificamos causas da perda de peso.

26

### Explicação para a fala

O objetivo foi testar a capacidade de estimar uma quantidade. Treinamos os modelos com 108 pacientes e avaliamos em 27 que ficaram reservados. A referência sempre estimava a mediana de treino, 2,675%, exibida como 2,68%. No teste, o MAE foi 5,375 pontos percentuais para a referência, 5,429 para a floresta e 5,619 para o Lasso. Isso significa que os modelos que usaram as características dos pacientes não reduziram o erro absoluto médio em relação à resposta constante. A floresta apresentou menor RMSE, que dá mais peso a erros grandes, por isso a comparação depende da medida escolhida. Ambos subestimaram as maiores perdas. Não contamos acertos e erros como numa classificação e não calculamos uma porcentagem de acertos. O resultado mostra uma limitação do procedimento estudado. Não prova que sintomas sejam irrelevantes nem identifica causas. Se o professor perguntar para que os métodos serviram: serviram para avaliar se essas informações permitiam estimativas melhores que uma estratégia simples. Nesta amostra, não houve vantagem consistente. Limitações: amostra pequena, um único hospital e ausência de validação externa. Os dados se referem à perda já ocorrida nos seis meses anteriores. Fonte: resultados do notebook da autora.

## Slide 27

Referências

Viana et al. (2020)

Base brasileira e artigo de origem

PLOS ONE 15(12): e0241305

Tibshirani (1996): regressão Lasso

Breiman (2001): florestas aleatórias

Documentação scikit-learn: modelos e validação

Banco individual disponível no material suplementar S1 Data.

27

### Explicação para a fala

Viana etal: https://doi.org/10.1371/journal.pone.0241305 . TibshiraniR: Regression Shrinkage and Selection via the Lasso, JRSSB 58(1),267–288,1996. https://doi.org/10.1111/j.2517-6161.1996.tb 02080.x . BreimanL: Random Forests,Machine Learning 45,5–32,2001. https://doi.org/10.1023/A:1010933404324 . https://scikit-learn.org/stable/ . Os exemplos hipotéticos são didáticos e não são registros de pacientes.
