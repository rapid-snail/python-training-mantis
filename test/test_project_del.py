import random


def test_project_del(app, db):
    old_list = db.get_project_list()
    if not old_list:
        app.project.add_new("proj_asdfgqwert")
        old_list = db.get_project_list()
    name = random.choice(old_list)
    app.project.delete(name)
    new_list = db.get_project_list()
    old_list.remove(name)
    assert sorted(old_list) == sorted(new_list)
