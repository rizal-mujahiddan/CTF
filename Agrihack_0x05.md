# Agrihack 0x05

Agrihack merupakan Ajang untuk penyeleksian menjadi anggota CSI(Cyber Security IPB). CSI merupakan komunitas yang berada di ilmu komputer yang prestise di ilmu komputer IPB

## Crpytography

### 1. Base64
[file](https://drive.google.com/drive/folders/1WUNUQX8EpcEXnz9HMS59zdoqlzx1rM65?usp=sharing) ini dengan isinya `YWdyaWhhY2t7YmFzaWNfdG9fa25vd19iYXNlNjR9`. DIkarenakan judulnya itu base64 maka bisa kita di dekripsi dengan [tools](http://rumkin.com/tools/cipher/base64.php) ini maka hasilnya
![](foto/base64.png)
adalah <br/>
```agrihack{basic_to_know_base_64}```

### 2. crypto/Introduction to Cipher_Series : ROMAN
dikarenakan didalam foto tersebut ada data foto caesar.png yang ada kluenya dengan menggunakan _caesar cipher_ maka dengan [tools](http://rumkin.com/tools/cipher/caesar.php) ini dan teks `rxizyrtb{Xrzlj_Alczlj_Trvjri}` maka akan menghasilkan ```agrihack{Gaius_Julius_Caesar}``` <br/> ![](foto/Roman.png)<br/>
<a href="https://drive.google.com/file/d/1NwgB5Bzkb8AO0z2aSKYhHjzew92FbtH1/view">caesar.png</a>

### 3. Introduction to Cipher_Series : GiovanBattistaBellaso
dengan meninjau dan memahami gambar dari foto ini <br/><br/>
![](foto/giovani_battista_bellaso.jpg)<br/><br/>
dan mencari tahu bahwa dia adalah [penemu vighere cipher](https://en.wikipedia.org/wiki/Giovan_Battista_Bellaso) dan dengan gambar kunci tersebut adalah `key :"vibonacci"`<br/>
`ciphertext :voswuaem{Ddoosee_Ej1x3m'a_I3f3}`
maka dengan [website ini](http://rumkin.com/tools/cipher/vigenere.php) maka ketemulah flagnya yakni
<br/><br/>
![](foto/vigenere.png)
<br/><br/>
flag : `agrihack{Vignere_Ch1p3r's_H3r3}`
[sumber file](https://drive.google.com/drive/folders/1oYDRwOURZPEL9frLmw45Nje_o428Wuce)
### 4. Introduction to Cipher_Series : Talking
lihatlah kata kunci dari hint tersebut `'numbers come after letters, underscore come after numbers'` maka anda akan terkejut dengan ini karena sangat mudah untuk dipecahkan dengan hint ini maka saya akan membuatnya di [notepad](doc/talking_cipher) awal mulanya saya mencurigai `1 7 18 9 8 1 3 11` yang dikonversikan menjadi `agrihack` , maka saya langung mengkonversikan yang lain dan dengan petunjuk hint juga ya maka akan menjadi [ini](doc/boooo.txt)
<br/>
<br/>
![](foto/talking.png)
<br/>
<br/>
[sumber filenya](https://drive.google.com/drive/folders/1sO9aU4fKPLcuhQQEV5FHfdIU6D3VbqmP?usp=sharing)
### 5. BabyXOR
dengan mengikuti saran dari youtube [csi ipb](https://www.youtube.com/watch?v=-elQW05sgV8) dan dikarenakan dari pembuat soal tersebut terinspirasi dari _cyber jawara_ maka kita bisa mengubah UTF-16 menjadi UTF-8 dengan hexdump dan jadikan little endian <br/> <br/> ![](foto/babyxor_hexdump.png) <br/><br/>
dan saya olah dengan sistem babyxor di [python](doc/babyxor.py)<br/><br/>
![](foto/hasil_babyxor.png)<br/>
`agrihack{you've_learn_about_xor_______let's_moving_on}`
[sumber file](https://drive.google.com/drive/folders/18USKvC3aPP1GaG8-M5ZSF5iizZvKp_jj?usp=sharing)
### 6. Password Cracker
dengan hash MD5 `0f7c017187ad3c1d50a65015de71958c` maka dengan [crack ini](https://crackstation.net/)<br/><br/>
![](foto/crack1.png)
<br/><br/>
kemdian tinggal kita masukkan passwordnya `b33f` ke `nc 52.187.65.2 15001`
<br/><br/>
![](foto/crack1_ter.png)
<br/><br/>
`agrihack{brut3f0rc3333_as_1t5_f1n33______b33f}`
### 7. Introduction to Cipher_Series : Matrix
dengan foto seperti <br/> <br/>
![](foto/matrix.jpg)
 <br/> <br/>
maka dengan menyamakan konsep dari soal sebelumnya dari Talking maka akan menjadi seperti [ini](doc/matrix.txt) <br/>
`flag : agrihack{C0lumn4t_Tr4nsp051t1000N}`
<br/>
[sumber_file](https://drive.google.com/drive/folders/1UskrfztjMhYbpp7c3ZEYMTfNMpHh0ori?usp=sharing)
### 8. BabyAES : Introduction
dikarenakan ada bacaannya enkripsi 3x maka yang pertama adalah dengan dekripsi seperti _cyber jawara seperti enc.txt di babyxor_ maka saya lakukan hexdump dan mendapatkan ciphernya<br/><br/>
![](foto/introAES_hexdump.png)
<br/><br/>
![](foto/introAES_cipher.png)
<br/><br/>
kemudian saya melihat terlebih dahulu sourcenya dan ketemulah kuncinya buat AES
<br/><br/>
![](foto/introAES_source.png)
<br/><br/>
dan saya olah dengan [tools ini](https://www.devglan.com/online-tools/aes-encryption-decryption) 
<br/><br/>
![](foto/introAES_AES_64.png)
<br/><br/>
dikarenakan menghasilkan ciri ciri base64 dan saya konvertkan menjadi ascii dan hasilnya adalah ...
<br/><br/>
![](foto/introAES_64_hasil.png)
<br/><br/>
flagnya adalah `agrihack{51mpl3_ECB_MODE_34b6a5}`
[source.py](https://agrihack.codepwnda.id/uploads?key=1e137ba830987af7dd616a5761de8910f2bcc4fc7c0ab1242b51943f91954263%2Fsource.py)[enc.txt](https://agrihack.codepwnda.id/uploads?key=4ac3ed117c61d638505b36882a34a034ff596e4bff50fef3db5549db1f382e4b%2Fenc.txt)
### 9. Password Cracker 2
sama seperti Password Cracker dengan menggunakan [tools ini](https://crackstation.net/) dan kita crack `535fc078a3a273070809bfdbef6018bf`
<br/><br/>
![](foto/crack2_hash.png)
<br/><br/>
dan masukkan saja ke terminal `nc 52.187.65.2 15002`
<br/><br/>
![](foto/crack2_ter.png)
<br/><br/>
dan hasilnya adalah
flag : `agrihack{d0n7_u53_w34k__p455w000000RD}`

### 10. crypto/BabyXor Vol.2
dengan materi yang dikirim dari channel CSI IPB youtube tentang [xor cipher repeated](https://www.youtube.com/watch?v=-elQW05sgV8) dengan tools [xortool](https://github.com/hellman/XORTOOL) <br/>

berikut ini adalah walkthroughnya
<br/><br/>
![](foto/xortool_2.png)
<br/><br/>
![](foto/xortool_2_csv.png)
<br/><br/>
kita cek masing masing hasilnya yang berbentuk _*txt*_ ya . bukan yang berbentuk bin
<br/><br/>
![](foto/xortool_2_hasil.png)
<br/><br/>
maka ketemulah flag : `agrihack{common_character__is_space}`<br/><br/>
[sumber file](https://agrihack.codepwnda.id/uploads?key=f037303d30444fff4a69c6c23bbef4fae687ed793c827e24e63d1fada339b077%2Fenkrip.enc)

### 11. Password Cracker 3
hash : `29f1f8b054a15638a1a269a0f4b0d743`<br/>
salted : `secret_`<br/>
dengan [tools ini](https://www.dcode.fr/md5-hash) saya bisa mendekripsi hash tersebut 
<br/><br/>
![](foto/crack3_salt.png)
<br/><br/>
![](foto/crack3_ter.png)
<br/><br/>
flag : `agrihack{R0ck_y0u_1s_4_th1ng55____b33f}`<br/>
dengan netcat `nc 52.187.65.2 15003`

## Web
### 1. Inception
Dengan membuka website ini dan kita langsung saja *menginspect* websitenya dikarenakan adanya foto ini. (ingat kalau di chrome tekan `F12`)<br/><br/><br/>
<image src="foto/inspect_me.png" width="1000px" height="500px" style="margin :40px 20px;">
<br/><br/><br/>
maka akan menemukan flag seperti berikut <br/><br/><br/>
![](foto/inception.png)
Sumber website
<br/>`http://52.187.65.2:16000/` <br/>
flag : `agrihack{u_are_an_inspector!_LINZ_IS_HERE}`

### 2. X-header
dikarenakan sudah jelas yang dicari adalah X-header maka tinggal kita inspect -> Network dan temukan X-Header-nya 
<br/>
<br/>
<br/>
![](foto/X-Header.png)
<br/>
<br/>
flag : `agrihack{x-header_header_tersembunyi_LINZ_IS_HERE}`<br/>
website : `http://52.187.65.2:16007/`

### 3. Bipbip
ada kluenya yaitu `Mr.Robot : "Beep...Beep..Beepp"` maka saya mencari di google mengenai robot di website [ini](https://www.robotstxt.org/robotstxt.html) maka saya aplikasi website `http://52.187.65.2:16001/` dengan menambahkan `robots.txt` menjadi `http://52.187.65.2:16001/robots.txt` dengan hasil <br/>
<br/><br/>
![](foto/bipbip_robot.png)
<br/><br/>
dan kemudian dengan directorynya yakni `/linz-is-here` maka saya buka website `http://52.187.65.2:16001/linz-is-here` <br/><br/>
![](foto/bipbip_flag.png)<br/><br/>
flagnya `agrihack{robootssssssss_a_little_information_linz_is_here}`

### 4. Chef
Dengan 
