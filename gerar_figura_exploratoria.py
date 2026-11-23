from pathlib import Path
import pandas as pd,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent;t=pd.read_csv(p/'treino.csv')
labels={1:'Trato GI superior',2:'Trato GI inferior',3:'Glândulas anexas',6:'Outros'}
fig,ax=plt.subplots(1,2,figsize=(10,3.0))
ax[0].scatter(t.Age,t.weight_loss,c='#287D8E',alpha=.7,s=20)
ax[0].set(xlabel='Idade (anos)',ylabel='Perda de peso (%)',title='Idade e perda de peso')
ax[1].boxplot([t.loc[t.tumor_location==k,'weight_loss'] for k in labels],tick_labels=['GI sup.','GI inf.','Glândulas','Outros'])
ax[1].set(ylabel='Perda de peso (%)',title='Perda por localização do tumor')
fig.tight_layout();fig.savefig(p/'figuras/relacoes_treino.png',dpi=200,bbox_inches='tight')
# Numeric descriptive evidence, no significance claims.
print(t.groupby('tumor_location').weight_loss.agg(['count','median','mean']).round(3).to_string())
