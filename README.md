# django-whois-api

>##Note
- Currently supported only on Linux systems with ```whois``` package supported

##Installtion
1. Clone the repo
2. Install ```whois``` package from apt or supported package manager
   ex. ```[sudo] apt-get install whois```
3. Install requirements by ```[sudo] pip install requirements.txt``` 
Ready to Go!

##Usage
- ```GET``` Request on / with ```?domain=example.com``` retuens json output
- ```GET``` Request on /example.com returns raw whois info in browser
