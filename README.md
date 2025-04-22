### Three main features:

- Show the information about locations of VGU.
- Share the route of user.
- Show the current position of user.

### Technologies and related-libraries:

- Frontend: Kivy
- Backend: Flask, Flask-Session, Flask-CORS
- Database: Firebase Admin SDK (Firebase Real-time Database)
- Ecryption: Bcrypt
- Geometric and coordinate processing: Shapely (Polygon-Approach)
- Real-time: Datetime
- API's communication and feature Google Maps API: urllib.parse

---

### The API is used in the project:

- Google Maps API for sharing route of user, showing the current position of user (Frontend).

### The Structure of Database: Note that we use Firebase Real-time Database! Some of our data will be contained in unique keys because we use push or {}.

```json
{
  "zones": {
    "library": {
      "name": "Library",
      "polygon": [
        { "lat": 11.108388528571519, "lng": 106.61382062524984 },
        { "lat": 11.108032532109064, "lng": 106.61391651341684 },
        { "lat": 11.108308987165445, "lng": 106.61471129781462 },
        { "lat": 11.108616482485534, "lng": 106.61461540964787 }
      ]
    },
    "ceremoney_hall": {
      "name": "Ceremony Hall",
      "polygon": [
        { "lat": 11.108042232288632, "lng": 106.6129853108017 },
        { "lat": 11.1077599568676, "lng": 106.61307032505268 },
        { "lat": 11.108026711997663, "lng": 106.61388685727688 },
        { "lat": 11.108351667917553, "lng": 106.61374450783345 }
      ]
    },
    "admin_building": {
      "name": "Admin Building",
      "polygon": [
        { "lat": 11.10980589340776, "lng": 106.61435949231425 },
        { "lat": 11.109358684783043, "lng": 106.6145188647208 },
        { "lat": 11.109811380625883, "lng": 106.61575749588035 },
        { "lat": 11.11030522983522, "lng": 106.6156148995166 }
      ]
    },
    "lecture_hall": {
      "name": "Lecture Hall",
      "polygon": [
        { "lat": 11.107111000874026, "lng": 106.61433409957904 },
        { "lat": 11.106600769247835, "lng": 106.61452587591256 },
        { "lat": 11.106936396995874, "lng": 106.61543137653894 },
        { "lat": 11.107446628035303, "lng": 106.61524750850782 }
      ]
    },
    "sports_hall": {
      "name": "Sports Hall",
      "polygon": [
        { "lat": 11.106135424993408, "lng": 106.61355345648064 },
        { "lat": 11.105009548228654, "lng": 106.61384970167983 },
        { "lat": 11.10476960671742, "lng": 106.61539675994226 },
        { "lat": 11.105171047211694, "lng": 106.61589520424566 },
        { "lat": 11.10681371750534, "lng": 106.61545318759926 }
      ]
    },
    "dorm_1": {
      "name": "Dorm 1",
      "polygon": [
        { "lat": 11.107783774691464, "lng": 106.61207810676271 },
        { "lat": 11.107191586406204, "lng": 106.61230254639403 },
        { "lat": 11.10741182185925, "lng": 106.61292100226702 },
        { "lat": 11.10805947626555, "lng": 106.61270820024622 }
      ]
    },
    "dorm_2": {
      "name": "Dorm 2",
      "polygon": [
        { "lat": 11.106614079294477, "lng": 106.61250869835385 },
        { "lat": 11.106003943445598, "lng": 106.61274810062724 },
        { "lat": 11.106240493591871, "lng": 106.61335325637395 },
        { "lat": 11.106840840688609, "lng": 106.61315209196364 }
      ]
    },
    "academic_cluster_1": {
      "name": "Academic Cluster 1",
      "polygon": [
        { "lat": 11.108766932780382, "lng": 106.61475735229159 },
        { "lat": 11.108277522709393, "lng": 106.614941891544 },
        { "lat": 11.108520596480586, "lng": 106.61550049684865 },
        { "lat": 11.109013268872221, "lng": 106.61532593269095 }
      ]
    },
    "academic_cluster_2": {
      "name": "Academic Cluster 2",
      "polygon": [
        { "lat": 11.108233285717834, "lng": 106.61497410224997 },
        { "lat": 11.107843384968529, "lng": 106.61510576678295 },
        { "lat": 11.108053331590593, "lng": 106.61566063874334 },
        { "lat": 11.108447846262996, "lng": 106.61552897421036 }
      ]
    },
    "academic_cluster_5": {
      "name": "Academic Cluster 5",
      "polygon": [
        { "lat": 11.109020006958495, "lng": 106.61541376774471 },
        { "lat": 11.108417853951245, "lng": 106.61566534104878 },
        { "lat": 11.108630107260351, "lng": 106.61624607568527 },
        { "lat": 11.109269173356648, "lng": 106.61601801390495 }
      ]
    },
    "academic_cluster_6": {
      "name": "Academic Cluster 6",
      "polygon": [
        { "lat": 11.108325569839131, "lng": 106.61568179911791 },
        { "lat": 11.107741872258465, "lng": 106.61591221205062 },
        { "lat": 11.10796104737623, "lng": 106.61647883977287 },
        { "lat": 11.108549358720522, "lng": 106.61627664066866 }
      ]
    },
    "university_guest_house": {
      "name": "University Guest House",
      "polygon": [
        { "lat": 11.109462969306996, "lng": 106.61648354209245 },
        { "lat": 11.10828865621168, "lng": 106.61706897903385 },
        { "lat": 11.109430669984969, "lng": 106.61875710643875 },
        { "lat": 11.110152789535334, "lng": 106.61841618934763 },
      ]
    }
  },
  "users":{
    "username-of-the-user": {
      "History_GPS": {
        {"lat": "...", "lng": "..."},
      },
      "forget_password": {
        "city": "...",
        "country": "...",
        "fav_color": "...",
        "fav_pet": "...",
        "language": "..."
      },
      "password": "password-after-ecrypting-by-hashed",
      "username": "the-username-of-the-user",
    }
  }
}
```

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
- 10 là không lấy được GPS của người dùng.

