## Sebelum di tukar menjadi little endian

arr = ['0e','17','06','10','00','06','08','00','0f','12','17','06','18','48','3c'
,'04','0c','0f','1b','17','30','0c','03','0f','16','0c','29','1d','0d','11','31','1d','3c','3e','36','3c','36'
,'29','0a','0e','46','1a','3c','10','19','04','0b','1f','09','01','0c','3e','14','0d']

for i in range(0,len(arr),2):
	arr[i],arr[i+1]=arr[i+1],arr[i]

## penukaran menjadi little endian

k="vibonacci"
s=""
j=0
for i in range(len(arr)): 
	j=j%9 
	arr[i]=int(arr[i],16)^ord(k[j]) 
	j=j+1
## proses baby xor	

	
for i in range(len(arr)): 
	s+=chr(arr[i]) 
	
print(s)
#hasilnya
