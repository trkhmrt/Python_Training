# Veri setini yükleyin ve birkaç örnek görüntüyü görselleştirin
import os
import random
import matplotlib.pyplot as plt
from glob import glob

# Veri setinin yolu
data_path = "path/to/dataset"

# Kanserli ve sağlıklı hücrelerin yollarını belirleme
cancer_cells = glob(os.path.join(data_path, "cancer", "*.png"))
healthy_cells = glob(os.path.join(data_path, "healthy", "*.png"))

# Rastgele bir kanserli ve sağlıklı hücre görüntüsü seçme
cancer_img_path = random.choice(cancer_cells)
healthy_img_path = random.choice(healthy_cells)

# Görüntüleri gösterme
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(plt.imread(cancer_img_path))
axes[0].set_title("Kanserli Hücre")

axes[1].imshow(plt.imread(healthy_img_path))
axes[1].set_title("Sağlıklı Hücre")

plt.show()
