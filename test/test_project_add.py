import string
import random


def random_string(prefix, max_len):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for _ in range(max_len)])


def test_project_add(app, db):
    old_list = db.get_project_list()
    name = random_string("proj_", 10)
    app.project.add_new(name)
    new_list = db.get_project_list()
    old_list.append(name)
    assert sorted(old_list) == sorted(new_list)
