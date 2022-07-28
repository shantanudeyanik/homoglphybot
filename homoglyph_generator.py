
# used to covert english to unicode https://www.englishtools.org/en/convert-english-to-unicode-and-unicode-to-english
# homograph unicode collection https://www.irongeek.com/homoglyph-attack-generator.php
def homograph(text_):

    avc = text_


    small_letter_list= ['\u0430','\u0441','\u0501','\u0435','\u0261','\u0456','\u0458','\u03bf','\u0440','\u0455','\u0445','\u0443']
    cap_l_lst =     ['\u0391','\u0412','\u03f9','\u0395','\u0397','\u0399','\u0408','\u212a','\u041c','\u039d','\u041e','\u0420','\u03a4','\u0425','\u03a5','\u0396']
    cap_basic_lst = ['\u0041','\u0042','\u0043','\u0045','\u0048','\u0049','\u004a','\u004b','\u004d','\u004e','\u004f','\u0050','\u0054','\u0058','\u0059','\u005a']


    avc = avc.replace("\u0020","\u2005") # space " "
    avc = avc.replace("\u0061",small_letter_list[0])
    avc = avc.replace("\u0063",small_letter_list[1])
    avc = avc.replace("\u0064",small_letter_list[2])
    avc = avc.replace("\u0065",small_letter_list[3])
    avc = avc.replace("\u0067",small_letter_list[4])
    avc = avc.replace("\u0069",small_letter_list[5])
    avc = avc.replace("\u006a",small_letter_list[6])
    avc = avc.replace("\u006f",small_letter_list[7])
    avc = avc.replace("\u0070",small_letter_list[8])
    avc = avc.replace("\u0073",small_letter_list[9])
    avc = avc.replace("\u0078",small_letter_list[10])
    avc = avc.replace("\u0079",small_letter_list[11])
    avc = avc.replace("\u006f","\u043e") #o

    avc = avc.replace(cap_basic_lst[0] ,cap_l_lst [0])
    avc = avc.replace(cap_basic_lst[1] ,cap_l_lst [1])
    avc = avc.replace(cap_basic_lst[2] ,cap_l_lst [2])
    avc = avc.replace(cap_basic_lst[3] ,cap_l_lst [3])
    avc = avc.replace(cap_basic_lst[4] ,cap_l_lst [4])
    avc = avc.replace(cap_basic_lst[5] ,cap_l_lst [5])
    avc = avc.replace(cap_basic_lst[6] ,cap_l_lst [6])
    avc = avc.replace(cap_basic_lst[7] ,cap_l_lst [7])
    avc = avc.replace(cap_basic_lst[8] ,cap_l_lst [8])
    avc = avc.replace(cap_basic_lst[9] ,cap_l_lst [9])
    avc = avc.replace(cap_basic_lst[10] ,cap_l_lst [10])
    avc = avc.replace(cap_basic_lst[11] ,cap_l_lst [11])
    avc = avc.replace(cap_basic_lst[12] ,cap_l_lst [12])
    avc = avc.replace(cap_basic_lst[13] ,cap_l_lst [13])
    avc = avc.replace(cap_basic_lst[14] ,cap_l_lst [14])
    avc = avc.replace(cap_basic_lst[15] ,cap_l_lst [15])

    return avc

