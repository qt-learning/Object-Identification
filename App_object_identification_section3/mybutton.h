// Copyright (C) 2026 Qt Group.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

#ifndef MYBUTTON_H
#define MYBUTTON_H

#include <QPushButton>
#include <QObject>

class MyButton : public QPushButton
{
    Q_OBJECT
    Q_PROPERTY(QString myText READ myText WRITE setMyText NOTIFY myTextChanged FINAL)

public:
    MyButton(QWidget *parent = nullptr);
    QString myText() const;
    Q_INVOKABLE void setMyText(const QString &newMyText);

public slots:
    void setMyButtonText(const QString &text);

signals:
    void myTextChanged();

private:
    QString m_myText;
};

#endif // MYBUTTON_H
