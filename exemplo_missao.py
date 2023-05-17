# Trabalho 1: Projeto de motor foguete # ------------------------------------------------- #
# Autores:      Enzo Filippo Centenaro da Silva
#               Bernardo Eckert Recktenvald
# Data:         11/05/2023
# Curso:        Engenharia Aeroespacial - CT, Universidade Federal de Santa Maria
# Disciplina:   FUNDAMENTOS DE PROPULSÃO AEROESPACIAL
# Professor:    Dr. Cesar Addis Valverde Salvador

# ----------------------------------------------------------------------------------------- #
# Bibliotecas necessárias # --------------------------------------------------------------- #

import matplotlib.pyplot as plt
import propespacial as prop

# ----------------------------------------------------------------------------------------- #
# Parâmetros físicos # -------------------------------------------------------------------- #

area_da_garganta = 0.0005  #m²
P1 = 2.0265e6  #Pa
T1 = 2200  #K
k = 1.2  #adimensional
mp_ponto = 1  #kg/s
R = 345.7  #J/kg.K

# ----------------------------------------------------------------------------------------- #
# Parâmetros de altitude # ---------------------------------------------------------------- #

H_1_min = 0  #Altitude mínima estágio 1
H_1_max = 17000  #Altitude máxima estágio 1
H_2_min = H_1_max  #Altitude mínima estágio 2
H_2_max = 44000  #Altitude máxima estágio 2
H_3_min = H_2_max  #Altitude mínima estágio 3
H_3_max = 120000  #Altitude máxima estágio 3

# ----------------------------------------------------------------------------------------- #
# Parâmetros do programa # ---------------------------------------------------------------- #

n_pontos = 1000  #Número de pontos calculados, quanto maior, melhor a resolução, mais lento o programa

# ----------------------------------------------------------------------------------------- #
# Criação dos diferentes estágios da atmosfera -------------------------------------------- #

atmosfera_estagio1 = prop.Atmosfera(n_pontos, H_1_min, H_1_max)
atmosfera_estagio1.calculo_propriedades()
atmosfera_estagio2 = prop.Atmosfera(n_pontos, H_2_min, H_2_max)
atmosfera_estagio2.calculo_propriedades()
atmosfera_estagio3 = prop.Atmosfera(n_pontos, H_3_min, H_3_max)
atmosfera_estagio3.calculo_propriedades()
atmosfera = prop.Atmosfera(n_pontos, H_1_min, H_3_max)
atmosfera.calculo_propriedades()

# ----------------------------------------------------------------------------------------- #
# Plotas atmosferas ----------------------------------------------------------------------- #

atmosfera_estagio1.plotar_atmosfera()
atmosfera_estagio2.plotar_atmosfera()
atmosfera_estagio3.plotar_atmosfera()
atmosfera.plotar_atmosfera()

# ----------------------------------------------------------------------------------------- #
# Criação de motores para os diferentes estágios da atmosfera ----------------------------- #

# Primeiro estágio:
motor1_estagio1_epsilon5 = prop.MotorFoguete(1,  5, atmosfera_estagio1, 1, area_da_garganta, k, P1, n_pontos, "#069AF3" , "o")
motor1_estagio1_epsilon10 = prop.MotorFoguete(1, 10, atmosfera_estagio1, 1, area_da_garganta, k, P1, n_pontos, "crimson"   , "v")
motor1_estagio1_epsilon15 = prop.MotorFoguete(1, 15, atmosfera_estagio1, 1, area_da_garganta, k, P1, n_pontos, "orange" , "p")
motor1_estagio1_epsilon20 = prop.MotorFoguete(1, 20, atmosfera_estagio1, 1, area_da_garganta, k, P1, n_pontos, "teal"      , "s")
motor1_estagio1_epsilon25 = prop.MotorFoguete(1, 25, atmosfera_estagio1, 1, area_da_garganta, k, P1, n_pontos, "darkblue"  , "P")

# Segundo estágio:
motor1_estagio2_epsilon27 = prop.MotorFoguete(1, 27, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "black"     , "o")
motor1_estagio2_epsilon29 = prop.MotorFoguete(1, 29, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "magenta"   , "v")
motor1_estagio2_epsilon31 = prop.MotorFoguete(1, 31, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "#069AF3" , "p")
motor1_estagio2_epsilon33 = prop.MotorFoguete(1, 33, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "crimson"   , "s")
motor1_estagio2_epsilon35 = prop.MotorFoguete(1, 35, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "orange" , "P")
motor1_estagio2_epsilon37 = prop.MotorFoguete(1, 37, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "teal"      , "*")
motor1_estagio2_epsilon39 = prop.MotorFoguete(1, 39, atmosfera_estagio2, 2, area_da_garganta, k, P1, n_pontos, "darkblue"  , "d")

# Terceiro estágio:
motor1_estagio3_epsilon50 = prop.MotorFoguete(1, 50,  atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "black"     , "o")
motor1_estagio3_epsilon80 = prop.MotorFoguete(1, 80,  atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "#069AF3" , "v")
motor1_estagio3_epsilon110 = prop.MotorFoguete(1, 110, atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "crimson"   , "p")
motor1_estagio3_epsilon140 = prop.MotorFoguete(1, 140, atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "orange" , "s")
motor1_estagio3_epsilon170 = prop.MotorFoguete(1, 170, atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "teal"      , "P")
motor1_estagio3_epsilon200 = prop.MotorFoguete(1, 200, atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "darkblue"  , "*")
motor1_estagio3_epsilon300 = prop.MotorFoguete(1, 300, atmosfera_estagio3, 3, area_da_garganta, k, P1, n_pontos, "darkblue"  , "d")

