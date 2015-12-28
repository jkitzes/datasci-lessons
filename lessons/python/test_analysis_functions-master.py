import pandas as pd
import analysis_functions as af
import numpy as np

def test_count_birds_small_table():
    input_df = pd.read_csv('birds_sm.csv', index_col='Species')
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df['2010'], 24.5)

def test_count_birds_simulated_data():
    input_df = pd.DataFrame([[1,2],[3,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[2, 3]])

def test_count_birds_zero_year():
    input_df = pd.DataFrame([[0,2],[0,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df['2010'], 0)

def test_count_birds_handles_bad_input():
    input_df = pd.DataFrame([[None,2],[3,4]],
        index=['Sp1', 'Sp2'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[3, 3]])

def test_count_birds_one_species():
    input_df = pd.DataFrame([[1,2]],
        index=['Sp1'], columns=['2010', '2011'])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[1, 2]])

def test_count_birds_empty_input():
    input_df = pd.DataFrame([[]])
    results_df = af.count_birds(input_df)
    np.testing.assert_array_equal(results_df, [[]])
