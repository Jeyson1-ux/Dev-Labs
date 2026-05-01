# Day 1 - Deploy a Flask App on AWS EC2 with Nginx Reserve Proxy & Gunicorn

# Overview: This project demonstrates the steps to deploy a Python Flask application on an AWS EC2 instance using gunicorn as the application server and Nginx as a reserve proxy

Live Demo
http://demo.devvie.se


# Architecture: Browser -> Nginx -> Gunicorn -> Flask -> EC2
# Components
- EC2 (Amazon Linuz 2023) -- Virtual server hosting the app
- Nginx - Reserve proxy handling incoming HTTP traffic (port 80)
- Gunicorn - WSGI server running the Flask application (on Port 8000)
- Flask - A python web framework to initiate the web server
- DNS (One.com) - Maps domain to EC2 public IP

# How to deploy your application
1. Connect to EC2
ssh -i <key.pem> ec2-user@<public-ip>

2. Clone Repository
git clone <repo-url> ¨
cd Dev-Labs/day1

3. Time to set up the virtual environment
python3 -m venv .venv source 
.venv/bin/activate 
pip install -r requirements.txt

4. How to run the application with Gunicorn
gunicorn --bind 0.0.0.0:8000 app:app &

5. Configure Nginx (reserve proxy)
location / { 
    proxy_pass http://127.0.0.1:8000; 
    proxy_set_header Host $host; 
    proxy_set_header X-Real-IP $remote_addr; 
}

6. Restart the Nginx server
sudo systemctl restart nginx

# Verification
Check                 Command
App running           curl localhost:8000
Gunicorn              lsof -i :8000
Nginx                 curl localhost
Public access         http://demo.devvie.se

📸 Screenshots
(All the screenshots are under the /screenshots folder)


# Key Learnings
- AWS Security groups (firewall rules)
- How to initiate SSH authentication with key pairs with the usage of a PEM file
- How to start the server with Nginx and run python applications with gunicorn
- How to map my domain using DNS (A record)

# Some Limitations faced
- Not able to run my app on a secure browser(HTTPS was introduced in Lab 2)
- No process manager (manual restart required)
- Not running as a system service for automatic executions (gunicor not managed by systemd)


