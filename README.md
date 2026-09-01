# DevCareer 🚀

### A developer career management platform that turns career activity into measurable progress.

DevCareer is a full-stack career management platform built with **Python and Flask** that gives developers one centralized workspace to manage their projects, technical skills, job applications, career goals, and learning progress.

Instead of simply storing career information, DevCareer connects these areas to provide **Career Score, Career Intelligence, application analytics, and personalized next-action recommendations**.

---

## 🎯 What is DevCareer?

Managing a developer career often means switching between multiple tools:

* GitHub for projects
* Spreadsheets for applications
* Notes for career goals
* Learning platforms for courses
* Separate tools for tracking technical skills

DevCareer brings these workflows together into a single career workspace.

> **Track what you're building, what you're learning, where you're applying, and what you should focus on next — all from one place.**

---

## ✨ Key Features

### 📊 Career Dashboard

A centralized career command center showing:

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

---

### 🚀 Project Management

Manage your development portfolio from one place.

* Create projects
* Edit project information
* Track project status
* Monitor completed, in-progress, and planned projects
* View recent projects directly from the dashboard

---

### 🧠 Skill Tracking

Track technical skills and monitor proficiency over time.

* Add technical skills
* Assign proficiency levels
* Identify strongest skills
* Identify skills that need improvement
* Calculate average skill proficiency

---

### 💼 Job Application Tracker

Manage internship and job applications through a structured pipeline.

Supported stages include:

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

The application system provides:

* Application tracking
* Company and position information
* Application dates
* Job posting links
* Notes
* Status management
* Edit and delete functionality

---

### 📈 Application Analytics

DevCareer transforms application records into useful job-search metrics.

The dashboard provides:

* Total applications
* Active applications
* Interviews
* Offers
* Rejections
* Interview rate
* Offer rate
* Application pipeline breakdown

This helps developers understand not only **how many applications they submitted**, but also how their job search is performing.

---

### 🎯 Goal Management

Set and track career objectives.

* Create career goals
* Track progress
* Monitor active goals
* Track completed goals
* Calculate average goal progress
* Identify goals requiring attention

---

### 📚 Learning Tracker

Keep learning progress connected to career development.

* Add learning topics
* Track progress
* Track learning status
* Monitor active learning
* Track completed learning
* Calculate overall learning progress

---

### 🧠 Career Intelligence

One of DevCareer's core concepts is moving beyond traditional CRUD functionality.

The Career Intelligence layer analyzes the user's existing career data and identifies areas that may require attention.

It considers information from:

```text
Projects ───────┐
Skills ─────────┤
Applications ───┼──► Career Intelligence
Goals ──────────┤           │
Learning ───────┘           ▼
                    Personalized Insights
                    + Next Best Action
```

Examples of recommendations include:

* Strengthening a weak technical skill
* Turning learning into a practical project
* Improving portfolio strength
* Increasing application activity
* Making progress on an inactive goal

The system is designed to answer:

> **"What should I focus on next?"**

rather than simply:

> "What data do I have?"

---

## 🎯 Career Score

DevCareer calculates a **0–100 Career Score** using multiple career signals.

Current scoring factors include:

* Project activity
* Number of technical skills
* Skill proficiency
* Job application activity

The score is intended as a **progress indicator**, not as a definitive measurement of someone's career.

As the user's career activity changes, the score changes with it.

---

## 📈 Career Progress

Career Progress provides a unified view of development across multiple areas.

It brings together:

* Overall Career Score
* Portfolio progress
* Skill development
* Learning progress
* Goal progress
* Job-search activity

This makes it easier to identify strengths and areas that need additional attention.

---

## 🐙 GitHub Integration

DevCareer includes GitHub profile integration to connect a developer's coding identity with their career dashboard.

The dashboard can display GitHub-related information such as:

* GitHub profile
* Repository information
* Programming language summary

This creates a stronger connection between **career tracking and actual development work**.

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
│        Flask Application        │
│                                 │
│ Authentication                  │
│ Routes / Blueprints             │
│ Dashboard                       │
│ API Endpoints                   │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│          Service Layer          │
│                                 │
│ Career Intelligence             │
│ Career Analysis                 │
│ GitHub Integration              │
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
* GitHub API integration
* VS Code
* Python Virtual Environment

---

## 🔌 API Layer

DevCareer includes a backend API layer that provides a foundation for accessing platform functionality programmatically.

This architecture allows the project to be extended in the future toward:

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

### Clone the repository

```bash
git clone https://github.com/Rohittt-commits/DevCareer---platform-.git
cd DevCareer---platform-
```

### Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
```

If additional integrations require credentials, configure them through environment variables.

**Never commit API keys, passwords, or other secrets to GitHub.**

### Run the application

```bash
python run.py
```

Open the application at:

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

---

## 💡 Development Philosophy

DevCareer is built around one simple idea:

> **Career data should be useful, not just stored.**

A traditional tracker answers:

> "What have I done?"

DevCareer aims to additionally answer:

> **"Where am I progressing, where am I falling behind, and what should I focus on next?"**

This philosophy drives the Career Score, Career Intelligence, Application Analytics, and Career Progress features.

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

These features are intentionally kept outside the current core scope so the existing platform can remain focused and maintainable.

---

## 📌 Current Status

### ✅ Core Platform Functional

DevCareer currently includes:

* User authentication
* Developer dashboard
* Project management
* Skill tracking
* Job application tracking
* Application Analytics
* Goal management
* Learning management
* Career Score
* Career Intelligence
* Next Best Action recommendations
* Career Progress
* GitHub integration
* Backend API layer

The project is currently being prepared as a **portfolio-ready full-stack Python project**.

---

## 👨‍💻 Author

### Rohit Joshi

**BCA Student · Python Backend Developer · AI/ML Enthusiast**

Building practical software projects focused on backend development, AI-assisted applications, and real-world problem solving.

**GitHub:**
https://github.com/Rohittt-commits

**LinkedIn:**
https://www.linkedin.com/in/rohit-joshi-910346381

---

## 📄 License

This project is currently developed as a personal portfolio and learning project.
