import os
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from IPython.display import Image, display

# Criar a pasta 'gráficos' se não existir
os.makedirs('/workspaces/Fuzzy/gráficos', exist_ok=True)

# Definir variáveis linguísticas
comida = ctrl.Antecedent(np.arange(0, 10, 1), 'comida')
peso = ctrl.Consequent(np.arange(0, 150, 1), 'peso')  # Aumentar o intervalo de peso

# Definir conjuntos fuzzy
comida['pouco'] = fuzz.trimf(comida.universe, [0, 0, 3])
comida['razoavel'] = fuzz.trimf(comida.universe, [2, 5, 8])
comida['bastante'] = fuzz.trimf(comida.universe, [7, 10, 10])

peso['leve'] = fuzz.trimf(peso.universe, [0, 0, 40])  
peso['medio'] = fuzz.trimf(peso.universe, [50, 75, 85])
peso['pesado'] = fuzz.trimf(peso.universe, [90, 150, 150])

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

# Atividade física
regra4 = ctrl.Rule(atividade['baixa'], peso['leve'])
regra5 = ctrl.Rule(atividade['media'], peso['medio'])
regra6 = ctrl.Rule(atividade['alta'], peso['pesado'])

# Atualizar o sistema de controle com as novas regras
sistema_peso = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6])
simulacao = ctrl.ControlSystemSimulation(sistema_peso)

# Capturar entradas do usuário
comida_input = float(input("Digite a quantidade de comida (0 a 10): "))
atividade_input = float(input("Digite o nível de atividade (0 a 10): "))

# Entrada de exemplo
simulacao.input['comida'] = comida_input
simulacao.input['atividade'] = atividade_input

# Executar a simulação (caso a pessoa coma muito e não treine vai ficar pesada)
simulacao.compute()

# Exibir o resultado
print(f"Peso previsto: {simulacao.output['peso']}")

# Visualizar os conjuntos fuzzy e salvar como imagens
comida.view()
plt.savefig('/workspaces/Fuzzy/gráficos/comida.png')
peso.view()
plt.savefig('/workspaces/Fuzzy/gráficos/peso.png')
atividade.view()
plt.savefig('/workspaces/Fuzzy/gráficos/atividade.png')

# Mostrar as imagens salvas
display(Image(filename='/workspaces/Fuzzy/gráficos/comida.png'))
display(Image(filename='/workspaces/Fuzzy/gráficos/peso.png'))
display(Image(filename='/workspaces/Fuzzy/gráficos/atividade.png'))