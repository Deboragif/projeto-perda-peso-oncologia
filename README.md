# Perda de peso em pacientes oncológicos do Hospital Universitário Cassiano Antônio Moraes

Autora: Débora de Cássia de Morais. Disciplina: Introdução à Ciência de Dados, UFPE. Professor: Jodavid Ferreira. Data: 23/11/2026.

## Conteúdo

- `Relatorio_Perda_de_Peso.pdf`: relatório com seis páginas.
- `Relatorio_Perda_de_Peso.qmd`: fonte Quarto com código R para as tabelas. PDF renderizado com Quarto, knitr/R e Typst.
- `Trabalho_ICD_Perda_de_Peso.ipynb`: notebook Python com os códigos e as saídas originais do Colab, organizado por seções. As saídas dos modelos não foram substituídas ou recalculadas para melhorar as métricas.
- `base_oncologia_original.sav`: arquivo original publicado pelos autores.
- `base_oncologia.csv`: conversão numérica sem rótulos aplicados.
- `treino.csv`, `teste.csv`, `divisao.csv`: registros e índices da divisão com semente 42.
- `dicionario.json`: descrições e rótulos originais das categorias.
- `resultados_cv.csv`, `resultados_teste.csv`: métricas transcritas das saídas do notebook, arredondadas a três casas decimais.
- `figuras/`: gráficos usados no relatório.
- `gerar_figura_exploratoria.py`: código da figura adicional de idade e localização do tumor.
- `Roteiro_Apresentacao.md`: conteúdo e explicações da sequência de slides.
- `Apresentacao_Perda_de_Peso.pptx`: slides em PowerPoint.

## Fonte dos dados

Viana ECR de M et al. (2020). Malnutrition and nutrition impact symptoms (NIS) in surgical patients with cancer. PLOS ONE 15(12):e0241305.

Artigo: https://doi.org/10.1371/journal.pone.0241305

Banco original S1 Data: https://journals.plos.org/plosone/article/file?type=supplementary&id=10.1371/journal.pone.0241305.s001

Coleta: março/2017 a outubro/2019, hospital público em Vitória, ES. Dados de 135 pacientes adultos cirúrgicos. Preservar a atribuição aos pesquisadores responsáveis pelo banco. A autora deste trabalho não realizou a coleta clínica.

## Reprodução

### Análise Python

Abra o notebook no Colab e execute as células na ordem. A primeira instala `pyreadstat` e baixa o banco público. O restante utiliza pandas, numpy, matplotlib e scikit-learn. As saídas armazenadas correspondem à execução original no Colab. O notebook original não registrou todas as versões dos pacotes, por isso pequenas diferenças numéricas entre versões podem ocorrer. Não modificar a divisão ou os ajustes para favorecer o resultado do teste.

### Relatório Quarto com R

Instale Quarto, R e os pacotes R `knitr` e `rmarkdown`. Na pasta do projeto:

```sh
quarto render Relatorio_Perda_de_Peso.qmd --to typst
```

O Quarto executa os blocos R e compila o PDF com Typst, sem exigir instalação LaTeX. As figuras da execução original são arquivos de entrada preservados. Para refazer a figura adicional, execute `gerar_figura_exploratoria.py` na pasta do projeto.

## Slides

A apresentação está em `Apresentacao_Perda_de_Peso.pptx`, com 27 slides em sequência única. As explicações de conceitos e os exemplos integram os assuntos correspondentes. As notas incluem explicações para a fala. O roteiro está em `Roteiro_Apresentacao.md`.

## Publicação no GitHub

Extraia o ZIP e envie os arquivos do projeto ao seu repositório. Não envie apenas o ZIP se quiser que o professor navegue pelo código. Inclua o PDF, o QMD, o notebook, os arquivos de dados, figuras e este README. Confira o acesso do professor ao repositório. Este pacote não foi publicado automaticamente no GitHub.

## Interpretação

Resposta: perda percentual registrada nos seis meses anteriores, sem previsão de evolução futura. Treino:108; teste:27. MAE final: referência5,375; floresta5,429; Lasso5,619 p.p. Floresta: RMSE9,356 p.p. e R²0,100. Não houve vantagem consistente sobre a referência. Não houve validação externa.

## Autoria

Débora de Cássia de Morais: 100% da participação discente. Trabalho individual, com definição da temática, execução das etapas no Colab e discussão dos resultados.
