# mini-projeto-python-PedroRufino-JoaoEduardo

## SISTEMA 1: CADASTRO DE PRODUTO

### O QUE SISTEMA FAZ:

-Cadastra novos produtos com código, nome, preço, quantidade e categoria

-Mostra a lista de produtos

-Busca um produto pelo código

-Atualiza as informações de um produto

-Exclui um produto

- tem a opção de sair do sistema

COMO FUNCIONA:

-Os produtos ficam guardados dentro de uma lista, e cada um tem um dicionário com as informações.
Tem também um set pra não deixar cadastrar o mesmo código duas vezes,
e uma tupla com as categorias dos produtos.

## Sistema 2 - Sistema de Controle de alunos e notas

### Começando pela criaçãode uma lista e um conjunto, onde serão guardadas as primeiras informações:
~~~
# Estruturas de dados principais
alunos_e_notas = {}
nomes_cadastrados = set()
~~~

### Após isso, a criação de algumas funções que servirão para alxiliar as proximas funcionalisdades que serão usados futuramente no código:

~~~
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
~~~

### Então, após criar as funções onde serão calculados a média de notas e a conversão dessas notas para uma tupla, entra-se nas funções de interação do menu, como:

- cadastrar o aluno
- registrar as notas do aluno
- listar notas e médias
- buscar alunos pela matrícula
- mostrar alunos aprovados e reprovados
- Gerar relatórios

### Após definir no que será nas funções de cada interação do menu principal, é criado uma "tela" mostrando opções de como será feita essas interações:

~~~
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
~~~

## Exemplos de uso do sistema:
### O uso do sistema pode ser facilmente usado por um professor de uma turma pequena (por exemplo, uma turma de reforço, um curso preparatório, ou uma oficina de programação com 15-25 alunos.
