# 📋 Job Application Tracker

A full‑stack web application built with **Django** that helps job seekers track their applications across multiple companies. It provides CRUD operations, status dashboards, form validation, custom middleware, and a responsive Bootstrap 5 interface.

---

## ✨ Features

- **Dashboard** – view total applications and counts by status (Applied, Interview, Offer, Accepted, Rejected).  
- **CRUD Operations** – create, read, update, and delete job applications.  
- **Form Validation** – ensures data integrity (required fields, negative salary prevention, date logic, note length limit).  
- **Responsive UI** – built with Bootstrap 5, works seamlessly on desktop, tablet, and mobile.  
- **Custom Middleware** – logs each request’s timestamp, method, and path to the console.  
- **Success Messages** – user feedback after every create, update, or delete action.  
- **Detail Page** – bonus view for a single application’s full information.

---

## 🛠️ Tech Stack

| Layer       | Technology                               |
|-------------|------------------------------------------|
| Backend     | Django 4.x (Python)                      |
| Database    | SQLite (default, can switch to PostgreSQL/MySQL) |
| Frontend    | HTML5, Bootstrap 5, Django Template Language |
| Middleware  | Custom Request Logger                    |
| Version Control | Git & GitHub                         |

---

## 📁 Project Structure

```
job_tracker/
├── job_tracker/               # Project settings
├── jobs/                      # Main app
│   ├── migrations/
│   ├── templates/jobs/        # App-specific templates
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py               # ModelForm with validations
│   ├── models.py              # JobApplication model
│   ├── views.py               # CRUD views
│   ├── urls.py                # App routes with namespace
│   └── middleware.py          # RequestLoggerMiddleware
├── templates/                 # Project-level templates
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── home.html
│   └── jobs/                  # Shared templates (list, create, update, delete, detail)
├── static/                    # Static files (CSS, JS) – optional
├── manage.py
└── db.sqlite3                 # Default database
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
https://github.com/yeaminhossainfuhad-cloud/Job_Application_Tracker.git
cd job-application-tracker
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install django
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

6. **Open your browser** and go to `http://127.0.0.1:8000/`

---

## 📸 Screenshots

> *Add your own screenshots by placing images in a `screenshots/` folder and referencing them.*

![Dashboard](screenshots/dashboard.png)  
![Add Form](screenshots/add.png)  
![List View](screenshots/list.png)

---

## 🔧 Usage Guide

- **Home** – summary cards showing application counts per status.  
- **All Applications** – table view of all jobs with actions (View, Edit, Delete).  
- **Add Application** – form with validation; all fields except salary are required.  
- **Edit** – update any existing application.  
- **Delete** – confirmation page before removal.  
- **Detail** – see all fields for a specific application.

---

## 🧪 Validation Rules

| Field          | Rule                                                   |
|----------------|--------------------------------------------------------|
| Company Name   | Required                                               |
| Position       | Required                                               |
| Salary         | Cannot be negative (optional)                          |
| Deadline       | Cannot be earlier than Application Date                |
| Notes          | Maximum 500 characters                                 |

Errors are displayed directly below each field.

---

## 🧩 Custom Middleware

The `RequestLoggerMiddleware` logs every request to the console in the format:

```
---------------------------------
Time : 2026-07-22 10:45 AM
Method : GET
Path : /jobs/
---------------------------------
```

It is registered in `MIDDLEWARE` and runs on every request.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository.  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).  
4. Push to the branch (`git push origin feature/AmazingFeature`).  
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

Your Name – [MD Yeamin Hossain Fuhad](mailto:yeaminhossainfuhad@gmail.com)  
Project Link: [GitHub](https://github.com/yeaminhossainfuhad-cloud/Job_Application_Tracker.git)

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)  
- [Bootstrap 5](https://getbootstrap.com/)  
- [Font Awesome](https://fontawesome.com/) (optional icons)

---

**Happy job tracking!** 🚀
