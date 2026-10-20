# 📊 Revisão — Gráficos com Python

Este README é uma revisão dos principais gráficos trabalhados utilizando Python, Pandas, Matplotlib e Seaborn.

## 🛠️ Bibliotecas

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

### Pandas
Usado para ler e manipular arquivos CSV:

```python
df = pd.read_csv("arquivo.csv")
```

### Matplotlib
Usado para criar e configurar os gráficos:

```python
fig, ax = plt.subplots(figsize=(8, 4))
plt.show()
```

### Seaborn
Usado para criar gráficos de forma simples:

```python
sns.lineplot()
sns.barplot()
sns.scatterplot()
```

---

# 📈 1. Gráfico de Linhas

**Serve para:** evolução, tendências e mudanças ao longo do tempo.

Arquivo: `dados_linhas.csv`

Colunas principais: `data`, `vendas`, `loja`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

df_linhas = pd.read_csv("dados_linhas.csv")
df_linhas["data"] = pd.to_datetime(df_linhas["data"])

fig, ax = plt.subplots(figsize=(10, 4))

sns.lineplot(
    data=df_linhas,
    x="data",
    y="vendas",
    marker="o",
    color="#2563eb",
    linewidth=2,
    ax=ax
)

ax.set_title("Evolução das Vendas", fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Principais parâmetros:**
- `x` → eixo X
- `y` → eixo Y
- `marker="o"` → coloca pontos na linha

---

# 📊 2. Gráfico de Barras

**Serve para:** comparar categorias.

Arquivo: `dados_barras.csv`

Colunas: `categoria`, `regiao`, `vendas_medias`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_barras = pd.read_csv("dados_barras.csv")

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=df_barras,
    x="categoria",
    y="vendas_medias",
    hue="regiao",
    palette="Set2",
    errorbar=None,
    ax=ax
)

