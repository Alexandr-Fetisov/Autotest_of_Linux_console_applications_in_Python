import yaml
from sshcheckers import ssh_checkout
from sshcheckers import upload_files

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def test_step0():
    res = []
    upload_files(data["host"], data["user"], "1111", "{}/p7zip-full.deb".format(data["local_path"]),
                 "{}/p7zip-full.deb".format(data["remote_path"]))
    res.append(ssh_checkout("0.0.0.0", "user2", "1qazXSW!", "echo '1qazXSW!' | sudo -S dpkg -i /home/user2/p7zip-full.deb",
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "usr2", "12345", "echo '12345' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


def test_step1(make_folders, clear_folders, make_files, task1):
    # test1
    res1 = ssh_checkout(data["host"], data["user"], "1111",
                        "cd {}; 7z a {}/arx1.7z ".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"
    res2 = ssh_checkout(data["host"], data["user"], "1111",
                        "ls {}".format(data["folder_out"]), "arx.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files, task1):
    # test2
    res = []
    res.append(ssh_checkout(data["host"], data["user"], "1111",
                            "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    res.append(ssh_checkout(data["host"], data["user"], "1111",
                            "cd {}; 7z e arx1.7z -o{} -y".format(data["folder_out"], data["folder_ext"]),
                            "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "1111",
                                "ls {}".format(data["folder_ext"]), ""))
    assert all(res)


def test_step3(task1):
    # test3
    assert ssh_checkout(data["host"], data["user"], "1111",
                        "cd {}; 7z t {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    # test4
    assert ssh_checkout(data["host"], data["user"], "1111",
                        "cd {}; 7z u {}/arx1.7z".format(data["folder_in"], data["folder_out"]),
                        "Everything is Ok"), "Test1 Fail"


def test_step5(clear_folders, make_files, task1):
    # test5
    res = []
    res.append(
        ssh_checkout(data["host"], data["user"], "1111",
                     "cd {}; 7z a {}/arx1.7z".format(data["folder_in"], data["folder_out"]), "Everything is Ok"))
    for item in make_files:
        res.append(ssh_checkout(data["host"], data["user"], "1111",
                                "cd {}; 7z l arx1.7z".format(data["folder_out"]), item))
    assert all(res)


# def test_step6():


def test_step7(task1):
    assert ssh_checkout(data["host"], data["user"], "1111",
                        "7z d {}/arx1.7z".format(data["folder_out"]), "Everything is Ok"), "Test1 Fail"


def test_step8(make_files, home_task):
    # type of arch
    assert ssh_checkout(data["host"], data["user"], "1111",
                        "7z t {}/{}".format(data['folder_out'], data['name_of_arch']),
                        "Everything is Ok"), "Test8 Fail"
