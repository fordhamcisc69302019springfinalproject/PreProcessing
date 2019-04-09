# Statistical Description
This is a statistical description file for raw train set.


## Ignored Features:
- **fnlwgt**: unmeaningful
- **capital-gain, capital-loss**: almost all zero


## Distribution  

* feature - **age**:  
{36: 898, 31: 888, 34: 886, 23: 877, 35: 876, 33: 875, 28: 867, 30: 861, 37: 858, 25: 841, 27: 835, 32: 828, 38: 827, 39: 816, 29: 813, 41: 808, 24: 798, 40: 794, 26: 785, 42: 780, 43: 770, 22: 765, 20: 753, 46: 737, 45: 734, 44: 724, 21: 720, 19: 712, 47: 708, 50: 602, 51: 595, 49: 577, 18: 550, 48: 543, 52: 478, 53: 464, 55: 419, 54: 415, 17: 395, 58: 366, 56: 366, 57: 358, 59: 355, 60: 312, 61: 300, 62: 258, 63: 230, 64: 208, 65: 178, 67: 151, 66: 150, 68: 120, 69: 108, 70: 89, 71: 72, 72: 67, 73: 64, 74: 51, 76: 46, 75: 45, 90: 43, 77: 29, 78: 23, 80: 22, 79: 22, 81: 20, 82: 12, 84: 10, 83: 6, 85: 3, 88: 3, 87: 1, 86: 1}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/age.jpg)  

----  
* feature - **workclass**:  
{' Private': 22696, ' Self-emp-not-inc': 2541, ' Local-gov': 2093, ' ?': 1836, ' State-gov': 1298, ' Self-emp-inc': 1116, ' Federal-gov': 960, ' Without-pay': 14, ' Never-worked': 7}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/workclass.jpg)  

----  
* feature - **education**:  
{' HS-grad': 10501, ' Some-college': 7291, ' Bachelors': 5355, ' Masters': 1723, ' Assoc-voc': 1382, ' 11th': 1175, ' Assoc-acdm': 1067, ' 10th': 933, ' 7th-8th': 646, ' Prof-school': 576, ' 9th': 514, ' 12th': 433, ' Doctorate': 413, ' 5th-6th': 333, ' 1st-4th': 168, ' Preschool': 51}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/education.jpg)  

----  
* feature - **education-num**:  
{9: 10501, 10: 7291, 13: 5355, 14: 1723, 11: 1382, 7: 1175, 12: 1067, 6: 933, 4: 646, 15: 576, 5: 514, 8: 433, 16: 413, 3: 333, 2: 168, 1: 51}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/education-num.jpg)  

----  
* feature - **marital-status**:  
{' Married-civ-spouse': 14976, ' Never-married': 10683, ' Divorced': 4443, ' Separated': 1025, ' Widowed': 993, ' Married-spouse-absent': 418, ' Married-AF-spouse': 23}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/marital-status.jpg)  

----  
* feature - **occupation**:  
{' Prof-specialty': 4140, ' Craft-repair': 4099, ' Exec-managerial': 4066, ' Adm-clerical': 3770, ' Sales': 3650, ' Other-service': 3295, ' Machine-op-inspct': 2002, ' ?': 1843, ' Transport-moving': 1597, ' Handlers-cleaners': 1370, ' Farming-fishing': 994, ' Tech-support': 928, ' Protective-serv': 649, ' Priv-house-serv': 149, ' Armed-Forces': 9}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/occupation.jpg)  

----  
* feature - **relationship**:  
{' Husband': 13193, ' Not-in-family': 8305, ' Own-child': 5068, ' Unmarried': 3446, ' Wife': 1568, ' Other-relative': 981}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/relationship.jpg)  

----  
* feature - **race**:  
{' White': 27816, ' Black': 3124, ' Asian-Pac-Islander': 1039, ' Amer-Indian-Eskimo': 311, ' Other': 271}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/race.jpg)  

----  
* feature - **sex**:  
{' Male': 21790, ' Female': 10771}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/sex.jpg)  

----  
* feature - **hours-per-week**:  
{40: 15217, 50: 2819, 45: 1824, 60: 1475, 35: 1297, 20: 1224, 30: 1149, 55: 694, 25: 674, 48: 517, 38: 476, 15: 404, 70: 291, 10: 278, 32: 266, 24: 252, 65: 244, 36: 220, 42: 219, 44: 212, 16: 205, 12: 173, 43: 151, 37: 149, 8: 145, 52: 138, 80: 133, 56: 97, 28: 86, 99: 85, 46: 82, 18: 75, 72: 71, 75: 66, 6: 64, 5: 60, 4: 54, 47: 49, 84: 45, 22: 44, 54: 41, 3: 39, 33: 39, 39: 38, 41: 36, 14: 34, 2: 32, 27: 30, 26: 30, 17: 29, 49: 29, 90: 29, 58: 28, 34: 28, 7: 26, 53: 25, 21: 24, 13: 23, 23: 21, 1: 20, 62: 18, 9: 18, 66: 17, 57: 17, 19: 14, 64: 14, 51: 13, 85: 13, 68: 12, 98: 11, 11: 11, 63: 10, 78: 8, 29: 7, 77: 6, 59: 5, 31: 5, 96: 5, 67: 4, 91: 3, 76: 3, 81: 3, 73: 2, 89: 2, 97: 2, 88: 2, 86: 2, 61: 2, 95: 2, 92: 1, 94: 1, 87: 1, 74: 1, 82: 1}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/hours-per-week.jpg)  

----  
* feature - **native-country**:  
{' United-States': 29170, ' Mexico': 643, ' ?': 583, ' Philippines': 198, ' Germany': 137, ' Canada': 121, ' Puerto-Rico': 114, ' El-Salvador': 106, ' India': 100, ' Cuba': 95, ' England': 90, ' Jamaica': 81, ' South': 80, ' China': 75, ' Italy': 73, ' Dominican-Republic': 70, ' Vietnam': 67, ' Guatemala': 64, ' Japan': 62, ' Poland': 60, ' Columbia': 59, ' Taiwan': 51, ' Haiti': 44, ' Iran': 43, ' Portugal': 37, ' Nicaragua': 34, ' Peru': 31, ' France': 29, ' Greece': 29, ' Ecuador': 28, ' Ireland': 24, ' Hong': 20, ' Trinadad&Tobago': 19, ' Cambodia': 19, ' Laos': 18, ' Thailand': 18, ' Yugoslavia': 16, ' Outlying-US(Guam-USVI-etc)': 14, ' Honduras': 13, ' Hungary': 13, ' Scotland': 12, ' Holand-Netherlands': 1}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/native-country.jpg)  

----  
* feature - **label**:  
{' <=50K': 24720, ' >50K': 7841}  

![image](http://github.com/fordhamcisc69302019springfinalproject/PreProcessing/raw/master/jpg/label.jpg)  

----  
