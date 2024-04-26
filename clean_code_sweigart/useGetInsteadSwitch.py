# Все следующие условия if и elif содержат "season ==":
season = 'Fall'
if season == 'Winter':
    holiday = 'New Year\'s Day'
elif season == 'Spring':
    holiday = 'May Day'
elif season == 'Summer':
    holiday = 'Juneteenth'
elif season == 'Fall':
    holiday = 'Halloween'
else:
    holiday = 'Personal day off'
print(holiday)


season = 'Winter'
holiday = {
    'Winter': 'New Year\'s Day',
    'Spring': 'May Day',
    'Summer': 'Juneteenth',
    'Fall': 'Halloween'
}
result = holiday.get(season, 'Personal day off')
print(result)
