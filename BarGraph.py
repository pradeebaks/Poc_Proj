#import matplotlib.pyplot as plt;

#plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

xname = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp','lite']
yvalue = [50, 8, 6, 4, 2, 1,30]
#noX = list (range(len(xname)))
plt.bar(xname, yvalue)
plt.ylabel('Usage')
plt.xlabel("Language")
plt.title('Programming language usage')
plt.show()
