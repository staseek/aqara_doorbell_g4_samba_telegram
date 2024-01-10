# aqara_doorbell_g4_samba_telegram
Home Automation script. Monitoring samba share which stores videos from Aqara Doorbell G4.

This repository has an Ansible playbook to configure and deploy it to your home media server

1. Generate your own password ```openssl rand -base64 32 > ansible_deploy/vault_password```
2. Create your own ```inventory.yml```
   - Generate encrypted values for it with command ```ansible-vault -v encrypt_string --vault-password vault_password 'your_password_here' --name 'ansible_become_pass'```
   - Fill ```ansible_user```
   - Fill ```ansible_host```
   - Fill ```ansible_become_pass```
    And others if you need
3. Make deploy script executable ```chmod +x ./deploy.sh```
4. Just run ```./deploy.sh```