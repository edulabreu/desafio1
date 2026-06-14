# 🧪 Desafio 1 — Automação E2E com Saucedemo

Este projeto automatiza um fluxo completo de e-commerce utilizando Selenium WebDriver em Python.

---

## 🎯 Objetivo

Simular um fluxo real de compra em uma aplicação web:

- Login
- Filtro de produtos
- Adição ao carrinho
- Checkout
- Finalização da compra
- Logout

---

## 🔗 Site utilizado

https://www.saucedemo.com/

---

## ⚙️ Fluxo automatizado

1. Acesso ao site
2. Login com usuário padrão
3. Aplicação de filtro:
   - Price (low to high)
4. Adição dos 3 primeiros produtos ao carrinho
5. Validação do badge do carrinho
6. Acesso ao carrinho
7. Checkout
8. Preenchimento de dados do usuário
9. Finalização da compra
10. Logout

---

## 🧠 Validações realizadas

- Login bem-sucedido (URL contém `/inventory`)
- Carrinho com 3 itens
- Finalização com sucesso (URL contém `/complete`)
- Logout retorna à tela inicial

---

## 🚀 Como executar

```bash
pip install -r requirements.txt
python desafio1.py
