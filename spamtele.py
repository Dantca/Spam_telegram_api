import requests
# user memasukan api bot whatspapp
apiTelegram = input('masukan token api bot Telegram: \n token : ')
link = f"https://api.telegram.org/{apiTelegram}/sendMessage"
#masukan pesan yang ingin kamu kirimkan ke bot whatsapp nya 
pesan = input('masukan pesan yang ingin kamu kirimkan !! \n pesan: ')
#masukan jumlah berapa pesan yang ingin kamu kirimkan
jumlah_spam = input('masukan berapa pesan yang ingin kamu kirimkan \n angka:')
#lupa convert jadi angka
banyak_pesan = int(jumlah_spam)
#kita kasih kondisi perulangan di sini
chat_ids = input('nomer UNIK chat_id : \n nomer:') 
int(chat_ids)
for  i in range(banyak_pesan):
    header = {
        #file json
        "parse_mode":"markdown",
        "chat_id":chat_ids,
        "text": pesan
    }
    #kita memerlukan status respon dari apinya 
    balasan_dariapi = requests.post(link, json=header)
    #kita melihat apakah pesan tersbut berhasil terkirim atau tidaknya 
    #apabila 200 berarti berhasil
    if balasan_dariapi.status_code == 200 :
        print(f'pesan berhasil terkirim {pesan} @dantca_ ')
    else:
            print(f'gagal mengirim pesan : {balasan_dariapi.status_code} - {balasan_dariapi.text} @dantca_ ')
           # saatnya kita jalankan