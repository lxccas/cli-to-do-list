# TodoCLI 📝

Uma simples **lista de tarefas (to-do list)** para o terminal, feito em Python!

## Funcionalidades ✨

- ✅ **Adicionar tarefas** com descrição.
- 📝 **Listar todas as tarefas** (concluídas e pendentes).
- ✔️ **Marcar tarefas como concluídas**.
- 💾 Salva automaticamente em um arquivo `todos.json`.
- 📱 Compatível com qualquer terminal.

## Como Usar 🛠️

### Comandos Disponíveis
| Comando    | Descrição                          | Exemplo                           |
|------------|------------------------------------|-----------------------------------|
| `add`      | Adiciona nova tarefa               | `python todo.py add "Ler livro"`  |
| `list`     | Lista todas as tarefas             | `python todo.py list`             |
| `complete` | Marca tarefa como concluída        | `python todo.py complete 1`       |
| `delete`   | Remove uma tarefa                  | `python todo.py delete 2`         |
| `help`     | Mostra ajuda                       | `python todo.py --help`           |

### Exemplo de Fluxo
```bash
# Adicionar tarefas
python todo.py add "Estudar Python"
python todo.py add "Fazer exercícios"

# Listar tarefas
python todo.py list
```
**Saída:**  
```
1. [ ] Estudar Python
2. [ ] Fazer exercícios
```

```bash
# Marcar tarefa como concluída
python todo.py complete 1

# Listar novamente
python todo.py list
```
**Saída:**  
```
1. [✓] Estudar Python
2. [ ] Fazer exercícios
```
