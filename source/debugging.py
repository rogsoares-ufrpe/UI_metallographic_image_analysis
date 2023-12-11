# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import numpy as np
import matplotlib.pyplot as plt

areas = np.array([12317.5, 12319.0, 12319.0, 12316.5, 12319.0, 12319.0, 12319.0,
                  12319.0, 12319.0, 12319.0, 12319.0, 12319.0, 12316.5, 12319.0,
                  12319.0, 12313.0, 12313.0])


plt.bar(np.linspace(1,len(areas), len(areas) ), areas)
plt.yscale('log')
plt.yticks([1e4, 1.25e4])
plt.show()
