import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('before_fix_raw.csv')

data['minute'] = pandas.to_datetime(data['minute'])
data['outage'] = (data['minute'] - data['minute'].shift(-1))

res = data[data['outage'] > pandas.to_timedelta(1, unit='m')]
outageTime = res['outage'].sum()

totalTime = data['minute'].iloc[0] - data['minute'].iloc[-1]
okTime = totalTime - outageTime

print('sum outage:', outageTime)
print('total time:', totalTime)

labels = 'Ok', 'Not OK'
sizes = [okTime.total_seconds(), outageTime.total_seconds()]

fix, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.2f%%')
ax.axis('equal')
plt.show()