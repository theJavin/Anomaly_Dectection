# Stage 2 Interview

## Task:
Quick Simulation:
Generate 50 human and 50 bot sessions (100 total). Each session should include a short sequence of pointer events (x, y, timestamp) and one metadata field (for example, time of day). It is important that the human sessions are not synthetic data. 

Feature & Model:
Engineer 3–5 simple features (for example: velocity statistics, inter‑event timing, direction entropy). Train one classifier (for example: Random Forest) and report ROC‑AUC and precision/recall.

Next‑Step Write‑Up:
In a single page, outline:
- How you would scale this to more realistic data (device sensors, pressure)
- One adversarial scenario and a high‑level defence sketch
- Approaches for low‑latency deployment





## Potential Improvements


### Data collection
- higher end botting
- more realistic captcha
- 

### Feature Extraction
- Add linearity feature
- 

### Machine Learning
- not using python, python = slow. prospects: julia, c++
- Automated hyperparameter tuning (optuna, raytune)
- Performance testing (lgbm, rf may be faster for same performance)

