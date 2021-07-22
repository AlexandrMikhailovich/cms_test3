from garpixcms.settings import *  # noqa

INSTALLED_APPS += [
    'catalog',
    'rest_framework.authtoken'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            os.path.join(BASE_DIR, '..', 'frontend', 'templates'),
            os.path.join(BASE_DIR, '..', 'frontend'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'garpix_menu.context_processors.menu_processor',
            ],
        },
    },
]

MENU_TYPE_INDEX_MENU = 'index_menu'
MENU_TYPE_HUY_MENU = 'index_huy'

MENU_TYPES.update(
{
    MENU_TYPE_INDEX_MENU: {
        'title': 'Index menu'
    },
    MENU_TYPE_HUY_MENU: {
        'title': 'Huy menu'
    }
}
)
CHOICE_MENU_TYPES = [(k, v['title']) for k, v in MENU_TYPES.items()]

# MIGRATION_MODULES
