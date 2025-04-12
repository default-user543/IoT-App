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
  - 9 là người dùng chưa đăng nhập hoặc chưa đăng ký.
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

#### Tính năng thông tin cụ thể người dùng: http://127.0.0.1:5000/user-information (Not done)
+ **Input data**: Frontend sẽ gửi một file JSON theo methods POST như dưới:

```json
{
  "city": "...",
  "fav_colour": "...",
  "fav_pet": "...",
  "country": "...",
  "language": "..."
}
```

+ **Cách hoạt động**:
  - Backend sẽ check xem thông tin nhập vào có hợp với luật hoặc thiếu không.
  - Backend sẽ update các thông tin vào trong phần "forgot_password" trong Firebase Real-time Database.
+ **Output data**: Backend trả về một file JSON như quy ước.

#### Tính năng khi người dùng quên mật khẩu: http://127.0.0.1:5000/forgot_password (Not done)
+ **Input data**: Frontend sẽ gửi file JSON giống như phần trên nhưng có thêm key resert_password.
+ **Cách thức hoạt động**:
  - Backend sẽ check xem thông tin nhập vào có hợp với luật hoặc thiếu không.
  - Backend sẽ xem xét xem các user-information có trùng khớp trong cơ sở dữ liệu không.
  - Nếu trùng khớp thì mới đổi password của người dùng (Nhớ mã hoá theo phương thức hashed rồi mới up lên database)
+ **Output data**: Backend trả về một file JSON nhưu theo quy ước.

### Validation Rules:
- **Username**:
  - Must be between 6 and 20 characters.
  - Cannot contain special characters.
  - Can include Vietnamese characters and spaces.
- **Password**:
  - Must be longer than 6 characters.
  - Must contain at least one special character.

---

### Giai đoạn 2: Build tính năng liên quan đến GPS:

#### Tính năng khi người dùng bước vào một vùng định sẵn thì thông báo: http://127.0.0.1:5000/check-location
+ **Input data**: Frontend sẽ gửi một file JSON chứa thông tin vị trí của người dùng như sau:

```json
{
  "latitude": latitude,
  "longitude": longitude
}
```

+ **Cách thức hoạt động**: Sử dụng các thuật toán liên quan đến Polygon-based để xác định vị trí của người dùng so với vùng polygon đã định sẵn trong database.

+ **Output data**: Backend trả về một file JSON như sau:

```json
{
  "message": "Thông báo lỗi hoặc thành công",
  "zone_name": "Tên của vùng mà người dùng bước vào"
}
```
