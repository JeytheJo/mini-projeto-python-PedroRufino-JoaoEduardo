# Estruturas de dados principais
alunos_e_notas = {}
nomes_cadastrados = set()

# --- Funções pra auxiliar

def calcular_media(notas):
    """Calcula a média aritmética de uma tupla de notas."""
    if not notas:
        return 0.0
    soma = 0.0
    for nota in notas:
        soma += nota
    return soma / len(notas)

def obter_notas_do_usuario():
    """Função para receber as notas de um aluno e retornar como tupla."""
    notas_temp = []
    print("\n--- Registro de Notas ---")
    while True:
        try:
            entrada = input("Digite uma nota (ou 'fim' para terminar): ").strip().lower()
            if entrada == 'fim':
                if not notas_temp:
                    print("Nenhuma nota registrada. Tente novamente.")
                    continue
                break
            
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                notas_temp.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")
    
    # Conforme solicitado, armazena em lista temporária e transforma em tupla
    return tuple(notas_temp)

# --- Funções do Menu ---

def cadastrar_aluno():
    """Requisito 1: Cadastra um novo aluno (matrícula e nome)."""
    print("\n--- 1. Cadastrar Aluno ---")
    while True:
        matricula = input("Digite a matrícula (Ex: 2024001): ").strip()
        if not matricula:
            print("A matrícula não pode ser vazia.")
            continue
        if matricula in alunos_e_notas:
            print(f"Matrícula '{matricula}' já cadastrada.")
            return

        nome = input("Digite o nome completo do aluno: ").strip().title()
        if not nome:
            print("O nome não pode ser vazio.")
            continue
        
        if nome in nomes_cadastrados:
            print(f"Aluno com o nome '{nome}' já está cadastrado no sistema.")
            
        nomes_cadastrados.add(nome)
        alunos_e_notas[matricula] = tuple()
        print(f"Aluno {nome} (Matrícula: {matricula}) cadastrado com sucesso!")
        break


def registrar_notas():
    print("\n--- 2. Registrar Notas ---")
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado. Cadastre um aluno primeiro.")
        return

    matricula = input("Digite a matrícula do aluno para registrar as notas: ").strip()
    
    if matricula not in alunos_e_notas:
        print(f"Matrícula '{matricula}' não encontrada.")
        return

    # Obtém as novas notas do usuário
    novas_notas = obter_notas_do_usuario()
    
    # Combina as notas existentes com as novas notas (assumindo que o professor pode adicionar mais)
    # Se a intenção for substituir as notas, use: alunos_e_notas[matricula] = novas_notas
    notas_existentes = alunos_e_notas[matricula]
    todas_as_notas = notas_existentes + novas_notas
    
    alunos_e_notas[matricula] = todas_as_notas
    print(f"Notas registradas para a matrícula {matricula}. Total de notas: {len(todas_as_notas)}.")


def listar_alunos_e_medias():
    """Requisito 3: Lista todos os alunos e suas respectivas médias."""
    print("\n--- 3. Listar Alunos e Médias ---")
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado.")
        return

    print(f"{'Matrícula':<12} | {'Nome (Estimado)':<20} | {'Notas Registradas':<20} | {'Média':>5}")
    print("-" * 70)
    
    # Loop para percorrer as estruturas e exibir os resultados
    for matricula, notas in alunos_e_notas.items():
        media = calcular_media(notas)
        
        nome_estimado = "Desconhecido"
        
        nome_exibicao = "N/A (Estrutura Limitada)"
        for nome in nomes_cadastrados:
            pass #Função para que não se faça nada (função nula dentro de um loop)

        print(f"{matricula:<12} | {f'{nomes_cadastrados}':<20} | {str(notas):<20} | {media:>5.2f}")


