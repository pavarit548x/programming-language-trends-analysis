# 🗄️ Team Database Project
PostgreSQL + Docker (Local Development)

## 👥 Team Members
1. Name 1 - Student ID
2. Name 2 - Student ID
3. Name 3 - Student ID
4. Name 4 - Student ID
5. Name 5 - Student ID

---

## 📌 Project Overview
This project is a PostgreSQL database system developed for academic submission.

The system includes:
- Database schema design
- Table creation using SQL migrations
- Sample data insertion
- Dockerized PostgreSQL environment
- Version control using GitHub

---

## 🛠 Technologies Used
- PostgreSQL 16
- Docker & Docker Compose
- Git & GitHub

---

## 📂 Project Structure


team-database-project/
│
├── docker-compose.yml
├── migrations/
│ ├── 001_create_tables.sql
│ ├── 002_insert_data.sql
│
├── docs/
│ └── ER-diagram.png
│
└── README.md


---

## 🚀 How to Run the Project

### 1️⃣ Start PostgreSQL Container

```bash
docker-compose up -d
2️⃣ Check Running Containers
docker ps
3️⃣ Connect to Database
docker exec -it team_db psql -U admin -d teamdb
4️⃣ Run Migration File (PowerShell)
Get-Content migrations/001_create_tables.sql | docker exec -i team_db psql -U admin -d teamdb
🔄 Team Workflow
📥 Pull latest updates
git pull
✏️ After making changes
git add .
git commit -m "Describe your changes"
git push
🧠 Database Design

The database includes:

APP_USER

LOGISTICS_PROVIDER

LOCATION

(Add your tables here)

Refer to ER Diagram inside /docs folder.

📝 Notes

Do NOT upload .env files

Do NOT modify main branch directly (if using branch workflow)

Always git pull before working

📦 Stop the Container
docker-compose down
