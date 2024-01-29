#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

#include "mybutton.h"

class Dialog : public QDialog
{
    Q_OBJECT

public:
    Dialog(QWidget *parent = nullptr);
    ~Dialog();

private:
    MyButton *m_button;
};
#endif // DIALOG_H
