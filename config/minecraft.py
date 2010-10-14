
def minecraft(kit):
    kit.update_config({
        "minecraft.path": "/vol/minecraft",
    })
    kit.include_recipe("minecraft.server")
