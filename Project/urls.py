import home_app

#
home_app.home.add_url_rule(
    rule = "/", #/ - головна стоірнка
    view_func= home_app.render_home #
)