# HILARIO | Unified XML Intelligence & Kinematic Abstraction Engine

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux-orange.svg)
![Domain](https://img.shields.io/badge/domain-Robotics%20%26%20Bionics-red.svg)
![Architecture](https://img.shields.io/badge/arch-OOP%20Strategy-gold.svg)

**HILARIO** is a high-performance orchestration engine designed for the abstraction and processing of complex XML schemas across heterogeneous domains. It operates as a critical middleware layer that bridges industrial financial systems with advanced robotic kinematic modeling.

##  Overview

HILARIO enables automated interpretation, transformation, and routing of structured XML data into domain-specific pipelines. Its architecture is built for scalability, modularity, and deployment in distributed Linux environments.

The system is designed to function **headlessly**, integrating seamlessly with real-time synchronization tools and external computational environments like MATLAB or ROS.

---

## Core Capabilities

### 🔹 Multi-Domain Processing
HILARIO supports dual-domain abstraction through a decoupled logic:
* **Industrial Finance:** Full CFDI 4.0 compliance.
* **Robotics Kinematics:** URDF parsing and physical modeling.

### 🔹 Autonomous Synchronization
Native integration with **Syncthing** allows automatic ingestion and processing of XML files in distributed systems without manual intervention.

### 🔹 Event-Driven Architecture
Implements an **Observer-based pipeline** (via Watchdog) for near real-time processing and proactive system monitoring.

### 🔹 Intelligent Data Routing
Automatic namespace normalization and root-tag detection enable dynamic selection of processing strategies based on the file's "DNA".

---

## Robotics Domain: Kinematic Descriptor Parsing

HILARIO processes **URDF (Unified Robot Description Format)** files to extract high-fidelity mechanical and structural parameters required for simulation and control systems.

### Features:
* **Kinematic Topology Mapping:** Identification of links, joints, and parent-child hierarchy reconstruction.
* **Physical Properties Extraction:** * Inertia tensors ($I_{xx}, I_{yy}, I_{zz}$)
    * Mass distribution and Center of Mass (CoM).
* **Joint Constraints Analysis:** Position limits (lower/upper), effort, and velocity constraints.
* **Geometry Path Resolution:** Detection of mesh files (`.stl`, `.dae`) and separation of collision vs. visual geometries.
* **Mathematical Integration:** Parameter extraction for **Denavit-Hartenberg (D-H)** modeling.

---

## Finance Domain: Industrial Accounting Automation

Optimized for high-density CFDI processing within the Mexican fiscal framework.

### Features:
* **Atomic Data Extraction:** Issuer/Receiver metadata, RFC, fiscal regimes, and UUID.
* **Tax Engine:** Parsing of transferred and retained taxes with base/rate validation.
* **Schema Validation:** XSD-based integrity verification prior to processing.
* **High-Throughput:** Designed for batch and real-time invoice handling.

---

## Technical Stack

* **Core Language:** Python 3.10+
* **Design Pattern:** Strategy Pattern for domain decoupling.
* **Architecture:** Object-Oriented Programming (OOP).
* **Environment:** Linux / Unix optimized.
* **Containerization:** Docker & Docker Compose.
* **Integration:** Syncthing, MATLAB, C++ interoperability.

---

## Project Structure

```text
Hilario/
├── hilario/            # Source code: Modular logic & Strategy handlers
├── scripts/            # Entry points and execution utilities
├── config_sync/        # Distribution & replication settings
├── docker/             # Dockerfiles for isolated environments
├── docker-compose.yml  # Microservices orchestration
├── data/               # Persistent volumes (Inbound/Outbound)
├── logs/               # System traceability and monitoring
└── tests/              # Unit and integration test suite

# Launch the orchestration environment
docker-compose up -d

# Monitor runtime logs
tail -f logs/hilario.log

Design Philosophy
HILARIO is not just an XML parser. It is a structured data intelligence engine designed to:

Transform raw structured data into actionable mathematical models.

Serve as a bridge between administrative systems and high-level engineering computation.

Enable scalable automation in both industrial and robotic domains.

Author
Uriel Alejandro Ramírez Gutiérrez Bionics & Robotics Systems Architect GitHub | Substack
