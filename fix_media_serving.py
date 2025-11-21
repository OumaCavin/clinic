#!/usr/bin/env python3
"""
Script to test and fix media file serving in Django development.
Run this to verify media files are accessible.
"""

import os
import sys
import django
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinicproject.settings')
django.setup()

from django.conf import settings
from django.test import Client

def test_media_serving():
    """Test if media files are being served correctly."""
    
    print("🔍 Django Media File Serving Test")
    print("=" * 50)
    
    # Check settings
    print(f"📁 MEDIA_URL: {settings.MEDIA_URL}")
    print(f"📁 MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"🔧 DEBUG: {settings.DEBUG}")
    print(f"🌐 ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    
    # Check if media directory exists
    media_dir = Path(settings.MEDIA_ROOT)
    if media_dir.exists():
        print(f"✅ Media directory exists: {media_dir}")
        
        # Check if images directory exists
        images_dir = media_dir / 'images'
        if images_dir.exists():
            print(f"✅ Images directory exists: {images_dir}")
            
            # List available images
            images = list(images_dir.glob('*'))
            if images:
                print(f"📸 Found {len(images)} images:")
                for img in images[:5]:  # Show first 5
                    print(f"   - {img.name}")
                if len(images) > 5:
                    print(f"   ... and {len(images) - 5} more")
            else:
                print("❌ No images found in media/images/")
        else:
            print("❌ Images directory not found in media/")
    else:
        print("❌ Media directory not found")
    
    # Test Django client (requires server to be running)
    print("\n🧪 Testing Django Client...")
    try:
        client = Client()
        
        # Test a few image URLs
        test_images = [
            '/media/images/medical_team_1.jpg',
            '/media/images/doctor_portrait_1.jpg',
            '/media/images/medical_equipment_1.jpg'
        ]
        
        for img_path in test_images:
            response = client.get(img_path)
            status = "✅" if response.status_code == 200 else "❌"
            print(f"   {status} {img_path}: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Django client test failed: {e}")
        print("💡 Make sure the Django development server is running!")
    
    print("\n" + "=" * 50)

def start_development_server():
    """Instructions to start the development server."""
    print("🚀 Django Development Server Instructions:")
    print("=" * 50)
    print("1. Navigate to the clinic directory:")
    print("   cd clinic/")
    print("\n2. Start the development server:")
    print("   python manage.py runserver 0.0.0.0:8000")
    print("\n3. Open your browser and test:")
    print("   http://localhost:8000/")
    print("   http://localhost:8000/media/images/medical_team_1.jpg")
    print("\n4. For production, configure your web server to serve media files")
    print("   from the MEDIA_ROOT directory.")

if __name__ == "__main__":
    test_media_serving()
    print()
    start_development_server()