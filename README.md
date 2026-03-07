# 🐝 Hivebox

A production-ready FastAPI application that aggregates and serves real-time environmental sensor data from the [openSenseMap](https://opensensemap.org/) API — built and deployed following a full DevOps lifecycle including containerization, Kubernetes orchestration, CI/CD automation, and observability.

---

## 📐 Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     GitHub Actions                       │
│         (CI: lint → test → build → push image)          │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   Docker / Kubernetes                    │
│                                                         │
│   ┌──────────────┐      ┌──────────────────────────┐   │
│   │  FastAPI App │ ───▶ │   openSenseMap REST API   │   │
│   │  (uvicorn)   │      └──────────────────────────┘   │
│   └──────┬───────┘                                      │
│          │                                              │
│   ┌──────▼───────┐      ┌──────────────────────────┐   │
│   │  Prometheus  │ ───▶ │         Grafana           │   │
│   │  (metrics)   │      │      (dashboards)         │   │
│   └──────────────┘      └──────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Features

- **REST API** — FastAPI endpoints to query and aggregate sensor data from openSenseMap boxes
- **Containerized** — Fully Dockerized application with multi-service Docker Compose setup
- **Kubernetes-ready** — K8s manifests for pod deployment, service exposure, and resource management
- **CI/CD Pipeline** — GitHub Actions workflow automating lint, test, Docker image build, and deployment
- **Observability** — Prometheus metrics collection + Grafana dashboards for real-time monitoring
- **Automated Testing** — Unit tests with pytest, enforced as a CI quality gate on every commit

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI (Python) |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes (manifests in `/kubernetes`) |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus, Grafana |
| External API | openSenseMap REST API |
| Testing | pytest |

---

## 📁 Project Structure

```
Hivebox/
├── .github/
│   └── workflows/         # GitHub Actions CI/CD pipeline definitions
├── app/                   # FastAPI application source code
├── kubernetes/            # K8s deployment, service, and config manifests
├── tests/                 # pytest unit and integration tests
├── Dockerfile             # Multi-stage Docker image build
├── compose.yml            # Multi-container local development stack
├── prometheus.yml         # Prometheus scrape configuration
└── requirements.txt       # Python dependencies
```

---

## ⚡ Quick Start

### Run locally with Docker Compose

```bash
# Clone the repository
git clone https://github.com/Mustafaa8/Hivebox.git
cd Hivebox

# Start all services (API + Prometheus + Grafana)
docker compose up --build
```

The API will be available at `http://localhost:8000`
Prometheus at `http://localhost:9090`
Grafana at `http://localhost:3000`

### API Docs

FastAPI auto-generates interactive documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## ☸️ Kubernetes Deployment

```bash
# Apply all manifests
kubectl apply -f kubernetes/

# Verify pods are running
kubectl get pods

# Check service endpoints
kubectl get services
```

---

## 🔁 CI/CD Pipeline

Every push to `main` triggers the GitHub Actions workflow:

1. **Lint** — Code style checks
2. **Test** — pytest suite with coverage
3. **Build** — Docker image build
4. **Push** — Image published to container registry
5. **Deploy** — Updated manifests applied

---

## 📊 Monitoring

Prometheus scrapes application metrics defined in `prometheus.yml`. Grafana dashboards provide visibility into:

- Request rate and latency
- Error rates by endpoint
- Container CPU and memory utilization
- API upstream health (openSenseMap connectivity)

---

## 🧪 Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run test suite
pytest tests/ -v
```

---

## 📬 Contact

**Mostafa Abdallah**
[mostafa.abdallah99@outlook.com](mailto:mostafa.abdallah99@outlook.com) | [LinkedIn](https://linkedin.com/in/mostafa-abdallah-8319b4208) | [GitHub](https://github.com/Mustafaa8)
