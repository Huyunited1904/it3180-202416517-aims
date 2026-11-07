import unittest
from aims.cart import Cart


class TestCart(unittest.TestCase):

    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm 20 DVD đầu tiên
        for i in range(20):
            result = cart.add_dvd(i)
            self.assertTrue(result)

        # DVD thứ 21 phải bị từ chối
        result = cart.add_dvd(20)

        self.assertFalse(result)
        self.assertEqual(len(cart.items), 20)


if __name__ == "__main__":
    unittest.main()