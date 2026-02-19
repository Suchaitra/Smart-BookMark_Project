🔖 Smart Bookmark Manager
A full-stack web application built using Django that allows users to manage bookmarks efficiently.
This project demonstrates CRUD (Create, Read, Update, Delete) operations with a clean UI and persistent database storage.


📌 1️⃣ Project Overview
The Smart Bookmark Manager allows users to:
- Add new bookmarks
- View all saved bookmarks
- Update existing bookmarks
- Delete bookmarks
Each bookmark contains:
- Title
- URL


🚀 Features
- ➕ Add new bookmarks
- 📄 View all saved bookmarks
- ✏️ Update existing bookmarks
- 🗑️ Delete bookmarks
- 🎨 Clean UI with external CSS styling
- 💾 Persistent data storage using SQLite database



🛠️ Tech Stack
- Backend: Python, Django
- Frontend: HTML, CSS
- Database: Deflaut SQLite
- Deployment: Render 



📂 Project Structure
BookMark_project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── Procfile
│
├── myapp/
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ └── static/
│
└── BookMark_project/
└── settings.py

⚙️ Installation & Setup

Follow these steps to run the project locally:

1️. Clone the repository
```bash
git clone https://github.com/yourusername/Smart-BookMark_Project.git
cd Smart-BookMark_Project


2. Create Virtual Environment
python -m venv test
.test\Scripts\activate 


3. Apply Migrations
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser


4. Run Development Server
py manage.py runserver


5. API Endpoints :
/ → View all bookmarks
/add/ → Add bookmark
/update/<id>/ → Update bookmark
/delete/<id>/ → Delete bookmark

📌 Samples of Project :
  In folder Assests.


LIVE DEPLOYMENT LINK :
      https://smart-bookmark-project.onrender.com/
