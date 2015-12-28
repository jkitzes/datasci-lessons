import pandas as pd
import analysis_functions as af

birds_df = pd.read_csv('birds_lg.csv', index_col='Species')

results_df = af.count_birds(birds_df)

results_df.to_csv('birds_results.csv')
ax = results_df.T.plot()  # 11
fig = ax.get_figure()
fig.savefig('birds_results.pdf')