# LOAM_TEST
## Folder contents
### LOAM
稍微修改之後的LOAM source code，須安裝完PCL後再編譯過才能使用。
### Python
包含幾個python程式碼：

- area_update.py
將發布過的點雲資訊蒐集成一個完整的點雲地圖，並發布至另一個獨立的ROS topic。
- drone_control.py
一個很簡易的無人機控制程式，透過輸入指令的方式操作。
- lidar_publisher.py
將Airsim的lidar資訊經過座標軸轉換後發布至LOAM接收資料的topic。
- position_publisher.py
將Airsim中無人機位置的ground truth發布至一個ROS topic上，供網頁顯示使用。

### Web
一個顯示目前點雲Mapping結果的網頁，做一些修改後也能夠應用在不同地方，可以作為參考的程式使用。
