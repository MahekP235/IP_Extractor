# Log File IP Extraction

## Project Overview
 This project processes a log file to extract IP addresses, categorizes them into Public and Private, and stores them in MongoDB using a Dockerized Python application.

## Prerequisites
1. Docker
2. Python 3.9+
3. MongoDB (running inside Docker)
4. VS Code (with the MongoDB extension for viewing the database)

## How to Run
### **Step 1: Setup Instruction**
1. `git clone https://github.com/MahekP235/IP_Extractor.git`
2. `cd IT_EXTRACTOR`

### **Step 2: Build and Run**
Open the terminal and navigate to the project directory. Then run the following commands:
1. `docker-compose down --remove-orphans` (optional)
2. `docker-compose build --no-cache`
3. `docker-compose up app`

### **Step 3: Verification**
1. `docker-compose exec mongo mongosh ip_database --eval "db.public_ips.find()"`
2. `docker-compose exec mongo mongosh ip_database --eval "db.private_ips.find()"`

