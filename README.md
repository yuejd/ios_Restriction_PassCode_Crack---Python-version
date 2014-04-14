# ios Restriction PassCode Crack -Python version



## Overview 

**ios Restriction PassCode Cracker**, this version of the application is written with Python programming language,which is used to crack the Restriction PassCode of iphone/ipad.
(iphone/ipad 访问限制密码破解)

### Method(the same as C version)
**bruce crack**

>1 .get the Base64 key and salt from the backup file in Computer.

>2 .decode the Base64 key and salt.

>3 .try from 1 to 9999 to with the pbkdf2-hmac-sha1 hash with passlib
(passlib moudle need to be installed before:easy_install passlib)


### How to Use
1.Make sure to use Itunes to back up the ios device to Computer

2.change dir to the code.

```
python ./ioscrack.py
```


### Source Code
```
  htos.py : hex and string transition moudle
  ioscrack.py : main process
```

### Note
about python version, the code is far more simple than C version 
especially file parsing and decoding process. It's obvious that python is easier to code.
On another hand, I set a timer for these two version,python version takes nearly a minute but it take only 10 more seconds in C version,and it's indeed more productive.
So, we can combine them together for less code and more productive. just As next Version
ios Restriction PassCode Crack -Py_C version, using python to parse file and decode base64
,and C language to encode for pbkdf2-hmac-sha1 hash with openssl.


*jdyue19@gmail.com*
