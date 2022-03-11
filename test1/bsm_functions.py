"""
    作者：xiao-yi.yu
    日期：2019/10/17
    功能：求期权的隐含波动率
    版本：1.0
"""


def bsm_call_value(so_price, K, T, r, sigma):
    from math import log, sqrt, exp
    from scipy import stats
    s0 = float(so_price)
    d1= (log(so_price / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2= (log(so_price / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value= (so_price * stats.norm.cdf(d1, 0.0, 1.0)) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0)
    return value

def bsm_vega(S0,K,T,r,sigma):
    from math import log,sqrt
    from scipy import stats
    
    S0=float(S0)
    d1=(log(S0/K)+(r+0.5*sigma**2)*T)/(sigma*sqrt(T))
    vega=S0*stats.norm.pdf(d1,0.0,1.0)*sqrt(T)
    return vega

def bsm_call_imp_vol(S0,K,T,r,C0,sigma_est,it=100):
    for i in range(it):
        sigma_est-=((bsm_call_value(S0,K,T,r,sigma_est)-C0)
                 /bsm_vega(S0,K,T,r,sigma_est))
    return sigma_est

