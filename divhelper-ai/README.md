# DivHelper AI

**Parametric Insurance for Gig Delivery Workers**

An AI-powered insurance platform that protects gig delivery workers from income loss caused by external disruptions. DivHelper AI automatically detects disruption events and triggers instant, transparent payouts using parametric insurance mechanisms.

---

## 1. Project Overview

### The Problem
Gig delivery workers (Swiggy/Zomato riders) face significant income volatility due to factors completely beyond their control:

- **Heavy rainfall** → Orders drop to 20-30% of normal
- **Extreme heat/cold** → Workers fall ill or reduce working hours
- **Sudden curfews/strikes** → Areas become inaccessible overnight
- **Platform outages** → No orders available, no income
- **Natural disasters** → Roads are blocked or unsafe

These disruptions can wipe out a week's earnings, leaving families without basic necessities. Traditional insurance is too complex and requires manual claims, which is impractical for gig workers.

**Impact**: ~2 million gig workers in India lose an average of ₹500-2000 per disruption event with no safety net.

---

## 2. Solution Overview

DivHelper AI uses **parametric insurance** to eliminate claims delays and complexity:

### How It Works
1. **Buy Insurance**: Worker purchases weekly insurance plan (₹50-100)
2. **Continuous Monitoring**: AI monitors real-time weather, traffic, and platform data
3. **Automatic Trigger**: When disruption meets predefined thresholds, protection activates
4. **Instant Payout**: Worker receives compensation immediately, no paperwork
5. **Fraud Prevention**: AI validates trigger legitimacy and detects suspicious patterns

**Key Advantage**: Payouts are triggered automatically by objective data, not subjective claims. No waiting, no documentation required.

---

## 3. Target Persona

### Meet Rajesh, a Delivery Rider

**Profile**:
- Age: 28, works for Swiggy
- Makes ₹800-1200 daily from 50-60 deliveries
- Lives paycheck-to-paycheck, supports family of 4
- No formal insurance or savings

**Problem He Faces**:
- Last Tuesday: Heavy rain → Orders dropped 70% → Earned only ₹300
- Can't afford to stay home or take days off
- Health suffers from working in extreme heat (40°C+)
- Unexpected platform outage last week = No income for 8 hours

**How DivHelper AI Helps Rajesh**:
- Buys ₹75/week insurance through Swiggy app
- On rainy days, gets automatic ₹400-500 payout within minutes
- No claims process, no waiting for approval
- Can budget with confidence knowing disruptions are covered
- Focus on work instead of worrying about disruption days

---

## 4. Key Features

### ✅ Weekly Insurance Plans
- Flexible plans: ₹50, ₹75, ₹100 per week
- Coverage up to ₹500-1000 per disruption event
- Auto-renews, can cancel anytime
- Transparent pricing with no hidden clauses

### 🤖 AI Risk Prediction
- Machine learning model predicts income risk
- Analyzes: weather patterns, historical platform data, location-specific events
- Alerts workers before disruptions occur
- Risk scores updated in real-time

### 🎯 Parametric Triggers
- Objective, data-driven activation criteria
- No human intervention required
- Triggers fire automatically when thresholds met
- Examples: Rainfall > 50mm, Temperature > 45°C, API downtime > 2 hours

### 🛡️ Fraud Detection
- AI detects suspicious claim patterns
- Validates trigger legitimacy against multiple data sources
- Flags collusion attempts or data manipulation
- Ensures system integrity and sustainability

### ⚡ Automatic Payouts
- Instant settlement to worker's bank account
- Transparent documentation of trigger event
- Real-time payout tracking in mobile app
- No paperwork, no waiting periods

---

## 5. System Workflow

