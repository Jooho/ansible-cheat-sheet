Download RHEV certificate
------------------------

In order to establish SSL conntion with RHEV api server, cert file have to be stored in somewhere.


### How to get RHEVE cert?

Store cert content(START - END) that can get from following command to /root/rhev.crt. If the you want to change the path of cert, you should change the variable of [vars/all file](../vars/all).


```
# openssl s_client -connect lab-rhevm-2.X.X.com:443 -showcerts -servername lab-rhevm-2.X.X.com -verify 5

verify depth is 5
CONNECTED(00000003)
depth=1 C = US, O = XXX, CN = CA-lab-rhevm.X.X.com.26106
verify error:num=19:self signed certificate in certificate chain
verify return:1
depth=1 C = US, O = XXX, CN = CA-lab-rhevm.X.X.com.26106
verify return:1
depth=0 C = US, O = XXX, CN = lab-rhevm-2.X.X.com
verify return:1
---
Certificate chain
 0 s:/C=US/O=XXX/CN=lab-rhevm-2.X.X.com
   i:/C=US/O=XXX/CN=CA-lab-rhevm.X.X.com.26106
-----BEGIN CERTIFICATE-----                                               # <------ START
MIIDvTCCAyagAwIBAgIBHzANBgkqhkiG9w0BAQUFADBPMQswCQYDVQQGEwJVUzEM
MAoGA1UEChMDR1NTMTIwMAYDVQQDEylDQS1sYWItcmhldm0uZ3NzbGFiLnJkdTIu
cmVkaGF0LmNvbS4yNjEwNjAeFw0xNzA0MjYxMjA4NDdaFw0yMjA0MDExMjA4NDda
MEgxCzAJBgNVBAYTAlVTMQwwCgYDVQQKEwNHU1MxKzApBgNVBAMTImxhYi1yaGV2
bS0yLmdzc2xhYi5yZHUyLnJlZGhhdC5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IB
...............................
BgkqhkiG9w0BAQUFAAOBgQAbVxTgHnKcoM1JaTXt+QUDIYkuhhEtLqLeupbAhF0l
G/Kw3TbQrQAAWyO9iTJH+50anLhp+C0WqKz3k/0Q3syh4oxH9E8FUTefxxjt3m3D
mjQ2eajME7ywLiGeOd0Cvu9twiTMyM/FMREXKodroAYZ/u8yN1qCwI+Vph9PLYvn
PA==
-----END CERTIFICATE-----                                                 # <------- END
 1 s:/C=US/O=XXX/CN=CA-lab-rhevm.X.X.com.26106
   i:/C=US/O=XXX/CN=CA-lab-rhevm.X.X.com.26106
-----BEGIN CERTIFICATE-----
MIIDJDCCAo2gAwIBAgIBATANBgkqhkiG9w0BAQUFADBPMQswCQYDVQQGEwJVUzEM
MAoGA1UEChMDR1NTMTIwMAYDVQQDEylDQS1sYWItcmhldm0uZ3NzbGFiLnJkdTIu
cmVkaGF0LmNvbS4yNjEwNjAeFw0xNzA5MjIwMzI0NDdaFw0yNzA5MjAwMzI0NDda
ME8xCzAJBgNVBAYTAlVTMQwwCgYDVQQKEwNHU1MxMjAwBgNVBAMTKUNBLWxhYi1y
.............................
MAoGA1UEChMDR1NTMTIwMAYDVQQDEylDQS1sYWItcmhldm0uZ3NzbGFiLnJkdTIu
cmVkaGF0LmNvbS4yNjEwNjAeFw0xNzA5MjIwMzI0NDdaFw0yNzA5MjAwMzI0NDda
ME8xCzAJBgNVBAYTAlVTMQwwCgYDVQQKEwNHU1MxMjAwBgNVBAMTKUNBLWxhYi1y

```


