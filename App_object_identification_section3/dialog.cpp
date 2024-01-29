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