# ---------------------------------------------------------------------------------------- #
# Plotar gráficos de empuxo -------------------------------------------------------------- #

# Todos estágios
prop.plotar_empuxo_por_altitude_dos_motores([motor1_estagio1_epsilon5,
                                            motor1_estagio1_epsilon10, 
                                            motor1_estagio1_epsilon15, 
                                            motor1_estagio1_epsilon20, 
                                            motor1_estagio1_epsilon25,
                                            motor1_estagio2_epsilon27, 
                                            motor1_estagio2_epsilon29, 
                                            motor1_estagio2_epsilon31, 
                                            motor1_estagio2_epsilon33, 
                                            motor1_estagio2_epsilon35, 
                                            motor1_estagio2_epsilon37, 
                                            motor1_estagio2_epsilon39,
                                            motor1_estagio3_epsilon50, 
                                            motor1_estagio3_epsilon80, 
                                            motor1_estagio3_epsilon110,
                                            motor1_estagio3_epsilon140,
                                            motor1_estagio3_epsilon170,
                                            motor1_estagio3_epsilon200,
                                            motor1_estagio3_epsilon300])


# Primeiro estágio
prop.plotar_empuxo_por_altitude_dos_motores([motor1_estagio1_epsilon5,
                                            motor1_estagio1_epsilon10, 
                                            motor1_estagio1_epsilon15, 
                                            motor1_estagio1_epsilon20, 
                                            motor1_estagio1_epsilon25])

# Segundo estágio
prop.plotar_empuxo_por_altitude_dos_motores([motor1_estagio2_epsilon27, 
                                            motor1_estagio2_epsilon29, 
                                            motor1_estagio2_epsilon31, 
                                            motor1_estagio2_epsilon33, 
                                            motor1_estagio2_epsilon35, 
                                            motor1_estagio2_epsilon37, 
                                            motor1_estagio2_epsilon39])

# Terceiro estágio
prop.plotar_empuxo_por_altitude_dos_motores([motor1_estagio3_epsilon50, 
                                            motor1_estagio3_epsilon80, 
                                            motor1_estagio3_epsilon110,
                                            motor1_estagio3_epsilon140,
                                            motor1_estagio3_epsilon170,
                                            motor1_estagio3_epsilon200,
                                            motor1_estagio3_epsilon300])

# ---------------------------------------------------------------------------------------- #
# Plotar gráficos de pressão -------------------------------------------------------------- #

# Todos estágios
prop.plotar_pressao_por_altitude_dos_motores([motor1_estagio1_epsilon5,
                                            motor1_estagio1_epsilon10, 
                                            motor1_estagio1_epsilon15, 
                                            motor1_estagio1_epsilon20, 
                                            motor1_estagio1_epsilon25,
                                            motor1_estagio2_epsilon27, 
                                            motor1_estagio2_epsilon29, 
                                            motor1_estagio2_epsilon31, 
                                            motor1_estagio2_epsilon33, 
                                            motor1_estagio2_epsilon35, 
                                            motor1_estagio2_epsilon37, 
                                            motor1_estagio2_epsilon39,
                                            motor1_estagio3_epsilon50, 
                                            motor1_estagio3_epsilon80, 
                                            motor1_estagio3_epsilon110,
                                            motor1_estagio3_epsilon140,
                                            motor1_estagio3_epsilon170,
                                            motor1_estagio3_epsilon200,
                                            motor1_estagio3_epsilon300])


# Primeiro estágio
prop.plotar_pressao_por_altitude_dos_motores([motor1_estagio1_epsilon5,
                                            motor1_estagio1_epsilon10, 
                                            motor1_estagio1_epsilon15, 
                                            motor1_estagio1_epsilon20, 
                                            motor1_estagio1_epsilon25])

# Segundo estágio
prop.plotar_pressao_por_altitude_dos_motores([motor1_estagio2_epsilon27, 
                                            motor1_estagio2_epsilon29, 
                                            motor1_estagio2_epsilon31, 
                                            motor1_estagio2_epsilon33, 
                                            motor1_estagio2_epsilon35, 
                                            motor1_estagio2_epsilon37, 
                                            motor1_estagio2_epsilon39])

# Terceiro estágio
prop.plotar_pressao_por_altitude_dos_motores([motor1_estagio3_epsilon50, 
                                            motor1_estagio3_epsilon80, 
                                            motor1_estagio3_epsilon110,
                                            motor1_estagio3_epsilon140,
                                            motor1_estagio3_epsilon170,
                                            motor1_estagio3_epsilon200,
                                            motor1_estagio3_epsilon300])

# ---------------------------------------------------------------------------------------- #
# Criação de missões --------------------------------------------------------------------- #

missao1 = prop.Missao('Missão de 3 estágios com 3 motores', motor1_estagio1_epsilon20, motor1_estagio2_epsilon27, motor1_estagio3_epsilon50, atmosfera, n_pontos)
missao1.plotar_missao()

plt.show()
