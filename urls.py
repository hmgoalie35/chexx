from home.views import HomeView, StreamView

urlpatterns = [
    ('/', {'view_func': HomeView.as_view('home')}),
    ('/video_feed', {'view_func': StreamView.as_view('stream')})
]

blueprints = []
