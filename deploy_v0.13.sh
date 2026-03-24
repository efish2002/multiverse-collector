#!/bin/bash
# v0.13 修复部署脚本
echo "🚀 部署 twine_version_v11.html 到服务器..."
scp /root/Sync/Code/game-scifi-hybrid/twine_version_v11.html root@139.155.138.232:/var/www/html/game.html
if [ $? -eq 0 ]; then
    echo "✅ 部署成功！"
    echo "🌐 访问地址：http://139.155.138.232/game.html"
else
    echo "❌ 部署失败，请检查 SSH 连接"
fi
