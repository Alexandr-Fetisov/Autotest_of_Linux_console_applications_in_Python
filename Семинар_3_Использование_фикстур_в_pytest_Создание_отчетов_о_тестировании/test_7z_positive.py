import pytest
import yaml
from checkout import checkout_positive

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1(self, make_folders, clear_folders, make_files, task1):
        # test1
        res1 = checkout_positive("cd {}; 7z a {}/arx1.7z ".format(data["folder_in"], data["folder_out"]),
                                 "Everything is Ok"), "Test1 Fail"
        res2 = checkout_positive("ls {}".format(data["folder_out"]), "arx.7z"), "Test1 Fail"
        assert res1 and res2, "Test Fail"

    def test_step2(self, clear_folders, make_files, task1):
        # test2
        res = [
            checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                              "Everything is Ok"),
            checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                              "Everything is Ok")]
        for item in make_files:
            res.append(checkout_positive("ls {}".format(data["folder_ext"]), ""))
            assert all(res)

    def test_step3(self, task1):
        # test3
        assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                                 "Everything is Ok"), "Test1 Fail"

    def test_step4(self, make_folders, clear_folders, make_files):
        # test4
        assert checkout_positive("cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                                 "Everything is Ok"), "Test1 Fail"

    def test_step5(self, clear_folders, make_files, task1):
        # test5
        res = [
            checkout_positive("cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                              "Everything is Ok")]
        for item in make_files:
            res.append(checkout_positive("cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
        assert all(res)

    def test_step7(self, task1):
        assert checkout_positive("7z d {}/arx1.7z".format(data["folder_out"]), "Everything is Ok"), "Test1 Fail"

    def test_step8(self, make_files, home_task):
        # type of arch
        assert checkout_positive("7z t {}/{}".format(data['folder_out'], data['name_of_arch']),
                                 "Everything is Ok"), "Test8 Fail"


if __name__ == '__main__':
    pytest.main(['-v'])
