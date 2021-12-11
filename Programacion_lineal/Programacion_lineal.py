from pyomo.environ import *

model = ConcreteModel()

# Variables
model.x = Var(domain=NonNegativeReals)

#Funcion objetivo
model.profit= Objective(expr= 40*model.x,sense=maximize)

#Constrains
model.demanda= Constraint(expr = model.x <= 40)
model.trabajoA= Constraint(expr =model.x <= 80)
model.trabajoB = Constraint(expr = model.x <= 100)



SolverFactory('cbc', executable=r'C:\Users\rosal\OneDrive\Escritorio\PYTHON\Pyomo\solvers\solvers\cbc.exe',solver_io='nl').solve(model).write()

# display solution
print('\nProfit = ', model.profit())

print('\nDecision Variables')
print('x = ', model.x())

print('\nConstraints')
print('Demand  = ', model.demanda())
print('Labor A = ', model.trabajoA())
print('Labor B = ', model.trabajoB())

print('Labor B = ', model.trabajoB())























# create a model
model = ConcreteModel()

# declare decision variables
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# declare objective
model.profit = Objective(expr = 40*model.x + 30*model.y, sense=maximize)

# declare constraints
model.demand = Constraint(expr = model.x <= 40)
model.laborA = Constraint(expr = model.x + model.y <= 80)
model.laborB = Constraint(expr = 2*model.x + model.y <= 100)

model.pprint()


SolverFactory('cbc', executable=r'C:\Users\rosal\OneDrive\Escritorio\PYTHON\Pyomo\solvers\solvers\cbc.exe',solver_io='nl').solve(model).write()

# display solution
print('\nProfit = ', model.profit())

print('\nDecision Variables')
print('x = ', model.x())
print('y = ', model.y())

print('\nConstraints')
print('Demand  = ', model.demand())
print('Labor A = ', model.laborA())
print('Labor B = ', model.laborB())