#!/bin/bash
# SPDX-FileCopyrightText: 2025 Ryota Miyauchi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
. install/setup.bash

ng () {
    echo "${1}行目のテストが失敗しました。"
    res=1
}

res=0

ros2 run my_disk_monitor monitor &
node_pid=$!

out=$(timeout 15 ros2 topic echo /disk_usage --once)

kill $node_pid

echo "${out}" | grep -E "data: [0-9]+\.[0-9]+" || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
