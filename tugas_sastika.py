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
labels = ['Matematika','Fisika', 'Kimia', 'Biologi','Bahasa Inggris', 'Bahasa Indonesia'] #nama mata pelajaran
men_means = [80, 82, 79, 81, 85, 89] #nilai rata-rata men pada setiap mata pelajaran
women_means = [79, 83, 78, 85, 88, 88] #nilai rata-rata women pada setiap mata pelajaran

x = np.arange(len(labels)) #lokasi label tiap mata pelajaran
width = 0.35 #lebar bar 

fig, ax = plt.subplots() #letak subplot
rects1 = ax.bar(x - width/2, men_means, width, label = 'Men') #letak bar men
rects2 = ax.bar(x + width/2, women_means, width, label = 'Women') #letak bar women

#Menambhakan text pada label, judul, dan legenda
ax.set_ylabel('Nilai') #label sumbu-y
ax.set_title('Nilai berdasarkan Mata Pelajaran dan Jenis Kelamin') #judul grafik
ax.set_xticks(x, labels) #nama label
plt.xticks(rotation=45) #merotasikan label
ax.legend() #menambahkan legenda

ax.bar_label(rects1, padding = 3) #jarak antar bar men
ax.bar_label(rects2, padding = 3) #jarak antar bar women

fig.tight_layout()

plt.show()