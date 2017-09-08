# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 16:44:37 2017

@author: ricardo
"""
from random import randint ## funcao para gerar valores aleatorios inteiros

#x = (2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,20,21,24,25)
x =  (6,8,15,21,26,31,35,43,44,49,60,70,75,79,80,83,89,1,3,10,17,22,24,25,27,28,29,30,33,36,37,38,39,40,41,48,50,52,55,56,59,61,62,66,69,73,76,77,82,86,90,95,97,4,11,12,13,23,47,68,74,84,93,5,2,14,19,42,45,53,57,65,72,85,87,88,94,96,99,00)
tamX = len(x)

def encontraValor(x,z,n):
    ''' funcao para verificar se valor encontrado é unico na estrutura z, afim de nao haver valores repetidos
    '''
    for i in range(0,n):
        if x == z[i]:
            return False
    return True

j = 0
while j < 50: ## quantidade de combinacoes 
    i = 0 
    z = ()
    while i < 50:         ## quantidade de valores por jogo
        q = x[randint(0,tamX-1)]
        if encontraValor(q,z,i) == True:
            z += (q,)
            i += 1
    print z
    j += 1
      

        
        
    
    

    


