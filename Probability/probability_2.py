import numpy as np
import pandas as pd

coin_tosses = np.random.randint(0,2,1000)
print(pd.crosstab(index=coin_tosses, columns='count'))


dice_throws = np.random.randint(1,7,1200)
print(pd.crosstab(index=dice_throws, columns='count'))

###############
def prob(a, b):
    c=a/b
    return c

# from cards pick a black probability
prob(26,52)

# from cards pick a black-spade probability
prob(13,52)

#kind or queen
prob(4,52)+prob(4,52)
    
#non face card
prob(40,52)

#black face card
#Ans.3 spads black and 3 clubs black
prob(6,52)

#9 of red color
prob(2,52)

