# home
This is the code for my website

## CV setup

1. Save your CV PDF to `private_assets/cv.pdf` (the folder is git-ignored).
2. For deployments, place the file there before building the image, or set `CV_FILE_PATH=/path/to/cv.pdf` in the environment.
3. Visit `/cv` to access it; the route returns 404 if the file is missing.
