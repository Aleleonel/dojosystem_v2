# DOJO SYSTEM V2

## Arquitetura
- Django 6
- SaaS Multiacademia
- Controle por academia
- Usuário vinculado à academia
- Controle de permissões:
  - MASTER
  - ADMIN
  - PROFESSOR

## Estrutura Templates
templates/
    base.html
    includes/
        navbar.html
        sidebar.html
    alunos/
    aulas/
    dashboard/
    financeiro/
    usuarios/
    registration/

## Regras Implementadas
- Sidebar dinâmica por perfil
- Usuário MASTER controla admins
- ADMIN controla professores
- PROFESSOR não acessa financeiro
- Avatar de usuário funcional
- Perfil editável

## Fluxo Git
main -> produção
develop -> integração
feature/* -> funcionalidades

## Próximas Etapas
- Dashboard dinâmico
- Relatórios
- Multiacademia avançado
- Planos SaaS
- Permissões avançadas