#!/usr/bin/env python3
"""
Program uji untuk mengamati pembatasan CPU dan Memori pada Docker container
"""
import time
import sys
import psutil
import os

def print_system_info():
    """Menampilkan informasi sistem"""
    print("=" * 60)
    print("INFORMASI SISTEM")
    print("=" * 60)
    print(f"CPU Count: {psutil.cpu_count()}")
    print(f"Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB")
    print("=" * 60)
    print()

def cpu_intensive_task(duration=10):
    """
    Tugas intensif CPU - melakukan komputasi matematika berulang
    
    Args:
        duration: durasi dalam detik
    """
    print(f"[CPU TEST] Memulai komputasi intensif selama {duration} detik...")
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        # Komputasi matematika sederhana
        result = sum([i**2 for i in range(1000)])
        counter += 1
    
    elapsed = time.time() - start_time
    print(f"[CPU TEST] Selesai!")
    print(f"  - Waktu eksekusi: {elapsed:.2f} detik")
    print(f"  - Iterasi yang diselesaikan: {counter:,}")
    print(f"  - Kecepatan: {counter/elapsed:.2f} iterasi/detik")
    print()
    
    return counter

def memory_intensive_task(size_mb=100, steps=5):
    """
    Tugas intensif memori - mengalokasikan memori bertahap
    
    Args:
        size_mb: ukuran memori per step dalam MB
        steps: jumlah langkah alokasi
    """
    print(f"[MEMORY TEST] Mengalokasikan memori {size_mb}MB x {steps} langkah...")
    memory_blocks = []
    
    for i in range(steps):
        try:
            # Alokasi memori (1 MB = 1024 * 1024 bytes)
            block = bytearray(size_mb * 1024 * 1024)
            memory_blocks.append(block)
            
            mem_info = psutil.virtual_memory()
            print(f"  Step {i+1}/{steps}: Allocated {size_mb}MB")
            print(f"    - Total allocated: {(i+1)*size_mb}MB")
            print(f"    - Memory used: {mem_info.percent}%")
            print(f"    - Available: {mem_info.available / (1024**2):.2f} MB")
            
            time.sleep(1)
            
        except MemoryError:
            print(f"  [ERROR] Memori tidak cukup pada step {i+1}")
            print(f"  Total yang berhasil dialokasikan: {i*size_mb}MB")
            return False
    
    print(f"[MEMORY TEST] Berhasil mengalokasikan total {steps*size_mb}MB")
    print()
    
    # Cleanup
    memory_blocks.clear()
    return True

def monitor_resources(interval=2, count=5):
    """
    Memonitor penggunaan resource secara real-time
    
    Args:
        interval: interval monitoring dalam detik
        count: jumlah sampel
    """
    print(f"[MONITORING] Memantau penggunaan resource ({count} sampel)...")
    print("-" * 60)
    
    for i in range(count):
        cpu_percent = psutil.cpu_percent(interval=1)
        mem_info = psutil.virtual_memory()
        
        print(f"Sample {i+1}/{count}:")
        print(f"  CPU Usage: {cpu_percent}%")
        print(f"  Memory Usage: {mem_info.percent}%")
        print(f"  Available Memory: {mem_info.available / (1024**2):.2f} MB")
        
        if i < count - 1:
            time.sleep(interval - 1)
    
    print("-" * 60)
    print()

def main():
    """Fungsi utama"""
    print("\n" + "=" * 60)
    print("DOCKER RESOURCE LIMIT - PROGRAM UJI")
    print("=" * 60)
    print()
    
    # Tampilkan informasi sistem
    print_system_info()
    
    # Test 1: CPU Intensive Task
    print("\n### TEST 1: CPU INTENSIVE ###\n")
    cpu_iterations = cpu_intensive_task(duration=10)
    
    # Test 2: Memory Intensive Task
    print("### TEST 2: MEMORY INTENSIVE ###\n")
    # Coba alokasi 50MB x 5 = 250MB
    memory_success = memory_intensive_task(size_mb=50, steps=5)
    
    # Test 3: Resource Monitoring
    print("### TEST 3: RESOURCE MONITORING ###\n")
    monitor_resources(interval=2, count=5)
    
    # Summary
    print("=" * 60)
    print("RINGKASAN HASIL")
    print("=" * 60)
    print(f"CPU Test: {cpu_iterations:,} iterasi diselesaikan")
    print(f"Memory Test: {'Berhasil' if memory_success else 'Gagal'}")
    print("=" * 60)
    print("\nProgram selesai!")

if _name_ == "_main_":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")
        sys.exit(1)