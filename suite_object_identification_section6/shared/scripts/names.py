# encoding: UTF-8

from objectmaphelper import *

my_Application_QQuickWindowQmlImpl = {"title": "My Application", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
my_Application_Rectangle = {"container": my_Application_QQuickWindowQmlImpl, "type": "Rectangle", "unnamed": 1, "visible": True}
my_Application_Rectangle_2 = {"container": my_Application_QQuickWindowQmlImpl, "occurrence": 2, "type": "Rectangle", "unnamed": 1, "visible": True}
my_Application_Rectangle_3 = {"container": my_Application_QQuickWindowQmlImpl, "occurrence": 3, "type": "Rectangle", "unnamed": 1, "visible": True}

#objectName could be used instead of occurrence
#my_Application_Rectangle = {"container": my_Application_QQuickWindowQmlImpl, "objectName": "rectangle_0", "type": "Rectangle", "visible": True}
#my_Application_Rectangle_2 = {"container": my_Application_QQuickWindowQmlImpl, "objectName": "rectangle_1", "type": "Rectangle", "visible": True}
#my_Application_Rectangle_3 = {"container": my_Application_QQuickWindowQmlImpl, "objectName": "rectangle_2", "type": "Rectangle", "visible": True}
