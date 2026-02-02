# Computer Vision

Welcome to the GitHub repository for the Computer Vision course. This repository is designed to provide you with hands-on experience and in-depth understanding of fundamental AI topics. The notebooks include both coding exercises and project-based activities, and were created using Python 3 as the interpreter.


## Getting Started

1. Clone this repository to your local machine:  

   ```
   git clone https://github.com/eugeniomorocho/Computer_Vision.git
   ```

2. Navigate to the specific Notebook's directory:  

   ```
   cd Computer_Vision/NOTEBOOK_x/
   ```
   
3. Follow the instructions in the file for each week's lab.

4. To update your local fork to the newest commit, execute:

   ```
   git fetch 
   ```


## Requirements

- Python 3.x as the interpreter
- Additional dependencies specified in each week's lab instructions

## Course Structure

### **Unit 1: Foundations of Computer Vision & Convolutions**
**Topics:**  
Images as tensors, image filtering and convolution, understanding visual features. 

**Slides:**  
Unit 1: Foundations of Computer Vision & Convolutions  
[![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://www.canva.com/design/DAG9kh3-RYE/s26i4QoK_D1lUX510QcoZQ/view?utm_content=DAG9kh3-RYE&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he981cdd10d)

**Tools:** Python, NumPy, OpenCV, PyTorch

**Datasets:**  
[CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html), *Department of Computer Science, University of Toronto*

**Notebooks:**  

1. Images as tensors  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.01%20Introduction%20to%20Computer%20Vision/1.%20Images%20as%20tensors.ipynb)

2. Image filtering and convolution   
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.01%20Introduction%20to%20Computer%20Vision/2.%20Filters%20and%20convolution.ipynb)

3. Filters in OpenCV  
[![Open in GitHub](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.01%20Introduction%20to%20Computer%20Vision/3.%20Filters%20in%20openCV.ipynb)

**Assignments:**  
   - Implement image filters (max 2 filters) manually and visualize convolution effects (feature maps). Create a image classifier with at least 70% of accuracy. The dataset should contain at least 10 images per class.   

   - [Image Processing in Python (DataCamp)](https://app.datacamp.com/learn/courses/image-processing-in-python)

**Aditional Readings:**
   - **Chapter 15: Linear Image Filtering** Torralba, A., Isola, P., & Freeman, W. (2024). Foundations of Computer Vision. MIT Press. https://visionbook.mit.edu/


---

### **Unit 2: CNNs for Image Classification**
**Topics:** Neural networks for vision, convolutional layers, pooling, training pipeline, evaluation metrics  
**Tools:** PyTorch  
**Lab / Deliverable:** Train a CNN for image classification  

---

### **Unit 3: Transfer Learning & Model Improvement**
**Topics:** Overfitting, regularization, data augmentation, pretrained CNNs, fine-tuning vs feature extraction  
**Tools:** PyTorch, torchvision  
**Lab / Deliverable:** Transfer learning using ResNet or MobileNet  

---

### **Unit 4: Object Detection (Midterm Unit)**  
**Topics:** Classification vs detection, bounding boxes & IoU, YOLO architecture, dataset annotation  

**Notebooks:**  
1. Drawing a Bounding Box with OpenCV  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.06%20Object%20Detection%20(YOLO%20%2B%20Roboflow)/Object%20Detection/1.%20Drawing%20a%20Bounding%20Box%20with%20OpenCV.ipynb)

2. Real-time Object Detection with YOLO  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.06%20Object%20Detection%20(YOLO%20%2B%20Roboflow)/Object%20Detection/2.%20Real-time%20Object%20Detection%20with%20YOLO.ipynb)

3. Custom YOLO Object Detection with Roboflow  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Computer_Vision/blob/main/UC.06%20Object%20Detection%20(YOLO%20%2B%20Roboflow)/Object%20Detection/3.%20Custom%20YOLO%20Object%20Detection%20with%20Roboflow.ipynb)

**Resources:**

