from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth_sign_in')
def auth_sign_in():
    return render_template('auth-sign-in.html')

@app.route('/auth_sign_up')
def auth_sign_up():
    return render_template('auth-sign-up.html')

@app.route('/page_add_event')
def page_add_event():
    return render_template('page-add-event.html')

@app.route('/page_new_event')
def page_new_event():
    return render_template('page-new-event.html')

@app.route('/main_my_schedule')
def main_my_schedule():
    return render_template('main-my-schedule.html')

@app.route('/main_integration')
def main_integration():
    return render_template('main-integration.html')

@app.route('/ui_avatars')
def ui_avatars():
    return render_template('ui-avatars.html')

@app.route('/ui_alerts')
def ui_alerts():
    return render_template('ui-alerts.html')

@app.route('/ui_badges')
def ui_badges():
    return render_template('ui-badges.html')

@app.route('/ui_breadcrumb')
def ui_breadcrumb():
    return render_template('ui-breadcrumb.html')

@app.route('/ui_buttons')
def ui_buttons():
    return render_template('ui-buttons.html')

@app.route('/ui_buttons_group')
def ui_buttons_group():
    return render_template('ui-buttons-group.html')

@app.route('/ui_boxshadow')
def ui_boxshadow():
    return render_template('ui-boxshadow.html')

@app.route('/ui_colors')
def ui_colors():
    return render_template('ui-colors.html')

@app.route('/ui_cards')
def ui_cards():
    return render_template('ui-cards.html')

@app.route('/ui_carousel')
def ui_carousel():
    return render_template('ui-carousel.html')

@app.route('/ui_grid')
def ui_grid():
    return render_template('ui-grid.html')

@app.route('/ui_helper_classes')
def ui_helper_classes():
    return render_template('ui-helper-classes.html')

@app.route('/ui_images')
def ui_images():
    return render_template('ui-images.html')

@app.route('/ui_list_group')
def ui_list_group():
    return render_template('ui-list-group.html')

@app.route('/ui_media_object')
def ui_media_object():
    return render_template('ui-media-object.html')

@app.route('/ui_modal')
def ui_modal():
    return render_template('ui-modal.html')

@app.route('/ui_notifications')
def ui_notifications():
    return render_template('ui-notifications.html')

@app.route('/ui_pagination')
def ui_pagination():
    return render_template('ui-pagination.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)