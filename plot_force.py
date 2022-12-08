import matplotlib.pyplot as plt
import json

plt.style.use('ggplot')

def read_json(file):
  with open(file, 'r') as f:
    data = json.load(f)
  return data

def plot_force(data):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    
    fig, ax = plt.subplots(len(data), figsize=(14, 8), sharex=True, sharey=True)
    plt.subplots_adjust(hspace=0.7)
    
    fig.suptitle('Joint Forces', fontsize=16)
    fig.text(0.5, 0.04, 'Time', ha='center')
    fig.text(0.08, 0.5, 'Forces', va='center', rotation='vertical')
    
    for i in range(len(data)):
        ax[i].plot(data[i], label=f'joint{i+1}', c = colors[i])
        ax[i].legend(loc='best')

    plt.show()
        
    
data = read_json('data.txt')
plot_force(data)