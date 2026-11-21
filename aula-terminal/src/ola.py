nome = input("Qual é o seu nome? ").strip()
tarefas = [{"Titulo" : "Comer nuggets", "Status" : "Feito"},
           {"Titulo": "Jogar LOL", "Status" : "Pendente"},
            {"Titulo" : "Dormir", "Status" : "Pendente"}
]
pendentes = 0



if not nome:
    print("Você não digitou nada.")
else:
    print(f"Olá, {nome}!")

try: 
    idade = int(input("Qual é a sua idade? "))
    print(f"Você tem {idade} anos.")
    if idade >= 18:
        print("Você é de maior")
    else:
        print("Você é de menor")
except ValueError:
    print("Por favor, digite uma idade válida.")


print("Suas Tarefas para hoje são")
for tarefa in tarefas:
    if tarefa.get("Status") == "Pendente":
        pendentes = pendentes + 1 
    print("-", tarefa["Titulo"], "Status:", tarefa["Status"])

print(f"Você tem {pendentes} tarefas pendentes")
