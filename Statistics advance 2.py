#!/usr/bin/env python
# coding: utf-8

# Q1: What are the Probability Mass Function (PMF) and Probability Density Function (PDF)? Explain with
# an example.

# Probability mass function denotes the probability that a discrete random variable will take on a particular value. Probability density function gives the probability that a continuous random variable will lie between a certain specified interval. It is used for discrete random variables.

# Q2: What is Cumulative Density Function (CDF)? Explain with an example. Why CDF is used?

# The cumulative distribution function (cdf) gives the probability that the random variable X is less than or equal to x and is usually denoted F(x)
# 
# The cumulative distribution function, CDF, is a function whose output is the probability that X is less than or equal to the input. Denoted always by the capital letter F, its mathematical notation is written as F ( x 0 ) = P ( X ≤ x 0 ) . So, if the input is 3, F ( 3 ) = P ( X ≤ 3 ) 

# Q9: What is Central Limit Theorem? State the significance of the Central Limit Theorem.

# The central limit theorem relies on the concept of a sampling distribution, which is the probability distribution of a statistic for a large number of samples taken from a population.
# 
# Imagining an experiment may help you to understand sampling distributions:
# 
# Suppose that you draw a random sample from a population and calculate a statistic for the sample, such as the mean.
# Now you draw another random sample of the same size, and again calculate the mean.
# You repeat this process many times, and end up with a large number of means, one for each sample.
# 
# The distribution of the sample means is an example of a sampling distribution.
# 
# The central limit theorem says that the sampling distribution of the mean will always be normally distributed, as long as the sample size is large enough. Regardless of whether the population has a normal, Poisson, binomial, or any other distribution, the sampling distribution of the mean will be normal.
# 
# 
# Significance of Central Limit Theorem
# 
# The CLT has several applications. Look at the places where you can use it.
# 
# Political/election polling is a great example of how you can use CLT. These polls are used to estimate the number of people who support a specific candidate. You may have seen these results with confidence intervals on news channels. The CLT aids in this calculation.
# You use the CLT in various census fields to calculate various population details, such as family income, electricity consumption, individual salaries, and so on.
# 

# Q10: State the assumptions of the Central Limit Theorem.

# The data must adhere to the randomization rule. It needs to be sampled at random.
# The samples should be unrelated to one another. One sample should not impact the others.
# When taking samples without replacement, the sample size should not exceed 10% of the population.
# 

# Q8: What is the z score? State the importance of the z score.

# Z-score is a statistical measurement that describes a value's relationship to the mean of a group of values. Z-score is measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean. 

# Q7: Explain uniform Distribution with an example.

# uniform distribution is a term used to describe a form of probability distribution where every possible outcome has an equal likelihood of happening. The probability is constant since each variable has equal chances of being the outcome.
# 
# For example, if you stand on a street corner and start to randomly hand a RS 100 bill to any lucky person who walks by, then every passerby would have an equal chance of being handed the money. The percentage of the probability is 1 divided by the total number of outcomes (number of passersby). However, if you favored short people or women, they would have a higher chance of being given the RS 100 bill than the other passersby. It would not be described as uniform probability.
# 
# A deck of cards also has a uniform distribution. It is because an individual has an equal chance of drawing a spade, a heart, a club, or a diamond. Another example of a uniform distribution is when a coin is tossed. The likelihood of getting a tail or head is the same. The graph of a uniform distribution is usually flat, whereby the sides and top are parallel to the x- and y-axes.

# Q5: What is Bernaulli Distribution? Give an Example. What is the difference between Bernoulli
# Distribution and Binomial Distribution?

# Bernoulli distribution is a discrete distribution in which the random variable has only two possible outcomes and a single trial known as a Bernoulli.
# 
# Every time you flip a coin, there are only two possible outcomes. It either lands on heads or it lands on tails, and there's a 50% chance of either outcome. A coin flip is an example of a Bernoulli trial, which is any random experiment in which there are exactly two possible outcomes.
# 
# 
# Bernoulli deals with the outcome of the single trial of the event, whereas Binomial deals with the outcome of the multiple trials of the single event.Bernoulli is used when the outcome of an event is required for only one time, whereas the Binomial is used when the outcome of an event is required multiple times.
# 

