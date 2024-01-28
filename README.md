# Aqara Doorbell G4 samba Tcelegram
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/drkostas/Youtube-FirstCommentBot/master/LICENSE)
## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [License](#license)

## About <a name = "getting_started"></a>
Home Automation script. It monitors samba-share, which stores videos from Aqara Doorbell G4.
This repository has an Ansible playbook to configure and deploy it to your home media server.
Especially this solution is good if you don't want to give Agara Doorbell direct access to the internet.

## Getting started <a name = "prerequisites"></a>
### Configure aqara doorbell
1. [Configure samba-server on your Home server](https://ubuntu.com/server/docs/samba-file-server?ref=homelab.casaursus.net)
1. Open Aqara app
2. Choose your Doorbell
3. Device Settings
4. Dorbell Settings
5. SD Card Storage
6. NAS (Network Attached Storage)
7. Configure connection to your NAS
### Configure script and deploy it to home server 
1. Generate your own password ```openssl rand -base64 32 > ansible_deploy/vault_password```
2. Create your own ```inventory.yml```
   - Generate encrypted values for it with command ```ansible-vault -v encrypt_string --vault-password vault_password 'your_password_here' --name 'ansible_become_pass'```
   - Fill ```ansible_user```
   - Fill ```ansible_host```
   - Fill ```ansible_become_pass```
    And others if you need
2. Generate your own ssh-key ```ssh-keygen``` and add it to ```ansible_host``` with command ```ssh-copy-id -f ~/.ssh/id_rsa user@host```
3. Make deploy script executable ```chmod +x ./deploy.sh```
4. Copy env file and change values there as you need ```cp .env.example .env`
```
TG_BOT_TOKEN=123:eijfijerfijf
TG_CHAT_ID=123
MONITORING_FOLDER_VIDEO=/videos/aqara
```
6. Just run ```./deploy.sh```

## License <a name = "license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.