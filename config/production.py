
def production(kit):
    base(kit)
    kit.update_config({
        "munin.bind": "0.0.0.0",
        "munin.allow": ["127.0.0.1/32", "10.0.0.0/8"],
        "limits": [
            dict(domain="mongodb", type="soft", item="nofile", value="10000"),
            dict(domain="mongodb", type="hard", item="nofile", value="10000"),
            dict(domain="nginx", type="soft", item="nofile", value="10000"),
            dict(domain="nginx", type="hard", item="nofile", value="10000"),
            dict(domain="www-data", type="soft", item="nofile", value="10000"),
            dict(domain="www-data", type="hard", item="nofile", value="10000"),
            dict(domain="root", type="soft", item="nofile", value="30000"),
            dict(domain="root", type="hard", item="nofile", value="30000"),
        ],
    })

    kit.include_recipe("skeleton.production", "munin.node", "limits")
