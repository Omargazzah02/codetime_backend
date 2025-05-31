import pandas as pd
from .models import UserLoginHistory, UserLoginPrediction
from django.utils.timezone import localtime

def update_user_prediction(user):
    # Fetch all login timestamps for the user
    logs = UserLoginHistory.objects.filter(user=user).order_by('-timestamp')

    if logs.count() < 3:
        return

    days = [localtime(log.timestamp).strftime("%A") for log in logs]
    df = pd.DataFrame(days, columns=["day"])

    predicted_day = df["day"].mode()[0]

    prediction, _ = UserLoginPrediction.objects.get_or_create(user=user)
    prediction.predicted_day = predicted_day
    prediction.save()
