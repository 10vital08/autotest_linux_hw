"""
Доработать позитивные тесты таким образом, чтобы при
архивации дополнительно проверялось создание файла
архива, а при распаковке проверялось создание файлов.
"""

from sem import checkout, checkout_negative

folderin = "/home/vvl/tst"
folderout = "/home/vvl/out"
folderext = "/home/vvl/folder1"
folderbad = "/home/vvl/folder2"


def test_step1():
    # test1
    assert checkout(f"cd {folderin};  7z a {folderout}/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    # test3
    assert checkout(f"cd {folderout}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step4():
    # test4
    assert checkout(f"cd {folderout}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step5():
    # test5
    assert checkout(f"cd {folderin}; 7z u {folderout}/arx2.7z", "Everything is Ok"), "test5 FAIL"


def test_step6():
    # test6
    res1 = checkout(f"cd {folderin}; 7z a {folderout}/arx2", "Everything is Ok")
    res2 = checkout(f"ls {folderout}", "arx2.7z")
    assert res1 and res2, "test6 FAIL"


def test_step7():
    # test7
    res1 = checkout(f"cd {folderout}; 7z e arx2.7z -o{folderext} -y", "Everything is Ok"), "test7 FAIL"
    res2 = checkout(f"ls {folderext}", "test1.txt")
    res3 = checkout(f"ls {folderext}", "test2.txt")
    assert res1 and res2 and res3, "test7 FAIL"


def test_step8():
    # test8  команды вывода списка файлов
    assert checkout(f"cd {folderout}; 7z l arx2.7z", "2 files")


def test_step9():
    # test9  команды разархивирования
    # assert checkout(f"cd {folderout}; 7z x {folderext}/arx2.7z", "Everything is Ok"), "test9 FAIL"
    assert checkout(f"cd {folderout}; 7z x arx2.7z {folderext}", "Everything is Ok"), "test9 FAIL"
