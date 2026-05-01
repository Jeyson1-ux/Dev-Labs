# Day 2 - Production Steup: HTTPS, PostgreSQL & and S3 backup

# Overview:
In Day 2, we evolved out Day 1 application from a simple Flask deployment into a producton-ready system by adding:
- HTTPS security (Let's Encrypt + Certbot)
- PostgreSQL database integration
- Secure configuration using environment variables
- A secured backup strategy by using S3 + IAM roles


# Architecture: User -> HTTPS -> Gunicorn -> Flask APP -> PostgreSQL -> Backup -> Se (via IAM Role)

# Part 1
- We installed certbot
- Verified domain ownership using HTTP challenge
- Generated SSL certifcates to fully execute our project
- Configured Nginx to serve HTTPS traffic properly

By using HTTPS, we manage to encrypt our communication with the browser, protect our data from being accessed to by unwanted parties and ensure trust on our website/app(browser padlock).

# Part 2 - PostgreSQL integration
In the next part:
- I installed PostgreSQL15
- Created a database (mydb)
- I configured authentication by using md5
- I later on connected Flask app using my DB_LINK

Here is an example of a connection string:
postgresql://postgres:<password>@localhost:5432/mydb

Key concept: We moved from a having a stateless app -> to now having a Statful Application (data persistence)

# Part 3 - Application changes
The new functionalities added:
- User signup (INSERT)
- User listing (SELECT)

# Part 4 - IAM Role for accessing S3
- In this part, I created an IAM role (ecs-s3-backup-role)
- I then attached it to EC2
- After the connection, verified the access by using : 
  aws s3 ls

# Why i didnt use access keys
- Because hardcoded credentials is insecure while establishing an IAM Role is temporary, secured and auto-rotated

# Part 5 - Backup Strategy

Database backup

pg_dump -> /tmp -> S3

Command:
pg_dump $DB_LINK -F c -f /tmp/mydb_<timestamp>.dump
aws s3 cp /tmp/mydb_*.dump s3://<bucket>/backups/

# NGINX config backup
cp /etc/nginx/nginx.conf -> /tmp -> S3

Command:
sudo cp /etc/nginx/nginx.com /tmp/nginx.conf.bak
aws s3 cp /tmp/nginx.conf.bak s3://<bucket>/configs/nginx.conf

# What devops concepts that was learned
Concept                        Explanation
Reserve proxy         Nginx forwards traffic to backend app
App server               Gunicorn runs Flask in production
Environment variables    Secure way to manage config
IAM roles                Secure AWS access without credentials
Backup strategy          Data must survive server failure
HTTPS                    Mandatory to use for production systems


Using backups are non-negotiable because if you lose connection to a server, you lose your data and has to restart the whole procedure. Security must be built in in order to secure your system from unauthorized access. Servers are pretty much replaceable which can put data in a critical position.

# Summary
We managed to transform a basic Flask Aapp into a secure, database-backed, production-style application with proffesional backu capabilities.
This is the foundation for the usage of scaling (Load Balancers), managed databases (RDS), and high availability architectures.







