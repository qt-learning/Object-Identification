// Copyright (C) 2026 Qt Group.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

import QtQuick

Window {
    id: window
	
    width: 640
    height: 480
    visible: true
    title: qsTr("My Application")

    Column {
        anchors.centerIn: parent
        spacing: 15

        Repeater {
            model: 3

            delegate: Rectangle {
                required property int index

                //objectName: "rectangle_%1".arg(index) //more reliable than Squish's occurence
                height: 100
                width: 100
                color: "red"
            }
        }
    }
}
