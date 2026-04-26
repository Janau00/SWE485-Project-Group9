### Test Case 1 — Heart Disease Detected

#### Input
| Feature | Value |
|---------|-------|
| Age | 55 |
| Sex | Male |
| ChestPainType | ATA |
| RestingBP | 140 |
| Cholesterol | 240 |
| FastingBS | 160 |
| RestingECG | Normal |
| MaxHR | 150 |
| ExerciseAngina | Yes |
| Oldpeak | 2.3 |
| STSlope | Flat |
| Prediction | Heart Disease |

#### Response
> The result suggests an increased likelihood of heart disease, indicating that your cardiovascular health may require closer medical attention. Several factors may have contributed to this result, including elevated blood pressure, higher cholesterol, elevated fasting blood sugar, and experiencing chest discomfort during exercise, along with signs of stress on the heart during activity. These patterns are often associated with higher cardiovascular risk. It is strongly recommended that you consult a healthcare professional for further evaluation and follow appropriate guidance on lifestyle changes and risk management.

---

### Test Case 2 — No Heart Disease (All Healthy)

#### Input
| Feature | Value |
|---------|-------|
| Age | 35 |
| Sex | Female |
| ChestPainType | NAP |
| RestingBP | 110 |
| Cholesterol | 180 |
| FastingBS | 80 |
| RestingECG | Normal |
| MaxHR | 175 |
| ExerciseAngina | No |
| Oldpeak | 0.0 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> The result suggests that there is no current strong indication of heart disease. Your clinical profile appears very reassuring, especially with normal blood pressure and cholesterol levels, no exercise-related chest discomfort, a healthy heart rate response during activity, and a normal ECG. These factors are commonly associated with a very low cardiovascular risk profile. It is still important to maintain these healthy habits, including regular exercise, balanced nutrition, and routine medical checkups, to support excellent long-term heart health.


---

### Test Case 3 — No Heart Disease (Borderline Values)

#### Input
| Feature | Value |
|---------|-------|
| Age | 45 |
| Sex | Male |
| ChestPainType | NAP |
| RestingBP | 128 |
| Cholesterol | 210 |
| FastingBS | 100 |
| RestingECG | Normal |
| MaxHR | 160 |
| ExerciseAngina | No |
| Oldpeak | 0.8 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> The result suggests that there is no current strong indication of heart disease. Your overall clinical profile appears reassuring, particularly with a normal ECG, no exercise-related chest discomfort, a good heart rate response during activity, and healthy signs during stress on the heart. These factors are commonly associated with a lower cardiovascular risk profile. However, it is still important to maintain healthy habits such as regular exercise, balanced nutrition, and routine medical checkups to support long-term heart health.


---

### Test Case 4 — Edge Case

#### Input
| Feature | Value |
|---------|-------|
| Age | 45 |
| Sex | Male |
| ChestPainType | ATA |
| RestingBP | 0 |
| Cholesterol | 210 |
| FastingBS | 100 |
| RestingECG | Normal |
| MaxHR | 150 |
| ExerciseAngina | No |
| Oldpeak | 0.8 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> The result suggests that there is no current strong indication of heart disease. Your overall clinical profile appears reassuring, particularly with a normal ECG, no exercise-related chest discomfort, and a good heart rate response and favorable heart activity pattern during exercise. These factors are commonly associated with a lower cardiovascular risk profile. However, it is still important to maintain healthy habits such as regular exercise, balanced nutrition, and routine medical checkups to support long-term heart health.



---