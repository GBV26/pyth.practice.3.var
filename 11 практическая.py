import tkinter as tk
import requests
import json

def fetch_repo_info():
    repo_name = entry.get()
    url = f'https://api.github.com/repos/{repo_name}'
    response = requests.get(url)

    if response.status_code == 200:
        repo_info = response.json()
        data = {
            'company': repo_info.get('owner', {}).get('login'),
            'created_at': repo_info.get('created_at'),
            'email': repo_info.get('owner', {}).get('email'),
            'id': repo_info.get('id'),
            'name': repo_info.get('name'),
            'url': repo_info.get('owner', {}).get('url')
        }

        with open('repo_info.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        label.config(text='Информация сохранена в repo_info.json')
    else:
        label.config(text='Ошибка: Репозиторий не найден')

root = tk.Tk()
root.title('Получение данных о репозитории')

label = tk.Label(root, text='Введите имя репозитория: (например, kubernetes/kubernetes обычно идет после https://github.com/, т.е. https://github.com/kubernetes/kubernetes)')
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text='Получить информацию', command=fetch_repo_info)
button.pack(pady=10)

label_result = tk.Label(root, text='', fg='red')
label_result.pack(pady=10)

root.mainloop()