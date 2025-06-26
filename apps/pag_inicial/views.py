from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.usuario.models import CustomUser, Cerimonialista, Cliente, Fornecedor

def auth_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')  # cerimonialista, fornecedor ou cliente
        action = request.POST.get('action')  # login ou register

        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if action == 'register':
            nome = request.POST.get('nome')
            telefone = request.POST.get('telefone')
            cpf_cnpj = request.POST.get('cpf_cnpj')
            categoria = request.POST.get('categoria')
            nome_empresa = request.POST.get('nome_empresa')

            # Verificar se já existe usuário com esse email
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado.')
                return redirect('pagina_inicial')

            # Criar usuário
            user = CustomUser.objects.create_user(
                username=email,  # usa o email como username
                email=email,
                password=senha,
                tipo=role
            )
            user.save()

            # Criar perfil específico
            if role == 'cerimonialista':
                Cerimonialista.objects.create(
                    usuario=user,
                    cpf_cnpj=cpf_cnpj,
                    empresa=nome
                )
            elif role == 'fornecedor':
                Fornecedor.objects.create(
                    usuario=user,
                    nome_empresa=nome_empresa,
                    cpf_cnpj=cpf_cnpj,
                    categoria=categoria
                )
            elif role == 'cliente':
                Cliente.objects.create(
                    usuario=user,
                    cpf=cpf_cnpj,
                    telefone=telefone
                )

            messages.success(request, 'Cadastro realizado com sucesso! Agora faça login para continuar.')
            # NÃO loga automaticamente após cadastro
            return redirect('pagina_inicial')

        elif action == 'login':
            user = authenticate(request, username=email, password=senha)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('meus_casamentos')
            else:
                messages.error(request, 'E-mail ou senha inválidos.')
                return redirect('pagina_inicial')

    # Para requisições GET ou outras, redireciona para a página inicial
    return redirect('pagina_inicial')


def pagina_inicial(request):
    return render(request, 'pag_inicial/index.html')


def meus_casamentos(request):
    return render(request, 'pag_inicial/meus_casamentos.html')
aaaaa