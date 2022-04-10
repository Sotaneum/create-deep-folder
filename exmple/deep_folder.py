from deepfolder import create, remove


def test(name, result):
    if result is False:
        raise Exception(name + ": Test Failed!")


create_target = './create_new_folder/create_new_sub_folder/create_new_deep_folder'
remove_target = './create_new_folder'
test("create test1", create(create_target) is True)
test("remove test1", remove(remove_target) is True)
test("remove test2", remove(remove_target) is False)
print("Test Pass!")
