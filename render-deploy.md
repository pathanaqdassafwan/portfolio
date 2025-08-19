# Deploy to Render — Flask portfolio

This guide walks through deploying the Flask portfolio (`app.py`) to Render as a Web Service.

## Prerequisites
- GitHub repository with this project pushed.
- `requirements.txt` contains production deps (includes `gunicorn`).
- `Procfile` present (recommended) with: `web: gunicorn app:app`.
- A Render account (https://render.com).

## Quick summary (one-liner)
Connect the repo on Render, pick the `main` branch, set the start command to `gunicorn app:app --bind 0.0.0.0:$PORT`, and create the Web Service.

---

## Detailed steps

1. Commit & push changes

```powershell
git add requirements.txt Procfile
git commit -m "Add gunicorn and Procfile for Render"
git push origin main
```

2. Create a new Web Service on Render
- Login to Render and click **New** → **Web Service**.
- Connect your GitHub account and select the repository and `main` branch.

3. Service settings
- Environment: `Python 3` (Render will detect).
- Build Command: leave blank (Render runs `pip install -r requirements.txt`) or set explicitly:
  - `pip install -r requirements.txt`
- Start Command: either leave blank (Render honors `Procfile`) or use:
  - `gunicorn app:app --bind 0.0.0.0:$PORT`
- Instance Type: free / hobby depending on needs.
- Click **Create Web Service**.

4. Watch the deploy logs
- The initial deploy will show build logs (installing requirements) and then a start log from `gunicorn`.
- If it fails, check error messages in the Render dashboard logs.

## Environment variables and secrets
- Add any secrets in Render's Environment section (e.g., API keys) — do not commit credentials.

## Local testing tips (Windows)
- Use dev server for local development:
```powershell
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000
```
- For a production-like WSGI server on Windows, use `waitress`:
```powershell
pip install waitress
waitress-serve --port=5000 app:app
```
If you want `waitress` in `requirements.txt`, add `waitress>=2.1.0` (optional).

## Common issues and fixes
- `ModuleNotFoundError: No module named 'fcntl'` when running `gunicorn` locally on Windows:
  - This is expected on Windows because `gunicorn` depends on POSIX-only modules. Ignore for local Windows testing; Render runs Linux.
- Static files not found:
  - Ensure `static/` and `templates/` are committed and paths used in `app.py` are relative.
- Port issues on Render:
  - Use `$PORT` as Render supplies the port. Use the `--bind 0.0.0.0:$PORT` pattern.

## Optional: add a health check (recommended)
Add a lightweight health route in `app.py`:
```python
@app.route('/_health')
def health():
    return 'OK', 200
```
Render can use this for monitoring.

## Rollback & redeploy
- To trigger redeploy: push a new commit or use Render's **Manual Deploy** button in the service dashboard.

## Post-deploy: custom domain & TLS
- Add your custom domain in Render's dashboard → Custom Domains.
- Follow DNS instructions to add CNAME/A records. Render provides free TLS via Let's Encrypt.

---

If you'd like, I can also:
- Add `waitress` to `requirements.txt` for easier local WSGI testing.
- Add a `/ _health` route to `app.py`.
- Create a small `render-checks.yml` GitHub Action to run `pip install -r requirements.txt` on push.

"Deploy to Render" checklist status:
- `requirements.txt` includes `gunicorn` — yes
- `Procfile` exists — yes
- Repo pushed to GitHub — (you)
- Render service created — (you)