# Q4: Explain the importance of Normal Distribution. Give a few real-life examples of Normal
# Distribution.

# The Normal Distribution, also known as the Gaussian Distribution, is one of the most fundamental concepts in statistics and probability theory. Its importance lies in its widespread applicability across various fields due to its unique properties.
# 
# 1. **Central Limit Theorem**: The Normal Distribution plays a crucial role in the Central Limit Theorem, which states that the distribution of the sum (or average) of a large number of independent, identically distributed random variables approaches a normal distribution, regardless of the original distribution of the variables. This theorem is fundamental in statistical inference, as it allows us to make conclusions about populations based on samples.
# 
# 2. **Statistical Inference**: In many statistical methods, such as hypothesis testing and confidence interval estimation, assumptions about the distribution of data are made. The Normal Distribution is often assumed due to its mathematical tractability and because many real-world phenomena tend to approximate it.
# 
# 3. **Modeling Natural Phenomena**: Numerous natural phenomena follow a normal distribution. For instance:
#    - Human characteristics like height, weight, and intelligence tend to follow a normal distribution in large populations.
#    - Measurement errors in instruments often approximate a normal distribution.
#    - Random noise in electronic circuits and communication systems often conforms to a normal distribution.
# 
# 4. **Financial Applications**: In finance, the Normal Distribution is commonly used to model asset returns. While market returns are not perfectly normally distributed, many financial models, such as the Black-Scholes option pricing model, assume normally distributed returns for simplicity.
# 
# 5. **Quality Control**: In manufacturing and quality control processes, the Normal Distribution is used to analyze variations in product characteristics. For example, the distribution of product weights or lengths can often be approximated by a normal distribution, allowing manufacturers to set quality control limits and make decisions about product acceptance.
# 
# 6. **Biological Sciences**: Various biological measurements, such as blood pressure, enzyme activity, and birth weights, often exhibit a normal distribution in populations.
# 
# In essence, the Normal Distribution serves as a foundational concept in statistics and provides a convenient framework for understanding and modeling a wide range of phenomena in fields ranging from natural sciences to social sciences to finance. Its ubiquity makes it a powerful tool for analysis and inference in many practical scenarios.

# Q3: What are some examples of situations where the normal distribution might be used as a model?
# Explain how the parameters of the normal distribution relate to the shape of the distribution.

# 1. **Height of Individuals**: In a large population, heights tend to follow a normal distribution, with most people clustered around the average height and fewer people at the extreme ends of the height spectrum.
# 
# 2. **Exam Scores**: When many students take an exam, their scores often approximate a normal distribution, assuming the exam is well-designed and covers a broad range of difficulty levels.
# 
# 3. **Measurement Errors**: Errors in measurement instruments, such as rulers, scales, or thermometers, can often be modeled using a normal distribution. These errors may arise due to factors like precision limitations or environmental conditions.
# 
# 4. **Blood Pressure**: Blood pressure readings in a population often exhibit a bell-shaped curve when plotted, with most individuals clustering around the average blood pressure.
# 
# 5. **IQ Scores**: Intelligence quotient (IQ) scores across a large population tend to be normally distributed, with the majority of people falling within the average range and fewer individuals at the extreme ends of the intelligence spectrum.
# 
# Regarding the parameters of the normal distribution and their relationship to the shape of the distribution:
# 
# 1. **Mean (μ)**: The mean of a normal distribution determines the center or the average value around which the data is symmetrically distributed. It is the point of maximum probability density. Shifting the mean to the left or right changes the location of the peak of the curve without altering its shape.
# 
# 2. **Standard Deviation (σ)**: The standard deviation of a normal distribution measures the spread or dispersion of the data points around the mean. A smaller standard deviation indicates that the data points are closely clustered around the mean, resulting in a narrow and tall bell-shaped curve. Conversely, a larger standard deviation indicates that the data points are more spread out from the mean, resulting in a wider and shorter bell-shaped curve.
# 
# Together, the mean and standard deviation uniquely determine the shape, location, and spread of the normal distribution. Adjusting these parameters can transform the distribution to better fit observed data or to represent different scenarios in real-life applications.

# In[ ]:




