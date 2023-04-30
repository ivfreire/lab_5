import numpy as np
import pandas as pd

labels = [ 'Ruido', 'Violeta', 'Azul', 'Verde', 'Laranja', 'Vermelho' ]
labels_ = [ 'ruido', 'violeta', 'azul', 'verde', 'laranja', 'vermelho' ]

ints = [ 20, 40, 60, 80, 100 ]

data = {}

table = []
for i in range(10):
	df = pd.read_csv(f'Ruido/ruido_{i+1}.csv', sep=';', decimal=',')
	table.append(list( df['Corrente [A]'] ))
	data['Tensao'] = list(df['Tensao [V]'])

table = np.array(table)

data['ruido']	= table.mean(axis=0)
data['sRuido']	= table.std(axis=0)

for i,label in enumerate(labels):
	if label != 'Ruido':
		for intensity in [ 20, 40, 60, 80, 100 ]:
			table = []

			for j in range(10):
				try:
					df = pd.read_csv(f'{label}/{labels_[i]}_{intensity}_{j+1}.csv', sep=';', decimal=',')
					table.append(list( df['Corrente [A]'] ))
				except Exception as e:
					print(f'not found: {e}')

			table = np.array(table)
			print(intensity)

			data[f'{labels[i]}_{intensity}']	= table.mean(axis=0)
			data[f's{labels[i]}_{intensity}']	= table.std(axis=0)

df = pd.DataFrame(data)
df.to_csv('dados.csv')