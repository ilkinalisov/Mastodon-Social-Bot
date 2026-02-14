# DEVELOPMENT

## Local Setup

1. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your secrets.

```env
OPENAI_API_KEY=your_openai_key
MASTODON_ACCESS_TOKEN=your_mastodon_access_token
MASTODON_BASE_URL=https://your-instance.example
```

4. Start the web app.

```bash
uvicorn main:app --reload --port 8000
```

5. Open the UI at [http://localhost:8000](http://localhost:8000), use `Dry Run` if you want generation without publishing, then click `Generate & Post`.

## Local Testing

To test the API logic without the UI, you can use the terminal:

```bash
# Trigger a Dry Run
curl -X POST "http://localhost:8000/run-bot?dry_run=true"
```

To run the existing test suite:

```bash
PYTHONPATH=src pytest tests/
```

## Port Management

If you try to start the server and get an `Address already in use` error, follow these steps:

Mac/Linux:

```bash
# Find the PID (Process ID) running on port 8000
lsof -i :8000

# Kill the process (replace PID with the number found above)
kill -9 <PID>
```

Windows (PowerShell):

```powershell
# Find the PID
netstat -ano | findstr :8000

# Kill the process
stop-process -Id <PID>
```

## Production Deployment

When deploying to Vercel or Render, do NOT upload your `.env` file. Instead:

1. Go to **Settings > Environment Variables**.
2. Add `OPENAI_API_KEY`, `MASTODON_ACCESS_TOKEN`, and `MASTODON_BASE_URL`.
3. Set `ENV=production` to disable local debug logs.

Vercel notes:

1. This repo includes `vercel.json` configured to route all requests to `main.py`.
2. Set the framework to Python (or leave auto-detect) and deploy.

Render notes:

1. This repo includes a `Dockerfile` for container deployment.
2. Expose port `8000` and use the container start command from the Docker image (`uvicorn main:app --host 0.0.0.0 --port 8000`).
