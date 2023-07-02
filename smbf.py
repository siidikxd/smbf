import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print("[*] koneksi anda buruk,silahkan refresh data anda.")
	exit()
	
if __name__ == "__main__":
	os.system("git pull")
	if "Indonesia" == fc:
		__import__("smbf").menu()
	else:
		print("[*] tools ini hanya support/berlaku di indonesia.")
		exit()
