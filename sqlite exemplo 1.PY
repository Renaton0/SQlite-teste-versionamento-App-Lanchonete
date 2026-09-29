import sqlite3
import os

# descobre exatamente onde este arquivo .py esta salvo no pc
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_banco = os.path.join(diretorio_atual, "sistema.db")

#conecta ao banco usando o caminho completo e seguro
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

#cria a tabela caso el
cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
        nome TEXT,
        preco REAL,
        quantidade INTEGER
    )
""")
conexao.commit()

# FUNÇÕES DO PRODUTO

def cadastrar_produto():
    print("\n--- CADASTRO DE NOVOS PRODUTOS ---")
    while True:
        try:
            nome = input("1. Digite o nome do produto (ou digite 'sair' para voltar)")

            if nome.lower() == 'sair':
                break

            if not nome:
                print("O nome não pode estar vazio. Tente novamente. \n")
                continue

            preco = float(input("2. Digite o preço (R$)"))
            quantidade = int(input("3. Digite a quantidade em estoque"))


            cursor.execute("INSERT INTO produtos VALUES (?, ?, ?)", (nome, preco, quantidade))
            conexao.commit()

            print(f" Sucesso! produto '{nome}' cadastrado. \n")

        except ValueError:
            print("ERRO: Digite valores numéricos validos para preço e quantidade.\n")                   


def consultar_produtos():
    print("\n--- CONSULTA DE PRODUTOS CADASTRADOS ---") 

    cursor.execute("SELECT * FROM produtos")
    itens = cursor.fetchall()

    if not itens:
        print("Nenhum produto cadastrado no banco de dados.\n")      
        return

    print("-" * 60)
    for linha in itens:
        print(f"Produto: {linha[0]:<20} /// Preço: R$ {linha[1]:>8.2f} /// Estoque: {linha[2]}")
        print("-" * 60 + "\n")

# -- Menu Principal
def main():
    while True:
        print("## lanchonete Ennius Muniz - Senac-DF")
        print("=== SISTEMA DE CONTROLE (SQLITE) ===")
        print("1. Cadastrar Novos Produtos")
        print("2. Consultar Produtos Salvos")
        print("3. Sair do sistema")

        opcao = input("Escolha uma opção (1 - 3): ").strip()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produtos()
        elif opcao == "3":
            print("Encerrando o sistema, até logo!")
            break
        else:
            print("Opção invalida, escolha apenas de 1 - 3.\n")

    conexao.close()

if __name__ == "__main__":
    main()

    