val_kecerdasan = [
[2,4,3,3,2,2,4,3,2,3,'O1'],
[3,4,3,3,2,3,4,2,4,4,'O2']
]
val_kinerja = [
[3,4,3,1,3,1,'O1'],
[4,5,5,1,4,1,'O2']
]
val_perilaku = [
[4,4,4,4,'O1'],
[4,3,4,4,'O2']
]

target_kecerdasan = [3,3,4,4,3,4,4,5,3,4]
target_kinerja = [3,4,2,3,3,5]
target_perilaku = [3,3,4,5]

cf_kecerdasan = [1,2,5,8,9]
sf_kecerdasan = [3,4,6,7,10]

cf_kinerja = [1,2,5]
sf_kinerja = [3,4,6]

cf_perilaku = [1,2]
sf_perilaku = [3,4]

ni_cf = 60/100
ni_sf = 40/100

nr_kecerdasan = 20/100
nr_kinerja = 30/100
nr_perilaku = 50/100

selisih_bobot = [[0,1,-1,2,-2,3,-3,4,-4],[5,4.5,4,3.5,3,2.5,2,1.5,1]]

#======================== difference ==============

diff_kecerdasan = []
diff_kinerja = []
diff_perilaku = []

for i in range(len(val_kecerdasan)):
	diff_kecerdasan.append([])
	a = val_kecerdasan[i]
	for j in range(len(target_kecerdasan)):
		diff_kecerdasan[i].append(a[j]-target_kecerdasan[j])
	diff_kecerdasan[i].append('Org'+str(i+1))

for i in range(len(val_kinerja)):
	diff_kinerja.append([])
	a = val_kinerja[i]
	for j in range(len(target_kinerja)):
		diff_kinerja[i].append(a[j]-target_kinerja[j])
	diff_kinerja[i].append('Org'+str(i+1))

for i in range(len(val_perilaku)):
	diff_perilaku.append([])
	a = val_perilaku[i]
	for j in range(len(target_perilaku)):
		diff_perilaku[i].append(a[j]-target_perilaku[j])
	diff_perilaku[i].append('Org'+str(i+1))

#================= N result =============
n_kecerdasan = []
n_kinerja = []
n_perilaku = []
sb1 = selisih_bobot[0]
sb2 = selisih_bobot[1]
for i in range(len(val_kecerdasan)):
	n_k = diff_kecerdasan[i]
	n = 0
	for j in cf_kecerdasan:
		l = n_k[j-1]
		m = sb2[sb1.index(l)]
		n += m
		cf = n / len(cf_kecerdasan)
	n = 0
	for k in sf_kecerdasan:
		l = n_k[k-1]
		m = sb2[sb1.index(l)]
		n += m
		sf = n / len(sf_kecerdasan)
	n_kecerdasan.append((cf*ni_cf)+(sf*ni_sf))

for i in range(len(val_kinerja)):
	n_k = diff_kinerja[i]
	n = 0
	for j in cf_kinerja:
		l = n_k[j-1]
		m = sb2[sb1.index(l)]
		n += m
		cf = n / len(cf_kinerja)
	n = 0
	for k in sf_kinerja:
		l = n_k[k-1]
		m = sb2[sb1.index(l)]
		n += m
		sf = n / len(sf_kinerja)
	n_kinerja.append((cf*ni_cf)+(sf*ni_sf))

for i in range(len(val_perilaku)):
	n_k = diff_perilaku[i]
	n = 0
	for j in cf_perilaku:
		l = n_k[j-1]
		m = sb2[sb1.index(l)]
		n += m
		cf = n / len(cf_perilaku)
	n = 0
	for k in sf_perilaku:
		l = n_k[k-1]
		m = sb2[sb1.index(l)]
		n += m
		sf = n / len(sf_perilaku)
	n_perilaku.append((cf*ni_cf)+(sf*ni_sf))

#===================== rangking
result = []
for i in range(len(val_kecerdasan)):
	result.append([(n_kecerdasan[i] * nr_kecerdasan)+(n_kinerja[i] * nr_kinerja)+(n_perilaku[i] * nr_perilaku),'Orang'+str(i+1)])
print(result)