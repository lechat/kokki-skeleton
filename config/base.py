
import os.path

def base(kit):
    kit.add_cookbook_path(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cookbooks"),
        "kokki.cookbooks")
    kit.update_config({
    })
    kit.include_recipe("skeleton")
