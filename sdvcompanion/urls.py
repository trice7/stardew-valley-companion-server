"""sdvcompanion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from sdvapi.views import BundleItemView, BundleView, CenterRoomView, FarmView, ItemTypeView, ItemView, NPCEventView, SeasonEventView, SeasonView, ShopView, TownieView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'bundle_items', BundleItemView, 'bundle_item')
router.register(r'bundles', BundleView, 'bundle')
router.register(r'center_rooms', CenterRoomView, 'center_room')
router.register(r'farms', FarmView, 'farm')
router.register(r'item_types', ItemTypeView, 'item_type')
router.register(r'items', ItemView, 'item')
router.register(r'npc_events', NPCEventView, 'npc_event')
router.register(r'season_events', SeasonEventView, 'season_event')
router.register(r'seasons', SeasonView, 'season')
router.register(r'shops', ShopView, 'shop')
router.register(r'townies', TownieView, 'townie')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
