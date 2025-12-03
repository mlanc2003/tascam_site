# TASCAM Website – Deployment Guide

This document provides step-by-step instructions for running, configuring, and deploying the TASCAM website on any hosting environment. It is designed for future developers or administrators managing the platform.

---

# 1. Project Overview

The TASCAM website is a Django-based full-stack platform supporting:
- Multi-step tutor request workflow
- Tutor job application system
- Testimonials page
- Program-specific tutoring pages
- Client and tutor resource sections
- Dynamic dropdown and timeslot logic
- Modern CSS and template structure
- Custom navigation and branding

This guide covers **local setup**, **production deployment**, and **general server configuration**.

---

# 2. Local Development Setup

## Step 1 — Install Requirements
You must install:
- Python 3.10+
- pip
- virtualenv (optional but recommended)
- Git

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git
```

---

## Step 2 — Clone the Repository
```bash
git clone https://github.com/mlanc2003/tascam_site
cd tascam_site
```

---

## Step 3 — Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
# Windows:
# venv\Scripts\activate
```

---

## Step 4 — Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Step 5 — Configure Environment Variables
Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Use the `.env.example` included in the repository as a reference.

---

## Step 6 — Apply Database Migrations
```bash
python manage.py migrate
```

---

## Step 7 — Collect Static Files
```bash
python manage.py collectstatic
```

---

## Step 8 — Run the Development Server
```bash
python manage.py runserver
```

Access the site at:
```
http://127.0.0.1:8000/
```

---

# 3. Preparing for Production Deployment

This project can be deployed on:
- AWS EC2 / Lightsail
- DigitalOcean Droplets
- Heroku-like container services
- Any Linux VPS (Ubuntu preferred)
- Internal company servers

The typical production stack is:

- **Nginx** → Reverse proxy  
- **Gunicorn** → Application server  
- **Supervisor/systemd** → Process manager  
- **PostgreSQL** → Production database  
- **Django** → Backend framework  
- **Static files served by Nginx**  

---

# 4. Production Deployment Steps

## Step 1 — Set Environment Variables on Server
Set variables based on the private `env_variables.txt` file:

```
SECRET_KEY=xxx
DEBUG=False
ALLOWED_HOSTS=tascam-domain.com
DATABASE_URL=postgres://username:password@host:5432/db
```

---

## Step 2 — Install Dependencies
Same as local environment.

---

## Step 3 — Collect Static Files
```bash
python manage.py collectstatic --noinput
```

---

## Step 4 — Start Gunicorn
```
gunicorn tascam_site.wsgi:application --bind 0.0.0.0:8000
```

---

## Step 5 — Configure Nginx
Example:

```
server {
    listen 80;
    server_name tascam-domain.com;

    location /static/ {
        alias /path/to/tascam_site/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
    }
}
```

---

# 5. Optional Enhancements
- Add HTTPS using Let’s Encrypt  
- Switch from SQLite to PostgreSQL  
- Use a managed database service (AWS RDS, DigitalOcean Managed DB, etc.)  
- Set up CI/CD from GitHub  

---

# 6. Contact
For questions, refer to the **PROJECT_SUMMARY.md** or inspect the project tree in GitHub.

---

# End of Deployment Guide