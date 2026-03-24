#!/usr/bin/env python3
"""图片批量压缩脚本 v2 - 强制压缩到 500KB 以内"""

from PIL import Image
import os

def compress_image(input_path, output_path, target_size=500000):
    """压缩图片到目标大小以内"""
    try:
        img = Image.open(input_path)
        
        # 转换为 RGBA
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # 逐步降低质量和尺寸
        scale = 1.0
        while scale > 0.3:
            # 调整尺寸
            new_size = (int(img.width * scale), int(img.height * scale))
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # 保存
            img_resized.save(output_path, 'PNG', optimize=True)
            
            # 检查大小
            file_size = os.path.getsize(output_path)
            if file_size <= target_size:
                print(f"✅ {os.path.basename(input_path)}: {file_size/1024:.0f}KB ({scale*100:.0f}%)")
                return True
            
            scale -= 0.1
        
        # 如果还是太大，强制压缩到 30% 尺寸
        final_size = (int(img.width * 0.3), int(img.height * 0.3))
        img_final = img.resize(final_size, Image.Resampling.LANCZOS)
        img_final.save(output_path, 'PNG', optimize=True)
        file_size = os.path.getsize(output_path)
        print(f"⚠️ {os.path.basename(input_path)}: {file_size/1024:.0f}KB (30%)")
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
    count = 0
    
    for filename in sorted(os.listdir(images_dir)):
        if filename.endswith('.png'):
            input_path = os.path.join(images_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # 如果已压缩过且小于 500KB，跳过
            if os.path.exists(output_path):
                compressed_size = os.path.getsize(output_path)
                if compressed_size <= 500000:
                    print(f"⏭️ {filename}: 已压缩 ({compressed_size/1024:.0f}KB)")
                    total_compressed += compressed_size
                    count += 1
                    continue
            
            original_size = os.path.getsize(input_path)
            total_original += original_size
            
            if compress_image(input_path, output_path):
                compressed_size = os.path.getsize(output_path)
                total_compressed += compressed_size
                count += 1
    
    print(f"\n📊 压缩统计:")
    print(f"处理图片：{count} 张")
    print(f"原始大小：{total_original/1024/1024:.1f}MB")
    print(f"压缩后：{total_compressed/1024/1024:.1f}MB")
    if total_original > 0:
        print(f"压缩率：{(1 - total_compressed/total_original)*100:.1f}%")

if __name__ == '__main__':
    main()
