import matplotlib.pyplot as plt
from uncertainties import ufloat


data = '''
0.947739 -- 0.218967
0.948277 -- 0.188794
0.943390  -- 0.173533
0.943300  -- 0.160800
'''

stopping_v_vals = []
photocurrent_v_vals = []

for line in data.split('\n'):
    if line:
        stopping_v, photocurrent_v = line.split('--')
        stopping_v_vals.append(float(stopping_v))
        photocurrent_v_vals.append(float(photocurrent_v))

# add uncertainty
stopping_v_err = 0.0000005
photocurrent_v_err = 0.0000005

for i in range(len(stopping_v_vals)):
    stopping_v_vals[i] = ufloat(stopping_v_vals[i], stopping_v_err)
    photocurrent_v_vals[i] = ufloat(photocurrent_v_vals[i], photocurrent_v_err)


# reverse the list
stopping_v_vals = stopping_v_vals[::-1]
photocurrent_v_vals = photocurrent_v_vals[::-1]


plt.xkcd()

# Create two subplots
fig, (ax2, ax1) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

fig.suptitle('Photocurrent Voltage and Stopping Voltage vs Intensity Setting')

color = 'tab:red'
# Plot the data in the top subplot
ax1.set_ylabel('Photocurrent Voltage (V)')
ax1.set_xlabel('Intensity setting')
ax1.errorbar(range(len(photocurrent_v_vals)), [val.n for val in photocurrent_v_vals], yerr=[
             val.s for val in photocurrent_v_vals], color=color, fmt='o')
ax1.plot(range(len(photocurrent_v_vals)), [
         val.n for val in photocurrent_v_vals], color=color)

color = 'tab:blue'
# Plot the data in the bottom subplot

ax2.set_ylabel('Stopping Voltage (V)')
ax2.errorbar(range(len(stopping_v_vals)), [val.n for val in stopping_v_vals], yerr=[
             val.s for val in stopping_v_vals], color=color, fmt='o')
ax2.plot(range(len(stopping_v_vals)), [
         val.n for val in stopping_v_vals], color=color)

# Set the limits of the y-axis for each subplot
ax1.set_ylim(0.15, 0.250)
ax2.set_ylim(0.93, 1.03)


fig.tight_layout()
plt.savefig('Results/Part2/Part2.png')
