# Copyright (C) 2026 Qt Group.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# -*- coding: utf-8 -*-

import names


def main():
    startApplication("addressbook")
    clickButton(waitForObject(names.Open_QToolButton))
