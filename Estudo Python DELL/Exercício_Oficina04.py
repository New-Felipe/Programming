lista_desejos = {"talher", "prato", "copos", "toalha", "cama", "mesa", "sofá", "decoração"}

loja1 = {"talher", "prato", "copos", "toalha"}
loja2 = {"prato", "copos", "cama", "mesa"}
loja3 = {"talher", "cama", "sofá"}
loja4 = {"sofá", "mesa", "toalha"}

lojas = [loja1, loja2, loja3, loja4]

produtos_oferecidos = set().union(*lojas)
print("1. Produtos oferecidos em ao menos uma loja:", produtos_oferecidos)

produtos_comuns = set(loja1)
for loja in lojas[1:]:
    produtos_comuns.intersection_update(loja)
print("2. Produtos oferecidos em todas as lojas:", produtos_comuns if produtos_comuns else "Nenhum")

produtos_nao_encontrados = lista_desejos - produtos_oferecidos
print("3. Produtos não encontrados em nenhuma loja:", produtos_nao_encontrados if produtos_nao_encontrados else "Nenhum")

print("\n4. Produtos exclusivos de cada loja:")
for i, loja in enumerate(lojas, 1):
    outras_lojas = [l for j, l in enumerate(lojas, 1) if j != i]
    exclusivos = loja - set().union(*outras_lojas)
    print(f"  Loja {i}: {exclusivos if exclusivos else 'Nenhum'}")

from itertools import combinations

max_cobertura = 0
melhor_combinacao = None

for loja_a, loja_b in combinations(lojas, 2):
    cobertura = len(loja_a.union(loja_b))
    if cobertura > max_cobertura:
        max_cobertura = cobertura
        melhor_combinacao = (loja_a, loja_b)

print("\n5. Quantidade máxima de presentes cobertos por duas lojas:", max_cobertura)
print("   (Combinação que cobre esses produtos):", melhor_combinacao)
