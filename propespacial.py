# Trabalho 1: Projeto de motor foguete # ------------------------------------------------- #
# Autores:      Enzo Filippo Centenaro da Silva
#               Bernardo Eckert Recktenvald
# Data:         11/05/2023
# Curso:        Engenharia Aeroespacial - CT, Universidade Federal de Santa Maria
# Disciplina:   FUNDAMENTOS DE PROPULSÃO AEROESPACIAL
# Professor:    Dr. Cesar Addis Valverde Salvador

# ----------------------------------------------------------------------------------------- #
# Bibliotecas necessárias # --------------------------------------------------------------- #

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# ----------------------------------------------------------------------------------------- #
# Parâmetros do programa # ---------------------------------------------------------------- #

np.seterr(divide='ignore', invalid='ignore')  #Ignorar divisões por zero
motores = []
motores_estagio1 = []
motores_estagio2 = []
motores_estagio3 = []
def marcadores(n_pontos):
  markers_on = np.add(np.sort((np.random.rand(1, 5)*(n_pontos)-1)[0])*0.3, np.linspace(1, n_pontos-1, 5)*0.7).astype(int)   #Define o número de marcadores nos gráficos por curva
  return markers_on

if not os.path.exists('figures'):
  os.makedirs('figures')

# ----------------------------------------------------------------------------------------- #
# Atmosfera # ----------------------------------------------------------------------------- #

class Atmosfera:

  def __init__(self, n_pontos, H_min, H_max):
    self.n_pontos = n_pontos
    self.H_min = H_min
    self.H_max = H_max
    self.T = np.zeros(self.n_pontos)
    self.P = np.zeros(self.n_pontos)
    self.rho = np.zeros(self.n_pontos)
    self.H = np.zeros(self.n_pontos)
    self.tabela = np.array([
      #H(m)      T(K)    P(atm)        rho(kg/m3)
      [-500, 291.4, 1.0610, 1.0490],
      [0, 288.2, 1.0000, 1.0000],
      [500, 284.9, 0.9421, 0.9529],
      [1000, 281.7, 0.8870, 0.9075],
      [1500, 278.4, 0.8345, 0.8638],
      [2000, 275.2, 0.7846, 0.8217],
      [2500, 271.9, 0.7372, 0.7812],
      [3000, 268.7, 0.6920, 0.7423],
      [3500, 265.4, 0.6492, 0.7048],
      [4000, 262.2, 0.6085, 0.6689],
      [4500, 258.9, 0.5700, 0.6343],
      [5000, 255.7, 0.5334, 0.6012],
      [6000, 249.2, 0.4660, 0.5389],
      [7000, 242.7, 0.4057, 0.4817],
      [8000, 236.2, 0.3519, 0.4292],
      [9000, 229.7, 0.3040, 0.3813],
      [10000, 223.3, 0.2615, 0.3376],
      [11000, 216.8, 0.2240, 0.2978],
      [12000, 216.7, 0.1915, 0.2546],
      [13000, 216.7, 0.1636, 0.2176],
      [14000, 216.7, 0.1399, 0.1860],
      [15000, 216.7, 0.1195, 0.1590],
      [16000, 216.7, 0.1022, 0.1359],
      [17000, 216.7, 0.08734, 0.1162],
      [18000, 216.7, 0.07466, 0.09930],
      [19000, 216.7, 0.06383, 0.08489],
      [20000, 216.7, 0.05457, 0.07258],
      [22000, 218.6, 0.03995, 0.05266],
      [24000, 220.6, 0.02933, 0.03832],
      [26000, 222.5, 0.02160, 0.02797],
      [28000, 224.5, 0.01595, 0.02047],
      [30000, 226.5, 0.01181, 0.01503],
      [40000, 250.4, 0.002834, 0.003262],
      [50000, 270.7, 0.0007874, 0.0008383],
      [60000, 255.8, 0.0002217, 0.0002497],
      [70000, 219.7, 0.00005448, 0.00007146],
      [80000, 180.7, 0.00001023, 0.00001632],
      [90000, 180.7, 0.000001622, 0.000002588]
    ])

  def calculo_propriedades(self):
    H_tabela = self.tabela[:, 0]  # m
    T_tabela = self.tabela[:, 1]  # K
    P_tabela = self.tabela[:, 2] * 101325  # Pa
    rho_tabela = self.tabela[:, 3] * 1.225  # kg/m3

    incremento_H = (self.H_max - self.H_min) / self.n_pontos
    for motor in range(self.n_pontos):
      self.H[motor] = motor * incremento_H + self.H_min             # Altitude
      self.T[motor] = np.interp(self.H[motor], H_tabela, T_tabela)  # Temperatura
      self.P[motor] = np.interp(self.H[motor], H_tabela, P_tabela)  # Pressão
      self.rho[motor] = np.interp(self.H[motor], H_tabela, rho_tabela)  # Densidade

  def plotar_atmosfera(self):
    plt.figure(figsize=[16, 9])

    plt.subplot(1, 3, 1)  #linha, coluna, número do plot
    plt.grid(visible=True)
    plt.title('Temperatura atmosférica')
    plt.plot(self.T, self.H/1e3, '-r')
    plt.xlabel('Temperatura [K]')
    plt.ylabel('Altitude [Km]')

    plt.subplot(1, 3, 2)
    plt.grid(visible=True)
    plt.title('Pressão atmosférica')
    plt.plot(self.P/1e3, self.H/1e3, '-b')
    plt.xlabel('Pressão [KPa]')
    plt.ylabel('Altitude [Km]')

    plt.subplot(1, 3, 3)
    plt.grid(visible=True)
    plt.title('Densidade atmosférica')
    plt.plot(self.rho, self.H/1e3, '-g')
    plt.xlabel('Densidade [kg/m³]')
    plt.ylabel('Altitude [Km]')

  
    plt.savefig(os.path.join('figures', 'atmosfera_' + str(self.H_min) + "_" + str(self.H_max) + '.pdf'), dpi=500)

