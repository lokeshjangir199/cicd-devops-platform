# Automated CI/CD & DevOps Deployment Platform

A production-style CI/CD platform that automatically tests, containerizes, publishes, and deploys a FastAPI application to AWS EC2. The pipeline also uses an LLM-based analyzer to diagnose CI test failures and suggest fixes.

## Architecture

```text
                    Developer
                        │
                     git push
                        │
                        ▼
                 ┌──────────────┐
                 │   GitHub     │
                 │ Repository   │
                 └──────┬───────┘
                        │
                        ▼
              ┌───────────────────┐
              │  GitHub Actions   │
              ├───────────────────┤
              │ • Run Tests       │
              │ • AI Failure      │
              │   Analysis        │
              │ • Build Docker    │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │       GHCR        │
              │ Docker Registry   │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │     AWS EC2       │
              │                   │
              │ Docker Container  │
              │       ↓           │
              │ FastAPI App       │
              └───────────────────┘
# Automated CI/CD & DevOps Deployment Platform

A production-style CI/CD platform that automatically tests, containerizes, publishes, and deploys a FastAPI application to AWS EC2. The pipeline also uses LLM-based analysis to diagnose CI test failures and suggest fixes.

---

## Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----> Automated Tests
    |
    +----> AI Failure Analysis
    |
    +----> Docker Build
    |
    v
GitHub Container Registry
    |
    v
AWS EC2
    |
    v
Docker Container
    |
    v
FastAPI Application
```

---

## Key Features

- Automated CI/CD pipeline using GitHub Actions
- Automated Python testing with Pytest
- Dockerized FastAPI application
- Docker image publishing through GitHub Container Registry
- Automated deployment to AWS EC2
- Automatic container replacement on new deployments
- Secure deployment credentials using GitHub Actions Secrets
- LLM-assisted CI failure analysis using OpenRouter
- Automatic root-cause and remediation suggestions for failed tests
- Health endpoint for deployment verification

---

## Tech Stack

| Category           | Technology                      |
|--------------------|---------------------------------|
| Backend            | FastAPI, Python                 |
| Testing            | Pytest                          |
| Containerization   | Docker                          |
| CI/CD              | GitHub Actions                  |
| Container Registry | GitHub Container Registry       |
| Cloud              | AWS EC2                         |
| AI                 | OpenRouter                      |
| Operating System   | Ubuntu Linux                    |
| Version Control    | Git, GitHub                     |

---

## CI/CD Workflow

1. Developer pushes code to the `main` branch.
2. GitHub Actions checks out the repository.
3. Python dependencies are installed.
4. Automated tests are executed.
5. Failed tests are analyzed using an LLM.
6. Docker image is built.
7. Docker image is pushed to GHCR.
8. GitHub Actions connects to the EC2 instance.
9. EC2 pulls the latest Docker image.
10. The previous container is stopped and removed.
11. A new container is started automatically.

---

## AI Failure Analysis

When a test fails, the pipeline captures the Pytest output and sends the failure log to an LLM.

The analyzer provides:
- Failure summary
- Root cause
- Suggested fix
- Likely affected files or components

> **Note:** AI analysis does not hide CI failures. The original test exit code is preserved, ensuring that a failed test still causes the pipeline to fail.

```text
Test Failure
     |
     v
Capture Pytest Logs
     |
     v
OpenRouter LLM
     |
     +--> Failure Summary
     +--> Root Cause
     +--> Suggested Fix
     |
     v
CI remains FAILED
```

---

## Application Endpoints

| Method | Endpoint   |
|--------|------------|
| GET    | `/`        |
| GET    | `/health`  |
| GET    | `/version` |

**Example health response:**

```json
{
  "status": "healthy"
}
```

---

## Local Development

**Clone the repository:**

```bash
git clone https://github.com/lokeshjangir199/cicd-devops-platform.git
cd cicd-devops-platform
```

**Create a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run tests:**

```bash
python -m pytest
```

**Run the application:**

```bash
uvicorn app.main:app --reload
```

---

## Docker

**Build the image:**

```bash
docker build -t cicd-devops-platform .
```

**Run the container:**

```bash
docker run -p 8000:8000 cicd-devops-platform
```

**Test the application:**

```bash
curl http://localhost:8000/health
```

---

## Automated Deployment

Every push to `main` automatically triggers:

```text
Git Push
   |
   v
GitHub Actions
   |
   +--> Tests
   |
   +--> AI Failure Analysis
   |
   +--> Docker Build
   |
   v
GitHub Container Registry
   |
   v
AWS EC2
   |
   v
Docker Container
   |
   v
Live FastAPI Application
```

---

## Security

- Deployment SSH key is separate from the EC2 login key.
- Sensitive credentials are stored using GitHub Actions Secrets.
- API keys are never committed to the repository.
- Docker images are stored in GitHub Container Registry.

---

## Project Highlights

- End-to-end automated CI/CD deployment
- Cloud-based containerized application delivery
- Automated testing and Docker image publishing
- AWS EC2 production deployment
- LLM-powered CI failure diagnosis
- Linux-based deployment environment
- Automated container lifecycle management
