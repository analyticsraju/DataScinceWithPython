#Here Toss a coin predition and confident level increase/decrease

def bayes(prior, likeliwood, evidence):
    return prior*(likeliwood/evidence)
    
#after 1st evidance of head outcome but expected tail
print(bayes(0.9,0.5,(0.5*0.9+1*0.1)))#0.81

#after second evidance of head outcome but expected tail
print(bayes(0.81,0.5,(0.5*0.81+1*0.19)))#0.68

#after third evidance of head outcome but expected tail
print(bayes(0.68,0.5,(0.5*0.68+1*0.32)))#0.51

#after foruth evidance of head outcome but expected tail
print(bayes(0.51,0.5,(0.51*0.5+1.0*0.49))) #0.34

#after fifth evidance of head outcome but expected tail
print(bayes(0.34,0.5,(0.34*0.5+1*0.66)))#0.20

#after sixth evidance of head outcome but expected tail
print(bayes(0.2,0.5,(0.2*0.5+1*0.80)))#0.11

#after seventh evidance of head outcome but expected tail
print(bayes(0.11,0.5,(0.11*0.5+1*0.89)))#0.05

#after eight evidance of head outcome but expected tail
print(bayes(0.05,0.5,(0.05*0.5+1*0.95)))#0.02
