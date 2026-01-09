# robosys2025_kadai2

![test](https://github.com/s24c1118sb-hub/robosys2025_kadai2/actions/workflows/test.yml/badge.svg)

これはPCのディスク使用率を、ROS 2トピックとして配信するパッケージです。

## 配信
- **配信トピック**: `/disk_usage`
- **型**: `std_msgs/Float32`
| トピック名 | 型 | 内容 |
| :--- | :--- | :--- |
| `/disk_usage` | `std_msgs/Float32` | ルートディレクトリのディスク使用率（0.0〜100.0） |

## 実行方法
1. `colcon build`
2. `. install/setup.bash`
3. `ros2 run my_disk_monitor monitor`

## 必要なソフトウェア
- ROS 2 Jazzy Jalisco
- Python 3.12以上

## ライセンス
- BSD 3-Clause License
- © 2025 Ryota Miyauchi
