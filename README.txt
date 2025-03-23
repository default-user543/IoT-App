### Các tính năng chính của dự án:
+Chia sẻ thông tin vị trí các địa danh nổi tiếng (For example: Hồ con rùa có gì, địa đạo củ chi có gì).
+Chia sẻ lộ trình đã đi.
+Chia sẻ cảm nhận về địa danh này.

### Công nghệ:
- Frontend: Kivy
- Backend: Flask 
- Database: Realtime Database of Firebase 

---

### Giai đoạn 1: Build các giao diện đăng nhập:

#### Tính năng sign up: http://127.0.0.1:5000/sign-up (Done)
    +***Input data***: Frontend sẽ gửi một file JSON gồm 3 keys: username, password, confirm_password cho phía backend xử lý qua route, method POST.
    +***Features***:
        +Kiểm tra xem username và password có hợp lệ không, kiểm tra xem password == confirm_password.
        +Kiểm tra xem username có tồn tại trên Firebase Real-time Database chưa.
        +Up dữ liệu gồm username, password, mẫu của GPS (mật khẩu đã mã hoá theo phương thức hashed) lên Database.
    +***Output data***: Backend luôn trả về một file JSON chứa key "message" dùng để báo liệu đăng nhập thành công hoặc lỗi cụ thể của người dùng + Status code.
        +Nếu gặp lỗi cụ thể sẽ trả về status 400
        +Nếu gặp thành công sẽ trả về status 200

#### Tính năng log in: http://127.0.0.1:5000/login (Not done)
    +***Input data***: Frontend sẽ gửi một file JSON gồm 2 keys: username và password theo phương thức POST.
    +***Features***: Người build log in. (Lưu ý: Password được lưu trên firebase đã được mã hoá theo hashed)
    +***Output data***: Như sign up

#### Tính năng thông tin cụ thể người dùng: http://127.0.0.1:5000/user-information (Not done)
    +***Input data***: Frontend sẽ gửi một file JSON gồm các keys sau: city, fav_colour, fav_pet, country, language.
    +***Features***: Tạo một key forget_password bên trong unique_id và lưu các thông tin trên.
    +***Output data***: Như sign up

#### Tính năng khi người dùng quên mật khẩu: http://127.0.0.1:5000/huhu (Vì chúng ta muốn basic nên người dùng nhập đúng thông tin thì sẽ cho đặt lại mật khẩu) (Not done)
    +***Input data***: Frontend gửi một JSON gồm các keys như user-information.
    +***Features***: Kiểm tra độ trùng khớp chiếu theo các thông tin được lưu ở user-information.
    +***Output data***: Như sign up

### Validation Rules:
- **Username**:
  - Must be between 6 and 20 characters.
  - Cannot contain special characters.
  - Can include Vietnamese characters and spaces.
- **Password**:
  - Must be longer than 6 characters.
  - Must contain at least one special character.