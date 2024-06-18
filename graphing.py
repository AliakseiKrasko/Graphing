import pandas as pd
import random

# Генерация исходных данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# One-hot encoding вручную
data['robot'] = (data['whoAmI'] == 'robot').astype(int)
data['human'] = (data['whoAmI'] == 'human').astype(int)

# Удаляем исходный столбец 'whoAmI', если он больше не нужен
# data = data.drop('whoAmI', axis=1)

print(data.head())