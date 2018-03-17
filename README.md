# ddcBot doc

pre-req instals
```
Install anconda where  Python3 is part of the insgtallation
add  /anaconda3/bin to PATH as siad in other README file
```

How to use
The easy way is to clone it and use it via a virtualenv:
```
$ git clone https://github.com/PostPCEra/ddcBot.git
$ cd ddcBot
```


install virtualenv [as said here](https://stackoverflow.com/questions/31133050/virtualenv-command-not-found)
```
$pip install virtualenv

# then execute following steps

$ virtualenv env
$ . env/bin/activate
$ pip install Flask
```
Additional Installs required
Magnific-Popup : Light and responsive [lightbox script with focus on performance.](https://github.com/dimsemenov/Magnific-Popup)
```
- downloaded to /static/magnific-popup
- Magnific-Popup is Jquery dependent, so JQuery accessed directy from CDN in base.html 
- Content inside popup is style with Bootstrap, so it is fetched from CDN in base.html
```

Run the server:
```
$mkdir log    # to hold log files

$ python server_ddcBot*.py
```
Then visite with your web browser the URL: http://127.0.0.1:5000.
