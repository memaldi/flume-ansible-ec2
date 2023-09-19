1. Set AWS credentials at ~/.aws/credentials
2. Download SSH private key at ~/.ssh/vockey.pem
3. Set the proper permissions for the key: `chmod og-rwx ~/.ssh/vockey.pem`
4. Install requirements: `pip install -r requirements.txt`
5. Install vim and less: `sudo apt update && apt install -y vim less`
6. Run instances: `ansible-playbook create-instances.yml`


python random-events.py --name Bilbao --lat 43.26271 --long -2.92528 --wait 5 --output_dir /tmp