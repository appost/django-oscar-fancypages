from django.conf.urls.defaults import patterns, url, include

from oscar.core.application import Application
from oscar.views.decorators import staff_member_required

from . import views
from fancypages.assets.app import application as assets_app


class OscarFancypagesDashboardApplication(Application):
    name = 'fp-dashboard'
    assets_app = assets_app

    page_list_view = views.FancyPageListView
    page_create_view = views.FancyPageCreateView
    page_update_view = views.FancyPageUpdateView
    page_delete_view = views.FancyPageDeleteView

    widget_update_view = views.WidgetUpdateView
    widget_delete_view = views.WidgetDeleteView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^assets/', include(self.assets_app.urls)),

            url(
                r'^$',
                self.page_list_view.as_view(),
                name='page-list'
            ),
            url(
                r'^create/$',
                self.page_create_view.as_view(),
                name='page-create'
            ),
            url(
                r'^create/(?P<parent_pk>\d+)/$',
                self.page_create_view.as_view(),
                name='child-page-create'
            ),
            url(
                r'^update/(?P<pk>\d+)/$',
                self.page_update_view.as_view(),
                name='page-update'
            ),
            url(
                r'^delete/(?P<pk>\d+)/$',
                self.page_delete_view.as_view(),
                name='page-delete'
            ),

            url(
                r'^widget/update/(?P<pk>\d+)/$',
                self.widget_update_view.as_view(),
                name='widget-update'
            ),
            url(
                r'^widget/delete/(?P<pk>\d+)/$',
                self.widget_delete_view.as_view(),
                name='widget-delete'
            ),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = OscarFancypagesDashboardApplication()
