tarefas = []

while True:
    print("\n1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Listar tarefas")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        tarefa = input("Digite a descrição da tarefa: ")
        tarefas.append({'tarefa': tarefa, 'concluida': False})
        print(f"Tarefa '{tarefa}' adicionada!")
    
    elif opcao == '2':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                status = "Concluída" if tarefa['concluida'] else "Pendente"
                print(f"{i+1}. {tarefa['tarefa']} - {status}")
            try:                        
                indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefas[indice]['concluida'] = True
                    print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída!")
                else:
                    print("Índice inválido!")
            except ValueError:
                print("Por favor, insira um número válido.")
    
    elif opcao == '3':
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("Tarefas:")
            for i, tarefa in enumerate(tarefas):
                status = "Concluída" if tarefa['concluida'] else "Pendente"
                print(f"{i+1}. {tarefa['tarefa']} - {status}")
    
    elif opcao == '4':
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")
