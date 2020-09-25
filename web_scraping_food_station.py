# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:51:23 2020

@author: Steven
"""
# -*- coding: utf-8 -*-

'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

================================== WEB SCRAPING =============================
'''


from selenium import webdriver


from selenium.common.exceptions import TimeoutException



browser = webdriver.Chrome()


url = "http://www.foodstation.co.id/index.php/pusat-informasi-pasar/harga-beras-pibc-palawija" 
a=browser.get(url)
browser.implicitly_wait(10)



try:

    print("Belum")
   # browser.find_element_by_link_text("PUSAT INFORMASI PASAR").click()
    #print("Lewat1")
    browser.switch_to.frame(browser.find_element_by_name("iframe"))
    bet_fa = browser.find_element_by_id("tgl")
    bet_fa.clear()
    bet_fa.send_keys("01-01-2016")
    bet_fa2 = browser.find_element_by_id("tgl2")
    bet_fa2.clear()
    bet_fa2.send_keys("31-05-2020")
    browser.find_element_by_id("go").click()
    print("Lewat pemilihan tanggal dan klik button")
    

    #html = browser.get(url).read()
    list_harga=[]
    list_harga_semua=[]
    list_tanggal=[]
    list_jenis_beras=[]
    flattened_list_jenis_beras = []
    list_harga_CK=[]
    list_harga_CS=[]
    list_harga_setra=[]
    list_harga_saigon=[]
    list_harga_muncul1=[]
    list_harga_muncul2=[]
    list_harga_muncul3=[]
    list_harga_ir1=[]
    list_harga_ir2=[]
    list_harga_ir3=[]
    list_harga_ir42=[]
    list_harga_kpb=[]
    list_harga_kpp=[]
    list_harga_kh=[]
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n ++++++++++++++++++++ TAHAPAN Penarikan jenis beras ++++++++++++++++++++ \n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    
    for table in browser.find_elements_by_xpath('//*[contains(@id,"theTable")]//tr'):
        data_jenis_beras= [item.text for item in table.find_elements_by_xpath(".//*[self::th]")] 
        list_jenis_beras.append(data_jenis_beras)
        
    for jenis in list_jenis_beras[1]:    #[2:] berarti diambil mulai dari baris index ke 2 dan seterusnya, karena isi index 0 dan 1 tidak penting
            val = jenis.replace(',', '')
            #print("\n\nJenis beras : ",val)
            #print(type(val))
            flattened_list_jenis_beras.append(val)
            
    flattened_list_jenis_beras=flattened_list_jenis_beras[1:]

    
    print("\n\nIni FLATTEN jenis beras: ",flattened_list_jenis_beras)
 
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n +++++++++++++++++++ TAHAPAN Penarikan Semua Berbagai Jenis Beras ++++++++++++++++++ \n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    
    for table in browser.find_elements_by_xpath('//*[contains(@id,"theTable")]//tr'):
        data_harga = [item.text for item in table.find_elements_by_xpath(".//*[self::td]")]
        data_harga_CK = [item.text for item in table.find_elements_by_xpath(".//*[self::td][2]")]
        data_harga_CS = [item.text for item in table.find_elements_by_xpath(".//*[self::td][3]")]
        data_harga_setra = [item.text for item in table.find_elements_by_xpath(".//*[self::td][4]")]
        data_harga_saigon= [item.text for item in table.find_elements_by_xpath(".//*[self::td][5]")]
        data_harga_muncul1 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][6]")]
        data_harga_muncul2 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][7]")]
        data_harga_muncul3 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][8]")]
        data_harga_ir1 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][9]")]
        data_harga_ir2 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][10]")]
        data_harga_ir3 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][11]")]
        data_harga_ir42 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][12]")]
        data_harga_kpb = [item.text for item in table.find_elements_by_xpath(".//*[self::td][13]")]
        data_harga_kpp = [item.text for item in table.find_elements_by_xpath(".//*[self::td][14]")]
        data_harga_kh = [item.text for item in table.find_elements_by_xpath(".//*[self::td][15]")]
        data_tanggal = [item.text for item in table.find_elements_by_xpath(".//*[self::td][1]")]
        list_harga_semua.append(data_harga[1:]) #indeks ke-0 = tanggal
        list_harga_CK.append(data_harga_CK)
        list_harga_CS.append(data_harga_CS)
        list_harga_setra.append(data_harga_setra)
        list_harga_saigon.append(data_harga_saigon)
        list_harga_muncul1.append(data_harga_muncul1)
        list_harga_muncul2.append(data_harga_muncul2)
        list_harga_muncul3.append(data_harga_muncul3)
        list_harga_ir1.append(data_harga_ir1)
        list_harga_ir2.append(data_harga_ir2)
        list_harga_ir3.append(data_harga_ir3)
        list_harga_ir42.append(data_harga_ir42)
        list_harga_kpb.append(data_harga_kpb)
        list_harga_kpp.append(data_harga_kpp)
        list_harga_kh.append(data_harga_kh)
 
        list_tanggal.append(data_tanggal)
        print("\n\n Harga beras: \n", data_harga)
        print("\n\nTanggal : \n", data_tanggal)
  
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n +++++++++++++++++++++++++++++ TAHAPAN 'pembersihan' value ++++++++++++++++++++++++++ \n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
  
    flattened_list_harga_CK= []
    for sublist in list_harga_CK:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_CK.append(int_val)   
    print("\n\nIni FLATTEN int harga CK : ",flattened_list_harga_CK)
    
    flattened_list_harga_CS= []
    for sublist in list_harga_CS: 
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_CS.append(int_val)
    print("\n\nIni FLATTEN int harga CS : ",flattened_list_harga_CS)
    
    flattened_list_harga_setra= []
    for sublist in list_harga_setra: 
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_setra.append(int_val)
    print("\n\nIni FLATTEN int harga Setra : ",flattened_list_harga_setra)
    
    flattened_list_harga_saigon= []
    for sublist in list_harga_saigon:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_saigon.append(int_val)
    print("\n\nIni FLATTEN int harga Saigon : ",flattened_list_harga_saigon)
    
    flattened_list_harga_muncul1= []
    for sublist in list_harga_muncul1:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_muncul1.append(int_val)
    print("\n\nIni FLATTEN int harga MUNCUL 1 : ",flattened_list_harga_muncul1)
    
    flattened_list_harga_muncul2= []
    for sublist in list_harga_muncul2:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_muncul2.append(int_val)
    print("\n\nIni FLATTEN int harga MUNCUL 2 : ",flattened_list_harga_muncul2)
    
    flattened_list_harga_muncul3= []
    for sublist in list_harga_muncul3: 
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_muncul3.append(int_val)
    print("\n\nIni FLATTEN int harga MUNCUL 3 : ",flattened_list_harga_muncul3)
    
    flattened_list_harga_ir1= []
    for sublist in list_harga_ir1:    
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_ir1.append(int_val)
    print("\n\nIni FLATTEN int harga IR 1 : ",flattened_list_harga_ir1)
    
    flattened_list_harga_ir2= []
    for sublist in list_harga_ir2:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_ir2.append(int_val)
    print("\n\nIni FLATTEN int harga IR 2 : ",flattened_list_harga_ir2)
    
    flattened_list_harga_ir3= []
    for sublist in list_harga_ir3:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_ir3.append(int_val)
    print("\n\nIni FLATTEN int harga IR 3 : ",flattened_list_harga_ir3)
    
    flattened_list_harga_ir42= []
    for sublist in list_harga_ir42:   
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_ir42.append(int_val)
    print("\n\nIni FLATTEN int harga IR 42 : ",flattened_list_harga_ir42)
    
    flattened_list_harga_kpb= []
    for sublist in list_harga_kpb:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_kpb.append(int_val)
    print("\n\nIni FLATTEN int harga Ketan Putih Biasa : ",flattened_list_harga_kpb)
    
    flattened_list_harga_kpp= []
    for sublist in list_harga_kpp:   
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_kpp.append(int_val)
    print("\n\nIni FLATTEN int harga Ketan Putih Pasir : ",flattened_list_harga_kpp)
    
    flattened_list_harga_kh= []
    for sublist in list_harga_kh:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_kh.append(int_val)
    print("\n\nIni FLATTEN int harga Ketan Hitam : ",flattened_list_harga_kh)
    

#    print("\n\nList harga = \n\n",data_harga)
    print("\n\nList harga = \n\n",list_harga_semua)
    print("\n\nList harga semua= \n\n",list_harga_semua[2:])
    print("\n\nList tanggal = \n\n",list_tanggal[1:])
    
    flattened_list_harga_semua= []
    for sublist in list_harga_semua:   
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_semua.append(int_val)
            #print(type(int_val))
            
    print("\n\nIni FLATTEN int harga SEMUA : ",flattened_list_harga_semua)
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n ++++++++++++++++++++ TAHAPAN Penarikan nilai khusus IR64-III ++++++++++++++++++++ \n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    '''
    for table in browser.find_elements_by_xpath('//*[contains(@id,"theTable")]//tr'):
        data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
        data_harga = [item.text for item in table.find_elements_by_xpath(".//*[self::td][11]")]
        data_tanggal = [item.text for item in table.find_elements_by_xpath(".//*[self::td][1]")]
        list_harga.append(data_harga)
        list_tanggal.append(data_tanggal)
        print("Data beras IR-64 II : \n", data_harga)
        print("Tanggal : \n", data_tanggal)
    print("\n\nList harga = \n\n",list_harga[2:])
    print("\n\nList tanggal = \n\n",list_tanggal[2:])

    flattened_list_harga = []
    flattened_list_tanggal = []
    for sublist in list_harga[2:]:   #[2:] berarti diambil mulai dari baris index ke 2 dan seterusnya, karena isi index 0 dan 1 tidak penting
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga.append(int_val)
           # print(type(int_val))
        
    '''
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n +++++++++++++++++++++++++++++++++ FLATTENED TANGGAL +++++++++++++++++++++++++++++++ \n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    flattened_list_tanggal = []
    for sublist in list_tanggal[2:]:    #[2:] berarti diambil mulai dari baris index ke 2 dan seterusnya, karena isi index 0 dan 1 tidak penting
        for val in sublist:
            from dateutil.parser import parse
            date = val
            format_tanggal=parse(date).strftime("%Y%m%d")
            #print("\n\nFormat tanggal : ",format_tanggal)
            #print(type(date))
            flattened_list_tanggal.append(format_tanggal)

    flattened_list_harga_semua.reverse()          #reverse = membalik posisi urutan
    flattened_list_tanggal.reverse()
    
    print("\n\nIni FLATTEN int harga : ",flattened_list_harga_semua)
    print("\n\nIni FLATTEN tanggal : ",flattened_list_tanggal)
    '''
     # Bundle data ke format dataframe
    df_harga_tipeIII = pd.DataFrame({
    "Tanggal": flattened_list_tanggal,
    "Harga": flattened_list_harga,
    })
    '''
  
    #print("\n\nIsi dataframe (10 pertama) = \n",df_harga_tipeIII[:10])
    
  

except TimeoutException:
    print("Timed out waiting for page to load")



#++++++++++++++++++++++++++++++++++ INPUT DATABASE +++++++++++++++++++++++++++++++++

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="lstm_beras"
)

mycursor = mydb.cursor()

# masukkan jenis beras ke table lstm_data_semua

'''

for val in flattened_list_jenis_beras:
    mycursor.execute("""INSERT IGNORE INTO lstm_jenis_beras (jenis_beras) VALUES (%s)""", (val,))
'''

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n +++++++++++++++++++++++ TAHAPAN INSERT semua beras DATABASE ++++++++++++++++++++++++ \n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

for tgl,ck in zip(flattened_list_tanggal,flattened_list_harga_CK):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Cianjur Kepala",ck))

for tgl,cs in zip(flattened_list_tanggal,flattened_list_harga_CS):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Cianjur Slyp",cs))
                     
for tgl,setra in zip(flattened_list_tanggal,flattened_list_harga_setra):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Setra",setra))

for tgl,saigon in zip(flattened_list_tanggal,flattened_list_harga_saigon):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Saigon",saigon))
                     
for tgl,muncul1 in zip(flattened_list_tanggal,flattened_list_harga_muncul1):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Muncul 1",muncul1))

for tgl,muncul2 in zip(flattened_list_tanggal,flattened_list_harga_muncul2):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Muncul 2",muncul2))
                     
for tgl,muncul3 in zip(flattened_list_tanggal,flattened_list_harga_muncul3):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Muncul 3",muncul3))

for tgl,ir1 in zip(flattened_list_tanggal,flattened_list_harga_ir1):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"IR 1",ir1))

for tgl,ir2 in zip(flattened_list_tanggal,flattened_list_harga_ir2):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"IR 2",ir2))

for tgl,ir3 in zip(flattened_list_tanggal,flattened_list_harga_ir3):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"IR 3",ir3))

for tgl,ir42 in zip(flattened_list_tanggal,flattened_list_harga_ir42):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"IR 42",ir42))

for tgl,kpb in zip(flattened_list_tanggal,flattened_list_harga_kpb):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Ketan Putih Biasa",kpb))

for tgl,kpp in zip(flattened_list_tanggal,flattened_list_harga_kpp):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Ketan Putih Pasir",kpp))
                     
for tgl,kh in zip(flattened_list_tanggal,flattened_list_harga_kh):
    mycursor.execute("""INSERT IGNORE INTO lstm_data_semua (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,"Ketan Hitam",kh))
                     
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n ++++++++++++++++++++++ TAHAPAN INSERT DB khusus IR64-III +++++++++++++++++++++++++ \n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                      
                    
'''
for t,i in zip(flattened_list_tanggal,flattened_list_harga):
    #sql = "INSERT INTO data_beras (tanggal,harga) VALUES (%s %s)"
    #print("\n\nT :",t)
    #print("\n\n i = ",i)
    #mycursor.execute("SELECT tanggal FROM data_beras WHERE tanggal = '%s'" %t)
    # gets the number of rows affected by the command executed
    #row_count = mycursor.rowcount

    #if row_count == 0:
       #print ("It Does Not Exist")
    mycursor.execute("""INSERT IGNORE INTO lstm_data_beras (tanggal,harga) 
                     VALUES (%s, %s)""", (t, i))
  #  else:
        #print ("data sudah ada")
'''

mydb.commit()

print(mycursor.rowcount, " record inserted.")
