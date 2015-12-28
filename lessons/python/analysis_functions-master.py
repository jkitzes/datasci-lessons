import pandas as pd

def count_birds(birds_df):
    years = birds_df.columns
    results_df = pd.DataFrame(index=['Mean'], columns=years)
    
    for year in years:
        birds_this_year = birds_df[year]
        sum_counts = birds_this_year.sum()
        species_seen = (birds_this_year > 0).sum()
        
        if species_seen == 0:
            results_df[year] = 0
        else:
            results_df[year] = sum_counts / species_seen
    
    return results_df
