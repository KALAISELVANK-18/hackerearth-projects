ses = int(input())
costs = []
#finding cost of baloons in certain order
for i in range(ses):
    rs = input()
    rupe = []
    rup = rs.split(' ')
    for i in range(len(rup)):
        rupe.append(int(rup[i]))
    parti = int(input())
    solve = []
    for i in range(parti):
        so = []
        sol = input()
        solv = sol.split(' ')
        for i in range(2):
            so.append(int(solv[i]))
        solve.append(so)
    costi=[]
    for i in range(2):
        cost=0
        if i == 0:
            for i in range(parti):
                for z in range(2):
                    cost += rupe[z] * solve[i][z]
            costi.append(cost)
        else:
            for i in range(parti):
                for z in range(2):
                    cost += rupe[-(z + 1)]*solve[i][z]
            costi.append(cost)
    costs.append(costi)

for i in range(len(costs)):
    print(min(costs[i]))