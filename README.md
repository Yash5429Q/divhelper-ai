# 🚀 DivHelper AI  
**Parametric Insurance for Gig Delivery Workers**

---

## 📌 Overview  
DivHelper AI is a real-time, AI-powered parametric insurance system that protects gig delivery workers from income loss caused by external disruptions like heavy rain, extreme heat, platform outages, or curfews.

Instead of manual claims, payouts are triggered automatically using real-world data.

---

## ⚠️ Problem  
- Gig workers earn daily → no financial safety net  
- Disruptions (weather, outages) reduce income drastically  
- Traditional insurance fails → slow, manual, not designed for gig economy  

---

## 💡 Solution  
An **event-driven insurance engine** that:

- Monitors real-time data (weather, platform, GPS)
- Detects disruptions automatically  
- Triggers payouts instantly (no claims needed)  
- Uses fraud detection to prevent misuse  

---

## 👤 User Personas

DivHelper AI serves three distinct user types across the gig insurance ecosystem.

**🛵 Ravi Kumar — Gig Delivery Worker (Primary User)**  
A 26-year-old delivery rider in Hyderabad earning ₹600–900/day with no financial safety net. He loses ₹700+ on every rain day and has zero access to traditional insurance. DivHelper pays him automatically — no claims, no paperwork, straight to UPI.

**📋 Meena Sharma — City Ops Manager (B2B)**  
Manages 500–2000 riders for a food delivery platform. During disruptions, riders go offline and orders go undelivered. DivHelper is offered as a white-label welfare benefit — riders stay active, SLA breaches drop.

**📊 Arjun Mehta — Insurtech Product Head (B2B2C)**  
Exploring parametric insurance as a new product vertical. Needs auditable trigger logic, GPS fraud protection, and multi-signal data to price micro-premiums fairly. DivHelper's fraud engine and transparent payout logic make it a credible white-label partner.

> 📄 [View full interactive persona cards →](./personas.html)

---

## 🧠 Architecture  

![System Architecture](./Divhelper.png)

### 🔄 System Flow

External APIs → Ingestion → Kafka → Detection → Eligibility → AI Layer → Trigger → Payout → Storage


---

### 🔹 1. Data Ingestion Layer
- Collects data from APIs (weather, platform, GPS)
- Normalizes and validates data
- Ensures clean, structured input

---

### 🔹 2. Event Streaming (Kafka)
- Decouples services  
- Enables real-time processing  
- Topics: weather, traffic, platform, alerts  

---

### 🔹 3. Disruption Detection Engine
- Checks thresholds (e.g., rain > 50mm)  
- Combines multiple signals (rain + order drop)  
- Classifies disruption type  

---

### 🔹 4. Zone & Worker Eligibility
- Maps disruption → affected workers  
- Checks:
  - Active insurance  
  - Worker location  
  - Online status  

---

### 🔹 5. AI Layer

#### ✅ Risk Prediction Engine
- Predicts disruption before it happens  
- Outputs: LOW / MEDIUM / HIGH risk  

#### 🛡️ Fraud Detection Engine
Ensures only valid payouts.

---

## 🚨 GPS Spoofing Detection (Key Innovation)

We prevent fake location manipulation using:

- **Device Integrity Checks**  
  (rooted device, emulator, mock GPS)

- **GPS Behavior Analysis**  
  (impossible jumps, unrealistic speed)

- **Sensor Fusion**  
  (GPS + network + motion sensors mismatch)

- **Geo-Fencing Validation**  
  (worker must stay in valid delivery zone)

- **Pattern Analysis**  
  (repeated suspicious claims)

- **Cluster Detection**  
  (multiple users abusing same trigger)

---

## ⚙️ Trigger Engine

Core logic:

IF disruption detected
AND worker eligible
AND fraud check = CLEAR
→ Trigger payout


---

## 💰 Payout Engine
- Calculates payout based on:
  - Plan type  
  - Event severity  

- Fully automated:
- Trigger → Validate → Calculate → Transfer → Notify

---

## 🗄️ Data Storage
- Events database  
- Worker registry  
- Payout history  
- Fraud logs  

---

## ⚙️ Tech Stack

**Frontend**
- React.js + Tailwind CSS  

**Backend**
- FastAPI (Python)  
- REST APIs  

**Data & Processing**
- PostgreSQL / SQLite  
- Pandas, NumPy  

**Streaming (Future)**
- Kafka  

**Integrations**
- OpenWeather API  
- Razorpay  
- Google Maps API  

---