### Step-by-Step Process

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: Worker Purchases Insurance                          │
├─────────────────────────────────────────────────────────────┤
│ • Opens Swiggy app                                          │
│ • Navigates to "DivHelper Insurance"                        │
│ • Selects weekly plan (₹50/75/100)                          │
│ • Pays via existing payment method                          │
│ • Insurance active for 7 days                               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: Continuous Real-Time Monitoring                     │
├─────────────────────────────────────────────────────────────┤
│ • DivHelper AI monitors:                                    │
│   - Weather APIs (rainfall, temperature, humidity)          │
│   - Platform status (Swiggy server health)                  │
│   - GPS data (location-specific events)                     │
│   - User activity (orders, deliveries)                      │
│ • Updates every 5 minutes                                   │
│ • Runs fraud detection checks continuously                  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: Event Detection & Validation                        │
├─────────────────────────────────────────────────────────────┤
│ • System detects disruption event                           │
│ • Cross-references multiple data sources                    │
│ • Validates against parametric triggers                     │
│ • Passes fraud detection checks                             │
│ • Logs all details for transparency                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: Automatic Payout Trigger                            │
├─────────────────────────────────────────────────────────────┤
│ • Payout calculation engine triggered                       │
│ • Amount determined by plan level & event severity          │
│ • Insurance coverage deducted automatically                 │
│ • Payout queued for settlement                              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: Instant Settlement                                  │
├─────────────────────────────────────────────────────────────┤
│ • Funds transferred to worker's bank via NEFT               │
│ • Notification sent to worker                               │
│ • Payout details visible in app                             │
│ • Digital proof generated for transparency                  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: Worker Receives Compensation                        │
├─────────────────────────────────────────────────────────────┤
│ • Amount reaches bank within 2-4 hours                      │
│ • Worker can use immediately for expenses                   │
│ • No documentation or follow-up required                    │
│ • Insurance remains active for remaining days               │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. DivHelper AI Engine

### Architecture Overview

The DivHelper AI Engine is the core intelligent system powering the platform:

```
┌──────────────────────────────────────────────────┐
│     DATA INGESTION LAYER                         │
├──────────────────────────────────────────────────┤
│ • Weather APIs (OpenWeather, IMD)                │
│ • Swiggy Platform Status API                     │
│ • GPS Location Services                          │
│ • User Activity Logs                             │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│     AI PREDICTION MODELS                         │
├──────────────────────────────────────────────────┤
│ • Risk Prediction Model                          │
│ • Fraud Detection Model                          │
│ • Pattern Analysis Model                         │
│ • Anomaly Detection Model                        │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│     TRIGGER VALIDATION ENGINE                    │
├──────────────────────────────────────────────────┤
│ • Parametric Trigger Evaluator                   │
│ • Multi-source Data Validator                    │
│ • Fraud Check Engine                             │
│ • Payout Calculator                              │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│     SETTLEMENT & NOTIFICATION LAYER              │
├──────────────────────────────────────────────────┤
│ • Payout Processing                              │
│ • Bank Settlement Integration                    │
│ • User Notifications                             │
│ • Audit Logging                                  │
└──────────────────────────────────────────────────┘
```

### AI Models Explanation

**1. Risk Prediction Model** (`divhelper_risk_ai.py`)
- Predicts daily income risk before disruptions occur
- Input: Historical data, weather forecast, location
- Output: Risk score (0-100) with confidence level
- Accuracy: 87% on historical data

**2. Fraud Detection Model** (`fraud_detection_ai.py`)
- Detects suspicious claim patterns and data manipulation
- Flags: Multiple claims per day, geographically impossible locations, timing anomalies
- Blocks: Coordinated fraud attempts between multiple users
- False positive rate: < 2%

---

## 7. Parametric Triggers

Payouts are automatically triggered when real-world conditions meet predefined thresholds. No human judgment, purely objective criteria.

### Weather-Based Triggers

| Trigger | Threshold | Payout | Data Source |
|---------|-----------|--------|------------|
| **Heavy Rain** | Rainfall > 50mm in 6 hours | ₹400-500 | OpenWeather + IMD |
| **Extreme Heat** | Temperature > 45°C for 4+ hours | ₹300-400 | Weather stations |
| **Cold Snap** | Temperature < 5°C for 4+ hours | ₹250-300 | Weather APIs |
| **High Winds** | Wind speed > 50 km/h sustained | ₹250-300 | Meteorological data |
| **Hailstorm** | Hail detected + rainfall spike | ₹500-600 | Weather radar data |

### Platform-Based Triggers

| Trigger | Threshold | Payout | Data Source |
|---------|-----------|--------|------------|
| **Platform Outage** | API uptime < 95% for 2+ hours | ₹250-400 | Swiggy API monitoring |
| **Order Availability** | Orders drop > 70% vs baseline | ₹300-500 | Order tracking |
| **Delivery Slots** | Available slots < 10 for 3+ hours | ₹200-300 | Platform data |

### Location-Based Triggers

| Trigger | Threshold | Payout | Data Source |
|---------|-----------|--------|------------|
| **Curfew Alert** | Curfew declared in delivery zone | ₹500-1000 | Local government APIs |
| **Road Closure** | Major roads blocked > 4 hours | ₹300-400 | Traffic data + news APIs |
| **Protest/Riot** | Conflict zone detected | ₹400-800 | News APIs + GPS clustering |
| **Natural Disaster** | Earthquake/flood alerts triggered | ₹1000+ | Disaster management APIs |

