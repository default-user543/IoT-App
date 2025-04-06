### Các tính năng chính của dự án:
+ Chia sẻ thông tin vị trí các địa danh nổi tiếng (For example: Hồ con rùa có gì, địa đạo củ chi có gì).
+ Chia sẻ lộ trình đã đi.
+ Chia sẻ cảm nhận về địa danh này.

### Công nghệ:
+ Frontend: Kivy
+ Backend: Flask 
+ Database: Realtime Database of Firebase 
+ Mã hoá password: Hashed

---


### Giai đoạn 1: Build các giao diện đăng nhập:

### Quy ước về cách trả về của Backend, backend trả về một file JSON có cấu trúc như sau:

```json
{
  "message": "Đây là một tin nhắn ví dụ",
  "a": "Một giá trị khác"
}
```

### Quy ước của biến a:
  - 0 là đăng nhập thành công
  - 1 là username phải từ 6-20 ký tự
  - 2 là username không được chứa ký tự đặc biệt
  - 3 là password và confirm_password không giống nhau
  - 4 là password phải có hơn 6 ký tự
  - 5 là password phải có ít nhất một ký tự đặc biệt
  - 6 là chưa nhập đầy đủ thông tin
  - 7 là username đã tồn tại
  - 8 là user-information của người dùng nhập vào không trùng khớp với cơ sở dữ liệu nên sẽ không resert.
#### Tính năng sign up: http://127.0.0.1:5000/sign-up (Done)
+ **Input data**: Frontend sẽ gửi một file JSON như bên dưới theo phương thức POST:

```json
{
	"username": "...",
	"password": "...",
	"confirm_password": "..."
}
```

+ **Output data**: Backend trả về một file JSON như quy ước.

#### Tính năng log in: http://127.0.0.1:5000/login (Not done):
+ **Input data**: Frontend sẽ gửi một file JSON như bên dưới theo phương thức POST:

```json
{
	"username": "...",
	"password": "..."
}
```

+ **Cách hoạt động**:
  -	Backend nhận file JSON chứa 2 data như trên.
  -	Backend dùng phương thức hashed để mã hoá mật khẩu người dùng nhập vào và dùng thuật toán để thực hiện tính năng log in.
+ **Output data**: Backend trả về một file JSON như quy ước.

+ ### Validation Rules:
- **Username**:
  - Must be between 6 and 20 characters.
  - Cannot contain special characters.
  - Can include Vietnamese characters and spaces.
- **Password**:
  - Must be longer than 6 characters.
  - Must contain at least one special character.

---
