from cidade import Cidade
from pessoa import Pessoa
from categoria import Categoria
from produto import Produto
from pedido import Pedido

c1 = Cidade(1,"Cachoeira do Sul")
c2 = Cidade(2,"Campo bom")
p1 = Pessoa("João","993838045",c1)
p2 = Pessoa("Laura","298132813",c2)

product = Produto("Shampoo",5.50,"Higiene")
product2 = Produto("Anabolizante",90,"Academia")

cat1 = Categoria(1,"Bebidas")
cat2 = Categoria(2,"Alimentos")


prod1 = Produto("Coca-cola",7.85, cat1)
prod2 = Produto("Fanta",6.85, cat1)
prod2 = Produto("Arroz",3.85, cat2)

ped01 = Pedido("Rua nehita martins ramos 208",p1)
ped01.imprimir()

print(" Soma: " , ped01.addProduto(prod1))
# print("Nome da cidade da", p2.nome, ":", p2.cidade.nome) 
# p1.imprimir()


