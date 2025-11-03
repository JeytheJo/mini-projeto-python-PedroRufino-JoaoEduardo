categorias = ("Alimentos", "Limpeza", "Bebidas")
estoque = []
codigos_usados = set()

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código: "))
        if codigo in codigos_usados:
            print("Código já existe.")
            continue
        nome = input("Nome: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        for i, cat in enumerate(categorias):
            print(f"{i+1} - {cat}")
        c = int(input("Categoria: "))
        categoria = categorias[c-1] if 1 <= c <= len(categorias) else "Outros"
        produto = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade, "categoria": categoria}
        estoque.append(produto)
        codigos_usados.add(codigo)
        print("Produto cadastrado.")

    elif opcao == "2":
        if not estoque:
            print("Nenhum produto.")
        else:
            for p in estoque:
                print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: {p['preco']} | Qtd: {p['quantidade']} | Categoria: {p['categoria']}")

    elif opcao == "3":
        codigo = int(input("Código: "))
        for p in estoque:
            if p["codigo"] == codigo:
                print(p)
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        codigo = int(input("Código: "))
        for p in estoque:
            if p["codigo"] == codigo:
                nome = input("Novo nome (ou Enter): ")
                preco = input("Novo preço (ou Enter): ")
                quantidade = input("Nova quantidade (ou Enter): ")
                if nome: p["nome"] = nome
                if preco: p["preco"] = float(preco)
                if quantidade: p["quantidade"] = int(quantidade)
                print("Atualizado.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        codigo = int(input("Código: "))
        for p in estoque:
            if p["codigo"] == codigo:
                estoque.remove(p)
                codigos_usados.remove(codigo)
                print("Excluído.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")


#TESTE TESTE TESTE