ax.set_title("Média de Vendas por Categoria e Região", fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas Médias")
ax.legend(title="Região")

plt.tight_layout()
plt.show()
```

`hue="regiao"` separa as barras de acordo com a região.

---

# 🔵 3. Gráfico de Dispersão + Regressão

**Serve para:** analisar a relação entre duas variáveis numéricas.

Arquivo: `dados_dispersao.csv`

Colunas: `altura_cm`, `peso_kg`, `sexo`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_dispersao = pd.read_csv("dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=df_dispersao,
    x="altura_cm",
    y="peso_kg",
    hue="sexo",
    alpha=0.8,
    ax=ax
)

sns.regplot(
    data=df_dispersao,
    x="altura_cm",
    y="peso_kg",
    scatter=False,
    color="gray",
    ax=ax
)

ax.set_title("Relação entre Altura e Peso", fontweight="bold")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")

plt.tight_layout()
plt.show()
```

- `scatterplot()` → cria as bolinhas.
- `regplot()` → cria a linha de tendência.
- Linha subindo → tendência positiva.
- Linha descendo → tendência negativa.

---

# 📦 4. Boxplot

**Serve para:** analisar distribuição, mediana, quartis e possíveis outliers.

Arquivo: `dados_boxplot.csv`

Colunas: `departamento`, `salario`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_boxplot = pd.read_csv("dados_boxplot.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.boxplot(
    data=df_boxplot,
    x="departamento",
    y="salario",
    palette="Pastel1",
    ax=ax
)

ax.set_title("Dispersão dos Salários por Departamento", fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")

plt.tight_layout()
plt.show()
```

A caixa mostra principalmente:
- mediana;
- Q1 e Q3;
- dispersão;
- possíveis outliers.

---

# 🔥 5. Heatmap

**Serve para:** visualizar valores em uma matriz usando cores.

Arquivo: `dados_heatmap.csv`

Colunas: `dia_semana`, `horario`, `movimento_clientes`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_heatmap = pd.read_csv("dados_heatmap.csv")

matriz_clientes = df_heatmap.pivot(
    index="dia_semana",
    columns="horario",
    values="movimento_clientes"
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.heatmap(
    matriz_clientes,
    annot=True,
    fmt=".0f",
    cmap="coolwarm",
    linewidths=.5,
    ax=ax
)

ax.set_title("Movimento de Clientes por Dia e Horário", fontweight="bold")
ax.set_xlabel("Horário")
ax.set_ylabel("Dia da Semana")

plt.tight_layout()
plt.show()
```

- `pivot()` transforma os dados em matriz.
- `annot=True` mostra os valores nas células.
- `cmap` define a escala de cores.

---

# 🥧 6. Gráfico de Pizza / Rosca

**Serve para:** mostrar proporções ou participação de cada categoria em um total.

Arquivo: `dados_pizza.csv`

Colunas: `canal_venda`, `faturamento`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_pizza = pd.read_csv("dados_pizza.csv")

valores = df_pizza["faturamento"]
categorias = df_pizza["canal_venda"]
cores = sns.color_palette("Set2")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    valores,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
    colors=cores,
    wedgeprops=dict(width=0.6, edgecolor="white")
)

ax.set_title(
    "Distribuição do Faturamento por Canal de Venda",
    fontweight="bold"
)

plt.tight_layout()
plt.show()
```

- `autopct` → mostra porcentagens.
- `wedgeprops` com `width` → transforma pizza em rosca.

---

# 📊 7. Gráfico de Frequência

Arquivo: `dados_frequencia.csv`

Colunas: `id_chamado`, `tipo_atendimento`.

Como `tipo_atendimento` é categórico, o melhor é usar `countplot()`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_frequencia = pd.read_csv("dados_frequencia.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.countplot(
    data=df_frequencia,
    x="tipo_atendimento",
    hue="tipo_atendimento",
    palette="Set2",
    legend=False,
    ax=ax
)

ax.set_title("Frequência dos Tipos de Atendimento", fontweight="bold")
ax.set_xlabel("Tipo de Atendimento")
ax.set_ylabel("Quantidade de Chamados")

plt.tight_layout()
plt.show()
```

`countplot()` conta quantas vezes cada categoria aparece.

### Barplot x Countplot

- `barplot()` → compara uma medida, como média.
- `countplot()` → conta ocorrências.

---

# 📉 8. Histograma + KDE

**Serve para:** visualizar a distribuição de uma variável numérica.

Arquivo mais adequado: `dados_distribuicao.csv`

Colunas: `cliente_id`, `idade`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_distribuicao = pd.read_csv("dados_distribuicao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=df_distribuicao,
    x="idade",
    bins=10,
    kde=True,
    color="#2563eb",
    ax=ax
)

ax.set_title("Distribuição da Idade dos Clientes", fontweight="bold")
ax.set_xlabel("Idade")
ax.set_ylabel("Quantidade de Clientes")

plt.tight_layout()
plt.show()
```

- `bins=10` → divide os valores em 10 intervalos.
- `kde=True` → adiciona a curva de distribuição suavizada.

---

# 📈 9. Regressão

Arquivo: `dados_regressao.csv`

Colunas: `renda_mensal`, `gasto_mensal`.

O melhor gráfico é um scatterplot com linha de regressão:

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df_regressao = pd.read_csv("dados_regressao.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.scatterplot(
    data=df_regressao,
    x="renda_mensal",
    y="gasto_mensal",
    alpha=0.8,
    ax=ax
)

sns.regplot(
    data=df_regressao,
    x="renda_mensal",
    y="gasto_mensal",
    scatter=False,
    color="gray",
    ax=ax
)

ax.set_title("Relação entre Renda e Gasto Mensal", fontweight="bold")
ax.set_xlabel("Renda Mensal (R$)")
ax.set_ylabel("Gasto Mensal (R$)")

plt.tight_layout()
plt.show()
```

---

# 🧠 Resumo para prova

| Gráfico | Usado para | Função |
|---|---|---|
| 📈 Linha | Evolução/tendência | `sns.lineplot()` |
| 📊 Barras | Comparação | `sns.barplot()` |
| 🔵 Dispersão | Relação entre variáveis | `sns.scatterplot()` |
| 📏 Regressão | Tendência | `sns.regplot()` |
| 📦 Boxplot | Distribuição/outliers | `sns.boxplot()` |
| 🔥 Heatmap | Matriz/intensidade | `sns.heatmap()` |
| 🥧 Pizza/Rosca | Proporção | `ax.pie()` |
| 📊 Frequência | Contagem | `sns.countplot()` |
| 📉 Histograma | Distribuição numérica | `sns.histplot()` |

---

# 🎯 Como escolher o gráfico?

**Evolução ao longo do tempo?**  
→ Gráfico de linhas.

**Comparar categorias?**  
→ Gráfico de barras.

**Contar categorias?**  
→ Countplot.

**Distribuição de números?**  
→ Histograma.

**Distribuição + outliers?**  
→ Boxplot.

**Relação entre duas variáveis numéricas?**  
→ Scatterplot.

**Relação + tendência?**  
→ Scatterplot + regressão.

**Porcentagem de um total?**  
→ Pizza/Rosca.

**Valores organizados em uma matriz?**  
→ Heatmap.

---

# 🔑 Comandos para decorar

```python
pd.read_csv("arquivo.csv")

fig, ax = plt.subplots(figsize=(8, 4))

sns.lineplot()
sns.barplot()
sns.scatterplot()
sns.regplot()
sns.boxplot()
sns.heatmap()
sns.countplot()
sns.histplot()

ax.set_title("Título")
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")

plt.tight_layout()
plt.show()
```

## Fórmula mental

```text
CSV
 ↓
pd.read_csv()
 ↓
DataFrame
 ↓
Escolher o gráfico
 ↓
Definir x e y
 ↓
Configurar título/eixos
 ↓
plt.show()
```
