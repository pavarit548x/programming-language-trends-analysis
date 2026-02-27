🐘 Team Database Project

PostgreSQL + Docker + Migration Workflow

โปรเจคนี้ใช้ PostgreSQL รันผ่าน Docker เพื่อให้ทีม 5 คนสามารถใช้ database ตัวเดียวกันได้

📦 ส่วนที่ 1: Docker Commands (จัดการ Database Server)
1️⃣ เริ่ม PostgreSQL Container
docker compose up -d

ทำอะไร?

สร้างและเปิด PostgreSQL container จาก docker-compose.yml

รันแบบ background (-d = detached mode)

ใช้เมื่อไร?

ครั้งแรกที่เริ่มโปรเจค

หลังจากใช้ docker compose down

2️⃣ ปิด Container
docker compose down

ทำอะไร?

หยุดและลบ container

ใช้เมื่อไร?

ต้องการ restart ใหม่

เปลี่ยน config ใน docker-compose.yml

3️⃣ ดูว่า Container รันอยู่ไหม
docker ps

ทำอะไร?

แสดง container ที่กำลังรันอยู่

4️⃣ เข้า PostgreSQL (psql)
docker exec -it team_db psql -U admin -d teamdb

ทำอะไร?

เข้า PostgreSQL interactive mode

-it = เปิด terminal mode

ใช้เมื่อไร?

พิมพ์ SQL ตรง ๆ

ตรวจสอบ table

debug ปัญหา

เมื่อเข้าแล้วจะเห็นแบบนี้:

teamdb=#
🐘 ส่วนที่ 2: PostgreSQL Commands (ใช้ใน psql)
5️⃣ ดูรายการ Table
\dt

แสดง table ทั้งหมดใน database

6️⃣ ดูโครงสร้าง Table
\d table_name

ตัวอย่าง:

\d users

แสดง:

column

datatype

constraint

7️⃣ ออกจาก PostgreSQL
\q
📂 ส่วนที่ 3: Migration Commands (รันไฟล์ SQL)
8️⃣ รันไฟล์ SQL (PowerShell - Windows)
Get-Content .\migrations\001_create_tables.sql | docker exec -i team_db psql -U admin -d teamdb

ทำอะไร?

อ่านไฟล์ SQL

ส่งเข้า PostgreSQL

ใช้แทน < ใน Windows

ใช้เมื่อไร?

สร้าง table

เพิ่ม column

เพิ่ม constraint

9️⃣ รันไฟล์ SQL (Git Bash / Mac / Linux)
docker exec -i team_db psql -U admin -d teamdb < migrations/001_create_tables.sql
📊 ส่วนที่ 4: SQL พื้นฐานที่ควรรู้
🔟 สร้าง Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL
);
1️⃣1️⃣ เพิ่ม Column
ALTER TABLE users ADD COLUMN email TEXT;
1️⃣2️⃣ เพิ่มข้อมูล
INSERT INTO users (username)
VALUES ('John');
1️⃣3️⃣ ดูข้อมูล
SELECT * FROM users;
1️⃣4️⃣ ลบ Table
DROP TABLE users;

⚠ คำเตือน: ลบถาวร กู้คืนไม่ได้

🧠 ส่วนที่ 5: Debug Commands
ดู database ทั้งหมด
\l
เปลี่ยน database
\c teamdb
🎓 Workflow ที่ทีมควรใช้
✅ ทุกครั้งที่เริ่มงาน
docker compose up -d
✅ เมื่อเพิ่มโครงสร้างใหม่

สร้างไฟล์ใหม่ในโฟลเดอร์ migrations/

ตัวอย่าง:

migrations/002_add_email_to_users.sql

รันไฟล์

PowerShell

Get-Content .\migrations\002_add_email_to_users.sql | docker exec -i team_db psql -U admin -d teamdb

Git Bash

docker exec -i team_db psql -U admin -d teamdb < migrations/002_add_email_to_users.sql
✅ ตรวจสอบผลลัพธ์
docker exec -it team_db psql -U admin -d teamdb

แล้วพิมพ์

\dt
📁 โครงสร้างโปรเจคแนะนำ
    └── 002_add_email.sql
