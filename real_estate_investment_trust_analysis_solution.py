#!/usr/bin/env python
# coding: utf-8

# ## REIT STOCK ANALYSIS

# In this project, you will analyze Real Estate Investment Trusts, commonly known as REITs. REITs are companies that own or operate real estate that produces income. REITs, like the stocks of regular public companies, are traded on different stock exchanges. Investing in a REIT allows you to invest in portfolios of real estate assets the same way you can invest in a company by buying its stock.
# 
# Using financial statistics and NumPy you will analyze two REITs: [Sabra Health Care REIT Inc. (NASDAQ: SBRA)](https://finance.yahoo.com/quote/SBRA/), which invests in health care real estate, and [Equity Residential (NASDAQ:EQR)](https://finance.yahoo.com/quote/EQR/), which invests in rental apartment properties.
# 

# The time period for analysis we will be using is `Jan 1 2018` to `Dec 31 2018`. The REIT data for SBRA (`SBRA.csv`) and EQR (`EQR.csv`) can be found in the same folder as this file.

# 1. Import the numpy module as np

# In[1]:


import numpy as np


# 2. Load the adjusted closings for SBRA

# In[2]:


adj_closings_sbra = np.loadtxt("SBRA.csv", skiprows=1, usecols=5, delimiter=',')
print(adj_closings_sbra)


# ## Calculate Simple Rate of Return

# 3. To calculate the daily RoR for the SBRA stock we need the daily adjusted closing price. The formula we are using for the daily rate of return is out[n] = a[n+1] - a[n] 

# 4. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `rate_of_return`
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. Within the function use np.diff() and set it to the variable `daily_simple_ror`
#     
#     step 4. return `daily_simple_ror`

# In[3]:


def simple_rate_of_return(adj_closings):
    daily_simple_ror = np.diff(adj_closings)/adj_closings[:-1]
    return daily_simple_ror


# 5. Call the function `simple_rate_of_return` with the arguments `adj_closings_sbra`. Then print the results. 

# In[4]:


daily_simple_returns_sbra = simple_rate_of_return(adj_closings_sbra)
print(daily_simple_returns_sbra )


# ## Calculate Average Daily Return

# 6. Use `np.mean()` with the argument `daily_simple_returns_sbra` to calculate the average daily return. Then set it to the variable name `average_daily_simple_return_sbra`

# In[5]:


average_daily_simple_return_sbra = np.mean(daily_simple_returns_sbra)
print(average_daily_simple_return_sbra)


# ## Calculate Daily Log Returns

# 7. Create a function that returns the daily rate of return
# 
#     step 1. define a function named log_returns
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. use np.log() to get the log of each adjusted closing price and set it to the variable `log_adj_closings`
#     
#     step 4. use np.diff() to get the diff of each daily log adjusted closing price and set it to the variable `daily_log_returns`
#     
#     step 5. return `daily_log_returns`

# In[6]:


def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns


# 8. Call the function `log_returns` with the arguments `adj_closings_sbra`. Set it to the variable `daily_log_returns_sbra`. Then print the results. 

# In[7]:


daily_log_returns_sbra = log_returns(adj_closings_sbra)
print(daily_log_returns_sbra)


# ## Calculate Annualize Daily Log Return

# 9. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `annualize_log_return`
#     
#     step 2. create parameter for  `daily_log_returns`
#     
#     step 3. use `np.mean()` with the argument `daily_log_returns` to calculate the average daily return. Then set it to the variable name `average_daily_log_returns`
#     
#     step 4. then multiply `average_daily_log_returns` by 250 and set it to the variable `annualized_log_return`
#     
#     step 5. return `annualized_log_return`

# In[8]:


def annualize_log_return(daily_log_returns):
    average_daily_log_returns = np.mean(daily_log_returns)
    annualized_log_return = average_daily_log_returns*250
    return annualized_log_return


# 10. Call the function `annualize_log_return` with the arguments `daily_log_returns`. Set it to the variable `annualized_log_return_sbra`. Then print the results. 

# In[9]:


annualized_log_return_sbra = annualize_log_return(daily_log_returns_sbra)
print(annualized_log_return_sbra)


# ## Calculate Variance of Daily Log Returns

# 11. Calculate the variance of the daily logarithmetic return. Use the function `.var()` with the argument `log_daily_ror`. Set it to the variable `daily_varaince_sbra`. Then print the results. 

# In[10]:


daily_varaince_sbra = np.var(daily_log_returns_sbra)
print(daily_varaince_sbra)


# ## Calculate Standard Deviation

# 12. Calculate the Standard Deviation of the daily logarithmetic return. Use the function `.std()` with the argument `daily_log_returns_sbra`. Set it to the variable `daily_sd_sbra`. Then print the results. 

# In[11]:


daily_sd_sbra = np.std(daily_log_returns_sbra)
print(daily_sd_sbra)


# In[12]:


## Load EQR Data


# 13. Load the adjusted closings for EQR

# In[13]:


adj_closings_eqr = np.loadtxt("EQR.csv", skiprows=1, usecols=5, delimiter=',')
print(adj_closings_eqr)


# ## Calculate Simple Rate of Return EQR

# 14. Call the function `simple_rate_of_return` with the arguments `adj_closings_eqr`. Then print the results. 

# In[14]:


daily_simple_returns_eqr = simple_rate_of_return(adj_closings_eqr)
print(daily_simple_returns_eqr)


# ## Calculate Average Daily Return EQR

# 15. Use `np.mean()` with the argument `daily_simple_returns_eqr` to calculate the average daily return. Then set it to the variable name `average_daily_simple_return_eqr`

# In[15]:


average_daily_simple_return_eqr = np.mean(daily_simple_returns_eqr)
print(average_daily_simple_return_eqr)


# ## Calculate Daily Log Returns EQR

# 16. Call the function `log_returns` with the arguments `adj_closings_eqr`. Set it to the variable `daily_log_returns_eqr`. Then print the results. 

# In[16]:


daily_log_returns_eqr = log_returns(adj_closings_eqr)
print(daily_log_returns_eqr)


# ## Calculate Annualize Daily Log Return EQR

# 17. Call the function `annualize_log_return` with the arguments `daily_log_returns_eqr`. Set it to the variable `annualized_log_return_eqr`. Then print the results. 

# In[17]:


annualized_log_return_eqr = annualize_log_return(daily_log_returns_eqr)
print(annualized_log_return_eqr)


# ## Calculate Variance of Daily Log Returns

# 18. Calculate the variance of the daily logarithmetic return. Use the function `.var()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_varaince_eqr`. Then print the results. 

# In[18]:


daily_varaince_eqr = np.var(daily_log_returns_eqr)
print(daily_varaince_eqr)


# ## Calculate Standard Deviation

# 19. Calculate the Standard Deviation of the daily logarithmetic return. Use the function `.std()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_sd_eqr`. Then print the results. 

# In[19]:


daily_sd_eqr = np.std(daily_log_returns_eqr)
print(daily_sd_eqr)


# ## Calculate the Correlation between SBRA and EQR

# 20. Calculate the Correlation of the daily logarithmetic return between SBRA and ERQ assets. Use the function `.corrcoef()` with the arguments `daily_log_returns_sbra` and `daily_log_returns_eqr`. Set it to the variable `corr_sbra_eqr`. Then print the results. 

# In[20]:


corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra,daily_log_returns_eqr)
print(corr_sbra_eqr)


# The dates have to be equivalent for corrcoef to work. The dates are for all of 2018 for EBR and SBRA
