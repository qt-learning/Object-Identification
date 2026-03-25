// Copyright (C) 2026 Qt Group.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

#include "mybutton.h"

MyButton::MyButton(QWidget *parent)
    : QPushButton{parent}
    , m_myText(QString("My Text"))
{
    setText("My Button");
}

QString MyButton::myText() const
{
    return m_myText;
}

void MyButton::setMyText(const QString &newMyText)
{
    if (m_myText == newMyText)
        return;
    m_myText = newMyText;
    emit myTextChanged();
}

void MyButton::setMyButtonText(const QString &text)
{
    setText(text);
}
