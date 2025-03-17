import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variáveis linguísticas
comida = ctrl.Antecedent(np.arange(0, 10, 1), 'comida')
peso = ctrl.Consequent(np.arange(0, 100, 1), 'peso')

# Definir conjuntos fuzzy
comida['pouco'] = fuzz.trimf(comida.universe, [0, 0, 3])
comida['razoavel'] = fuzz.trimf(comida.universe, [2, 5, 8])
comida['bastante'] = fuzz.trimf(comida.universe, [7, 10, 10])

peso['leve'] = fuzz.trimf(peso.universe, [0, 0, 40])
peso['medio'] = fuzz.trimf(peso.universe, [30, 50, 70])
peso['pesado'] = fuzz.trimf(peso.universe, [60, 100, 100])

# Definir regras
regra1 = ctrl.Rule(comida['pouco'], peso['leve'])
regra2 = ctrl.Rule(comida['razoavel'], peso['medio'])
regra3 = ctrl.Rule(comida['bastante'], peso['pesado'])

# Sistema de controle
sistema_peso = ctrl.ControlSystem([regra1, regra2, regra3])
simulacao = ctrl.ControlSystemSimulation(sistema_peso)

atividade = ctrl.Antecedent(np.arange(0, 10, 1), 'atividade')
atividade['baixa'] = fuzz.trimf(atividade.universe, [0, 0, 3])
atividade['media'] = fuzz.trimf(atividade.universe, [2, 5, 8])
atividade['alta'] = fuzz.trimf(atividade.universe, [7, 10, 10])

# Novas regras considerando atividade física
