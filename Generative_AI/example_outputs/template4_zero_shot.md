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
> Based on your information, it suggests your heart health needs a closer look. We noticed your blood pressure is a bit higher than ideal, and your cholesterol and blood sugar levels are elevated. You also mentioned experiencing some chest discomfort during exercise, and tests showed your heart working harder during physical activity.

> These findings are important to address. We strongly recommend discussing this overview with your doctor soon. They can help you understand these points better and create a personalized plan to support your heart health, possibly including lifestyle adjustments and other steps.

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
> Your current health profile is very encouraging, suggesting that you do not show signs of heart disease. Your blood pressure, cholesterol, and blood sugar levels are all looking good. This is a wonderful foundation for your heart health. Continue with your healthy habits to keep your heart strong.


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
> Your recent heart health assessment is reassuring, indicating you do not show signs of heart disease at this time.

> To support your long-term well-being, we noticed a few areas that could benefit from your attention. Your blood pressure and cholesterol levels are a little higher than ideal. Additionally, your fasting blood sugar is at a level where it's good to keep an eye on it.

> Embracing a healthy lifestyle with a balanced diet and regular activity is a wonderful way to care for your heart. We recommend discussing these points with your doctor for personalized guidance.


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
> Based on the information, your heart health outlook appears reassuring, indicating no heart disease at this time. It's great that your heart's electrical activity is normal and you don't experience chest discomfort with exercise.

> We noticed your cholesterol level of 210 is a little higher than ideal, and your fasting blood sugar of 100 is at the upper end of the normal range. It's also a good idea to ensure your blood pressure is regularly checked and within a healthy range.

> Focusing on a balanced diet, regular physical activity, and routine check-ups with your doctor can help keep your heart healthy and manage these numbers effectively. Your doctor can offer personalized advice and support.

---