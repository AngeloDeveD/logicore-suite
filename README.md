# LogiCore Suite: Enterprise Logistics Ecosystem

LogiCore Suite is a distributed, high-performance platform designed for global supply chain management. It leverages a microservices architecture to handle complex business logic, real-time telemetry tracking, and asynchronous event processing.

This repository is structured as a **Monorepo**, simulating a real-world enterprise environment where multiple specialized services share common internal libraries and infrastructure standards.

## 🏗 System Architecture

The ecosystem consists of the following components:

*   **Core Platform (`/apps/core_platform`):** A **Django**-based service acting as the "Source of Truth." It manages master data (carriers, shipments, contracts) using **PostgreSQL**.
*   **Tracking Provider (`/apps/tracking_provider`):** A high-load **FastAPI** service that ingests real-time GPS and IoT telemetry data. Optimized with **asyncio** and utilizing **MySQL** for high-write telemetry logs.
*   **Notification Worker (`/apps/notification_service`):** A background processing engine built with **Celery** and **RabbitMQ** for handling alerts, automated emails, and webhooks.
*   **Shared Library (`/libs/logicore_common`):** A proprietary internal package used across all services to ensure consistency in event schemas, logging, and security protocols.
*   **Message Bus:** **Apache Kafka** serves as the backbone for Event-Driven Architecture (EDA), enabling seamless synchronization between services.

## 🛠 Technology Stack

*   **Languages:** Python 3.10+
*   **Frameworks:** Django (DRF), FastAPI
*   **Databases:** PostgreSQL (Transactional), MySQL (Time-series/Telemetry)
*   **Messaging:** Apache Kafka (Inter-service), RabbitMQ (Task Queuing)
*   **Async Processing:** Celery, asyncio
*   **Infrastructure:** Docker, Docker Compose, GitLab CI (Templates)
*   **Testing:** Pytest (Unit & Integration)

## 📁 Project Structure

```text
logicore-suite/
├── apps/
│   ├── core_platform/       # Django: Business logic & Master data
│   ├── tracking_provider/   # FastAPI: High-load telemetry ingestion
│   └── notification_worker/ # Celery: Background tasks & Alerting
├── libs/
│   └── logicore_common/     # Shared domain models, Kafka utils, & Middleware
├── deploy/
│   ├── docker/              # Service-specific Dockerfiles
│   └── k8s/                 # Kubernetes manifests (Drafts)
├── scripts/                 # Development and migration utilities
└── docker-compose.yml       # Full-stack orchestration