import random


class GroupHelper:

    def __init__(self, app):
        self.app = app


    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def get_group_nodes(self):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        return root.children()

    def delete_group(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        delete_dialog = self.app.application.window(title="Delete group")
        delete_dialog.wait("visible")
        delete_dialog.window(auto_id="uxOKAddressButton").click()


    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()


    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    #def count_groups(self):
