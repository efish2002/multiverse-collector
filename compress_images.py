#!/usr/bin/env python3
"""图片批量压缩脚本 - 将 PNG 图片压缩到 500KB 以内"""

from PIL import Image
import os
import sys

def compress_image(input_path, output_path, max_size=500000):
    """压缩图片到指定大小以内"""
    try:
        img = Image.open(input_path)
        
        # 转换为 RGBA 模式
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 降低质量并调整大小
        quality = 95
        scale = 1.0
        
        # 保存为 PNG
        while quality > 50:
            # 调整大小
            if scale < 1.0:
                new_size = (int(img.width * scale), int(img.height * scale))
                img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            else:
                img_resized = img
            
            # 保存
            img_resized.save(output_path, 'PNG', optimize=True)
            
            # 检查大小
            file_size = os.path.getsize(output_path)
            if file_size <= max_size:
                print(f"✅ {os.path.basename(input_path)}: {file_size/1024:.0f}KB ({scale*100:.0f}%)")
                return True
            
            # 降低质量
            quality -= 5
            scale *= 0.9
        
        # 如果还是太大，强制压缩
        img_final = img.resize((int(img.width * 0.5), int(img.height * 0.5)), Image.Resampling.LANCZOS)
        img_final.save(output_path, 'PNG', optimize=True)
        file_size = os.path.getsize(output_path)
        print(f"⚠️ {os.path.basename(input_path)}: {file_size/1024:.0f}KB (50%)")
        return True
        
    except Exception as e:
        print(f"❌ {os.path.basename(input_path)}: {e}")
        return False

def main():
    images_dir = '/root/Sync/Code/game-scifi-hybrid/images'
    output_dir = '/root/Sync/Code/game-scifi-hybrid/images-compressed'
    
    os.makedirs(output_dir, exist_ok=True)
    
    total_original = 0
    total_compressed = 0
    
    for filename in os.listdir(images_dir):
        if filename.endswith('.png'):
            input_path = os.path.join(images_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            original_size = os.path.getsize(input_path)
            total_original += original_size
            
            if compress_image(input_path, output_path):
                compressed_size = os.path.getsize(output_path)
                total_compressed += compressed_size
    
    print(f"\n📊 压缩统计:")
    print(f"原始大小：{total_original/1024/1024:.1f}MB")
    print(f"压缩后：{total_compressed/1024/1024:.1f}MB")
    print(f"压缩率：{(1 - total_compressed/total_original)*100:.1f}%")

if __name__ == '__main__':
    main()
