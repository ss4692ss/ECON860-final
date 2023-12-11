import pandas as pd

import pandas

import numpy

from factor_analyzer import FactorAnalyzer


original_data = pandas.read_csv("dataset_final.csv")


# variances = original_data.loc[:, 'Q1':'Q40'].var()


# top_20_questions = variances.nlargest(20)


# selected_questions = top_20_questions.index.tolist()


# print(selected_questions)




questionnaire_data = original_data.loc[:, 'Q1':'Q40']


num_factors = 4

factor_analyzer = FactorAnalyzer(n_factors=num_factors, rotation=None) 


factor_analyzer.fit(questionnaire_data)


factor_loadings = factor_analyzer.loadings_

sum_squared_loadings = (factor_loadings ** 2).sum(axis=1)

selected_questions_indices = sum_squared_loadings.argsort()[-20:][::-1]  
selected_questions = questionnaire_data.columns[selected_questions_indices].tolist()

print(selected_questions)
