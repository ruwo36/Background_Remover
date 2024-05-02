
# Background Remover

![Background Remover](Background-Remover.gif)

## About

**Background Remover** is a simple Python application, considered the simplest program that allows us to automate tasks and save time. For example: I had a folder containing 100 images that were decorative symbols, and I wanted to remove the backgrounds of all these images and keep only the symbol without a background. In such a case, the program saves a lot of time.
- The first program used the **OpenCV library** to read the images and then save them after removing their backgrounds.
- The second program used the **Pillow library** to read the images and then save them after removing their backgrounds.

Both programs are similar, the only difference is the method of reading the images and saving them, just to provide more information.
Then I used the **rembg library** to remove the backgrounds of the images.

## Features

- **Background Removal:** Automatically removes the background from input images.
- **User-Friendly Interface:** Simple command-line interface for easy interaction.
- **Supports Various Image Formats:** Supports common image formats such as JPG, PNG, etc. as reading and PNG as writing.

## Library's

- **rembg:** remove background lib [pypi](https://pypi.org/project/rembg).
- **OpenCV:** image processing lib [pypi](https://pypi.org/project/opencv-python).
- **Pillow:** image Editing lib [pypi](https://pypi.org/project/pillow).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ruwo36/background-remover.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

- OR you can install library's via your command line:

   ```bash
   pip install rembg
   pip install opencv-python
   pip install pillow
   ```

## Usage

1. Navigate to the project directory:

   ```bash
   cd background-remover
   ```

2. Run the application:
- With openCV:

   ```bash
   python main_with_cv2.py
   ```
- With Pillow:
 
   ```bash
   python main_with_PIL.py
   ```
   After run this command the program ask you to enter folder path that content your images which you want to remove his background.

## Example

```bash
python main_with_cv2.py
```
Show it in my [LinkedIn](https://www.linkedin.com/in/ali-n-ajeeb), I post a video explain it.

## License

This project is licensed under the Custom License - Free for Personal and Non-Commercial Use - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- [my Gmail](mailto:mayasajeeb123@gmail.com), or [my Business Gmail](mailto:it.academy.info1@gmail.com).
- [LinkedIn](https://www.linkedin.com/in/ali-n-ajeeb).
