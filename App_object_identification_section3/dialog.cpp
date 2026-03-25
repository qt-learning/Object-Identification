// Copyright (C) 2026 Qt Group.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

#include "dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
{
    m_button = new MyButton(this);
    resize(200, 200);
    m_button->resize(200, 200);
}

Dialog::~Dialog()
{
}

