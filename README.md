# DevCareer 🚀

### A developer career management platform that turns career activity into measurable progress.

**DevCareer** is a full-stack career management platform built with **Python and Flask** that gives developers one centralized workspace to manage their projects, technical skills, job applications, career goals, and learning progress.

Instead of simply storing career information, DevCareer connects these areas to provide **Career Score, Career Intelligence, application analytics, career progress tracking, and personalized next-action recommendations.**

> **Track what you're building, what you're learning, where you're applying, and what you should focus on next — all from one place.**

---

## 🎯 Why DevCareer?

A developer's career activity is usually spread across multiple tools:

* GitHub for projects
* Spreadsheets for job applications
* Notes for career goals
* Learning platforms for courses
* Separate tools for tracking technical skills

DevCareer brings these workflows together into a single career workspace.

The goal isn't just to answer:

> **"What have I done?"**

It also aims to answer:

> **"Where am I progressing, where am I falling behind, and what should I focus on next?"**

---

## ✨ Core Features

### 📊 Career Dashboard

A centralized career command center that provides an overview of career activity.

* Career Score
* Project statistics
* Skill proficiency
* Application pipeline
* Interview and offer metrics
* Goal progress
* Learning progress
* Recent career activity
* Career Intelligence
* Career Progress
* Next Best Action

---

### 🚀 Project Management

Manage and track development projects from one place.

* Create projects
* Edit project information
* Track project status
* Monitor completed projects
* Monitor in-progress projects
* Track planned projects
* View recent projects from the dashboard

---

### 🧠 Skill Tracking

Track technical skills and monitor proficiency.

* Add technical skills
* Assign proficiency levels
* Calculate average proficiency
* Identify strongest skills
* Identify skills requiring improvement
* Display top skills

---

### 💼 Job Application Tracker

Manage internship and job applications through a structured pipeline.

```text
Wishlist
   ↓
Applied
   ↓
Assessment
   ↓
Interview
   ↓
Offer
```

Additional outcomes:

```text
Rejected
Withdrawn
```

Application records can include:

* Company
* Position
* Application date
* Job posting link
* Notes
* Application status
* Edit functionality
* Delete functionality

---

### 📈 Application Analytics

DevCareer converts application records into useful job-search metrics.

The dashboard tracks:

* Total applications
* Active applications
* Interviews
* Offers
* Rejections
* Interview rate
* Offer rate
* Application pipeline

This helps developers understand not only **how many applications they submitted**, but also how their job search is performing.

---

### 🎯 Goal Management

Create and track career objectives.

* Create career goals
* Track progress
* Monitor active goals
* Track completed goals
* Calculate average goal progress
* Identify goals requiring attention

---

### 📚 Learning Tracker

Connect learning activity directly with career development.

* Add learning topics
* Track progress
* Track learning status
* Monitor active learning
* Track completed learning
* Calculate overall learning progress

---

## 🧠 Career Intelligence

One of DevCareer's core concepts is moving beyond traditional CRUD functionality.

The Career Intelligence layer analyzes the user's existing career activity and identifies areas that may require attention.

```text
Projects ───────┐
Skills ─────────┤
Applications ───┼──► Career Intelligence
Goals ──────────┤             │
Learning ───────┘             ▼
                    Personalized Insights
                              +
                       Next Best Action
```

The system can identify areas such as:

* Weak technical skills
* Lack of practical projects
* Low application activity
* Inactive career goals
* Learning that could be converted into practical work
* Portfolio areas requiring improvement

The underlying idea is simple:

> **Don't just tell the developer what they have done. Help them understand what they should focus on next.**

---

## 🎯 Career Score

DevCareer calculates a **0–100 Career Score** using multiple career signals.

Current scoring factors include:

* Project activity
* Number of technical skills
* Skill proficiency
* Job application activity

The score is designed as a **progress indicator**, not as a definitive measurement of someone's career ability.

As career activity changes, the score changes with it.

### Current scoring model

```text
Project Activity      → 30 points
Skill Count           → 25 points
Application Activity  → 20 points
Skill Proficiency     → 25 points
                         ─────
                         100
```

---

## 📈 Career Progress

Career Progress provides a unified view of development across multiple areas.

It combines:

* Overall Career Score
* Portfolio progress
* Skill development
* Learning progress
* Goal progress
* Job-search activity

This makes it easier to identify strengths and areas requiring additional attention.

---

## 🐙 GitHub Integration

DevCareer connects GitHub information with the career dashboard.

The integration can display:

* GitHub profile information
* Repository information
* Programming language summary

This creates a stronger connection between **career tracking and actual development activity**.

---

## 🔐 Authentication & Data Isolation

DevCareer uses **Flask-Login** for user authentication.

