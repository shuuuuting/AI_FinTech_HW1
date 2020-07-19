#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

call = {10700:266,10800:189,10900:120,11000:67,11100:32,11200:13,11300:6.1}
put = {10700:43,10800:63,10900:93,11000:139,11100:207,11200:290,11300:360}
x= np.arange(10500,11501)

def callr(K):
    global x
    global call
    return np.maximum(x-K,0)-call[K]

def putr(K):
    global x
    global put
    return np.maximum(K-x,0)-put[K]

#第一題
#買權
y1 = callr(10900)-callr(11000)
y2 = callr(11000)-callr(11100)
y3 = callr(10900)-callr(11100)
#plt.plot(x,y1,'cornflowerblue',x,y2,'b',x,y3,'darkblue',[x[0],x[-1]],[0,0],'--k')
#賣權
y4 = putr(10900)-putr(11000)
y5 = putr(11000)-putr(11100)
y6 = putr(10900)-putr(11100)
#plt.plot(x,y4,'lightcoral',x,y5,'r',x,y6,'brown',[x[0],x[-1]],[0,0],'--k')

#第二題
#straddle
y7 = -callr(11000)-putr(11000)
#strangle
y8 = -callr(11200)-putr(10800)
#plt.plot(x,y7,'indianred',x,y8,'seagreen',[x[0],x[-1]],[0,0],'--k')

#第三題
#butterfly spread
y9 = callr(10900)+callr(11100)-callr(11000)*2
y10 = callr(10800)+callr(11200)-callr(11000)*2
plt.plot(x,y9,x,y10,[x[0],x[-1]],[0,0],'--k')