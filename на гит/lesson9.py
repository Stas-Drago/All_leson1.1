time = int(input('Ведите колличество секунд: '))
day = time//86400
hours = (time//3600)%24
minutes = (time//60)%60
seconds = time%60
print('Now')
print(f'day {day}, hours {hours}, minutes {minutes}, seconds {seconds}')