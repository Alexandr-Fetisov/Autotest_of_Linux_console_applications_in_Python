from checkers import checkout

tst = "/home/user/tst"
out = "/home/user/out"
folder = "/home/user/folder1"


def test_step1():
    res1 = checkout("cd {}; 7z a {}/arx2".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(out), "arx2.7z")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder), "Everything is Ok")
    res2 = checkout("ls {}".format(folder), "test1")
    res3 = checkout("ls {}".format(folder), "test2")
    assert res1 and res2 and res3, "test2 FAIL"