Career records are associated with the authenticated user, allowing different users to maintain their own:

* Projects
* Skills
* Applications
* Goals
* Learning records

Passwords are stored using **Werkzeug password hashing utilities** rather than plain text.

---

## 🏗️ Technical Architecture

DevCareer follows a modular Flask architecture.

```text
┌─────────────────────────────────┐
│            Frontend             │
│       HTML + CSS + Jinja2       │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│       Flask Application         │
│                                 │
│  Authentication                 │
│  Routes / Blueprints            │
│  Dashboard                      │
│  API Endpoints                  │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│          Service Layer          │
│                                 │
│  Career Intelligence            │
│  Career Analysis                │
│  GitHub Integration             │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│         SQLAlchemy ORM          │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│             SQLite              │
└─────────────────────────────────┘
```

---

## 📁 Project Structure

```text
DevCareer/
│
├── app/
│   ├── models/
│   │   ├── application.py
│   │   ├── goal.py
│   │   ├── learning.py
│   │   ├── project.py
│   │   ├── skill.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── applications.py
│   │   ├── auth.py
│   │   ├── goals.py
│   │   ├── learning.py
│   │   ├── main.py
│   │   ├── projects.py
│   │   └── skills.py
│   │
│   ├── services/
│   │   └── career_intelligence.py
│   │
│   ├── templates/
│   ├── static/
│   └── __init__.py
│
├── instance/
├── .env
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## 🛠️ Technology Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login

### Database

* SQLite
* SQLAlchemy ORM

### Frontend

* HTML5
* CSS3
* Jinja2

### Integrations & Development

* Git
* GitHub
* GitHub API
* VS Code
* Python Virtual Environment

---

## 🔌 API Layer

DevCareer includes a backend API layer that provides a foundation for programmatic access to platform functionality.

This architecture creates opportunities for future integrations such as:

* External dashboards
* Mobile applications
* Automation
* AI-powered services
* Third-party integrations

---

## ⚙️ Getting Started

### Prerequisites

Make sure you have:

* Python 3.x
* Git

### 1. Clone the repository

```bash
git clone https://github.com/Rohittt-commits/DevCareer---platform-.git
cd DevCareer---platform-
```

### 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
```

If additional integrations require credentials, configure them through environment variables.

> **Never commit API keys, passwords, or other secrets to GitHub.**

### 5. Run the application

```bash
python run.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## 🧪 Development & Testing

Before committing changes, compile the application to catch Python syntax errors:

```bash
python -m compileall app
```

Then run the application:

```bash
python run.py
```

For Git workflow:

```bash
git status
git add .
git commit -m "Your commit message"
git push origin main
```

---

## 💡 Development Philosophy

DevCareer is built around one simple idea:

> **Career data should be useful, not just stored.**

A traditional tracker answers:

> "What have I done?"

DevCareer aims to additionally answer:

> **"Where am I progressing, where am I falling behind, and what should I focus on next?"**

This philosophy drives the platform's:

* Career Score
* Career Intelligence
* Application Analytics
* Career Progress
* Next Best Action

---

## 🗺️ Future Improvements

Potential future improvements include:

* [ ] AI-powered resume analysis
* [ ] Automated skill-gap detection
* [ ] Personalized learning recommendations
* [ ] Job recommendation engine
* [ ] Resume generation
* [ ] PostgreSQL support
* [ ] Cloud deployment
* [ ] OAuth authentication
* [ ] Advanced GitHub activity analysis

These features are intentionally outside the current core scope so the existing platform remains focused and maintainable.

---

## 📌 Current Status

### ✅ Core Platform Functional

DevCareer currently includes:

* ✅ User authentication
* ✅ Developer dashboard
* ✅ Project management
* ✅ Skill tracking
* ✅ Job application tracking
* ✅ Application Analytics
* ✅ Goal management
* ✅ Learning management
* ✅ Career Score
* ✅ Career Intelligence
* ✅ Next Best Action recommendations
* ✅ Career Progress
* ✅ GitHub integration
* ✅ Backend API layer

### 🚀 Project Status

**Portfolio-ready full-stack Python project.**

The project is actively maintained and serves as a practical demonstration of:

* Backend development with Flask
* Database design with SQLAlchemy
* Authentication and user data isolation
* Service-layer architecture
* Data-driven career analytics
* API integration
* Git/GitHub workflow
* Building a complete real-world web application

---

## 👨‍💻 Author

### Rohit Joshi

**BCA Student · Python Backend Developer · AI/ML Enthusiast**

Building practical software projects focused on backend development, AI-assisted applications, and real-world problem solving.

**GitHub:** Rohittt-commits

**LinkedIn:** Rohit Joshi

---

## 📄 License

This project is currently developed as a personal portfolio and learning project.
