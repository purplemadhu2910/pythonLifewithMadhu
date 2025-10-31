users={}
def get_recommendation (user_data):
    recommendations=[]
    
    interests=user_data['interests']
    age=user=user_data['age']
    location=user_data['location']
    
    if 'tech' in interests:
        recommendations.extend(['Smartphone','Laptop'])
    if 'books' in interests:
        recommendations.extend(['E-Reader','Kindle'])
    if 'workout' in interests:
        if age<30:
            recommendations.append('Gaming Console')
            
    if location == 'usa':
        recommendations.append("Amazon Prime Membership")
    elif location == 'india':
        recommendations.append('Netfliz Membership')
    elif location == 'germany':
        recommendations.append('Disney+Membership')
        
    return recommendations

def input_user_data():
    name=input("Enter you name: ").strip()
    interests_input=input('Enter your interests(comma-separated: tech,books,workout): ').strip().lower()
    interests=[i.strip() for i in interests_input.split(',') if i.strip()]
    
    try:
        age=int(input("Enter your age: "))
    except ValueError:
        print("Invaid age.Please enter a number.")
        return None
    
    location=input('Enter your location (usa/india/germany): ').strip().lower()
    if location not in ['usa','india','germany']:
        print("Unsupported location entered.")
        return None
    
    users[name]={
        'interests':interests,
        'age':age,
        'location':location
        }
    return name

if __name__=="__main__":
    print("====Personalized Learning Recommendation System====")
    username=input_user_data()
    if username:
        recommendations=get_recommendation(users[username])
        print(f"\nRecommendations for {username.capitalize()}:{recommendations}")
