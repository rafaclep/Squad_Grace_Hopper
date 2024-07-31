"""

Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.

"""

carrinho_de_compras = {}

carrinho_de_compras['banana'] = 5
carrinho_de_compras['ovo'] = 12
carrinho_de_compras['leite'] = 4
carrinho_de_compras['arroz'] = 1
carrinho_de_compras['feijao'] = 3

precos = {
    'banana': 3,
    'ovo': 6,
    'leite': 3.80,
    'arroz': 17,
    'feijao': 6.70
}

total = 0.0
for produto, quantidade in carrinho_de_compras.items():
    total += quantidade * precos[produto]

print(f'O total da compra do carrinho é: R$ {total:.2f}')
