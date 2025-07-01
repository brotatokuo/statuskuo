# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django/Wagtail CMS project for a photography business called "StatusKuo". It's built with Django 5.2 and Wagtail 7.0, using SQLite as the database.

## Development Commands

### Core Django Commands
- `python manage.py runserver` - Start development server (default: http://127.0.0.1:8000/)
- `python manage.py migrate` - Apply database migrations
- `python manage.py makemigrations` - Create new migrations
- `python manage.py createsuperuser` - Create admin user for Wagtail admin
- `python manage.py collectstatic` - Collect static files for production

### Testing and Validation
- `python manage.py check` - Check for common Django issues
- `python manage.py test` - Run Django test suite

### Wagtail-Specific Commands
- `python manage.py update_index` - Update search index
- `python manage.py wagtail_update_image_renditions` - Update image renditions
- `python manage.py setup_homepage` - Set up homepage with default content (custom command)
- `python manage.py setup_photography_pages` - Set up all photography gallery pages and booking page (custom command)

## Architecture

### Settings Structure
- `statuskuo_wagtail/settings/base.py` - Base settings shared across environments
- `statuskuo_wagtail/settings/dev.py` - Development settings (DEBUG=True, insecure secret key)
- `statuskuo_wagtail/settings/production.py` - Production settings (not yet configured)
- Default settings module: `statuskuo_wagtail.settings.dev`

### App Structure
- **home** - Main app containing the HomePage model with hero section, featured images, about section, and contact info
- **search** - Basic search functionality for Wagtail pages
- **statuskuo_wagtail** - Main project configuration

### Key Models
- `home.models.HomePage` - Main page model with fields for hero content, featured images, about text, and contact information
- `home.models.GraduationPage`, `WeddingPage`, `PersonalPage` - Photography gallery pages that inherit from `PhotoGalleryPage`
- `home.models.PhotoGalleryPage` - Base model for photo galleries with intro text and inline gallery images
- `home.models.PhotoGalleryImage` - Orderable model for gallery images with captions
- `home.models.BookingPage` - Page for booking form with intro text
- `home.models.BookingRequest` - Model to store booking requests from users

### URL Configuration
- Admin panel: `/admin/` (Wagtail admin)
- Django admin: `/django-admin/`
- Documents: `/documents/`
- Search: `/search/`
- Booking form: `/booking/` (custom view)
- Photography galleries: `/graduation/`, `/wedding/`, `/personal/` (Wagtail pages)
- All other URLs handled by Wagtail's page serving

### Static Files and Media
- Static files: `/static/` (collected to `static/` directory)
- Media uploads: `/media/` (stored in `media/` directory)
- Allowed document types: CSV, DOCX, KEY, ODT, PDF, PPTX, RTF, TXT, XLSX, ZIP

## Non-Technical User Guidance

### Initial Setup
1. Run `python manage.py createsuperuser` to create an admin account
2. Run `python manage.py setup_homepage` to set up the homepage
3. Run `python manage.py setup_photography_pages` to create all photography pages
4. Start the server with `python manage.py runserver`

### Managing Content
- **Homepage**: Visit `/admin/pages/` → Home to edit hero content, about text, and contact info
- **Photo Galleries**: Visit `/admin/pages/` → Graduation/Wedding/Personal Photography to add photos and captions
- **Booking Requests**: Visit `/django-admin/home/bookingrequest/` to view booking submissions
- **Adding Photos**: In gallery pages, scroll down to "Gallery images" section and click "Add Gallery images"

### Site Structure
- **Homepage** (`/`): Hero section, featured work, photography categories, about, contact
- **Graduation Photography** (`/graduation/`): Gallery of graduation photos
- **Wedding Photography** (`/wedding/`): Gallery of wedding photos  
- **Personal Photography** (`/personal/`): Gallery of personal/portrait photos
- **Booking** (`/booking/`): Contact form for photography session requests

## Docker Support

The project includes a Dockerfile for containerized deployment:
- Based on Python 3.12 slim
- Runs on port 8000 with Gunicorn
- Includes automatic migration on startup (not recommended for production)

## Database

Uses SQLite (`db.sqlite3`) for development. Database migrations are in `home/migrations/` and handle the evolution of the HomePage model structure.