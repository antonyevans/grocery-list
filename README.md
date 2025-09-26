# Grocery List (Flask)

A tiny web app to create and manage a household grocery list. It lets you add items, check them off, and clear or delete entries—all from a simple, mobile‑friendly page. Built with Flask using server‑rendered templates.

## Features

- Add grocery items (e.g., “eggs”, “milk”, “bananas”).
- Mark items as completed / uncompleted.
- Remove individual items or clear the whole list.
- Simple, fast, and local—no accounts required.
- Uses Flask’s `instance/` pattern for instance‑specific runtime data.

## Quickstart

### 1) Clone and set up Python

```bash
git clone https://github.com/antonyevans/grocery-list.git
cd grocery-list

# (Recommended) create a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2) Run the app

```bash
# Option A: via Flask CLI
export FLASK_APP=app.py           # Windows (PowerShell): $env:FLASK_APP="app.py"
export FLASK_ENV=development      # optional, enables hot reload
flask run

# Option B: directly with Python
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Usage

- **Add an item** in the input box and submit.
- **Check/Uncheck** to toggle completion.
- **Delete** an item using its delete action.
- **Clear list** to remove all items.

> UI templates live in `templates/` and static assets in `static/`.

## Project Structure

```
grocery-list/
├─ app.py               # Flask application (routes and view logic)
├─ templates/           # Jinja2 templates (HTML)
├─ static/              # CSS/JS assets
├─ instance/            # Instance-specific data (ignored by VCS)
├─ requirements.txt     # Python dependencies
├─ .replit              # Replit run config
└─ replit.nix           # Replit environment spec
```

## Configuration & Data

- **Instance data:** The app follows Flask’s `instance/` folder convention for data/config that differs per environment. You can place a SQLite DB or JSON file there if you extend persistence later.
- **Environment variables (optional):**
  ```bash
  export SECRET_KEY="change-me"
  export DATABASE_URL="sqlite:///instance/app.db"   # if you add a DB
  ```

## Deploying

### Replit
This repo includes `.replit` and `replit.nix`, so you can open it in Replit and press **Run**.

### Other platforms
Any host that supports Python + WSGI will work. Example with Gunicorn:

```bash
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

Put it behind Nginx/Caddy for TLS and static file caching.

## Development Notes

- **Auto‑reload:** Use `FLASK_ENV=development` for live reloads.
- **Formatting/Linting (optional):** Consider `black` and `ruff` as dev dependencies.
- **Testing:** `pytest` works well for small Flask apps if you add tests later.

## Roadmap Ideas

- Item categories (Produce, Dairy, Pantry).
- “Recent items” suggestions.
- Multi‑user sharing with basic auth.
- JSON/SQLite persistence + CRUD API endpoints.
- PWA manifest for offline use and “Add to Home Screen.”

## License

MIT (or your preferred license). Add a `LICENSE` file if you want to formalize it.
