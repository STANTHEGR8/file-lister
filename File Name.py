import os

# 🔧 Folder to scan
folder_path = r"C:\Users\h\Downloads\Certificates"  # <-- change this to your folder

# 📄 Output file path (saved in the same folder you're scanning)
output_file = os.path.join(folder_path, "file_list.txt")

# 🧭 Collect all files recursively
all_files = []
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        # Relative path (for readability)
        relative_path = os.path.relpath(os.path.join(root, file_name), folder_path)
        all_files.append(relative_path)

# 💾 Write all file names to text file
try:
    with open(output_file, "w", encoding="utf-8") as f:
        for file_name in all_files:
            f.write(file_name + "\n")

    print(f"✅ {len(all_files)} files found.")
    print(f"📄 File list saved here:\n{output_file}")
except Exception as e:
    print("❌ Error writing file:", e)
