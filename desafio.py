usuario_correto = 'Felipe123'
senha_correta = 'Outubro@17'

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite a sua senha:')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Parabens {usuario}, Acesso liberado com sucesso!!')
    else:
        print(f'Senha icorreta pra o usuário {usuario}')
else:
    print(f'usuário {usuario} não encontrado em nosso banco de dados );')
