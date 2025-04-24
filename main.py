from domain.user import User
from domain.zone import Zone

user = User(uid="abc123", email="user@example.com", full_name="Nguyễn Văn A")
print(user.to_dict())

zone = Zone(
    name="Zone A",
    polygon=[{"lat": 10.0, "lng": 20.0}, {"lat": 10.0, "lng": 21.0}]
)
print("Point in zone?", zone.contains_point(10.0, 20.0))
