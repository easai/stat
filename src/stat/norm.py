from scipy.stats import norm

# mean
loc = 100
# standard deviation
scale = 3

p = norm.cdf(x=90, loc=loc, scale=scale)  # 0.00042

# norm.ppf(q=パーセント, loc=平均, scale=標準偏差)

print("quantile q(.1) alpha=.05")
print(norm.ppf(q=1-.1, loc=0, scale=1))

print("quantile q(.05) alpha=.05")
print(norm.ppf(q=1-.05, loc=0, scale=1))

print("quantile q(.025) alpha=.025")
print(norm.ppf(q=1-.025, loc=0, scale=1))
