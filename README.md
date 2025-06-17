# 📒 Agenda de Contatos em Python

Este é um projeto simples de linha de comando que simula uma **agenda de contatos**. É possível adicionar, visualizar, atualizar, favoritar e excluir contatos.

## 🧰 Funcionalidades

- Adicionar novo contato
- Visualizar todos os contatos
- Atualizar informações de um contato
- Marcar ou desmarcar um contato como favorito
- Listar apenas os contatos favoritos
- Remover um contato da agenda

## 📌 Estrutura de um Contato

Cada contato é um dicionário com os seguintes campos:

```python
{
  "nome": "João",
  "telefone": "99999-9999",
  "email": "joao@email.com",
  "favorito": False
}
```

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado (versão 3.x).
2. Salve o código em um arquivo, por exemplo: `agenda.py`.
3. Execute o script via terminal:

```bash
python agenda.py
```

## 🖥️ Menu Interativo

Ao iniciar, você verá o seguinte menu:

```
Menu do Gerenciador de Lista de contatos:
1. Adicionar contato
2. Ver lista de contatos cadastrados
3. Atualizar contato
4. Adicionar e/ou remover um contato como favorito
5. Ver lista de contatos favoritos
6. Deletar um contato
7. Sair
```

Basta digitar o número da opção desejada e seguir as instruções do programa.

## 🛠️ Melhorias Futuras

- Persistência dos dados em arquivo (JSON ou CSV)
- Interface gráfica com Tkinter ou PyQt
- Validação de entradas (ex: e-mail e telefone)
- Exportação de contatos

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.