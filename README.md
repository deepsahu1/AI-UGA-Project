# Water Quality Monitoring: AI@UGA Research Project

## Overview
This repository contains the code, documentation, and resources for the AI@UGA Water Quality Monitoring project. Our goal is to build an end-to-end system that collects sensor data (pH, temperature, turbidity, dissolved oxygen), preprocesses it, trains and evaluates machine learning models for real-time prediction of water quality, and displays results via a live Flask + Dash dashboard.

## Table of Contents
- [Roles and Responsibilities](#roles-and-responsibilities)  
- [Project Timeline](#project-timeline)  
- [Getting Started](#getting-started)  

## Roles and Responsibilities
We’re organized into five cross-functional subteams:

- **ML Data Engineer**  
  Build and maintain the sensor data pipeline: data collection, cleaning (outlier removal, missing-value handling), normalization/scaling, and labeling assistance; deliver a mini-ML demonstration showing performance improvements on cleaned vs. raw data.

- **ML Model Developer**  
  Select, train, optimize, and export lightweight machine learning models (e.g., Random Forest, GBM, simple neural nets) for real-time inference on the Jetson Nano; experiment locally then deploy and benchmark on-device performance.

- **ML Evaluation & Testing Lead**  
  Define and implement evaluation scripts (MAE, RMSE, R², confusion matrices); run controlled lab and field validations; perform error analysis and refine labels or features based on failure modes.

- **ML Systems Integrator & Dashboard Engineer**  
  Integrate sensor pipeline, model inference, and communication modules; develop a Flask + Dash live dashboard; implement CI tests; ensure reliable streaming and OTA update capability.

- **Electrical Engineers**  
  Finalize sensor list and wiring (pH, temperature, turbidity, ADC, Raspberry Pi 4); flash OS and enable SSH/Wi-Fi; bench-test power/network stability; design enclosure sketches and prepare for field deployment.

## Project Timeline
High-level phases and deliverables by date:

- **Apr 21 – May 10**  
  - *ML Data Engineer*: Draft preprocessing pipeline (cleaning scripts, timestamp alignment, missing-value handling).  
  - *Systems Integrator & Dashboard*: Scaffold minimal Flask + Dash UI (“Awaiting data”); create dummy-data POSTs for end-to-end tests.  
  - *Electrical Engineers*: Finalize sensor list; flash Pi OS; enable SSH/Wi-Fi; install Python venv with numpy, pandas, scikit-learn, requests, paho-mqtt.

- **May 11 – May 24**  
  - *ML Data Engineer*: Download and clean full public datasets; normalize/scale features; produce ready-to-train CSVs.  
  - *ML Model Developer*: Hyperparameter-tune baseline models; compare regression vs. ARIMA/LSTM approaches.  
  - *ML Evaluation Lead*: Execute evaluation runs; document failure modes.  
  - *Systems Integrator*: Dry-run dashboard with CSVs; add basic CI tests.  
  - *Electrical Engineers*: Wire sensors into Pi GPIO; conduct 48 h stress tests; sketch enclosure concepts.

- **May 25 – Jun 7**  
  - *ML Data Engineer*: Ingest faculty-mentor sensor logs; log anomalies.  
  - *ML Model Developer*: Retrain on real data; export models to TensorFlow Lite/ONNX.  
  - *ML Evaluation Lead*: Benchmark real vs. public-data baselines; refine features.  
  - *Systems Integrator*: Full dry-run: preprocess → calibration → inference → dashboard POST.  
  - *Electrical Engineers*: Seal and label housing; bench commission with logging and on-device inference.

- **Jun 8 and beyond**  
  Continue iterative bench testing, field-deployment planning, model optimization, final validation, and knowledge transfer.

## Getting Started

### Prerequisites
- Python 3.8+  
- pip  
- virtualenv or venv module  

### Installation
1. **Clone the repo**  
   ```bash
   git clone git@github.com:deepsahu1/AI-UGA-Project.git
   cd AI-UGA-Project
   
2. **Create and activate virtual environment**
   ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install dependencies**
    pip install -r requirements.txt


