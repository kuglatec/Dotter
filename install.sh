echo "Thank you for installing dotter!"
echo "cloning repo..."
git clone https://github.com/kuglatec/dotter
cd dotter
echo "Copying file..."
chmod +x src/main.py
cp src/main.py /bin/dotter
echo "setup finished! start setting up you first package"
