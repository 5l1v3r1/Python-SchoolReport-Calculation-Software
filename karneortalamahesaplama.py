#!/usr/bin/env python
# -*- coding: utf-8 -*-

star = '--------------------------------------------------------------------------------'

print star

karneortalamahesaplama_ico = """
#########################################################
#       KARNE ORTALAMA HESAPLAMA - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print karneortalamahesaplama_ico

print star

beden_ort = input('Beden Donem Sonu Notunuzu Giriniz = ')
dil_ve_anlatim_ort = input('Dil Ve Anlatim Donem Sonu Notunuzu Giriniz = ')
din_kulturu_ve_ahlak_bilgisi_ort = input('Din Kulturu ve Ahlak Bilgisi Donem Sonu Notunuzu Giriniz = ')
felsefe_ort = input('Felsefe Donem Sonu Notunuzu Giriniz = ')
nesne_tabanli_programlama_ort = input('Nesne Tabanli Programlama Donem Sonu Notunuzu Giriniz = ')
biyoloji_ort = input('Biyoloji Donem Sonu Notunuzu Giriniz = ')
matematik_ort = input('Matematik Donem Sonu Notunuzu Giriniz = ')
inkilap_tarihi_ve_ataturkculuk_ort = input('Inkilap Tarihi Ve Ataturkculuk Donem Sonu Notunuzu Giriniz = ')
turk_edebiyati_ort = input('Turk Edebiyati Donem Sonu Notunuzu Giriniz = ')
veritabani_ort = input('Veritabani Donem Sonu Notunuzu Giriniz = ')
yabanci_dil_ort = input('Yabanici Dil Donem Sonu Notunuzu Giriniz = ')

print star

donem_genel_tplm = (dil_ve_anlatim_ort*2.0) + (turk_edebiyati_ort*3.0) + (matematik_ort*2.0) + (biyoloji_ort*2.0) + (felsefe_ort*2.0) + (din_kulturu_ve_ahlak_bilgisi_ort*1.0) + (beden_ort*2.0) + (inkilap_tarihi_ve_ataturkculuk_ort*2.0) + (yabanci_dil_ort*2.0) + (veritabani_ort*6.0) + (nesne_tabanli_programlama_ort*12.0)
donem_ort = donem_genel_tplm / 36.0

print 'Donem Sonu Ortalamsi = ', donem_ort, '|', 'Donem Genel Toplami = ', donem_genel_tplm
 
print star
