import os
from PIL import Image

def check_images(base_path):
    folders_to_check = ['train', 'val', 'test']
    rgb_images = []
    non_rgb_images = []

    for folder in folders_to_check:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            print(f"Carpeta no encontrada: {folder_path}")
            continue

        print(f"\nRevisando imágenes en: {folder_path}")
        
        for category in ['fractured', 'not fractured']:
            category_path = os.path.join(folder_path, category)
            if not os.path.exists(category_path):
                print(f"Categoría no encontrada: {category_path}")
                continue

            print(f"\nRevisando imágenes en la categoría: {category_path}")
            
            for idx, file in enumerate(os.listdir(category_path)):
                file_path = os.path.join(category_path, file)
                try:
                    with Image.open(file_path) as img:
                        # Comprobar modo de la imagen
                        if img.mode != 'RGB':
                            non_rgb_images.append((idx, file_path, img.mode))
                        else:
                            rgb_images.append((idx, file_path))
                except Exception as e:
                    print(f"[ERROR] No se pudo procesar {file_path}: {e}")

    return rgb_images, non_rgb_images

def show_summary(rgb_images, non_rgb_images):
    print("\nResumen de imágenes:")
    print(f"Total de imágenes: {len(rgb_images) + len(non_rgb_images)}")
    print(f"Total de imágenes RGB listas: {len(rgb_images)}")
    print(f"Total de imágenes NO RGB: {len(non_rgb_images)}")

def show_non_rgb_details(non_rgb_images):
    print("\nDetalles de imágenes NO RGB:")
    if not non_rgb_images:
        print("No hay imágenes NO RGB.")
        return

    # Contar imágenes por ruta
    path_counts = {}
    for _, file_path, _ in non_rgb_images:
        directory = os.path.dirname(file_path)
        if directory not in path_counts:
            path_counts[directory] = 0
        path_counts[directory] += 1

    # Mostrar conteo por ruta
    for directory, count in path_counts.items():
        print(f"Ruta: {directory}, Total: {count}")

def menu():
    base_path = "./archive/Bone_Fracture_Binary_Classification/Bone_Fracture_Binary_Classification"
    rgb_images, non_rgb_images = check_images(base_path)

    while True:
        print("\nMenú:")
        print("1. Mostrar resumen")
        print("2. Mostrar detalles de imágenes NO RGB")
        print("3. Salir")
        
        choice = input("Seleccione una opción: ")

        if choice == '1':
            show_summary(rgb_images, non_rgb_images)
        elif choice == '2':
            show_non_rgb_details(non_rgb_images)
        elif choice == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
