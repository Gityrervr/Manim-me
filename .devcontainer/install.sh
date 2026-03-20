Content:
#!/bin/bash
echo "Installing..."
sudo apt-get update -qq
sudo apt-get install -y libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra dvipng > /dev/null 2>&1
pip install manim jupyter numpy pillow --quiet
echo "Done!"
manim --version
