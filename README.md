# aqara_doorbell_g4_samba_telegram
Home Automation script. Monitoring samba share which stores videos from Aqara Doorbell G4.

This repository has an Ansible playbook to configure and deploy it to your home media server

1. Generate your own password ```openssl rand -base64 32 > vault_password_file```
2. Create your own ```inventory.yml```
    3. Generate encrypted values for it with command ```ansible-vault -v encrypt_string --vault-password vault_password 'your_password_here' --name 'ansible_become_pass'```
    3. Fill ```ansible_user```
    3. Fill ```ansible_host```
    3. Fill ```ansible_become_pass```
    4. And others if you need
3. Make deploy script executable ```chmod +x ./deploy.sh```
4. Just run ```./deploy.sh```