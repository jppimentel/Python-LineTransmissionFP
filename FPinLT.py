# -*- coding: utf-8 -*-


# Uma carga de 125MVA/215KV é alimentada através de uma LT média de 100 km cujos parâmetros valem ZL = 194<79º e YL = j4e-5 Siemens.
# Calcule o fator de potência

import math;
import numpy as np
import matplotlib.pyplot as plt


def pol2cart(rho, phi):
    x = rho * np.math.cos(phi)
    y = rho * np.math.sin(phi)
    return(x, y)

import cmath

#Dados
S = 125000000;            # VA
VR = 215000;              # V
L = 100;                  # km
yl = 0.00004j;            # ohm
zl = 37 + 190.4j;         #ohm 
Vs = [];
fp = []; 

Vs_pos = []
Vs_neg = []
fp_pos = []
fp_neg = []

IR=S/(VR*math.sqrt(3));


idx = 0; 

# Para variação da corrente IR de -0.9 atrado à 0.9 adiantado para o fp.
Vec = [x * 1 for x in range(2584, 15416)]
length = len(Vec) 
for i in range(length): 
    Vec[i] = Vec[i]/100
    idx = idx+ 1
    [X, Y] = pol2cart(IR, Vec[i]);
    Z = complex(X, Y)
    VS_rec = ((zl*yl/2)+1)*VR+zl*Z; 
    Vs.append(abs(VS_rec))
    fp.append(math.cos(np.angle(Z)))
    
    if math.cos(np.angle(Z)) > 0:
      fp_pos.append(math.cos(np.angle(Z)))
      Vs_pos.append(abs(VS_rec))
  

    if math.cos(np.angle(Z)) < 0:
      fp_neg.append(math.cos(np.angle(Z)))
      Vs_neg.append(abs(VS_rec)/100000)
    else: 
      fp_neg.append(np.nan)   
      Vs_neg.append(np.nan)    
 

plt.figure(1);
plt.plot(Vs_pos, fp_pos)
plt.xlabel('Vs')
plt.ylabel('FP Adiantado')
plt.title('Vs x FP Adiantado')

plt.figure(2);
plt.plot(Vs_neg, fp_neg)
plt.xlabel('Vs')
plt.ylabel('FP Atrasado')
plt.title('Vs x FP Atrasado')

# Considerando um custo de 50R$/kVAr, avaliar o custo do compensador
Vr = VR/math.sqrt(3);
Q3f = 3*Vr*IR*math.sin(math.radians(-25.85)); #Cálculo Reativo.
Q = Q3f*-1;
C = 50;  #$ por KVAr
Custo = int((Q*C)/1000) #$Custo do compensador
print("O custo será de " + str(Custo) + " reais")

