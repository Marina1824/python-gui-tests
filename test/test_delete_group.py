import random


def test_delete_group(app):
    group_list = app.groups.get_group_list()
    if len(group_list) == 1:
        app.groups.add_new_group("test2")
        group_list = app.groups.get_group_list()
    app.groups.open_group_editor()
    nodes = app.groups.get_group_nodes()
    random_node = random.choice(nodes)
    random_node.click()
    app.groups.delete_group()
    new_group_list=app.groups.get_group_list()
    assert len(group_list)==len(new_group_list)+1