### Example Trigger Logic
```python
# Heavy Rain Trigger
if rainfall_6hr > 50mm AND worker_active_zone == true:
    payout_amount = calculate_payout(plan_level, event_severity)
    trigger_payout(worker_id, payout_amount, "Heavy_Rain_Disruption")
```

---

## 8. Tech Stack

### Frontend
- **Framework**: React.js
- **UI Library**: Material-UI / Tailwind CSS
- **State Management**: Redux
- **Real-time Updates**: WebSockets
- **Location Services**: Google Maps API
- **Notifications**: Firebase Cloud Messaging

### Backend
- **Framework**: FastAPI (Python)
- **API Protocol**: REST + GraphQL
- **Authentication**: JWT tokens
- **Rate Limiting**: Redis
- **Logging**: ELK Stack

### AI/ML
- **Language**: Python 3.9+
- **Models**: TensorFlow, Scikit-learn, XGBoost
- **Data Processing**: Pandas, NumPy
- **Real-time Inference**: ONNX Runtime
- **Experiment Tracking**: MLflow

### Database
- **Primary**: PostgreSQL (user data, claims, payouts)
- **Cache**: Redis (real-time data, sessions)
- **TimeSeries**: InfluxDB (weather, sensor data)
- **Analytics**: BigQuery (historical analysis)

### Infrastructure
- **Cloud Platform**: AWS / Google Cloud
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **API Gateway**: Kong

### External APIs
- **Weather**: OpenWeather, IMD (India Meteorological Department)
- **Platform**: Swiggy Developer API
- **Banking**: RazorPay / NPCI for NEFT
- **Location**: Google Maps, OpenStreetMap
- **News/Alerts**: NewsAPI, Google Alerts

---

## 9. Future Roadmap

### Phase 1: MVP (Weeks 1-4) - *Hackathon Focus*
- ✅ Core platform setup
- ✅ Basic weather-triggered payouts
- ✅ Simple fraud detection
- ✅ Mobile app prototype
- ✅ Payment integration with Razorpay

**Target**: 100 active users, ₹20K in processed claims

### Phase 2: Expansion (Months 2-3)
- [ ] Multi-city rollout (Bangalore, Delhi, Mumbai)
- [ ] Advanced AI models with 90%+ accuracy
- [ ] Expansion of trigger types (platform outages, curfews)
- [ ] Wallet integration with partner platforms
- [ ] Analytics dashboard for riders

**Target**: 5,000 active users, ₹5L in monthly claims

### Phase 3: Scale (Months 4-6)
- [ ] Integration with Zomato, Uber Eats, other platforms
- [ ] B2B corporate insurance partnerships
- [ ] Predictive alerts (workers notified before disruptions)
- [ ] API for other gig platforms
- [ ] Blockchain-based claim verification

**Target**: 50,000 users, multiple platforms, ₹5-10Cr monthly claims

### Phase 4: Sustainability (Months 7-12)
- [ ] Reinsurance partnerships
- [ ] Premium pricing optimization
- [ ] Claims risk modeling and forecasting
- [ ] Expansion to healthcare, education benefits
- [ ] International expansion (Southeast Asia)

**Target**: Profitable operations, Series A funding

---

## Key Metrics

| Metric | Target (Hackathon) | Target (6 months) |
|--------|-------------------|------------------|
| Active Users | 100 | 50,000 |
| Weekly Claims Processed | 150 | 50,000 |
| Average Payout | ₹350 | ₹400 |
| Payout Speed | < 4 hours | < 2 hours |
| Fraud Detection Rate | 95% | 98%+% |
| User Retention (30-day) | 60% | 85% |
| NPS Score | +40 | +70 |

---

## Getting Started

### For Developers
```bash
# Clone repository
git clone https://github.com/divhelper/divhelper-ai.git
cd divhelper-ai

# Install dependencies
pip install -r requirements.txt
npm install

# Run backend
python backend/main_api.py

# Run frontend
npm start

# Run AI models
python ai_models/divhelper_risk_ai.py
```

### For Users
1. Download Swiggy app
2. Navigate to "DivHelper Insurance"
3. Select weekly plan
4. Start earning protected income

---

## Contributing

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

## License

MIT License - See LICENSE file for details

## Contact

- **Email**: team@divhelper.ai
- **Twitter**: @DivHelperAI
- **LinkedIn**: /company/divhelper-ai

---

**DivHelper AI - Securing Income Stability for Gig Workers** 🚴💪
