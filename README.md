# my_disk_monitor

![test](https://github.com/s24c1118sb-hub/robosys2025_kadai2/actions/workflows/test.yml/badge.svg)

これはPCのディスク使用率を、ROS 2トピックとして配信するパッケージです。

## 配信
| トピック名 | 型 | 内容 |
| :--- | :--- | :--- |
| `/disk_usage` | `std_msgs/Float32` | ルートディレクトリのディスク使用率（0.0〜100.0） |

## 実行･確認方法
1. ワークスペースの `src` ディレクトリに本リポジトリをクローンし、ビルドします。
2. ノードを起動します。
   ```
   ros2 run my_disk_monitor monitor
   ```
   ※成功するとターミナルに`[INFO] [disk_monitor]: Publishing: X.XX%` と表示されます。
3. 別のターミナルから、配信されているトピックを確認します。
   ```
   ros2 topic echo /disk_usage
   ```
## 必要なソフトウェア
- ROS 2 Jazzy Jalisco
- Python 3.12以上

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2025 Ryota Miyauchi
