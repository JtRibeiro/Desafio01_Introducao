contacts = []

print(len(contacts))

def add_contact(contacts, name, phone, email):
  contact = {"nome": name, "telefone": phone, "email": email, "favorito": False }
  contacts.append(contact)
  print(f"Contato {name} foi adicionando com sucesso!")

def show_contact(contacts):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contacts, start=1):
    status = "✓" if contato["favorito"] else ""
    nome_contato = contato["nome"]
    print(f"{indice}. [{status}] {nome_contato}, {contato['telefone']}, {contato['email']}, {contato['favorito']}")

def update_contact(contacts, id_contact, name=None, phone=None, email=None):
  id_ajustado = int(id_contact) -1

  if id_ajustado >=0 & id_ajustado < len(contacts):
    if name != "":
      contacts[id_ajustado]['nome'] = name

    if phone != "":
      contacts[id_ajustado]['telefone']= phone
    
    if email != "":
      contacts[id_ajustado]['email']= email
  
    print(f"Contato atualizado: nome: {name} - {phone} - {email}")
  else:
    print("Índice inválido")
  
  return
  
def add_or_remove_favorite(contacts, indice, opcao):
  indice_contact = int(indice) - 1
  if opcao == 1:
    contacts[indice_contact]["favorito"] = True
    print(f"Contato {indice_contact} marcada como favorito")
  elif opcao == 2:
    contacts[indice_contact]["favorito"] = False
    print(f"Contato {indice_contact} removido do favorito")
  else:
    print("Contato não listado nos favoritos")
  return

def show_contact_favorite(contacts):
  contacts_favorits = []
  for contact in contacts:
    if contact['favorito']:
      contacts_favorits.append(contact)

  if len(contacts_favorits) > 0:
      for contato in contacts_favorits:
        print(f"-> {contato['nome']}, {contato['telefone']}, {contato['email']}, {contato['favorito']}")
  else:
    print("Não tem nenhum contato favorito")

def delete_contact(contacts, id):
  id_delete = int(id) -1
  try:
    if id_delete >= 0 & id_delete < len(contacts):
      contacts.remove(contacts[id_delete])
  except:
    print("ID não encontrado!")

while True:
  print("\nMenu do Gerenciador de Lista de contatos:")
  print("1. Adicionar contato")
  print("2. Ver lista de contatos cadastrados")
  print("3. Atualizar contato")
  print("4. Adicionar e/ou remover um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair")


  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    name = input("Informe o nome do contato: ")
    phone = input("Informe o telefone do contato: ")
    email = input("Informe o e-mail do contato: ")

    add_contact(contacts, name, phone, email)

  elif escolha == "2":
    show_contact(contacts)

  elif escolha == "3":
    show_contact(contacts)
    id = int(input('Informe o id do contato a ser atualizado: '))
    name = input("Informe o nome do contato atualizado: ")
    phone = input("Informe o telefone do contato atualizado: ")
    email = input("Informe o e-mail do contato atualizado: ")
    update_contact(contacts, id, name, phone, email)

  elif escolha =="4":
    show_contact(contacts)
    try:
      opcao = int(input("Informe se quer marcar (1)/ desmarcar (2) favorito? "))
      while  opcao != 1 and opcao !=2 :
        opcao = int(input("Opção inválida, informe se quer marcar (1)/ desmarcar (2) favorito? "))

      if opcao == 1:
        indice_tarefa = int(input("Digite o id do contato que quer favoritar: "))
        add_or_remove_favorite(contacts, indice_tarefa, opcao)
      elif opcao == 2:
        indice_tarefa = int(input("Digite o id do contato que quer favoritar: "))
        add_or_remove_favorite(contacts, indice_tarefa, opcao)
      else:
        print("Deve digitar apenas número!")

    except:
      print("numero inválido")

  elif escolha == "5":
    show_contact_favorite(contacts)

  elif escolha == "6":
    if len(contacts) == 0:
      print("Lista esta vazia!")
      continue 
    
    show_contact(contacts)
    id = int(input('Informe o id do contato a ser deletado: '))
    delete_contact(contacts, id)

  elif escolha == "7":
    break;

print("Programa finalizado...");