# ----------------------------------------------------------------------------------------- #
# Motor Foguete # ------------------------------------------------------------------------- #

class MotorFoguete:

  def __init__(self, n_motores, epsilon, atmosfera, estagio, area_da_garganta, k, P1, n_pontos, cor, simbolo):
    self.nome = "n\u00b0 motores = " + str(n_motores) + ", \u03B5 = " + str(epsilon)
    self.n_motores = n_motores
    self.epsilon = epsilon
    self.atmosfera = atmosfera
    self.estagio = estagio
    self.area_da_garganta = area_da_garganta
    self.k = k
    self.P1 = P1
    self.n_pontos = n_pontos
    self.cor = cor
    self.simbolo = simbolo
    self.A2 = epsilon * self.area_da_garganta
    self.P2 = fsolve(self.funcao_epsilon, 1)
    self.F, self.F_acumulado = self.calculo_empuxo()
    self.H_min = self.atmosfera.H_min
    self.H_max = self.atmosfera.H_max
    self.salvar_motor()
    
  def salvar_motor(self):
    self.var = 'motor'+ str(self.n_motores) +'_estagio'+ str(self.estagio) +'_epsilon'+ str(self.epsilon)
    motores.append(self.var)
    match self.estagio:
      case 1:
        motores_estagio1.append(self.var)
      case 2:
        motores_estagio2.append(self.var)
      case 3:
        motores_estagio3.append(self.var)
    

  def funcao_epsilon(self, P2):
    return (((2 / (self.k + 1))**(1 / (self.k - 1))) * ((P2 / self.P1)**(-1 / self.k)) *
            ((((self.k + 1) / (self.k - 1)) *
              (1 - ((P2 / self.P1)**((self.k - 1) / self.k))))**(-1 / 2))) - self.epsilon

  def calculo_empuxo(self):
    coef_a = (2 * self.k**2) / (self.k - 1)
    coef_b = (2 / (self.k + 1))**((self.k + 1) / (self.k - 1))
    coef_c = (1 - (self.P2 / self.P1)**((self.k - 1) / self.k))
    F = self.n_motores*(self.area_da_garganta * self.P1 * np.sqrt(coef_a * coef_b * coef_c) + (self.P2 - self.atmosfera.P) * self.A2)
    F_acumulado = np.zeros(len(self.atmosfera.H))
    for i in range(len(self.atmosfera.H)):
      if i == 0:
        F_acumulado[i] = F[0]
      else:
        F_acumulado[i] = F_acumulado[i-1] + F[i]
    return F, F_acumulado

  def plotar_empuxo_por_altitude(self):
    if self.estagio == 1:
      self.linha = '-'
    elif self.estagio == 2:
      self.linha = '--'
    else:
      self.linha = ':'
    plt.plot(self.atmosfera.H/1e3,
             self.F,
             self.linha, color = self.cor, marker = self.simbolo,
             markevery=marcadores(self.n_pontos),
             label=self.nome)
    plt.legend(loc = 'lower right', bbox_to_anchor=(0.97, 0.07))
    plt.grid(visible=True)
    plt.xlabel("Altitude [km]")
    plt.ylabel("Empuxo [N]")

  def plotar_pressao_por_altitude(self):
    if self.estagio == 1:
      self.linha = '-'
    elif self.estagio == 2:
      self.linha = '--'
    else:
      self.linha = ':'
    vetor_P2 = np.ones(len(self.atmosfera.H))*self.P2
    plt.plot(self.atmosfera.H/1e3,
             vetor_P2/1e3,
             self.linha, color = self.cor, marker = self.simbolo,
             markevery=marcadores(self.n_pontos),
             label=self.nome)
    plt.legend(loc = 'lower right', bbox_to_anchor=(0.97, 0.07))
    plt.grid(visible=True)
    plt.xlabel("Altitude [km]")
    plt.ylabel("Pressão [kPa]")

