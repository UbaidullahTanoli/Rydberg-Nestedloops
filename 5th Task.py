#!/usr/bin/env python
# coding: utf-8

# In[1]:


#################################################################################################
### By Ubaidullah Tanoli
### Unit 5
### Plotting first-, third- and fifth-order Legendre polynomials 
### Calculating the wavelengths from emission espectrum of Hydrogen using Rydberg formula
#################################################################################################


# # Legendre polynomial
# Considering the first, third, and fifth order legendre polynomial followed by their plot over a domain ranging from -1 to +1

# In[13]:


#importing the necessary packages

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# In[5]:


x = np.linspace(-1,1,1000)


# $$y_1 = P_1(x) = x$$

# In[6]:


y1 = x


# $$y_3 = P_3(x) = 1/2 (5x^{3} - 3x)$$

# In[7]:


y3 = 1/2 * (5*x**3 - 3*x)


# $$y_5 = P_5(x) = 1/8 (63x^5 - 70x^3 + 15x)$$

# In[8]:


y5 = 1/8 * (63*x**5 - 70*x**3 + 15*x)


# In[10]:


# plotting the graphs

plt.figure()
# plotting the three graphs on the same graph
plt.plot(x,y1,label="P1(x)")     
plt.plot(x,y3,label="P3(x)")
plt.plot(x,y5,label="P5(x)")
plt.xlabel("x")                   # labelling x axis
plt.ylabel("P(x)")                # labelling y axis
plt.title("1st,2nd,and 3rd order Lenegdre polynomials")  # the title of the plot
plt.legend(loc="best")
plt.grid(True)


# The intended outcome of the above coding was to plot and compare the specific types of function called first,second, and third order Legendre polynomials. The task has been successful as the distinction between the three can be seen, hvaing the same range and domain, ie. $$-1<=y<=1$$ and $$-1<=x<=1$$ respectively. We can notice the higher the degree of polynomial, the more "loops" or "fluctuations" it has.

# # Rydberg formula
# Using Rydberg formula to caluculate the first 4 wavelengths in each of the first 5 emission series of a Hydrogen Series, namely Lyman, Balmer, Paschen, Brackett, Pfund series.

# $$\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)$$

# The formula is used to calculate the wavelengths associated with the emission of photon when electrons make a jump to a lower quantum number. 
# $\lambda$ is the wavelength of the light, $n_1$ is the final orbit number (the orbit which electron makes jump to), and $n_2$ is the initial orbit number (the orbit which an electron makes jump from).
# And R_H is a constant called Rydberg constant with a value of $1.09677583*10^7$

# In[87]:


def Rydberg(n1, n2):
    Lambda = (R * (1/n1**2 - 1/n2**2))**-1
    return Lambda*10**9

R = 1.09677583 * 10**7 
n2 = range(1,10)


# ### Lyman Series

# In[88]:


Ly = n2[1:5]
for x in range(1,5):
        y = x - 1
        print(f'A light of wavelength ~ {Rydberg(1,Ly[y]):.1f}nm is emitted from a Hydrogen atom when there is a jump of electron from principle {Ly[y]} to 1')


# ### Balmer Series

# In[81]:


Bal = n2[2:6]
for x in range(1,5):
        y = x - 1
        print(f'A light of wavelength ~ {Rydberg(2,Bal[y]):.1f}nm is emitted from a Hydrogen atom when there is a jump of electron from principle {Bal[y]} to 2')


# ### Paschen Series

# In[82]:


Pas = n2[3:7]
for x in range(1,5):
        y = x - 1
        print(f'A light of wavelength ~ {Rydberg(3,Pas[y]):.1f}nm is emitted from a Hydrogen atom when there is a jump of electron from principle {Pas[y]} to 3')


# ### Brackett Series

# In[83]:


Bra = n2[4:8]
for x in range(1,5):
        y = x - 1
        print(f'A light of wavelength ~ {Rydberg(4,Bra[y]):.1f}nm is emitted from a Hydrogen atom when there is a jump of electron from principle {Bra[y]} to 4')


# ### Pfund Series

# In[84]:


Pfu = n2[5:9]
for x in range(1,5):
        y = x - 1
        print(f'A light of wavelength ~ {Rydberg(5,Pfu[y]):.1f}nm is emitted from a Hydrogen atom when there is a jump of electron from principle {Pfu[y]} to 5')


# A light of wavelength ~ 656nm is emitted from a Hydrogen atom when there is a jump of electron from quantum number 3 to principle 2.
