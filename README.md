# Remnant
A keylogger written in Python with scheduled emailing functionality.

## Installation

Run the following command:
```
pip install -r requirements.txt
```

This installs several modules that you will need to run Remnant Keylogger.

* datetime
* email
* platform
* pyHook
* pythoncom
* pywin32
* smtplib
* threading

Most of these modules can be installed individually. For example:

```
pip install smtplib
```

### Troubleshooting

If the email module fails to install from pip it can be obtained using easy_install.

```
easy_install email
```

If you are having trouble installing pyHook module download the wheel file for it [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) and run the following command.

```
pip install pyHook‑1.5.1‑cp35‑cp35m‑win_amd64.whl
```
This example is installing pyHook for 64bit Windows and Python 3.5.

## Setup

Remnant Keylogger uses environment variables. To set these duplicate ```.env.example``` and name it ```.env```. It contains the following required settings.

### SENDING_EMAIL

The email from which the generated ```klog.txt``` will be sent from eg. name@example.com

### SENDING_EMAIL_PASSWORD

The password for the email account from which the keylog will be sent.

### RECEIVING_EMAIL

The email address to which the keylog will be sent. You can use the same email address as **SEND_EMAIL**.

### HOUR

The hour at which keylog will be sent. This use the 24 hour clock.

### MINUTE

The minute past the hour at which the keylog will be sent.

### SECOND

The second past the minute at which the keylog will be sent. Recommend leaving this as *00*.

### MICROSECOND

The microsecond past the second at which the keylog will be sent. Recommend leaving this as *00*.

### SERVER

Sending email server name.

### PORT

Port that sending email server uses.

### DELETE

Whether to delete the Remnant Keylogger after first email has been sent. Accepts boolean of *true* or *false*.


## Disclaimer
This code is distributed for educational and research purposes. Do not use without a person's consent.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
