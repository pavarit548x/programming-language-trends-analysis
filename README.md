ส่วนที่ 1: Docker Commands (จัดการ Database Server)
🔹 1️⃣ เริ่ม PostgreSQL Container
docker compose up -d

สร้างและเปิด PostgreSQL container จาก docker-compose.yml

ใช้เมื่อไร?

ครั้งแรกที่เริ่มโปรเจค

หรือหลังจาก docker compose down

🔹 2️⃣ ปิด Container
docker compose down

ทำอะไร?

หยุดและลบ container

ใช้เมื่อไร?

ต้องการ restart ใหม่

เปลี่ยน config ใน docker-compose.yml

🔹 3️⃣ ดูว่า container รันอยู่ไหม
docker ps

ทำอะไร?

แสดง container ที่กำลังรันอยู่

🔹 4️⃣ เข้า PostgreSQL (psql)
docker exec -it team_db psql -U admin -d teamdb

ทำอะไร?

เข้า PostgreSQL interactive mode

-it = เปิด terminal mode

ใช้เมื่อไร?

จะพิมพ์ SQL ตรง ๆ

จะตรวจสอบ table

🐘 ส่วนที่ 2: PostgreSQL Commands (ใช้ใน psql)

เมื่อเข้าแล้วจะเห็น:

teamdb=#
🔹 5️⃣ ดูรายการ table
\dt

ทำอะไร?

แสดง table ทั้งหมดใน database

🔹 6️⃣ ดูโครงสร้าง table
\d table_name

ตัวอย่าง:

\d users

ทำอะไร?

ดู column, datatype, constraint

🔹 7️⃣ ออกจาก PostgreSQL
\q


📂 ส่วนที่ 3: Migration Commands (รันไฟล์ SQL)
🔹 8️⃣ รันไฟล์ SQL (PowerShell version)
Get-Content .\migrations\001_create_tables.sql | docker exec -i team_db psql -U admin -d teamdb

ทำอะไร?

อ่านไฟล์ SQL

ส่งเข้า PostgreSQL

ใช้แทน < ใน Windows

ใช้เมื่อไร?

สร้าง table

เพิ่ม column

เพิ่ม constraint

🔹 9️⃣ รันไฟล์ SQL (ถ้าใช้ Git Bash)
docker exec -i team_db psql -U admin -d teamdb < migrations/001_create_tables.sql
📊 ส่วนที่ 4: SQL พื้นฐานที่ควรรู้
🔹 🔟 สร้าง table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL
);

ทำอะไร?

สร้าง table ใหม่

🔹 1️⃣1️⃣ เพิ่ม column
ALTER TABLE users ADD COLUMN email TEXT;
🔹 1️⃣2️⃣ เพิ่มข้อมูล
INSERT INTO users (username)
VALUES ('John');
🔹 1️⃣3️⃣ ดูข้อมูล
SELECT * FROM users;
🔹 1️⃣4️⃣ ลบ table
DROP TABLE users;

⚠ ใช้ระวัง เพราะลบถาวร

🧠 ส่วนที่ 5: คำสั่ง Debug ที่ใช้บ่อย
🔹 ดู database ทั้งหมด
\l
🔹 เปลี่ยน database
\c teamdb
🎓 สรุป Workflow ที่ทีมควรใช้
ทุกครั้งที่เริ่มงาน
docker compose up -d
เพิ่มโครงสร้างใหม่

สร้างไฟล์ใน migrations/

รันด้วย:

Get-Content .\migrations\xxx.sql | docker exec -i team_db psql -U admin -d teamdb
ตรวจสอบ
docker exec -it team_db psql -U admin -d teamdb
\dt
