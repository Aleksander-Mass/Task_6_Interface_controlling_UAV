'''
Задание № 6. «Создание пользовательского интерфейса для управления беспилотным
летательным аппаратом на Python»
'''
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from random import randint
import ftplib
ftp = ftplib.FTP()

host = '127.0.0.1'
port = 21
login = 'user'
passwd = 'user'

data = [str(randint(5, 50))+'\n' for i in range(100)]

def close_window():
    # необходимые действия перед закрытием
    root.destroy()  # Закрываем окно
    print("window closed")

# функция загрузки на сервер
def ftp_upload(obj, path):
    with open(path, 'rb') as fobj:
        obj.storbinary('STOR ' + path, fobj, 1024)
# функция записи в файл
def click_btnLocal():
    with open('db.txt', 'w') as f:
        f.writelines(data)


def click_btnServer():
    click_btnLocal()
    try:
        connect_str = ftp.connect(host=host, port=port, timeout=10)
        ftp.login(user=login, passwd=passwd)
        ftp_upload(ftp, 'db.txt')
        ftp.close()
    except:
        print("Error")

# Разработка интерфейса для управления движением дрона.

root = Tk()  # Создаем объект главного окна
root.title("BPLA interface")  # Устанавливаем заголовок
w_screen = root.winfo_screenwidth()
h_screen = root.winfo_screenheight()
print(w_screen, h_screen)
w_window = 600
h_window = 400

root.geometry(f"{w_window}x{h_window}+{w_screen // 2 - w_window // 2}+{h_screen // 2 - h_window // 2}") # Устанавливаем размеры в смещение окна
root.resizable(False, False)  # False запрещает изменения размера окна
root.minsize(w_window-100, h_window-100)
root.maxsize(w_window+100, h_window+100)
# root.attributes("-alpha", 0.5) # Прозрачность
# root.attributes("-fullscreen", True) # Полноэкранное окно
root.protocol("WM_DELETE_WINDOW", close_window)

# создание кнопки
# btn = ttk.Button(text="Click ME!", command=click_btn)
# btn.pack(anchor=CENTER, expand=1)

# создание вкладок
tab_control = ttk.Notebook(root)
tab_main = ttk.Frame(tab_control)
tab_setting = ttk.Frame(tab_control)
tab_help = ttk.Frame(tab_control)
tab_control.add(tab_main, text='Управление')
tab_control.add(tab_setting, text='Настройки')
tab_control.add(tab_help, text='Справка')

# добавление элементов на вкладку "Управление"
img_W = ImageTk.PhotoImage(file='img/w.jpg', height=100, width=100)
btn_W = Button(tab_main, image=img_W, height=100, width=100)
btn_W.grid(column=1, row=0)
img_A = ImageTk.PhotoImage(file='img/a.jpg', height=100, width=100)
btn_A = Button(tab_main, image=img_A, height=100, width=100)
btn_A.grid(column=0, row=1, padx=(15, 15))
img_D = ImageTk.PhotoImage(file='img/d.jpg', height=100, width=100)
btn_D = Button(tab_main, image=img_D, height=100, width=100)
btn_D.grid(column=3, row=1, padx=(15, 15))
img_Photo = ImageTk.PhotoImage(file='img/photo.jpg', height=100, width=100)
btn_Photo = Button(tab_main, image=img_Photo, height=100, width=100)
btn_Photo.grid(column=6, row=1, padx=(30, 30))
img_S = ImageTk.PhotoImage(file='img/s.jpg', height=100, width=100)
btn_S = Button(tab_main, image=img_S, height=100, width=100)
btn_S.grid(column=1, row=2)

# вывод статистической информации скорость, текущая высота, заряд батареи

info = Label(tab_main, text='Speed: 30 Hight: 100 Batary: 38%')
info.grid(column=0, row=3, pady=(20, 20))

# Сохранение информации о полете в локальную базу данных.

btn_saveLocal = Button(tab_setting, text='Сохранить в БД', height=4, width=17, command=click_btnLocal)
btn_saveLocal.grid(column=0, row=0, padx=(10, 10), pady=(10, 10))

#  сохранение информации в облачный сервис.

btn_saveServer = Button(tab_setting, text='Сохранить в облако', height=4, width=17, command=click_btnServer)
btn_saveServer.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))

tab_control.pack(expand=1, fill='both')

root.mainloop()