def plotar_empuxo_por_altitude_dos_motores(motores):
  plt.figure(figsize=[16, 9])
  nome_estagio_grafico = str(motores[0].estagio)
  nome_estagio_arquivo = str(motores[0].estagio)
  i = 0
  for motor in motores:
    nome_estagio_motor = str(motores[i].estagio)
    if not nome_estagio_motor in nome_estagio_grafico:
      nome_estagio_grafico = nome_estagio_grafico + ', ' + nome_estagio_motor
      nome_estagio_arquivo = nome_estagio_arquivo + nome_estagio_motor
    match nome_estagio_motor:
      case '1':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = '-', color = 'k')
      case '2':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = '--', color = 'k')
      case '3':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = ':', color = 'k')
    motor.plotar_empuxo_por_altitude()
    i = i + 1
  if len(nome_estagio_grafico) > 1:
    plural_ou_singular = 's: '
  else:
    plural_ou_singular = ': '
  plt.title('Empuxo dos motores foguete estágio' + plural_ou_singular + nome_estagio_grafico)
  plt.savefig(os.path.join('figures', 'empuxo_estagio'+ nome_estagio_arquivo +'.pdf'), dpi=500)

def plotar_pressao_por_altitude_dos_motores(motores):
  plt.figure(figsize=[16, 9])
  nome_estagio_grafico = str(motores[0].estagio)
  nome_estagio_arquivo = str(motores[0].estagio)
  i = 0
  for motor in motores:
    nome_estagio_motor = str(motores[i].estagio)
    if not nome_estagio_motor in nome_estagio_grafico:
      nome_estagio_grafico = nome_estagio_grafico + ', ' + nome_estagio_motor
      nome_estagio_arquivo = nome_estagio_arquivo + nome_estagio_motor
    match nome_estagio_motor:
      case '1':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = '-', color = 'k')
      case '2':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = '--', color = 'k')
      case '3':
        plt.axvline(x = motores[i].H_min/1e3, linestyle = ':', color = 'k')
    motor.plotar_pressao_por_altitude()
    i = i + 1
  if len(nome_estagio_grafico) > 1:
    plural_ou_singular = 's: '
  else:
    plural_ou_singular = ': '
  plt.title('Pressão dos motores foguete estágio' + plural_ou_singular + nome_estagio_grafico)
  plt.savefig(os.path.join('figures', 'pressao_estagio'+ nome_estagio_arquivo +'.pdf'), dpi=500)

# ----------------------------------------------------------------------------------------- #
# Missao # -------------------------------------------------------------------------------- #

