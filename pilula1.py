def validarSenha(senha):
    if len(senha) < 8:
        return 'Senha Invalida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
            if c == ' ':
                return 'Senha Invalida, não pode conter espaço.'
        
            if c >= '0' and c <= '9':
                temNumero = True
            
            if c >= 'A' and c <= 'Z':
                temMaiuscula = True
        
    if not temNumero:
            return 'Senha invalida, não tem numero.'
    
    if not temMaiuscula:
            return 'Senha invalida'
    return 'Senha Válida.'

 #main
senha = input('Digite sua senha: ')           
print(validarSenha(senha))
 