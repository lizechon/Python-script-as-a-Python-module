# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:27:49 2023

@author: echon
"""

import loanpackage as lp

PV= 2000
r = 7
n = 12

pmt = lp.computesPmt(PV, r, n)
print(f"Monthly Payment = {pmt}")
