import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.diagnostic as sm

years = [i for i in range(1987, 2014) if i != 1996]
la_total = [3958, 4422, 4927, 5236, 5044, 4808, 4725, 4731, 4651, 4952, 5060, 5204, 5490, 5737, 5883, 6402, 7194, 7062, 7222, 7785, 7641, 7531, 7182, 7148, 7504, 7510]
la_away = [1678, 1861, 2188, 2254, 2026, 1891, 1852, 1854, 1892, 2003,2110, 2192, 2303, 2529, 2688, 2895, 3131, 3185, 3349, 3528, 3343, 3271, 3240, 3189, 3166, 3056]
la_ratio = [float(la_away[i])/la_total[i] for i in range(len(la_total))]

sf_total = [4290, 4422, 4827, 5292, 5284, 5212, 5337, 5349, 5220, 6174, 6377, 6963, 7442, 6966, 6453, 6551, 7108, 7581, 7942, 8369, 8393, 7952, 7920, 8260, 8433, 8401]
sf_away = [1894, 1861, 2210, 2543, 2252, 2035, 2103, 2165, 2060, 2364, 2465, 2749, 3086, 3064, 3029, 2923, 3212, 3672, 3769, 3994, 4070, 3672, 3706, 3959, 3908, 3850]
sf_ratio = [float(sf_away[i])/sf_total[i] for i in range(len(sf_total))]

#<<<<Plot comparing LA and SF Total Food Spending>>>>

#plt.scatter(years, la_total)
#plt.plot(years, la_total)
#plt.scatter(years, sf_total, color = 'red')
#plt.plot(years, sf_total, color = 'red')
#plt.xlabel("Years")
#plt.ylabel("Dollars")
#plt.title("Average Total Expenditure on Food")
#plt.legend(["Los Angeles", "San Francisco"], loc = 4)
#plt.show()

#<<<Plot comparing LA and SF Food Away From Home Spending>>>>

#plt.scatter(years, la_away)
#plt.plot(years, la_away)
#plt.scatter(years, sf_away, color = 'red')
#plt.plot(years, sf_away, color = 'red')
#plt.xlabel("Years")
#plt.ylabel("Dollars")
#plt.title("Average Expenditure on Food Away From Home")
#plt.legend(["Los Angeles", "San Francisco"], loc = 4)
#plt.show()

#<<<<LA Analysis>>>>
#Generate the linear regression parameters for LA based on total spending and away from home spending
lareg_param_total = np.polyfit(years, la_total, 1)
lareg_param_away = np.polyfit(years, la_away, 1)

#Use these parameters to generate points on the regression line
lareg_values_total = [lareg_param_total[0] * i + lareg_param_total[1] for i in years]
lareg_values_away = [lareg_param_away[0] * i + lareg_param_away[1] for i in years]

#<<<<Plot Regression Line of Total Spending>>>>

#plt.scatter(years, la_total)
#plt.plot(years, la_total)
#plt.plot(years, , color = 'red')
#plt.xlabel("Years")
#plt.ylabel("Dollars")
#plt.title("Average Total Expenditure on Food in LA")
#plt.legend(["Los Angeles", "Linear Regression Line"], loc = 4)
#plt.show()

#Compute Error Statistics for total Food Spending
lasqr_err_total = [(la_total[i] - lareg_values_total[i])**2 for i in range(len(years))]
laerr_total = np.sqrt(lasqr_err_total)
laavg_err_total = np.sqrt(np.mean(lasqr_err_total))

#Check the number of years that the error exceeded the average error
laexceptions_total = 0
for i in range(len(years)):
    if laerr_total[i] >= laavg_err_total:
        laexceptions_total = laexceptions_total + 1

print lareg_param_total[0]*2014 + lareg_param_total[1]
print "Total Error = " + str(laavg_err_total)
print "Total Food Expenditure Exceptions in LA = " + str(laexceptions_total)
print "Mean Error of Last 5 Years in LA = " + str(np.mean(laerr_total[-5:]))

#Compute Error Statistics for Away from Home Spending
lasqr_err_away = [(la_away[i] - lareg_values_away[i])**2 for i in range(len(years))]
laerr_away = np.sqrt(lasqr_err_away)
laavg_err_away = np.sqrt(np.mean(lasqr_err_away))

laexceptions_away = 0
for i in range(len(years)):
    if laerr_away[i] >= laavg_err_away:
        laexceptions_away = laexceptions_away + 1

print lareg_param_away[0]*2014 + lareg_param_away[1]
print "Total Error = " + str(laavg_err_away)
print "Food Away From Home Expenditure Exceptions in LA = " + str(laexceptions_away)
print "Mean Error of Last 5 Years in LA = "+ str(np.mean(laerr_away[-5:]))

#<<<<Plot Regression Line for Away from Spending>>>>

#plt.scatter(years, la_away)
#plt.plot(years, la_away)
#plt.plot(years, lareg_values_away, color = 'red')
#plt.xlabel("Years")
#plt.ylabel("Dollars")
#plt.title("Average Total Expenditure on Food Away From Home in LA")
#plt.legend(["Los Angeles", "Linear Regression Line"], loc = 4)
#plt.show()

#Compute 'growth rate' in away from home spending each year.
la_away_gr = [la_away[i] - la_away[i - 1] if years[i] - years[i - 1] == 1 else (la_away[i] - la_away[i - 1])/2.0 for i in range(1, len(years))]
print la_away_gr

