# 🏥 Edge-Cloud Healthcare Microservices System

## 📌 Overview
This project is a distributed healthcare system built using a **microservices architecture** with an **edge-cloud design**.

It simulates a real-world hospital workflow where:
- Edge services handle fast local operations
- Cloud services manage data storage and processing

---

## 🧩 Services

### ⚡ Edge Layer
- **Appointment Service** → Handles patient appointments
- **Clinic Gateway** → Routes requests to cloud services

### ☁️ Cloud Layer
- **Patient Record Service** → Stores patient data
- **Billing Service** → Generates bills
- **Prescription Service** → Stores prescriptions

---

## 🛠️ Tech Stack
- Python (Flask)
- Docker
- Docker Compose

---

## 📁 Project Structure

```

CEC/
│
├── services/
│   ├── appointment/
│   ├── gateway/
│   ├── patient/
│   ├── billing/
│   ├── prescription/
│
├── docker-compose.yml
└── README.md

````

---

# 🚀 How to Run the Project

## ✅ Step 1 — Clone Repository

```bash
git clone https://github.com/cherrychhallani/edge-cloud-healthcare-system.git
cd edge-cloud-healthcare-system
````

---

## ✅ Step 2 — Install Docker

Make sure Docker is installed:

```bash
docker --version
```

If not installed:
👉 [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

---

## ✅ Step 3 — Run the System

```bash
docker compose up --build
```

👉 This will:

* Build all services
* Start all containers
* Create network automatically

---

## ✅ Step 4 — Test the System

Open a new terminal and run:

```bash
curl -X POST http://127.0.0.1:5001/appointment \
-H "Content-Type: application/json" \
-d '{"name":"TestUser","age":25,"problem":"Fever"}'
```

---

## 🎯 Expected Output

You should see:

* Appointment created ✅
* Patient record created ✅
* Bill generated ✅
* Prescription created ✅

---

## 🔁 Workflow

```
Client
   ↓
Appointment Service (Edge)
   ↓
Gateway Service (Edge)
   ↓
Patient + Billing + Prescription (Cloud)
   ↓
Response back to Client
```

---

## 🧠 Key Features

* Microservices architecture
* Edge-cloud separation
* REST API communication
* Docker containerization
* Docker Compose orchestration

---

## 🛑 Stop the System

```bash
docker compose down
```

---

## 📌 Notes

* All services run on different ports:

  * 5001 → Appointment
  * 5002 → Gateway
  * 5003 → Patient
  * 5004 → Billing
  * 5005 → Prescription

---

## 👨‍💻 Author

Cherry Sandeep Chhallani

---

## ⭐ Future Improvements

* Kubernetes deployment
* Database integration (MongoDB/PostgreSQL)
* Authentication system
* UI dashboard
