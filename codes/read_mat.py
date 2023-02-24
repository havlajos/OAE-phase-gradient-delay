#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 08:56:32 2022

@author: vencov
"""

import numpy as np
import matplotlib.pyplot as plt
#from scipy.io.wavfile import read
import scipy.io

plt.close('all')

# uncomment for Mac or Linux
'''
mat = scipy.io.loadmat(
    'data/SFOAE/sfoae20dBg130TM45R19rs2.mat')  # measured in 2021
'''

mat = scipy.io.loadmat(
    '/Users/vojta/Desktop/Josie/ČVUT/Bakalářská práce - OAE/data/SFOAE/sfoae20dBg130TM45R19rs2.mat')  # measured in 2021


fvect = mat['Fvect'].flatten()  # frequency axis
SFOAE = mat['oaeNum20'].flatten()  # celkove SFOAE
CRcomp = mat['CRc20'].flatten()  # CR komponenta
NLcomp = mat['Yunl20'].flatten()  # NL komponenta

#phase = np.angle(SFOAE)


fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(fvect, 20*np.log10(SFOAE), 'b')
ax.plot(fvect, 20*np.log10(CRcomp), 'r')
ax.plot(fvect, 20*np.log10(NLcomp), 'g')
#ax.plot(fvect, 20*np.log10(phase), 'y')
ax.set_xscale('log')
ax.set_xlim([1000, 3.8e3])
ax.set_ylim([-140, -70])
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Sound pressure level (dB)')
plt.show()
