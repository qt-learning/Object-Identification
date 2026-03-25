# Copyright (C) 2026 Qt Group.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# -*- coding: utf-8 -*-

import names


def main():
    startApplication("MyApp")
    mouseClick(waitForObject(names.my_Application_Rectangle))
    mouseClick(waitForObject(names.my_Application_Rectangle_2))
    mouseClick(waitForObject(names.my_Application_Rectangle_3))
