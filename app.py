# Đây là file phân luồng chạy frontend và backend cùng lúc:
import threading
import os 

# Đường dẫn tuyệt đối tới thư mục chứa app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def backend():
    path = os.path.join(BASE_DIR, "backend", "main2.py")
    os.system(f'python "{path}"')
    print("Backend started")

def frontend():
    path = os.path.join(BASE_DIR, "frontend", "main.py")
    os.system(f'python "{path}"')

if __name__ == '__main__':
    backend_t=threading.Thread(target=backend)
    frontend_t=threading.Thread(target=frontend)

    backend_t.start()
    frontend_t.start()

    backend_t.join()
    frontend_t.join()