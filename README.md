# 🚀 Projeto Exemplo - Sistema de Gerenciamento de Tarefas

![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Build](https://img.shields.io/badge/build-passing-success)

---

## 📘 Sobre o Projeto

Este projeto é um **Sistema de Gerenciamento de Tarefas** desenvolvido em **Python**, com foco em boas práticas de arquitetura e versionamento de código.  
Ele permite criar, listar, atualizar e excluir tarefas, armazenando os dados em um banco SQLite leve e eficiente.

---

## 🧩 Estrutura do Projeto

```
📦 task_manager
 ┣ 📂 src
 ┃ ┣ 📜 main.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 database.py
 ┃ ┗ 📜 utils.py
 ┣ 📂 tests
 ┃ ┗ 📜 test_main.py
 ┣ 📜 README.md
 ┣ 📜 requirements.txt
 ┗ 📜 LICENSE
```

---

## 🧠 Funcionalidades

- ✅ Criar novas tarefas
- 🕒 Acompanhar o status (pendente, em andamento, concluída)
- 🧹 Remover tarefas finalizadas
- 🔍 Buscar tarefas por nome ou data
- 💾 Persistência de dados local em SQLite

---

## 🧰 Tecnologias Utilizadas

| Tecnologia | Descrição |
|-------------|------------|
| **Python 3.11** | Linguagem principal do projeto |
| **SQLite** | Banco de dados leve e embutido |
| **PyTest** | Framework de testes automatizados |
| **Flake8** | Ferramenta de linting para manter o código limpo |

---

## 🗺️ Roadmap

| Etapa | Descrição | Status |
|-------|------------|--------|
| 1️⃣ | Estrutura base do projeto | ✅ Concluído |
| 2️⃣ | CRUD de tarefas | ✅ Concluído |
| 3️⃣ | Integração com interface gráfica (Tkinter) | 🔄 Em andamento |
| 4️⃣ | Testes automatizados | ⏳ Planejado |
| 5️⃣ | Publicação no PyPI | ⏳ Planejado |

---

## ⚙️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/usuario/task-manager.git

# Entre na pasta do projeto
cd task-manager

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Linux)
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python src/main.py
```

---

## 🧪 Testes

```bash
pytest tests/
```

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).  
Sinta-se livre para usar, modificar e distribuir este código.

---

## 💬 Contato

📧 **Autor:** João Silva  
🌐 [GitHub](https://github.com/usuario) | [LinkedIn](https://linkedin.com/in/usuario)

---

> Feito com ❤️ por João Silva - Estudo e prática de boas práticas em Python.
