from docplex.mp.model import Model

citta = 6

Costs = [[999., 3.71, 9.6, 8.03, 6.17, 11.12],
         [9.71, 999., 6.54, 5.2, 3.08, 7.42],
         [28.06, 19.54, 999., 4.66, 1999.5, 7.57],
         [24.03, 15.2, 1.66, 999., 6.12, 7.25],
         [18.17, 9.08, 3.5, 2.12, 999., 6.22],
         [29.12, 19.42, 6.57, 9.25, 15.22, 999.]]

m = Model(name='heuristic', log_output=True)

x = m.binary_var_matrix(citta, citta)

m.minimize(m.sum(m.sum(Costs[i][j] * x[i][j]) for j in range(1, citta)) for i in range(1, citta))

m.add_constraint(m.sum(x[i][j] == 1 for j in range(citta)) for i in range(citta))
m.add_constraint(m.sum(x[i][j] == 1 for i in range(citta)) for j in range(citta))

msol = m.solve()

m.report()
