import home_app

#
home_app.home.add_url_rule(
    rule= "/home", #
    view_func= home_app.render_home #
)