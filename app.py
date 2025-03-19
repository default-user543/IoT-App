# Đây là file phân luồng chạy frontend và backend cùng lúc:
import threading
import os 

def backend():
    os.system('python backend/main2.py')

def frontend():
    os.system('python frontend/main.py')

if __name__ == '__main__':
    backend_t=threading.Thread(target=backend)
    frontend_t=threading.Thread(target=frontend)

    backend_t.start()
    frontend_t.start()

    backend_t.join()
    frontend_t.join()