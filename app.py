import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
st.set_page_config(
    page_title="Página de Gráficos",
    page_icon="😂",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.subheader("Barra lateral")
st.sidebar.markdown("Nome: Gabriel Guimarães Rezende Teixeira")
st.sidebar.markdown("Turma: 3D2")
st.sidebar.markdown("N° de chamada: 13")

st.title("Gráficos")
st.caption("Está pagina contem gráficos da att6")

st.divider()

st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1:
    st.subheader("Gráfico de linha")
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de dispersão")
    df_dispersao = pd.read_csv("dados_dispersao.csv")

    fig, ax = plt.subplots(figsize=(8, 4))

    # Gráfico de dispersão + linha de regressão
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
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de boxplot")
    df_boxplot = pd.read_csv("dados_boxplot.csv")
    fig, ax = plt.subplots(figsize=(8, 4))
    # Boxplot por departamento
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
    st.pyplot(fig)


st.divider()
st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1: 
    st.subheader("Gráfico de Linhas")
    sns.set_theme(style="whitegrid")

    df_dados_linhas = pd.read_csv("dados_linhas.csv")

    df_dados_linhas["data"] = pd.to_datetime(df_dados_linhas["data"])

    fig, ax = plt.subplots(figsize=(10, 4))

    sns.lineplot(
        data=df_dados_linhas,
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de pizza")
    df_pizza = pd.read_csv("dados_pizza.csv")

    valores = df_pizza["faturamento"]
    categorias = df_pizza["canal_venda"]
    cores = sns.color_palette("Set2")

    fig, ax = plt.subplots(figsize=(6, 6))

    # Gráfico de Pizza / Rosca
    ax.pie(
        valores,
        labels=categorias,
        autopct="%1.1f%%",
        startangle=90,
        colors=cores,
        wedgeprops=dict(width=0.6, edgecolor="white")
    )

    ax.set_title("Distribuição do Faturamento por Canal de Venda", fontweight="bold")

    plt.tight_layout()
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de regressão")
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
    st.pyplot(fig)

st.divider()
st.write("Conteúdo abaixo da linha")
col1, col2, col3= st.columns([1,1,1])
with col1: 
    st.subheader("Gráfico de distribuição")
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
    st.pyplot(fig)

with col2:
    st.subheader("Gráfico de frequência")
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
    st.pyplot(fig)

with col3:
    st.subheader("Gráfico de heatmap")
    df_heatmap = pd.read_csv("dados_heatmap.csv")

    matriz_clientes = df_heatmap.pivot(
        index="dia_semana",
        columns="horario",
        values="movimento_clientes"
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    # Heatmap do movimento de clientes
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
    st.pyplot(fig)
