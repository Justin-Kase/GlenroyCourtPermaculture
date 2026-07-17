# Glenroy Court Permaculture

A full-stack permaculture garden website built with Django 4.0, featuring a plant database, blog, gallery, dashboard, and content management system.

🌱 [Live Demo](#) · 📖 [Documentation](#) · 🐛 [Report Bug](https://github.com/Justin-Kase/GlenroyCourtPermaculture/issues)

---

## ✨ Features

- **🌿 Plant Database** — 19 plants across 3 categories (vegetables, herbs, fruit) with detailed growing guides, companion planting, difficulty ratings, and seasonal calendars
- **📝 Blog** — Rich text articles with categories, tags, draft/published states, and comment system
- **🖼️ Gallery** — Filterable image gallery with lightbox viewer
- **📊 Dashboard** — Interactive charts powered by Chart.js showing greenhouse data over time
- **📬 Contact Form** — Working contact page with form validation
- **🔐 CMS (Admin Panel)** — Full content management system for blog posts, plants, and gallery
- **🎨 Custom Plant Images** — Auto-generated SVG plant illustrations with category badges
- **📱 Responsive Design** — Bootstrap 5-based responsive layout

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 4.0, Python 3 |
| **Frontend** | Bootstrap 5, Chart.js |
| **Rich Text** | django-summernote |
| **API** | GraphQL (graphene-django) |
| **Charts** | django-chartjs |
| **Database** | SQLite (dev), ready for PostgreSQL/Turso |

## 📁 Project Structure

```
├── GlenroyCourtPermaculture/    # Main Django project (settings, URLs, views)
├── vegetables/                  # Plant database app (models, views, admin)
├── dashboard/                   # Charts & greenhouse monitoring
├── gallery/                     # Image gallery with categories
├── utils/                       # Chart helper utilities
├── templates/                   # Shared HTML templates
├── static/                      # CSS, JS, images
├── staticfiles/                 # Collected static files
└── media/                       # User-uploaded media
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/Justin-Kase/GlenroyCourtPermaculture.git
cd GlenroyCourtPermaculture

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install django django-summernote graphene-django django-chartjs Pillow

# Run migrations
python manage.py migrate

# Create superuser (for CMS access)
python manage.py createsuperuser

# Start the dev server
python manage.py runserver
```

Visit **http://localhost:8000** to see the site.

### Access the CMS

1. Go to `/admin` or `/login`
2. Log in with your superuser credentials
3. Manage blog posts, plants, and gallery from the admin dashboard

### Generate Plant Images

```bash
python manage.py generate_plant_images
```

## 📄 License

ISC © Justin Trushell
