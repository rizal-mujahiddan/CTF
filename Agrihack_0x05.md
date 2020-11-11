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
### 4. Introduction to Cipher_Series : Talking
lihatlah kata kunci dari hint tersebut `'numbers come after letters, underscore come after numbers'` maka anda akan terkejut dengan ini karena sangat mudah untuk dipecahkan dengan hint ini maka saya akan membuatnya di [notepad](doc/talking_cipher) awal mulanya saya mencurigai `1 7 18 9 8 1 3 11` yang dikonversikan menjadi `agrihack` , maka saya langung mengkonversikan yang lain dan dengan petunjuk hint juga ya maka akan menjadi [ini](doc/boooo.txt)
<br/>
<br/>
![](foto/talking.png)
<br/>
<br/>
[sumber filenya](https://drive.google.com/drive/folders/1sO9aU4fKPLcuhQQEV5FHfdIU6D3VbqmP?usp=sharing)
### 5. BabyXOR
### 6. Password Cracker
### 7. Introduction to Cipher_Series : Matrix
dengan foto seperti <br/> <br/>
![](foto/matrix.jpg)
 <br/> <br/>
maka dengan menyamakan konsep dari soal sebelumnya dari Talking maka akan menjadi seperti [ini](doc/matrix.txt) <br/>
[sumber_file](https://drive.google.com/drive/folders/1UskrfztjMhYbpp7c3ZEYMTfNMpHh0ori?usp=sharing)
### 8. BabyAES : Introduction
### 9. Password Cracker 2
### 10. crypto/BabyXor Vol.2
### 11. Password Cracker 3
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
ada kluenya yaitu `Mr.Robot : "Beep...Beep..Beepp"` maka saya mencari di google mengenai robot di website [ini](https://www.robotstxt.org/robotstxt.html) maka saya aplikasi website `http://52.187.65.2:16001/` dengan menambahkan `robots.txt`
ketemulah flagnya <br/>


