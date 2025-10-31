sentiment_scores={
    'positive':0.7,
    'neutral':0.5,
    'negative':0.3
    }

volume_scores={
    'high':0.8,
    'medium':0.5,
    'low':0.2
    }

volatility_scores={
    'high':0.7,
    'medium':0.5,
    'low':0.3
    }

def predict_trend(sentiment,volume,volatility):
    sent_score=sentiment_scores.get(sentiment,0.0)
    vol_score=volume_scores.get(volume,0.0)
    volat_score=volatility_scores.get(volatility,0.0)
    
    overall_score=(sent_score+vol_score+volat_score)/3
    
    if overall_score>0.6:
        return 'bullish'
    elif overall_score<0.4:
        return 'bearish'
    else:
        return 'neutral'
    
    
if __name__ == "__main__":
    sentiment=input("Enter market sentiment (positive/neutral/negative): ")
    volume=input("Enter market volume (high/medium/low): ")
    volatility=input("Enter market volatility (high/medium/low): ")
    
    trend=predict_trend(sentiment,volume,volatility)
    
    print(f'\nPredicted Market Trend: {trend.upper()}')
