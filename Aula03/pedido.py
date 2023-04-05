class Pedido:
    def __init__(self,endereco,cliente) -> None:
        self.id = None
        self.end = endereco
        self.cliente = cliente
        self.produtos = []
        
    def addProduto(self,produto):
        self.produtos.append(produto)
        soma = 0 

        for prod in self.produtos:
            soma += prod.preco
        return soma
    def imprimir(self):
        print(" Pedido: ")
        print(" Endereço: ",self.end)
        print(" Cliente: ",self.cliente.nome)
        print(" Cidade do cliente: ",self.cliente.cidade.nome)
        print(" Produtos do pedido: ")
        if len(self.produtos) == 0:
            print(" Pedido Vazio! ")
        else:
            soma = 0
            for prod in self.produtos:
                soma += prod.preco
                print("Nome do Produto: ",prod.nome)
                print("Preço: ",prod.preco)
                print("Categoria: ",prod.cat.nome)
            print("Total: " , soma )