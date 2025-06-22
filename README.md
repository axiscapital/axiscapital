
# AxisCapital MVP

This is a minimal proof‑of‑concept for **AxisCapital** – a web platform where users register by email and deposit funds via Binance Pay.  
The stack:

| Part      | Tech |
|-----------|------|
| Backend   | Django 4.2 + Django Rest Framework |
| Frontend  | React 18 (vanilla) |
| Payments  | Binance Pay API (order v2) |
| Auth      | Django session (extend to JWT if needed) |
| Deploy    | Dockerfile (gunicorn) |

## Quick Start (dev)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

In another terminal:

```bash
cd frontend
npm install
npm run build
npx serve -s build
```

Visit <http://localhost:8000> for API and <http://localhost:3000> for UI (or wherever *serve* prints).

### Environment variables (backend)

```env
DJANGO_SECRET_KEY=change-this
BINANCE_API_KEY=...
BINANCE_API_SECRET=...
BINANCE_CERT_SN=...
```

## Production

Build the Docker image from `backend/` and serve the static files of `frontend/build` via Nginx or a CDN.

---

**DISCLAIMER:** This is just a *starting template*.  
*You* must add:  
- Proper authentication (JWT + CSRF, 2FA)  
- Binance webhook endpoint to update payment status  
- HTTPS, CORS, production DB, error handling, logging  
- KYC/KYB & legal pages (ToS, Privacy)  
- CI/CD, backups, monitoring  
- UI/UX polishing  
- Email verification (SendGrid, MailGun, etc.)  