class Missao:
  def __init__(self, nome_missao, motor_estagio1, motor_estagio2, motor_estagio3, atmosfera, n_pontos):
    self.nome_missao = nome_missao
    self.estagio1_motor = motor_estagio1
    self.estagio2_motor = motor_estagio2
    self.estagio3_motor = motor_estagio3
    self.estagio1_H_min = motor_estagio1.H_min
    self.estagio1_H_max = motor_estagio1.H_max
    self.estagio2_H_min = motor_estagio2.H_min
    self.estagio2_H_max = motor_estagio2.H_max
    self.estagio3_H_min = motor_estagio3.H_min
    self.estagio3_H_max = motor_estagio3.H_max
    self.atmosfera = atmosfera
    self.n_pontos = n_pontos
    self.F_acumulado_max_estagio1 = np.max(motor_estagio1.F_acumulado)
    self.F_acumulado_max_estagio2 = np.max(motor_estagio2.F_acumulado)
    self.F_acumulado_max_estagio3 = np.max(motor_estagio3.F_acumulado)
    
  def plotar_empuxo_por_altitude(self, motor):
    if motor.estagio == 1:
      self.linha = '-'
    elif motor.estagio == 2:
      self.linha = '--'
    else:
      self.linha = ':'
    plt.plot(motor.atmosfera.H/1e3,
             motor.F,
             self.linha, color = motor.cor, marker = motor.simbolo,
             markevery=marcadores(self.n_pontos),
             label=motor.nome)

  def plotar_empuxo_acumulado(self, motor):
    if motor.estagio == 1:
      self.linha = '-'
      plt.plot(motor.atmosfera.H/1e3,
              motor.F_acumulado/1e6,
              self.linha, color = motor.cor, marker = motor.simbolo,
              markevery=marcadores(self.n_pontos),
              label=motor.nome)
    elif motor.estagio == 2:
      self.linha = '--'
      plt.plot(motor.atmosfera.H/1e3,
              (motor.F_acumulado + self.F_acumulado_max_estagio1)/1e6,
              self.linha, color = motor.cor, marker = motor.simbolo,
              markevery=marcadores(self.n_pontos),
              label=motor.nome)
    else:
      self.linha = ':'
      plt.plot(motor.atmosfera.H/1e3,
              (motor.F_acumulado + self.F_acumulado_max_estagio1 + self.F_acumulado_max_estagio2)/1e6,
              self.linha, color = motor.cor, marker = motor.simbolo,
              markevery=marcadores(self.n_pontos),
              label=motor.nome)

  def plotar_missao(self):
    plt.figure(figsize=[16, 9])
    plt.title(self.nome_missao)
    plt.axvline(x = self.estagio1_H_min/1e3, linestyle = '-', color = 'k')
    plt.axvline(x = self.estagio2_H_min/1e3, linestyle = '--', color = 'k')
    plt.axvline(x = self.estagio3_H_min/1e3, linestyle = ':', color = 'k')
    self.plotar_empuxo_por_altitude(self.estagio1_motor)
    self.plotar_empuxo_por_altitude(self.estagio2_motor)
    self.plotar_empuxo_por_altitude(self.estagio3_motor)
    plt.legend(loc = 'lower right', bbox_to_anchor=(0.97, 0.07))
    plt.grid(visible=True)
    plt.xlabel("Altitude [km]")
    plt.ylabel("Empuxo [N]")
    plt.grid(visible=True)
    plt.savefig(os.path.join('figures', self.nome_missao + '.pdf'), dpi=500)

    plt.figure(figsize=[16, 9])
    plt.title(self.nome_missao)
    plt.axvline(x = self.estagio1_H_min/1e3, linestyle = '-', color = 'k')
    plt.axvline(x = self.estagio2_H_min/1e3, linestyle = '--', color = 'k')
    plt.axvline(x = self.estagio3_H_min/1e3, linestyle = ':', color = 'k')
    self.plotar_empuxo_acumulado(self.estagio1_motor)
    self.plotar_empuxo_acumulado(self.estagio2_motor)
    self.plotar_empuxo_acumulado(self.estagio3_motor)
    plt.legend(loc = 'lower right', bbox_to_anchor=(0.97, 0.07))
    plt.grid(visible=True)
    plt.xlabel("Altitude [km]")
    plt.ylabel("Empuxo acumulado [mN]")
    plt.grid(visible=True)
    plt.savefig(os.path.join('figures', 'empuxo_acumulado.pdf'), dpi=500)

  

  