#### Tính năng sign up: http://127.0.0.1:5000/sign-up (Done)

- **Input data**: Frontend sẽ gửi một file JSON như bên dưới theo phương thức POST:

```json
{
  "username": "...",
  "password": "...",
  "confirm_password": "..."
}
```

- **Output data**: Backend trả về một file JSON như quy ước.

#### Tính năng log in: http://127.0.0.1:5000/login (Not done):

- **Input data**: Frontend sẽ gửi một file JSON như bên dưới theo phương thức POST:

```json
{
  "username": "...",
  "password": "..."
}
```

- **Cách hoạt động**:
  - Backend nhận file JSON chứa 2 data như trên.
  - Backend dùng phương thức hashed để mã hoá mật khẩu người dùng nhập vào và dùng thuật toán để thực hiện tính năng log in.
- **Output data**: Backend trả về một file JSON như quy ước.

#### Tính năng thông tin cụ thể người dùng: http://127.0.0.1:5000/user-information (Not done)

- **Input data**: Frontend sẽ gửi một file JSON theo methods POST như dưới:

```json
{
  "city": "...",
  "fav_colour": "...",
  "fav_pet": "...",
  "country": "...",
  "language": "..."
}
```

- **Cách hoạt động**:
  - Backend sẽ check xem thông tin nhập vào có hợp với luật hoặc thiếu không.
  - Backend sẽ update các thông tin vào trong phần "forgot_password" trong Firebase Real-time Database.
- **Output data**: Backend trả về một file JSON như quy ước.

#### Tính năng khi người dùng quên mật khẩu: http://127.0.0.1:5000/forgot_password (Not done)

- **Input data**: Frontend sẽ gửi file JSON giống như phần trên nhưng có thêm key resert_password.
- **Cách thức hoạt động**:
  - Backend sẽ check xem thông tin nhập vào có hợp với luật hoặc thiếu không.
  - Backend sẽ xem xét xem các user-information có trùng khớp trong cơ sở dữ liệu không.
  - Nếu trùng khớp thì mới đổi password của người dùng (Nhớ mã hoá theo phương thức hashed rồi mới up lên database)
- **Output data**: Backend trả về một file JSON nhưu theo quy ước.

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

- **Input data**: Frontend sẽ gửi một file JSON chứa thông tin vị trí của người dùng như sau:

```json
{
  "latitude": latitude,
  "longitude": longitude
}
```

- **Cách thức hoạt động**: Sử dụng các thuật toán liên quan đến Polygon-based để xác định vị trí của người dùng so với vùng polygon đã định sẵn trong database.

- **Output data**: Backend trả về một file JSON như sau:

```json
{
  "message": "Thông báo lỗi hoặc thành công",
  "zone_name": "Tên của vùng mà người dùng bước vào"
}
```

---

#### Tính năng chia sẻ lộ trình của người dùng: http://127.0.0.1:5000/share

- **Input data**: Frontend gửi một method POST đến Backend Server.
- **Cách thức hoạt động**: Frontend phải trả về hai thứ:
  - Link Google Maps mà khi người dùng bấm vào hiện lộ trình theo điểm bắt đầu và điểm kết thúc.
  - Các khu vực cụ thể mà người dùng đã đi qua.
- **Output data**: Backend trả về một file JSON nhưu sau:

```json
{
  "link": "...",
  "areas": "Khu vực 1 -> Khu vực 2 -> Khu vực 3"
}
```
