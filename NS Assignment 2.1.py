
# coding: utf-8

# # Effect of tax on producers' revenue
# 
# ##Introduction
# In a free-market situation the government does not interfere with price and quantity of a good or service. In this case, there will be no welfare loss. Sometimes it is necesarry to promote or discourage a product or service because of e.g. public order.
# 
# Interference in a free market comes at a price, the deadweight loss. In this example we will calculate the revenue of producers of gasoline with and without the introduction of a tax  that has been imposed by the governement. 
# 
# The government can regulate the demand by imposing a subsidy or tax, which causes the quantity of a good demanded to rise or fall and/or the quantity of a good supplied to rise or fall. 

# ##Model
# 
# ###Demand & Supply
# 
# In a free market the producers offer a certain quantity of gas, according to his demand function:
# 
# $$q_d=150 - p_d$$
# 
# 
# and the consumer buys a gasoline under the following demand function:
# 
# $$q_s=60+p_s$$
# 

# ###Free market
# To check whether or not the market has an equilibrium price and quantity, I will plot both functions. 
# If an equilibrium exists, the revenue of the produces can be calculated. 
# Since there is no tax implied, tax is equal to 0.
# 

# In[1]:

import math 
from scipy import arange, optimize
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[1]:

def p_s(tax):
    return (90 - 25*tax)/45
def p_d(tax, p_s):
    return (p_s + tax)
def q_d(p_d):
    return 150 - 25*p_d
def q_s(p_s):
    return 60 + 20*p_s
def rev_s(q_s, p_s):
    return q_s*p_s
def rev_d(q_d, p_d):
    return q_d*p_d
def rev_gov(tax,q_s):
    return tax*q_s


# In[6]:

range_p_s = arange(0.0, 6.01)
range_p_d = arange(0.0, 6.01)
range_q_d = [q_d(p_d) for p_d in range_p_d]
range_q_s = [q_s(p_s) for p_s in range_p_s]

plt.clf()
plt.plot(range_q_d, range_p_d,'-', color = 'b', linewidth = 2)
plt.plot(range_q_s, range_p_s,'-', color = 'r', linewidth = 2)
plt.ylim(0, 7)
plt.xlim(0, 150)
plt.title("Gasoline market - without tax", fontsize = 15)
plt.xlabel("Q (billion gallons per year)", fontsize = 10)
plt.ylabel("P (dollars per gallon)" ,fontsize = 10,rotation = 90)
plt.annotate('Demand', xy=(60.0,4.0),  xycoords='data', # here we define the labels and arrows in the graph
              xytext=(30, 50), textcoords='offset points', size = 15,
              arrowprops=dict(arrowstyle="->", linewidth = 2,
                              connectionstyle="arc3,rad=.2")
              )
plt.annotate('Supply', xy=(110.0, 3.0),  xycoords='data', # here we define the labels and arrows in the graph
              xytext=(30, 50), textcoords='offset points', size = 15,
              arrowprops=dict(arrowstyle="->", linewidth = 2,
                              connectionstyle="arc3,rad=.2"))

plt.savefig('gasoline_market_without_tax.png')


# In[7]:

output = optimize.fsolve(lambda p: 90 - 45*p, 0)
print output


# According to the graph the two functions intersect at a price of USD2.0. The equilibrium quantity and total revenue the producers can be found via $optimize.fsolve$. 

# In[2]:

q_s(2.0)


# In[3]:

rev_s(100.0, 2.0)


# The optimal quantity is 100 billion gallons per year at a price of USD2 per gallon. The revenue, assuming that there will be no production costs, will be USD200 billion.

# ###Government regulations 
# 
# To put the production and consumption of gasoline on hold, the government introduces a tax. The astern thought of the tax is not to steal revenue from the producers, but to reduce the consumption. An ethical rule is set that tax revenue cannot exceed the sellers' revenue. And the tax must be paid partially by the consumer and partially by the producers. 
# 
# After the tax is in place, four conditions have to be met:
# 
# 
# * The quantity sold and the buyer's price $P_b$ must lie on the demand curve;
# * The quantity sold and the seller's price $P_s$ must lie on the supply curve;
# * The quantity demanded must equal the quantity supplied;
# * The difference between the price the buyer pays and the price the seller receives must equal the tax.
# 
# 
# After introduction of a tax, the maximum value of this tax can be calculated via $ optimize.fsolve $ what results in:

# In[10]:

output = optimize.fsolve(lambda tax: 2 - ((25*tax)/45) - tax, 0)
print output


# So, the government cannot imply a tax that exceeds USD 1.286, or their ethical issue will be violated. 
# 
# The revenue of the producers and the government is euqal to each other and will be:

# In[11]:

q_s(1.28571429)


# In[13]:

rev_s(85.7142858, 1.28571429)


# In[4]:

rev_gov(1.28571429,85.7142858)


# ## Conclusion
# The old revenue of the suppliers was USD 200 billion, and the new is almost USD 90 billion less. This are the cost of government's interference. 
