# System Architecture

## Overview
This document describes the overall system architecture for DivHelper AI.

## Components

### Frontend
- User interface and interactions
- Client-side processing

### Backend
- API server
- Business logic
- Data management

### AI Models
- Model implementations
- Inference engines
- Training pipelines

## Architecture Diagram
```
            ┌───────────────┐
            │   Frontend    │
            │  (React App)  │
            └───────┬───────┘
                    │ API
            ┌───────▼────────┐
            │  Backend API   │
            │   (FastAPI)    │
            └───────┬────────┘
                    │
        ┌───────────▼───────────┐
        │  Event Processing     │
        │  & Trigger Engine     │
        └───────────┬───────────┘
                    │
     ┌──────────────▼─────────────┐
     │      AI Services Layer     │
     │ Risk Model | Fraud Model   │
     └──────────────┬─────────────┘
                    │
      ┌─────────────▼─────────────┐
      │ Data Sources & APIs       │
      │ Weather | Traffic | News  │
      └───────────────────────────┘
```

## Data Flow
1. Frontend sends requests to Backend
2. Backend processes requests and communicates with AI Models
3. AI Models return predictions/results
4. Backend formats responses back to Frontend
