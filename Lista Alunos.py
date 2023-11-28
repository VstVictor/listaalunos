 #lista dos alunos

nome= input('seu nome:')
curso= input('curso:')
nota= int(input('nota:'))

if (nota < 50 and curso == 'python') or (nota < 60 and curso == 'java'):
    print('reprovado')
else:
    print('aprovado')




