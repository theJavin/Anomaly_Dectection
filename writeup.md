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


## Results

    ROC Curve: ROC.png


    plt.show()
                precision    recall  f1-score   support

            0       0.94      0.94      0.94        17
            1       0.92      0.92      0.92        13

        accuracy                           0.93        30
    macro avg       0.93      0.93      0.93        30
    weighted avg       0.93      0.93      0.93        30


## Walkthrough

    In this project, I created a simple CAPTCHA in a python flask application to collect human and bot data. I then take that data and extract features in pandas, which I trained an XGBoost (XGB) model on with a 70-30 train-test split. The accuracy of the XGB model reached 0.933... with no hyperparameter tuning, inference took 0.00167s, meaning it's feasable for low-latency deployments. 

    Requirements met:
    - 50 human generated and 50 bot sessions
    - X, Y, time features collected
    - Engineered dt and dx, dy
    - Trained XGBoost Classifier
    - Reporting Conf Matrix, ROC Curve

    The captcha task is a flask application in the captcha/ directory. Running this application in a python virtual environment gives us a basic drag and drop task, which resets on reload. The app monitors and writes the mouse inputs (x, y, time) into the file mouse_log.txt. I significant other and I both completed the drag and drop puzzle with varying speeds and input styles as to keep the data from being too uniform.

    The bot is written in python and leverages slenium to manipulate mouse movements. This allows it to open a firefox tab and complete the drag-and-drop task. I ran into a lot of issues with selenium not wanting to work with html5 drag-and-drop but used js to work around it. 

    Cleaning the data is always the most time consuming. I manipulated the DataFrames from a long format dataset (where a specific 'person' may have multiple rows) to a wide format dataset (where a specific 'person' can only have one row). In doing so I calculated the duration of time, as well as the change in X and Y values. 

    Fitting the XGBoost model to the cleaned data returned us the AUC of 0.95, precision avg of 0.93, and recall avg of 0.93. These results indicate a good balance between false-positive and false-negative results. Pair that with a quick inference time and this is a solid proof-of-concept for production deploymens. 

## Potential Improvements

### Data collection
    - higher end botting
    - more realistic captcha
    - increase number of samples
    - incorporate mobile device sensors source: https://github.com/BiDAlab/HuMIdb

### Feature Extraction
    - Add linearity feature
    - Add inverse tangent feature
    - Add device sensor information

### Machine Learning
    - Not using python, python = slow. prospects: julia, c++
    - Automated hyperparameter tuning (optuna, raytune)
    - Testing different models (lgbm, rf may be faster for same performance)
    - Subsampling: since we have more than 50 of each feature, we can randomly sample
    - Luckily, tree-based learners are eager learners. We can spend tons of time on training and not affect inference performance
- 