la_away_gr_mean = np.mean(la_away_gr)
la_away_gr_var = np.var(la_away_gr)

plt.hist(la_away_gr)
plt.title("Histogram of Year on Year Differences in Spending Away from Home in LA")
plt.show()

print "Annual Growth Rate Average = " + str(la_away_gr_mean)
print "Annual Growth Rate Variance = " + str(la_away_gr_var)
print "Annual Growth Rate Standard Deviation = " + str(np.sqrt(la_away_gr_var))

la_gr_ksstat = sm.lillifors(la_away_gr)[0]
if la_gr_ksstat <= 1.035:
    #This number is the 0.01 significance level critical value to apply the K-S Test on a normal population with estimated mean and variance
    print "LA Growth fits Normal Dist."


print "End LA"
#<<<<End LA>>>>

print "Begin SF"
#<<<<SF Analysis>>>>

#Generate the linear regression parameters for LA based on total spending and away from home spending
sfreg_param_total = np.polyfit(years, sf_total, 1)
sfreg_param_away = np.polyfit(years, sf_away, 1)


#Use these parameters to generate points on the regression line
sfreg_values_total = [sfreg_param_total[0] *i + sfreg_param_total[1] for i in years]
sfreg_values_away = [sfreg_param_away[0] * i + sfreg_param_away[1] for i in years]

#<<<<Plot Regression Line of Total Spending>>>>

plt.scatter(years, sf_total)
plt.plot(years, sf_total)
plt.plot(years, sfreg_values_total, color = 'red')
plt.xlabel("Years")
plt.ylabel("Dollars")
plt.title("Average Total Expenditure on Food in SF")
plt.legend(["San Francisco", "Linear Regression Line"], loc = 4)
plt.show()

#Compute Error Statistics for total Food Spending
sfsqr_err_total = [(sf_total[i] - sfreg_values_total[i])**2 for i in range(len(years))]
sferr_total = np.sqrt(sfsqr_err_total)
sfavg_err_total = np.sqrt(np.mean(sfsqr_err_total))

#Check the number of years whose error exceeds the average error
sfexceptions_total = 0
for i in range(len(years)):
    if sferr_total[i] >= sfavg_err_total:
        sfexceptions_total = sfexceptions_total + 1

print sfreg_param_total[0]*2014 + sfreg_param_total[1]
print "Total Error = " + str(sfavg_err_total)
print "Total Food Expenditure Exceptions in SF = " + str(sfexceptions_total)
print "Mean Error of Last 5 Years in SF = " + str(np.mean(sferr_total[-5:]))

#Compute Error Statistics for Away from Home Spending
sfsqr_err_away = [(sf_away[i] - sfreg_values_away[i])**2 for i in range(len(years))]
sferr_away = np.sqrt(sfsqr_err_away)
sfavg_err_away = np.sqrt(np.mean(sfsqr_err_away))

sfexceptions_away = 0
for i in range(len(years)):
    if sferr_away[i] >= sfavg_err_away:
        sfexceptions_away = sfexceptions_away + 1

print sfreg_param_away[0]*2014 + sfreg_param_away[1]
print "Total Error = " + str(sfavg_err_away)
print "Food Away From Home Expenditure Exceptions in SF = " + str(sfexceptions_away)
print "Mean Error of Last 5 Years in SF = "+ str(np.mean(sferr_away[-5:]))

#<<<<Plot Regression Line for Away from Spending>>>>

plt.scatter(years, sf_away)
plt.plot(years, sf_away)
plt.plot(years, sfreg_values_away, color = 'red')
plt.xlabel("Years")
plt.ylabel("Dollars")
plt.title("Average Total Expenditure on Food Away From Home in SF")
plt.legend(["San Francisco", "Linear Regression Line"], loc = 4)
plt.show()

#Compute 'growth rate' in away from home spending each year.
sf_away_gr = [sf_away[i] - sf_away[i - 1] if years[i] - years[i - 1] == 1 else (sf_away[i] - sf_away[i - 1])/2.0 for i in range(1, len(years))]
print sf_away_gr
sf_away_gr_mean = np.mean(sf_away_gr)
sf_away_gr_var = np.var(sf_away_gr)
plt.hist(sf_away_gr)
plt.title("Histogram of Year on Year Differences in Spending Away from Home in SF")
plt.show()
sf_gr_ksstat = sm.lillifors(sf_away_gr)[0]

if sf_gr_ksstat <= 1.035:
    print "SF Growth fits Normal Dist."

print "Annual Growth Rate Average = " + str(sf_away_gr_mean)
print "Annual Growth Rate Variance = " + str(sf_away_gr_var)
print "Annual Growth Rate Standard Deviation = " + str(np.sqrt(sf_away_gr_var))

print "End SF"
#<<<<Plot Showing fraction of Food Spending that is Away From Home>>>>

plt.scatter(years, la_ratio)
plt.plot(years, la_ratio)
plt.hlines(np.mean(la_ratio), 1987, 2013, linestyles = 'dashed', color = 'blue')
plt.scatter(years, sf_ratio)
plt.plot(years, sf_ratio)
plt.hlines(np.mean(sf_ratio), 1987, 2013, linestyles = 'dotted', color = 'red')
plt.xlabel("Years")
plt.legend(["Los Angeles", "San Francisco"], loc = 4)
plt.title("Ratios")
plt.show()

print np.mean(sf_ratio)
print np.mean(la_ratio)