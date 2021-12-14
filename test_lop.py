import unittest
from gui import MyDialog
import pymsgbox

class test_lop_device(unittest.TestCase):

    def test_lop_anamation(self):
        self.assertEqual(1, 1)

    def notest_测试动画(self):
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
        isOk = pymsgbox.confirm(text="按下呼梯按钮",title="呼梯",buttons="是")
        # send command by serial here
        #...
        
        isOk = pymsgbox.confirm(text="电梯呼到了",title="呼梯",buttons=["是呼到了","没反应"])
        
        self.assertEqual(isOk, "是呼到了")

    def test_故障显示(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)