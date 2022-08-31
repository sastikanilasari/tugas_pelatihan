"""
Identitas:
Nama: Sastika Nilasari
Email: sastikanila123@gmail.com
"""

#impor library plot
from matplotlib import pyplot as plt

#impor untuk numpy
import numpy as np

#data dasar
labels = ['Matematika','Fisika', 'Kimia', 'Biologi','Bahasa Inggris', 'Bahasa Indonesia']
men_means = [80, 82, 79, 81, 85, 89]
women_means = [79, 83, 78, 85, 88, 88]

x = np.arange(len(labels)) #lokasi label tiap mata pelajaran
width = 0.35 #lebar bar

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label = 'Men')
rects2 = ax.bar(x + width/2, women_means, width, label = 'Women')

#Menambhakan text pada label, judul, dan legenda
ax.set_ylabel('Nilai')
ax.set_title('Nilai berdasarkan Mata Pelajaran dan Jenis Kelamin')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding = 3)
ax.bar_label(rects2, padding = 3)

fig.tight_layout()

plt.show()