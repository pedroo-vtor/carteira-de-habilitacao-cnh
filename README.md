# AV2 – Disciplina de Framework Back-End

## 📌 Descrição do Projeto
API simples de **carteira de habilitação**, desenvolvida em *Flask*, com dados persistentes.

---

## 🚀 Rotas da API

### ➕ Adicionar carteira (CREATE)
**POST**  
`http://localhost:5000/carteiras`

### 📄 Listar carteiras (READ)
**GET**  
`http://localhost:5000/carteiras`

### ✏️ Atualizar carteira (UPDATE)
**PUT**  
`http://localhost:5000/carteiras/<int:id_carteira>`

### ❌ Deletar carteira (DELETE)
**DELETE**  
`http://localhost:5000/carteiras/<int:id_carteira>`

---

## 📦 Exemplo de JSON para envio

```json
{
  "nome": "Eduardo",
  "sobrenome": "Almeida Fonseca",
  "cpf": "59182437066",
  "nacionalidade": "Brasileira",
  "categoria": "AB",
  "data_emissao": "2023-02-10",
  "validade": "2029-02-10"
}
```
---

## Aluno:

  - **Instituição:** Uninassau
  - **Aluno-Matricula:** Pedro Vitor Lins - 03346257
  - **Curso:** Ciências da Computação (4° Período)
  - **Disciplina:** Framework Back-End
  - **Código da turma:** EPI0790104NMA
  - **Professor:** Viviano de Sousa


