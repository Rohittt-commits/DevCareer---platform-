# DevCareer

### A developer career management platform for turning career progress into measurable growth.

DevCareer is a full-stack career management platform built with **Python and Flask** that gives developers a centralized workspace to manage their projects, technical skills, job applications, career goals, and learning progress.

The platform combines structured career tracking with **Career Intelligence**, turning a user's activity into actionable recommendations instead of simply storing information.

---

## Overview

Managing a developer career often means using multiple disconnected tools:

* GitHub for projects
* Spreadsheets for job applications
* Notes for career goals
* Separate platforms for learning
* Different places to track technical skills

**DevCareer brings these workflows together.**

The goal is simple:

> **Track what you're building, what you're learning, where you're applying, and where you need to improve — all from one place.**

---

## Core Capabilities

| Area                    | What DevCareer Provides                          |
| ----------------------- | ------------------------------------------------ |
| **Dashboard**           | Centralized view of career activity and progress |
| **Projects**            | Create, manage, and track development projects   |
| **Skills**              | Track technical skills and proficiency           |
| **Applications**        | Manage internships and job applications          |
| **Goals**               | Define and monitor career objectives             |
| **Learning**            | Track courses, topics, and learning progress     |
| **Career Intelligence** | Generate data-driven career recommendations      |
| **Career Score**        | Measure overall career activity                  |
| **Authentication**      | Secure user registration and login               |
| **API**                 | Backend API layer for programmatic access        |

---

## Career Dashboard

The dashboard acts as the user's **career command center**.

It brings together:

* Career Score
* Project activity
* Skill proficiency
* Application pipeline
* Interview and offer metrics
* Goal progress
* Learning progress
* Recent activity
* Career Intelligence recommendations

This allows users to understand their current career position without manually combining data from different places.

---

## Career Intelligence

One of the main ideas behind DevCareer is moving beyond traditional CRUD functionality.

The **Career Intelligence** layer analyzes information already stored in the platform and identifies areas that may require attention.

For example:

```text
Projects ───────┐
Skills ─────────┤
Applications ───┼──► Career Intelligence ──► Recommendations
Goals ──────────┤
Learning ───────┘
```

Instead of simply showing:

> "You have 3 skills."

DevCareer can use that information alongside proficiency, projects, applications, and learning activity to provide more meaningful career guidance.

---

## Career Score

DevCareer provides a simple **0–100 Career Score** based on multiple career signals.

The score currently considers:

* Project activity
* Number of technical skills
* Skill proficiency
* Job application activity

The purpose isn't to claim that a number defines someone's career.

Instead, it provides a **quick progress indicator** that can change as the developer becomes more active and improves their profile.

---

## Application Tracking

The application tracker is designed around a real internship/job-search workflow.

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

It also supports outcomes such as:

```text
Rejected
Withdrawn
```

DevCareer calculates useful metrics such as:

* Total applications
* Active applications
* Interviews
* Offers
* Interview rate
* Offer rate

---

## Technical Architecture

DevCareer follows a modular Flask architecture.

```text
┌───────────────────────────────┐
│           Frontend            │
│     HTML + CSS + Jinja2       │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        Flask Application       │
│                               │
│  Authentication              │
│  Routes / Blueprints         │
│  Business Logic              │
│  API Endpoints               │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       Service Layer           │
│                               │
│   Career Intelligence         │
│   Career Analysis             │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       SQLAlchemy ORM          │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│           SQLite              │
└───────────────────────────────┘
```

---

## Project Structure

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

## Technology Stack

### Backend

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **Flask-Login**

### Database

* **SQLite**
* **SQLAlchemy ORM**

### Frontend

* **HTML5**
* **CSS3**
* **Jinja2**

### Development

* **Git**
* **GitHub**
* **VS Code**
* **Python Virtual Environment**

---

## Authentication & Data Isolation

DevCareer uses **Flask-Login** for authentication.

Each user's career data is associated with their authenticated account, allowing projects, skills, applications, goals, and learning records to remain user-specific.

Passwords are stored using Werkzeug's password hashing utilities rather than plain text.

---

## API Layer

DevCareer includes a backend API layer designed to make platform functionality accessible beyond the server-rendered interface.

This creates a foundation for future integrations such as:

* External dashboards
* Mobile applications
* Automation
* AI services
* Third-party career tools

The API architecture also keeps the project open for future expansion rather than limiting the application to server-rendered pages.

---

## Getting Started

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

Windows:

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

### Run the application

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Environment Configuration

Sensitive configuration should be stored in environment variables.

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
```

API credentials and other secrets should **never be committed to the repository**.

---

## Development Philosophy

DevCareer is intentionally built around a simple idea:

**career data should be useful, not just stored.**

A traditional tracker answers:

> "What have I done?"

DevCareer aims to additionally answer:

> **"What should I focus on next?"**

This distinction is what drives the Career Intelligence component and the overall direction of the project.

---

## Roadmap

Planned improvements include:

* [ ] AI-powered resume analysis
* [ ] Skill-gap detection
* [ ] Personalized learning recommendations
* [ ] GitHub activity integration
* [ ] Job recommendation engine
* [ ] Resume generation
* [ ] Advanced career analytics
* [ ] PostgreSQL support
* [ ] Cloud deployment
* [ ] OAuth authentication

---

## Current Status

**Active Development**

The core platform is functional, including authentication, career dashboard, project management, skill tracking, application tracking, goals, learning management, Career Score, Career Intelligence, and API functionality.

---

## Author

### Rohit Joshi

**BCA Student · Python Backend Developer · AI/ML Enthusiast**

Building projects focused on backend development, AI-assisted applications, and practical software engineering.

**GitHub:**
https://github.com/Rohittt-commits

**LinkedIn:**
https://www.linkedin.com/in/rohit-joshi-910346381

---

## License

This project is currently developed as a personal portfolio and learning project.
