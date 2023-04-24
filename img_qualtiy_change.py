from PIL import Image
def img_quality(source,dest):
    source="/Users/yerin/examples"
    dest="/Users/yerin/cropped/fakes000160_bigger"
    max_images=500
    transform="center-crop"
    resolution=(512,512)

    img = Image.open(source)

    # Resize the image to 512x512 with Lanczos filter
    resized_img = img.resize((1024, 1024), Image.LANCZOS)

    # Apply post-processing filters to reduce loss of quality
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    resized_img = resized_img.filter(ImageFilter.SMOOTH_MORE)


    # Save the resized image
    resized_img.save(dest)

if __name__ == '__main__':
  source = sys.argv[1]
  dest = sys.argv[2]
  img_quality(source,dest)
