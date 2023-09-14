import pytest
from checkout import checkout_negative
import yaml

folder_out = "/home/user/tst/badarx"
folder_ext = "/home/user/tst/ext"

with open('config.yaml') as fy:
    data = yaml.safe_load(fy)


class TestNegative:
    def test_step1(self, clear_folders, make_files, make_badarx):  # e извлекли из архива

        assert checkout_negative(f'cd {data["folder_bad"]}; 7z e arx2.{data["arc_type"]} -o{data["folder_ext"]} -y',
                                 "ERRORS")

    def test_step2(self):
        # test2
        assert checkout_negative("cd {}; 7z t badarx.7z".format(folder_out), "ERROR"), "Test5 Fail"


if __name__ == '__main__':
    pytest.main(['-v'])
