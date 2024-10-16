text = input('Please enter a word - ').strip()

for i in text:
    if i.lower() in 'qwrtypsdfghjklzxcvbnm':
        print(i, end = ' ')
              
"ამ ვარიანტში ციფრების და სხვა სიმბოლოების შეყვანის შემთხვევაშიც მხოლოდ თანხმოვნები დაიბეჭდება"