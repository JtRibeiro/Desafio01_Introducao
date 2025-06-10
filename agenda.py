contacts = []

def add_contact(contacts, name, phone, email):

  contact = {"nome": name, "telefone": phone, "email": email, "favorito": False }
  contacts.append(contact)
  print(f"Contato {name} foi adicionando com sucesso!")

def show_contact(contacts):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contacts, start=1):
    status = "✓" if contato["favorito"] else " "
    nome_contato = contato["nome"]
    print(f"{indice}. [{status}] {nome_contato}, {contato["telefone"]}, {contato["email"]}")

def add_or_remove_favorite(contacts, indice):
  indice_contact = int(indice) - 1
  contacts[indice_contact]["favorito"] == True
  print(f"Contato {indice_contact} marcada como favorito")
  return

while True:
  print("\nMenu do Gerenciador de Lista de contatos:")
  print("1. Adicionar contato")
  print("2. Ver lista de contatos cadastrados")
  print("3. Atualizar contato")
  print("4. Adicionar e/ou remover um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("5. Deletar tarefas completas")
  print("6. Sair")




  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    name = input("Informe o nome do contato: ")
    phone = input("Informe o telefone do contato: ")
    email = input("Informe o e-mail do contato: ")

    add_contact(contacts, name, phone, email)

  elif escolha == "2":
    show_contact(contacts)

  elif escolha == "3":
    print("3")

  elif escolha =="4":
    show_contact(contacts)
    indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
    add_or_remove_favorite(contacts, indice_tarefa)

  elif escolha == "5":
    print("5")

  elif escolha == "6":
    break;

print("Programa finalizado...");