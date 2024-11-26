from stats import *
import numpy as np
import matplotlib.pylab as plt
from scipy.stats import ttest_ind, ttest_rel, mannwhitneyu, wilcoxon

#  Single-test at end of the experiment
np.random.seed(8675309)
N = 40
control = np.random.randint(80,92,N)
treatment = np.random.randint(83,95,N)

print("Control:")
print(control)
print()
print("Treatment:")
print(treatment)
print()

print("Summary stats:")
mm,md,mo,st,ma = amean(control),median(control),mode(control),std(control),mad(control)
print("    Controls : mean: %0.2f, median: %0.2f, std: %0.2f, mad: %0.2f, mode:" % (mm,md,st,ma),mo)
mm,md,mo,st,ma = amean(treatment),median(treatment),mode(treatment),std(treatment),mad(treatment)
print("    Treatment: mean: %0.2f, median: %0.2f, std: %0.2f, mad: %0.2f, mode:" % (mm,md,st,ma),mo)
print()

ds = np.zeros((N,2))
ds[:,0] = control
ds[:,1] = treatment

plt.boxplot(ds, showmeans=True, labels=['Control','Treatment'])
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("memory_boxplot_single.eps", dpi=300)
plt.close()

t,p = ttest_ind(treatment, control, equal_var=False)
_,u = mannwhitneyu(treatment, control)
tcrit = t_critical(treatment, control, alpha=0.05)
lo = (amean(treatment) - amean(control)) - tcrit*np.sqrt(std(treatment)**2/len(treatment) + std(control)**2/len(control))
hi = (amean(treatment) - amean(control)) + tcrit*np.sqrt(std(treatment)**2/len(treatment) + std(control)**2/len(control))

print("Single test at end of the experiment:")
print("    t-test: (t=%0.5f, p=%0.6f), Mann-Whitney U (p=%0.5f)" % (t,p,u))
print("    Cohen's d for independent samples = %0.4f" % Cohen_d(treatment,control))
print("    95%% CI: [%0.5f, %0.5f]" % (lo,hi))
print()

#  Paired tests -- pre and post treatment tests
control0 = np.random.randint(80,92,N)
treatment0 = np.random.randint(80,92,N)

control1 = np.random.randint(80,92,N)
treatment1 = np.random.randint(83,95,N)

print("Control:")
print(control0)
print(control1)
print()
print("Treatment:")
print(treatment0)
print(treatment1)
print()

print("Paired tests: pre and post results:")

tc,pc = ttest_rel(control1, control0)
_,wc = wilcoxon(control1, control0)
tcrit = t_critical(control1,control0, alpha=0.05, paired=True)
d = [control1[i] - control0[i] for i in range(len(control1))]
lo_c = amean(d) - tcrit * std(d) / np.sqrt(len(control1))
hi_c = amean(d) + tcrit * std(d) / np.sqrt(len(control1))

tt,pt = ttest_rel(treatment1, treatment0)
_,wt = wilcoxon(treatment1, treatment0)
tcrit = t_critical(treatment1,treatment0, alpha=0.05, paired=True)
d = [treatment1[i] - treatment0[i] for i in range(len(treatment1))]
lo_t = amean(d) - tcrit * std(d) / np.sqrt(len(treatment1))
hi_t = amean(d) + tcrit * std(d) / np.sqrt(len(treatment1))

print("    Controls : paired t-test: (t=%0.5f, p=%0.6f), paired Wilcoxon (p=%0.5f)" % (tc,pc,wc))
print("               Cohen d for paired samples = %0.4f" % Cohen_d(control1,control0,paired=True))
print("               95%% CI: [%0.5f, %0.5f]" % (lo_c,hi_c))
print()
print("    Treatment: paired t-test: (t=%0.5f, p=%0.6f), paired Wilcoxon (p=%0.5f)" % (tt,pt,wt))
print("               Cohen d for paired samples = %0.4f" % Cohen_d(treatment1,treatment0,paired=True))
print("               95%% CI: [%0.5f, %0.5f]" % (lo_t,hi_t))
print()