- [Ultralytics](https://www.ultralytics.com)<br>
- [Roboflow](https://roboflow.com)


**Tools:** Ultralytics YOLO, Roboflow, OpenCV (Bounding Boxes Notebook)  
**Lab / Deliverable:** Train an object detector on a custom dataset using [Roboflow](https://roboflow.com)

---

### **Unit 5: Image Segmentation & Pose Estimation**
**Topics:** Semantic vs instance segmentation, encoder–decoder architectures, human pose estimation basics  
**Tools:** PyTorch, MediaPipe  
**Lab / Deliverable:** Segmentation **or** pose estimation mini-project  

---

### **Unit 6: Tracking & Video Analysis**
**Topics:** Detection vs tracking, classical trackers (KCF, CSRT), tracking-by-detection  
**Tools:** OpenCV  
**Lab / Deliverable:** Object tracking in video streams  

---

### **Unit 7: Model Deployment & Edge AI**
**Topics:** Inference vs training, running models with ONNX runtime, vision model APIs, edge inference and hardware constraints  
**Tools:** ONNX Runtime, FastAPI, Jetson Nano, MediaPipe, Flutter (iOS, Android and web)  
**Lab / Deliverable:** Deploy a trained model as an API and consume it from the cloud (AWS, MS Azure, Huawei Cloud, Oracle Cloud, etc.) **or** run inference on Jetson Nano using the GPU **or** on a mobile phone, tablet, watch, TV, etc., using [Flutter](https://flutter.dev/) with MediaPipe

---

### **Unit 8: Cloud & Modern Vision AI + Final Project Presentations**
**Topics:** Cloud vision APIs, Vision Transformers, Segment Anything Model (conceptual), ethics and real-world deployment  
**Tools:** Cloud vision services (overview)  
**Lab / Deliverable:** Use a cloud or foundation vision model for inference and compare results  

---

## Support and Feedback

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/eugeniomorocho/Computer_Vision/issues). We appreciate your feedback!

---

## Extra Topics:

- Face Detection: OpenCV (Haar / DNN Module), PyTorch
- 3D Reconstruction (from drone imagery)
- Generative AI for Computer Vision (OpenAI Dall-E, etc.)
- NVIDIA TAO Toolkit and DeepStream (Docker + Jetson Nano 2GB Developer Kit) ONNX 
- Computer Vision on the Cloud (AWS Rekognition, Lookout for Vision, and NVIDIA's SageMaker)


## Bibliography

### Primary Books

[1] Torralba, A., Isola, P., & Freeman, W. (2024). Foundations of Computer Vision. MIT Press. https://visionbook.mit.edu/

[2] Szeliski, R. (2022). Computer Vision: Algorithms and Applications (2nd ed.). Springer Cham. https://doi.org/https://doi.org/10.1007/978-3-030-34372-9 

[3] Ayyadevara, V. K., & Reddy, Y. (2024). Modern Computer Vision with PyTorch: A practical roadmap from Deep Learning fundamentals to advanced applications and Generative AI (2nd ed.). Packt Publishing Ltd. https://www.packtpub.com/en-mt/product/modern-computer-vision-with-pytorch-9781803240930 
<br>
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/PacktPublishing/Modern-Computer-Vision-with-PyTorch-2E)

[4] Shanmugamani, R. (2018). Deep Learning for Computer Vision: Expert techniques to train advanced neural networks using TensorFlow and Keras (1st ed.). Packt Publishing. https://www.packtpub.com/en-us/product/deep-learning-for-computer-vision-9781788295628 
<br>
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/packtpublishing/deep-learning-for-computer-vision)

[5] Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning (1st ed.). The MIT Press. https://www.deeplearningbook.org

### Complementary Books

[6] Elgendy, M. (2020). Deep Learning for Vision Systems. Manning Publications Co. https://www.manning.com/books/deep-learning-for-vision-systems 

[7] Prince, S. J. D. (2012). Computer Vision: Models, Learning and Inference. Cambridge University Press. https://www.cambridge.org/ca/universitypress/subjects/computer-science/computer-graphics-image-processing-and-robotics/computer-vision-models-learning-and-inference

[8] Zhang, A., Lipton, Z. C., Li, M. U., & Smola, A. J. (2023). Dive into Deep Learning. Cambridge University Press. https://D2L.ai
<br>
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/d2l-ai/d2l-en)

[9] Chollet, F. (2026). Deep Learning with Python (3rd ed.). Manning Publications. https://deeplearningwithpython.io 

### Research Papers

[10] Vaswani, A., Brain, G., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention Is All You Need. NIPS’17: Proceedings of the 31st International Conference on Neural Information Processing Systems, 6000–6010. https://doi.org/10.48550/arXiv.1706.03762

[11] Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. ICLR 2021 - 9th International Conference on Learning Representations. https://arxiv.org/abs/2010.11929v2

[12] Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers. Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 12346 LNCS, 213–229. https://doi.org/10.1007/978-3-030-58452-8_13

[13] SKirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W. Y., Dollár, P., & Girshick, R. (2023). Segment Anything. Proceedings of the IEEE International Conference on Computer Vision, 3992–4003. https://doi.org/10.1109/ICCV51070.2023.00371

### Online Resources

[14] [Stanford CS231N Deep Learning for Computer Vision 2025 (YouTube Playlist)](https://www.youtube.com/playlist?list=PLoROMvodv4rOmsNzYBMe0gJY2XS8AQg16)

[15] [Stanford Lecture Collection CNNs for Visual Recognition 2017](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)

[16] [NVIDIA Deep Learning Institute](https://www.nvidia.com/en-us/training/)

---
<br>
<p style="text-align: right; font-size:14px; color:gray;">
<b>Prepared by:</b><br>
Manuel Eugenio Morocho-Cayamcela, Ph.D.
</p>

<div style="text-align: right;">
  <img src="assets/yt.png" alt="drawing" style="width: 100px;" />
</div>