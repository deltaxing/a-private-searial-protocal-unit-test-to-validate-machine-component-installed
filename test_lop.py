import unittest
from gui import MyDialog


class test_lop_device(unittest.TestCase):

    def test_lop_anamation(self):
        self.assertEqual(1, 1)

    def test_测试动画(self):
        ret = MyDialog.show(self._testMethodName.removeprefix("test_"),
                            "请查看 电梯显示屏 是否 显示了 A",
                            ["是", "否", "取消", "pause"])
        print(ret)
        self.assertEqual(ret, "是")

    def test_呼梯(self):
        # ret = MyDialog.show("呼梯",
        #      "按下呼梯按钮",
        #      ["是"]
        # )
        self.assertEqual(1, 1)

    def test_故障显示(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)