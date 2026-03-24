@echo off
chcp 65001 >nul
echo ==========================================
echo  多元宇宙概念收集者 - 示例图片下载脚本
echo ==========================================
echo.
echo 正在下载示例图片（来自Unsplash免费图库）...
echo.

REM 创建临时下载目录
if not exist temp mkdir temp

REM 使用PowerShell下载图片
echo [1/6] 下载赛博朋克城市...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1515630278258-407f66498911?w=1920&q=80' -OutFile 'cyber_city.png'"

echo [2/6] 下载太空空间站...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1920&q=80' -OutFile 'space_station.png'"

echo [3/6] 下载时间概念...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1501139083538-0139583c61df?w=1920&q=80' -OutFile 'time_bureau.png'"

echo [4/6] 下载生物科技...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1920&q=80' -OutFile 'bio_lab.png'"

echo [5/6] 下载魔法场景...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1920&q=80' -OutFile 'magic_academy.png'"

echo [6/6] 下载宇宙背景...
powershell -Command "Invoke-WebRequest -Uri 'https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1920&q=80' -OutFile 'main_portals.png'"

echo.
echo ==========================================
echo  下载完成！
echo ==========================================
echo.
echo 已下载6张示例图片：
dir *.png /b
echo.
echo 注意：这些是来自Unsplash的免费图片，
echo 仅作为示例使用。建议根据插图生成指南.md
echo 使用AI工具生成更符合游戏内容的插图。
echo.
pause
