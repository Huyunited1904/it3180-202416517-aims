import unittest
from aims.cart import Cart


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD đầu tiên
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

        # Giả lập tổng tiền giỏ hàng là 100$
        cart.total_cost = lambda: 100

        # Giảm 20% thì phải còn 80$
        self.assertEqual(
            cart.total_cost_with_discount(20), 80
        )

        # Giảm 150% là không hợp lệ
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()