import numpy as np

# Set the parameters below
################################################################################
# 'beta' of the transistor
beta_F = 200
# Collector resistor
R_C = 1e3
# Device temperature (room temperature is ~300K)
T = 300
# R_1 in the input potential divider
R_2 = 220
# Positive rail voltage
V_p = 15
# Negative rail voltage
V_n = -15
# Base-emitter voltage
V_be = 0.6
# 
R_3 = 10e3

# Constant parameters
################################################################################
k = 1.3806488e-23
q = 1.602e-19

# Automatically derived parameters
################################################################################
# 'alpha' of the transistor
alpha_F = beta_F / (1 + beta_F)
# 
R_1 = R_2 * (q / (2 * k * T) - 1)
# 
I_BIAS = 1 / (alpha_F * R_C)
# 
I_REF = (V_p - V_n - V_be) / R_3
# 
R_4 = np.log(I_REF / I_BIAS) * (k * T) / (q * I_BIAS)

# Print values
################################################################################
print('Input values:\n'
      f'beta_F = {beta_F}\n'
      f'R_C = {R_C}\n'
      f'T = {T}\n'
      f'R_2 = {R_2}\n'
      f'V_p = {V_p}\n'
      f'V_n  = {V_n}\n'
      f'V_be = {V_be}\n'
      f'R_3 = {R_3}\n')

print('Output values:\n'
      f'alpha_F = {alpha_F}\n'
      f'R_1 = {R_1}\n'
      f'I_BIAS = {I_BIAS}\n'
      f'I_REF = {I_REF}\n'
      f'R_4 = {R_4}\n')