##Bayes Theorem

def bayes(prior, likeliwood, evidence):
    return prior*(likeliwood/evidence)
    
#test is 90% accurate, 2%cancer
print(bayes(0.02, 0.9, (0.9*0.02+0.1*0.98)))#doctor prediction say 0.15

#test is 98% accurate, 2%cancer
print(bayes(0.02,0.98,(0.98*0.02+0.02*0.98)))#doctor prediction say 0.5

#test is 100% accurate, 2%cancer
print(bayes(0.02,1.0,(1.0*0.02+0*0.98)))#doctor prediction say 1.0

#test is 90% accurate, 50%cancer
print(bayes(0.5,0.9,(0.9*0.5+0.1*0.5)))#doctor prediction say 0.9

#test is 98% accurate, 50%cancer
print(bayes(0.5,0.98,(0.98*0.5+0.02*0.50)))#doctor prediction say 0.98


