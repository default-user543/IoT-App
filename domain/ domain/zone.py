from dataclasses import dataclass
from typing import List, Dict

# Định nghĩa rõ kiểu dữ liệu cho một điểm trong polygon
Point = Dict[str, float]  # {"lat": 10.0, "lng": 20.0}

@dataclass
class Zone:
    name: str
    polygon: List[Point]  # Danh sách điểm, định nghĩa vùng (zone)

    def contains_point(self, lat: float, lng: float) -> bool:
        """
        Kiểm tra xem một điểm (lat, lng) có trùng khớp chính xác với
        bất kỳ điểm nào trong polygon hay không.

        ⚠️ Đây KHÔNG phải là thuật toán kiểm tra nằm trong vùng (inside polygon).
        Nếu cần chính xác hơn, dùng thư viện `shapely`.
        """
        return any(p["lat"] == lat and p["lng"] == lng for p in self.polygon)