def buscar_aluno():
    """Requisito 4: Busca um aluno pela matrícula e mostra detalhes."""
    print("\n--- 4. Buscar Aluno ---")
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado.")
        return

    matricula = input("Digite a matrícula do aluno para buscar: ").strip()
    
    if matricula in alunos_e_notas:
        notas = alunos_e_notas[matricula]
        media = calcular_media(notas)
        
        print("\n--- Detalhes do Aluno ---")
        print(f"Matrícula: {matricula}")
        # Estimativa.
        print(f"Nome: {nomes_cadastrados}") 
        print(f"Notas Registradas: {notas}")
        print(f"Média Final: {media:.2f}")
    else:
        print(f"Matrícula '{matricula}' não encontrada.")


def mostrar_aprovados_e_reprovados():
    """Requisito 5: Mostra alunos aprovados (média >= 7) e reprovados (média < 7)."""
    print("\n--- 5. Aprovados e Reprovados ---")
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado.")
        return
    
    aprovados = []
    reprovados = []
    
    # Loop para percorrer as estruturas
    for matricula, notas in alunos_e_notas.items():
        media = calcular_media(notas)
        
        # Usaremos um *placeholder*(marcador temporário usado para indicar onde um valor vai ser inserido) para o nome para manter a compatibilidade
        nome_aluno = f"Aluno({matricula})" 
        
        if media >= 7.0:
            aprovados.append((nome_aluno, media))
        else:
            reprovados.append((nome_aluno, media))

    print("\n--- APROVADOS ---")
    if aprovados:
        for nome, media in aprovados:
            print(f"  - {nome}: Média {media:.2f}")
    else:
        print("  Nenhum aluno aprovado.")
        
    print("\n--- REPROVADOS ---")
    if reprovados:
        for nome, media in reprovados:
            print(f"  - {nome}: Média {media:.2f}")
    else:
        print("  Nenhum aluno reprovado.")


def gerar_relatorios():
    # Requisito 6: Apresenta o submenu de relatórios.
    while True:
        print("\n--- 6. Relatórios ---")
        print("  A - Alunos Cadastrados (Lista de Nomes)")
        print("  B - Médias Individuais Detalhadas")
        print("  C - Aprovados e Reprovados (Reutiliza lógica)")
        print("  0 - Voltar ao Menu Principal")
        
        escolha_relatorio = input("Escolha o relatório: ").upper().strip() # --> O .upper() faz com que todos os caracteres seja mauiúsculos, e a função .strip() faz com que os espaços em branco sejam eliminados
        
        if escolha_relatorio == 'A':
            print("\n--- Relatório: Alunos Cadastrados ---")
            if not nomes_cadastrados:
                print("Nenhuma nome cadastrado.")
                continue
            # Loop para exibir os nomes
            for i, nome in enumerate(sorted(list(nomes_cadastrados)), 1):
                print(f"  {i}. {nome}")
                
        elif escolha_relatorio == 'B':
            listar_alunos_e_medias() # Reutiliza a função existente
            
        elif escolha_relatorio == 'C':
            mostrar_aprovados_e_reprovados() # Reutiliza a função existente
            
        elif escolha_relatorio == '0':
            break
        else:
            print("Opção de relatório inválida.")

# --- Menu Principal ---

def menu_principal():
    # Loop principal do sistema.
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE NOTAS ESCOLAR")
        print("="*30)
        print('''
        1 - Cadastrar aluno
        2 - Registrar notas
        3 - Listar alunos e médias
        4 - Buscar aluno
        5 - Mostrar aprovados e reprovados
        6 - Relatórios
        0 - Sair
        ''')
        print("-" * 30)
        

        
        try:
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                cadastrar_aluno()
            elif opcao == '2':
                registrar_notas()
            elif opcao == '3':
                listar_alunos_e_medias()
            elif opcao == '4':
                buscar_aluno()
            elif opcao == '5':
                mostrar_aprovados_e_reprovados()
            elif opcao == '6':
                gerar_relatorios()
            elif opcao == '0':
                print("\nSistema encerrado. Até mais!")
                break
            else:
                print("\nOpção inválida. Por favor, escolha um número do menu.")
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    
    menu_principal()