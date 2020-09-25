# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 07:54:17 2020

@author: Steven
"""



import requests
from selenium import webdriver
import pandas as pd
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


import urllib.request
browser = webdriver.Chrome()


url = "http://www.foodstation.co.id/index.php/pusat-informasi-pasar/harga-beras-pibc-palawija" 
a=browser.get(url)
browser.implicitly_wait(10)



try:

    print("Belum")
    browser.switch_to.frame(browser.find_element_by_name("iframe"))
    bet_fa = browser.find_element_by_id("tgl")
    bet_fa.clear()
    bet_fa.send_keys("01-01-2016")
    bet_fa2 = browser.find_element_by_id("tgl2")
    bet_fa2.clear()
    bet_fa2.send_keys("31-05-2020")
    browser.find_element_by_id("go").click()
    print("Lewat pemilihan tanggal dan klik button")
    

    list_tanggal=[]
    list_harga_jenis1=[]

    list_jenis_beras=[]


    
 
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n ++++++++++++++++++ TAHAPAN Penarikan Jenis Beras Cianjur Kepala ++++++++++++++++++ \n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    i=1
    for table in browser.find_elements_by_xpath('//*[contains(@id,"theTable")]//tr'):   
        jenis_beras=[item.text for item in table.find_elements_by_xpath(".//*[self::th][2]")]
        data_harga_jenis1 = [item.text for item in table.find_elements_by_xpath(".//*[self::td][2]")]
        data_tanggal = [item.text for item in table.find_elements_by_xpath(".//*[self::td][1]")]
        
        list_harga_jenis1.append(data_harga_jenis1)
        list_tanggal.append(data_tanggal)
        list_jenis_beras.append(jenis_beras)
        print("\n isi I = ",i)
        i+1
        
       
        print("\n\nTanggal : \n", data_tanggal)
    list_jenis_beras=list_jenis_beras[1]
    
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n +++++++++++++++++++++++++++++ TAHAPAN 'pembersihan' value ++++++++++++++++++++++++++ \n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
  
    flattened_list_harga_jenis1= []
    for sublist in list_harga_jenis1:  
        for val in sublist:
            val = val.replace(',', '')
            int_val=int(val)
            flattened_list_harga_jenis1.append(int_val)
    print("\n\nIni FLATTEN int harga jenis1 : ",flattened_list_harga_jenis1)
    
    list_jenis_beras_new=[]
    for i in range(len(flattened_list_harga_jenis1)):
        list_jenis_beras_new.append(list_jenis_beras)
        
    flattened_list_jenis_beras= []
    for sublist in list_jenis_beras_new:  
        for val in sublist:
            val = val.replace(',', '')
            flattened_list_jenis_beras.append(val)
    print("\n\nIni FLATTEN int jenis beras : ",flattened_list_jenis_beras)
   
    
  
    print("\n\nList tanggal = \n\n",list_tanggal[1:])
    
   
    flattened_list_tanggal = []
    for sublist in list_tanggal[2:]:    #[2:] berarti diambil mulai dari baris index ke 2 dan seterusnya, karena isi index 0 dan 1 tidak penting
        for val in sublist:
            from dateutil.parser import parse
            date = val
            format_tanggal=parse(date).strftime("%Y%m%d")
            flattened_list_tanggal.append(format_tanggal)

    flattened_list_harga_jenis1.reverse()    
    flattened_list_tanggal.reverse()
    
    print("\n\nIni FLATTEN int harga jenis1 : ",flattened_list_harga_jenis1)
    print("\n\nIni FLATTEN tanggal : ",flattened_list_tanggal)
   
  

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


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n +++++++++++++++++++++++ TAHAPAN INSERT data ke DATABASE ++++++++++++++++++++++++ \n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

for tgl,jenis,harga in zip(flattened_list_tanggal,flattened_list_jenis_beras,flattened_list_harga_jenis1):
    mycursor.execute("""INSERT IGNORE INTO semua_harga_beras (tanggal,jenis_beras,harga) 
                     VALUES (%s,%s,%s)""", (tgl,jenis,harga))


                    
   
mydb.commit()

print(mycursor.rowcount, " record inserted.")
