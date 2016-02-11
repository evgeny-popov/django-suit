from django import get_version
from django.apps import AppConfig
from django.contrib.admin.options import ModelAdmin
from . import VERSION


class DjangoSuitConfig(AppConfig):
    name = 'suit'
    verbose_name = 'Django Suit'
    django_version = get_version()
    version = VERSION

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of suit.menu.ParentItem
    menu = []

    # Automatically add home link
    menu_show_home = True

    # Form row sizing as Bootstrap CSS grid classes: (for label, for field column)
    SUIT_FORM_SIZE_HALF = ('col-xs-12 col-sm-3 col-md-2', 'col-xs-12 col-sm-7 col-md-6 col-lg-5')
    SUIT_FORM_SIZE_FULL = ('col-xs-12 col-sm-3 col-md-2', 'col-xs-12 col-sm-9 col-md-10')

    form_size = {
        'default': SUIT_FORM_SIZE_HALF
    }

    def __init__(self, app_name, app_module):
        self.setup_model_admin_defaults()
        super(DjangoSuitConfig, self).__init__(app_name, app_module)

    def ready(self):
        super(DjangoSuitConfig, self).ready()

    def setup_model_admin_defaults(self):
        """
        Override some ModelAdmin defaults
        """
        if self.toggle_changelist_top_actions:
            ModelAdmin.actions_on_top = True
        ModelAdmin.actions_on_bottom = True

        if self.list_per_page:
            ModelAdmin.list_per_page = self.list_per_page
