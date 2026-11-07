import unittest
from aims.cart import Cart


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD
        for i in range(20):
            dvd = type("DVD", (), {"title": f"DVD {i}"})()
            result = cart.add_dvd(dvd)
            self.assertTrue(result)

        # DVD thứ 21 phải bị từ chối
        dvd_21 = type("DVD", (), {"title": "DVD 21"})()
        result = cart.add_dvd(dvd_21)

        self.assertFalse(result)
        self.assertEqual(len(cart.items), 20)

    def test_discount_calculation(self):
        cart = Cart()

        # Giả lập tổng tiền là 100
        cart.total_cost = lambda: 100

        # Giảm 20% còn 80
        self.assertEqual(
            cart.total_cost_with_discount(20), 80
        )

        # Giảm 150% phải báo lỗi
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_remove_dvd(self):
        cart = Cart()
        dvd = type("DVD", (), {"title": "DVD 1"})()

        cart.add_dvd(dvd)

        # Xóa DVD thành công
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertEqual(len(cart.items), 0)

        # Xóa DVD không tồn tại
        self.assertFalse(cart.remove_dvd(dvd))

    def test_total_cost(self):
        cart = Cart()

        dvd1 = type("DVD", (), {"title": "DVD 1", "cost": 10})()
        dvd2 = type("DVD", (), {"title": "DVD 2", "cost": 20})()

        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)

        self.assertEqual(cart.total_cost(), 30)
    def test_sort_by_title(self):
        cart = Cart()
        for title, cost in [("Star Wars", 20), ("Aladdin", 15), ("Batman", 10)]:
            dvd = type("DVD", (), {"title": title, "cost": cost})()
            cart.add_dvd(dvd)

        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Batman", "Star Wars"]
        )

    def test_sort_by_cost(self):
        cart = Cart()
        for title, cost in [("A", 30), ("B", 10), ("C", 20)]:
            dvd = type("DVD", (), {"title": title, "cost": cost})()
            cart.add_dvd(dvd)

        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [10, 20, 30]
        )

if __name__ == "__main__":
    unittest.main()