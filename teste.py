import pandas as pd
df = pd.read_excel("vendas.xlsx")
print(df.head())

df['Receita'] = df['Quantidade'] * df['Preço Unitário']
df.to_excel('vendas_analisadas.xlsx', index=False)
receita_total = df['Receita'].sum()
print(f"📈 Receita total: R${receita_total:.2f}")

# Produto mais vendido em quantidade
mais_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print("\n🔝 Produto mais vendido:")
print(mais_vendido)

# Produto que mais gerou receita
mais_lucrativo = df.groupby('Produto')['Receita'].sum().sort_values(ascending=False)
print("\n💰 Produto mais lucrativo:")
print(mais_lucrativo)

# Receita total por dia
vendas_por_dia = df.groupby('Data')['Receita'].sum()
print("\n📅 Receita por dia:")
print(vendas_por_dia)