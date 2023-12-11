import pandas

from factor_analyzer import FactorAnalyzer

from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

import numpy

dataset1 = pandas.read_csv("dataset_final.csv")


dataset1 = dataset1.values

dataset1 = dataset1[:,0:39]

print(dataset1)


chi2 ,p=calculate_bartlett_sphericity(dataset1)
print(chi2, p)

machine = FactorAnalyzer(n_factors=39, rotation=None)

machine.fit(dataset1)

ev, v = machine.get_eigenvalues()
print(ev)




machine = FactorAnalyzer(n_factors=4, rotation=None)
machine.fit(dataset1)
output = machine.loadings_
print(output)

machine = FactorAnalyzer(n_factors=4, rotation='varimax')
machine.fit(dataset1)
factor_loadings = machine.loadings_
print(factor_loadings)


results = numpy.dot(dataset1, factor_loadings)

pandas.DataFrame(results).round().to_csv("results.csv", index=False)

